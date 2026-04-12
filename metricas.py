import math
import os
import time
from collections import Counter
import matplotlib.pyplot as plt
from datetime import datetime

def calcular_entropia(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'rb') as f:
            dados = f.read()
    except FileNotFoundError:
        return 0.0

    tamanho = len(dados)
    if tamanho == 0:
        return 0.0

    frequencias = Counter(dados)
    entropia = 0.0

    for frequencia in frequencias.values():
        probabilidade = frequencia / tamanho
        entropia -= probabilidade * math.log2(probabilidade)

    return entropia

def detectar_padroes(entropia):
    return entropia < 7.0

def calcular_throughput(tamanho_bytes, tempo_segundos):
    if tempo_segundos <= 0:
        return 0.0
    tamanho_mb = tamanho_bytes / (1024 * 1024)
    return tamanho_mb / tempo_segundos

def executar_testes_completos(funcao_cifrar, args_cifrar, funcao_decifrar, args_decifrar, arquivo_entrada, arquivo_saida):
    if not os.path.exists(arquivo_entrada):
        raise FileNotFoundError(f"Arquivo não encontrado: {arquivo_entrada}")

    tamanho_bytes = os.path.getsize(arquivo_entrada)
    
    # Executa a Cifragem 10 vezes
    tempos_cifrar = []
    for _ in range(10):
        inicio = time.time()
        funcao_cifrar(*args_cifrar)
        fim = time.time()
        tempos_cifrar.append(fim - inicio)
        
    tempo_medio_cifrar = sum(tempos_cifrar) / len(tempos_cifrar)
    throughput_medio_cifrar = calcular_throughput(tamanho_bytes, tempo_medio_cifrar)

    # Executa a Decifragem 10 vezes
    tempos_decifrar = []
    for _ in range(10):
        inicio = time.time()
        funcao_decifrar(*args_decifrar)
        fim = time.time()
        tempos_decifrar.append(fim - inicio)
        
    tempo_medio_decifrar = sum(tempos_decifrar) / len(tempos_decifrar)
    throughput_medio_decifrar = calcular_throughput(tamanho_bytes, tempo_medio_decifrar)
    
    entropia_resultado = calcular_entropia(arquivo_saida)
    padroes = detectar_padroes(entropia_resultado)

    return {
        "tamanho_bytes": tamanho_bytes,
        "tempo_cifrar_s": round(tempo_medio_cifrar, 4),
        "tempo_decifrar_s": round(tempo_medio_decifrar, 4),
        "throughput_cifrar_MB_s": round(throughput_medio_cifrar, 4),
        "throughput_decifrar_MB_s": round(throughput_medio_decifrar, 4),
        "entropia": round(entropia_resultado, 4),
        "padroes_detectados": padroes
    }

def gerar_grafico_throughput(resultados, pasta_destino):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        
    plt.figure(figsize=(10, 6))
    
    dados_por_algoritmo = {}
    for r in resultados:
        alg = r.get('algoritmo', 'Desconhecido')
        if alg not in dados_por_algoritmo:
            dados_por_algoritmo[alg] = {'x': [], 'y': []}
        
        tam_mb = r['tamanho_bytes'] / (1024 * 1024)
        dados_por_algoritmo[alg]['x'].append(tam_mb)
        dados_por_algoritmo[alg]['y'].append(r['throughput_cifrar_MB_s'])
        
    for alg, dados in dados_por_algoritmo.items():
        pontos = sorted(zip(dados['x'], dados['y']))
        x_ordenado = [p[0] for p in pontos]
        y_ordenado = [p[1] for p in pontos]
        
        plt.plot(x_ordenado, y_ordenado, marker='o', linestyle='-', label=alg)
        
    plt.title('Desempenho: Throughput vs Tamanho do Arquivo (Cifragem)')
    plt.xlabel('Tamanho do Arquivo (MB)')
    plt.ylabel('Throughput (MB/s)')
    plt.legend()
    plt.grid(True)
    
    data_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    caminho_grafico = os.path.join(pasta_destino, f'throughput_vs_tamanho_{data_atual}.png')
    
    plt.savefig(caminho_grafico)
    plt.close()
    return caminho_grafico

