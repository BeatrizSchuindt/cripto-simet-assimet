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

def executar_com_metricas(funcao_cripto, arquivo_entrada, arquivo_saida, *args):
    if not os.path.exists(arquivo_entrada):
        raise FileNotFoundError(f"Arquivo não encontrado: {arquivo_entrada}")

    tamanho_bytes = os.path.getsize(arquivo_entrada)
    tempos = []

    for _ in range(10):
        inicio = time.time()
        funcao_cripto(arquivo_entrada, arquivo_saida, *args)
        fim = time.time()
        tempos.append(fim - inicio)

    tempo_medio = sum(tempos) / len(tempos)
    throughput_medio = calcular_throughput(tamanho_bytes, tempo_medio)
    
    entropia_resultado = calcular_entropia(arquivo_saida)
    padroes = detectar_padroes(entropia_resultado)

    return {
        "tamanho_bytes": tamanho_bytes,
        "tempo_medio_s": round(tempo_medio, 4),
        "throughput_MB_s": round(throughput_medio, 4),
        "entropia": round(entropia_resultado, 4),
        "padroes_detectados": padroes
    }

def gerar_grafico_throughput(resultados, pasta_destino):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        
    tamanhos = [res['tamanho_bytes'] / (1024*1024) for res in resultados]
    throughputs = [res['throughput_MB_s'] for res in resultados]
    
    plt.figure(figsize=(10, 6))
    plt.plot(tamanhos, throughputs, marker='o', linestyle='-', color='b')
    plt.title('Desempenho: Throughput vs Tamanho do Arquivo')
    plt.xlabel('Tamanho do Arquivo (MB)')
    plt.ylabel('Throughput (MB/s)')
    plt.grid(True)
    
    caminho_grafico = os.path.join(pasta_destino, 'throughput_vs_tamanho.png')
    plt.savefig(caminho_grafico)
    plt.close()
    return caminho_grafico

def gerar_relatorio_md(resultados, caminho_grafico, pasta_destino):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        
    data_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    caminho_md = os.path.join(pasta_destino, f'relatorio_execucao_{data_atual}.md')
    
    with open(caminho_md, 'w', encoding='utf-8') as f:
        f.write("# Relatório de Testes de Criptografia\n\n")
        f.write(f"**Data da Execução:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
        f.write("## 1. Tabela de Desempenho\n\n")
        f.write("| Arquivo | Algoritmo | Modo | Tamanho (MB) | Tempo Médio (s) | Throughput (MB/s) | Entropia | Padrões Visíveis |\n")
        f.write("|---------|-----------|------|--------------|-----------------|-------------------|----------|------------------|\n")
        
        for r in resultados:
            tam_mb = r['tamanho_bytes'] / (1024*1024)
            padrao = "⚠️ Sim" if r['padroes_detectados'] else "✅ Não"
            algoritmo = r.get('algoritmo', 'N/A')
            modo = r.get('modo', 'N/A')
            linha = f"| {r.get('arquivo', 'N/A')} | {algoritmo} | {modo} | {tam_mb:.4f} | {r['tempo_medio_s']:.4f} | {r['throughput_MB_s']:.4f} | {r['entropia']:.4f} | {padrao} |\n"
            f.write(linha)
            
        f.write("\n## 2. Gráficos de Análise\n\n")
        nome_grafico = os.path.basename(caminho_grafico)
        f.write(f"![Gráfico de Throughput](../graficos/{nome_grafico})\n")
        
    return caminho_md