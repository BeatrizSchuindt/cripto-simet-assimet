import os
import gerador_massa
import metricas
import gerar_matriz_imagens
from algoritmos import simetricos, assimetricos 

PASTAS = {
    "entrada": "massa_de_teste",
    "saida": "outputs",
    "graficos": "relatorios/graficos",
    "md": "relatorios/md"
}

ALGORITMOS_TESTE = ["AES-128", "AES-256", "DES", "3DES"]
ALGORITIMO_ASSIMETRICO = ["RSA-1024", "RSA-2048", "RSA-4096"]
MODOS_TESTE = ["ECB", "CBC", "CFB", "OFB", "CTR"]
MODOS_RSA = ["ECB", "CBC", "CTR"] 

def garantir_pastas():
    for pasta in PASTAS.values():
        if not os.path.exists(pasta):
            os.makedirs(pasta)

if __name__ == "__main__":
    garantir_pastas()
    
    gerar_novamente = input("Deseja gerar a massa de testes agora? (s/n): ").strip().lower()
    
    if gerar_novamente == 's':
        gerador_massa.executar_menu()
    else:
        print("\nPulando a geração. Usando os arquivos existentes na pasta...")
        
    resultados_gerais = []
    arquivos_teste = os.listdir(PASTAS['entrada'])
    
    if not arquivos_teste:
        print("\nAVISO: A pasta 'massa_de_teste' está vazia! Rode novamente e escolha 's' para gerar.")
    else:
        for arquivo in arquivos_teste:
            if arquivo.startswith('.'):
                continue
                
            caminho_in = os.path.join(PASTAS['entrada'], arquivo)
            tamanho_mb = os.path.getsize(caminho_in) / (1024 * 1024) # Tamanho em MB
            
            for algoritmo in ALGORITMOS_TESTE:
                for modo in MODOS_TESTE:
                    caminho_out = os.path.join(PASTAS['saida'], f"cifrado_{algoritmo}_{modo}_{arquivo}")
                    caminho_decifrado = os.path.join(PASTAS['saida'], f"decifrado_{algoritmo}_{modo}_{arquivo}")
                    print(f"Processando Simétrico: {arquivo} | {algoritmo} | {modo}")
                    
                    # Geramos a chave no main para podermos decifrar depois
                    chave_simetrica = simetricos.gerar_chave(algoritmo)
                    
                    args_cifrar = (caminho_in, caminho_out, algoritmo, modo, chave_simetrica)
                    args_decifrar = (caminho_out, caminho_decifrado, algoritmo, modo, chave_simetrica)
                    
                    resultado = metricas.executar_testes_completos(
                        simetricos.cifrar_arquivo, args_cifrar,
                        simetricos.decifrar_arquivo, args_decifrar,
                        caminho_in, caminho_out
                    )
                    resultado.update({'arquivo': arquivo, 'algoritmo': algoritmo, 'modo': modo})
                    resultados_gerais.append(resultado)

            for algoritmo in ALGORITIMO_ASSIMETRICO:
                if tamanho_mb > 10: 
                    print(f"!! Saltando RSA para {arquivo} ({tamanho_mb:.2f}MB) - Muito lento para o teste.")
                    continue
                
                tamanho_bits = int(algoritmo.split('-')[1])
                chave_rsa = assimetricos.gerar_chave(tamanho_bits)
                
                for modo in MODOS_RSA:
                    caminho_out = os.path.join(PASTAS['saida'], f"cifrado_{algoritmo}_{modo}_{arquivo}")
                    caminho_decifrado = os.path.join(PASTAS['saida'], f"decifrado_{algoritmo}_{modo}_{arquivo}")
                    print(f"Processando Assimétrico: {arquivo} | {algoritmo} | {modo}")
                    
                    args_cifrar = (caminho_in, caminho_out, modo, chave_rsa)
                    args_decifrar = (caminho_out, caminho_decifrado, modo, chave_rsa)
                    
                    resultado = metricas.executar_testes_completos(
                        assimetricos.cifrar_arquivo_rsa, args_cifrar,
                        assimetricos.decifrar_arquivo_rsa, args_decifrar,
                        caminho_in, caminho_out
                    )
                    resultado.update({'arquivo': arquivo, 'algoritmo': algoritmo, 'modo': modo})
                    resultados_gerais.append(resultado)
            
        # Gerar os entregáveis finais
        if resultados_gerais:
            grafico_tp = metricas.gerar_grafico_throughput(resultados_gerais, PASTAS['graficos'])
            grafico_ent = metricas.gerar_grafico_entropia(resultados_gerais, PASTAS['graficos']) 
            metricas.gerar_relatorio_md(resultados_gerais, grafico_tp, PASTAS['md'], grafico_ent)
            
            gerar_matriz_imagens.gerar_matrizes(PASTAS['entrada'], PASTAS['saida'], PASTAS['graficos'])
            
            print("\n[+] Testes finalizados! Relatórios e gráficos gerados na pasta 'relatorios/'.")