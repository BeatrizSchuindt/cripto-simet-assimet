import os
import gerador_massa
import metricas
from algoritmos import simetricos

PASTAS = {
    "entrada": "massa_de_teste",
    "saida": "outputs",
    "graficos": "relatorios/graficos",
    "md": "relatorios/md"
}

ALGORITMOS_TESTE = ["AES-128", "AES-256", "DES", "3DES"]
MODOS_TESTE = ["ECB", "CBC", "CFB", "OFB", "CTR"]

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
            
            for algoritmo in ALGORITMOS_TESTE:
                for modo in MODOS_TESTE:
                    caminho_out = os.path.join(PASTAS['saida'], f"cifrado_{algoritmo}_{modo}_{arquivo}")
                    
                    print(f"Processando: {arquivo} | Algoritmo: {algoritmo} | Modo: {modo}")
                    
                    resultado = metricas.executar_com_metricas(
                        simetricos.cifrar_arquivo, 
                        caminho_in, 
                        caminho_out, 
                        algoritmo, 
                        modo
                    )
                    
                    resultado['arquivo'] = arquivo
                    resultado['algoritmo'] = algoritmo
                    resultado['modo'] = modo
                    resultados_gerais.append(resultado)
            
        grafico = metricas.gerar_grafico_throughput(resultados_gerais, PASTAS['graficos'])
        metricas.gerar_relatorio_md(resultados_gerais, grafico, PASTAS['md'])
        print("\n[+] Testes finalizados! Relatório gerado com sucesso.")