def gerar_grafico_entropia(resultados, pasta_destino):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        
    plt.figure(figsize=(10, 6))
    
    dados_por_algoritmo = {}
    for r in resultados:
        alg = r.get('algoritmo', 'Desconhecido')
        modo = r.get('modo', 'Desconhecido')
        entropia = r['entropia']
        
        if alg not in dados_por_algoritmo:
            dados_por_algoritmo[alg] = {}
        if modo not in dados_por_algoritmo[alg]:
            dados_por_algoritmo[alg][modo] = []
        dados_por_algoritmo[alg][modo].append(entropia)
        
    modos_ordenados = ["ECB", "CBC", "CFB", "OFB", "CTR"]
    
    for alg, modos_dados in dados_por_algoritmo.items():
        x_vals = []
        y_vals = []
        for modo in modos_ordenados:
            if modo in modos_dados:
                avg_entropia = sum(modos_dados[modo]) / len(modos_dados[modo])
                x_vals.append(modo)
                y_vals.append(avg_entropia)
        if x_vals:
            plt.plot(x_vals, y_vals, marker='s', linestyle='-', label=alg)
            
    plt.title('Segurança: Entropia vs Modo de Operação')
    plt.xlabel('Modo de Operação')
    plt.ylabel('Entropia Média (Shannon)')
    plt.axhline(y=7.0, color='r', linestyle='--', label='Limiar de Padrões (< 7.0)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, axis='y')
    plt.tight_layout()
    
    data_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    caminho_grafico = os.path.join(pasta_destino, f'entropia_vs_modo_{data_atual}.png')
    plt.savefig(caminho_grafico)
    plt.close()
    return caminho_grafico

def gerar_relatorio_md(resultados, caminho_grafico_tp, pasta_destino, caminho_grafico_ent=None):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        
    data_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    caminho_md = os.path.join(pasta_destino, f'relatorio_execucao_{data_atual}.md')
    
    with open(caminho_md, 'w', encoding='utf-8') as f:
        f.write("# Relatório de Testes de Criptografia\n\n")
        f.write(f"**Data da Execução:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
        
        f.write("## 1. Tabela de Desempenho Geral\n\n")
        f.write("| Arquivo | Alg | Modo | Tam (MB) | T. Cifrar (s) | T. Decifrar (s) | Throughput Cif. (MB/s) | Throughput Dec. (MB/s) | Entropia | Padrões |\n")
        f.write("|---------|-----|------|----------|---------------|-----------------|------------------------|------------------------|----------|---------|\n")
        
        for r in resultados:
            tam_mb = r['tamanho_bytes'] / (1024*1024)
            padrao = "⚠️ Sim" if r['padroes_detectados'] else "✅ Não"
            alg = r.get('algoritmo', 'N/A')
            modo = r.get('modo', 'N/A')
            linha = f"| {r.get('arquivo', 'N/A')} | {alg} | {modo} | {tam_mb:.4f} | {r['tempo_cifrar_s']:.4f} | {r['tempo_decifrar_s']:.4f} | {r['throughput_cifrar_MB_s']:.4f} | {r['throughput_decifrar_MB_s']:.4f} | {r['entropia']:.4f} | {padrao} |\n"
            f.write(linha)

        # TABELAS ESPECÍFICAS EXIGIDAS
        f.write("\n## 2. Tabelas Resumo \n\n")
        
        # Comparativo CSV
        f.write("### 2.1. Comparativo de Tempos para Arquivos CSV\n\n")
        f.write("| Arquivo CSV | Algoritmo | Modo | Tamanho (MB) | T. Cifrar (s) | T. Decifrar (s) |\n")
        f.write("|-------------|-----------|------|--------------|---------------|-----------------|\n")
        for r in resultados:
            if str(r.get('arquivo', '')).lower().endswith('.csv'):
                tam_mb = r['tamanho_bytes'] / (1024*1024)
                f.write(f"| {r['arquivo']} | {r.get('algoritmo', '')} | {r.get('modo', '')} | {tam_mb:.4f} | {r['tempo_cifrar_s']:.4f} | {r['tempo_decifrar_s']:.4f} |\n")

        resumo = {}
        for r in resultados:
            chave = (r['algoritmo'], r['modo'])
            if chave not in resumo:
                resumo[chave] = {'tp_cif': [], 'tp_dec': [], 'ent': []}
            resumo[chave]['tp_cif'].append(r['throughput_cifrar_MB_s'])
            resumo[chave]['tp_dec'].append(r['throughput_decifrar_MB_s'])
            resumo[chave]['ent'].append(r['entropia'])

        # Throughput Médio
        f.write("\n### 2.2. Throughput Médio por Algoritmo/Modo\n\n")
        f.write("| Algoritmo | Modo | Throughput Médio Cifrar (MB/s) | Throughput Médio Decifrar (MB/s) |\n")
        f.write("|-----------|------|--------------------------------|----------------------------------|\n")
        for (alg, modo), dados in sorted(resumo.items()):
            avg_tp_cif = sum(dados['tp_cif']) / len(dados['tp_cif'])
            avg_tp_dec = sum(dados['tp_dec']) / len(dados['tp_dec'])
            f.write(f"| {alg} | {modo} | {avg_tp_cif:.4f} | {avg_tp_dec:.4f} |\n")

        # Entropia Média
        f.write("\n### 2.3. Entropia Média por Abordagem\n\n")
        f.write("| Algoritmo | Modo | Entropia Média | Situação de Segurança |\n")
        f.write("|-----------|------|----------------|-----------------------|\n")
        for (alg, modo), dados in sorted(resumo.items()):
            avg_ent = sum(dados['ent']) / len(dados['ent'])
            seg = "✅ Alta" if avg_ent >= 7.5 else "⚠️ Baixa (Padrões Identificados)" if avg_ent < 7.0 else "🆗 Média"
            f.write(f"| {alg} | {modo} | {avg_ent:.4f} | {seg} |\n")
            
        f.write("\n## 3. Gráficos de Análise\n\n")
        nome_grafico_tp = os.path.basename(caminho_grafico_tp)
        f.write(f"### Throughput vs Tamanho\n")
        f.write(f"![Gráfico de Throughput](../graficos/{nome_grafico_tp})\n\n")
        
        if caminho_grafico_ent:
            nome_grafico_ent = os.path.basename(caminho_grafico_ent)
            f.write(f"### Entropia vs Modo de Operação\n")
            f.write(f"![Gráfico de Entropia](../graficos/{nome_grafico_ent})\n")
        
    return caminho_md