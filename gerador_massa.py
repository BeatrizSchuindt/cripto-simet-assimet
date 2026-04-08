import os
import json
import random
import numpy as np
from PIL import Image

PASTA_SAIDA = "massa_de_teste"
TAMANHO_CHUNK = 1024 * 1024

def garantir_pasta():
    if not os.path.exists(PASTA_SAIDA):
        os.makedirs(PASTA_SAIDA)

def gerar_txt_aleatorio(nome_arquivo, tamanho_alvo):
    caminho = os.path.join(PASTA_SAIDA, nome_arquivo)
    bytes_escritos = 0
    with open(caminho, 'wb') as f:
        while bytes_escritos < tamanho_alvo:
            escrever = min(TAMANHO_CHUNK, tamanho_alvo - bytes_escritos)
            f.write(os.urandom(escrever))
            bytes_escritos += escrever

def gerar_txt_repetitivo(nome_arquivo, tamanho_alvo):
    caminho = os.path.join(PASTA_SAIDA, nome_arquivo)
    padrao = "Ana_Beatriz_e_Emmylly_Criptografia_2026_" * 10
    padrao_bytes = padrao.encode('utf-8')
    bytes_escritos = 0
    with open(caminho, 'wb') as f:
        while bytes_escritos < tamanho_alvo:
            escrever = min(TAMANHO_CHUNK, tamanho_alvo - bytes_escritos)
            multiplicador = escrever // len(padrao_bytes) + 1
            f.write((padrao_bytes * multiplicador)[:escrever])
            bytes_escritos += escrever

def gerar_txt_natural(nome_arquivo, tamanho_alvo):
    caminho = os.path.join(PASTA_SAIDA, nome_arquivo)
    texto_natural = "A criptografia e essencial para garantir a confidencialidade e a integridade dos dados em sistemas modernos. " * 50
    padrao_bytes = texto_natural.encode('utf-8')
    bytes_escritos = 0
    with open(caminho, 'wb') as f:
        while bytes_escritos < tamanho_alvo:
            escrever = min(TAMANHO_CHUNK, tamanho_alvo - bytes_escritos)
            multiplicador = escrever // len(padrao_bytes) + 1
            f.write((padrao_bytes * multiplicador)[:escrever])
            bytes_escritos += escrever

def gerar_csv_repetitivo(nome_arquivo, tamanho_alvo):
    caminho = os.path.join(PASTA_SAIDA, nome_arquivo)
    linha_padrao = "1001,Produto_Teste,Eletronicos,199.99,Ativo\n"
    linha_bytes = linha_padrao.encode('utf-8')
    bytes_escritos = 0
    with open(caminho, 'wb') as f:
        cabecalho = "ID,Nome,Categoria,Preco,Status\n".encode('utf-8')
        f.write(cabecalho)
        bytes_escritos += len(cabecalho)
        while bytes_escritos < tamanho_alvo:
            escrever = min(TAMANHO_CHUNK, tamanho_alvo - bytes_escritos)
            multiplicador = escrever // len(linha_bytes) + 1
            f.write((linha_bytes * multiplicador)[:escrever])
            bytes_escritos += escrever

def gerar_csv_incremental(nome_arquivo, tamanho_alvo):
    caminho = os.path.join(PASTA_SAIDA, nome_arquivo)
    bytes_escritos = 0
    contador = 1
    with open(caminho, 'wb') as f:
        cabecalho = "ID,Timestamp,Contador\n".encode('utf-8')
        f.write(cabecalho)
        bytes_escritos += len(cabecalho)
        while bytes_escritos < tamanho_alvo:
            linhas = []
            for _ in range(10000):
                linhas.append(f"{contador},2026-04-08T10:00:00Z,{contador*10}\n")
                contador += 1
            bloco_bytes = "".join(linhas).encode('utf-8')
            escrever = min(len(bloco_bytes), tamanho_alvo - bytes_escritos)
            f.write(bloco_bytes[:escrever])
            bytes_escritos += escrever

def gerar_csv_categorico(nome_arquivo, tamanho_alvo):
    caminho = os.path.join(PASTA_SAIDA, nome_arquivo)
    bytes_escritos = 0
    cores = ["Vermelho", "Azul", "Verde", "Amarelo", "Preto", "Branco"]
    estados = ["SP", "RJ", "MG", "BA", "PR", "SC", "RS", "MT"]
    tipos = ["A", "B", "C", "D"]
    linhas_base = [f"{random.choice(cores)},{random.choice(estados)},{random.choice(tipos)}\n" for _ in range(20000)]
    bloco_bytes = "".join(linhas_base).encode('utf-8')
    with open(caminho, 'wb') as f:
        cabecalho = "Cor,Estado,Tipo\n".encode('utf-8')
        f.write(cabecalho)
        bytes_escritos += len(cabecalho)
        while bytes_escritos < tamanho_alvo:
            escrever = min(len(bloco_bytes), tamanho_alvo - bytes_escritos)
            f.write(bloco_bytes[:escrever])
            bytes_escritos += escrever

def gerar_csv_realista(nome_arquivo, tamanho_alvo):
    caminho = os.path.join(PASTA_SAIDA, nome_arquivo)
    bytes_escritos = 0
    contador = 1
    nomes = ["Ana", "Beatriz", "Carlos", "Daniel", "Emmylly", "Fernanda", "Gabriel", "Helena"]
    setores = ["TI", "RH", "Vendas", "Marketing", "Diretoria", "Operacoes"]
    with open(caminho, 'wb') as f:
        cabecalho = "ID_Funcionario,Nome,Setor,Salario,Data_Admissao\n".encode('utf-8')
        f.write(cabecalho)
        bytes_escritos += len(cabecalho)
        while bytes_escritos < tamanho_alvo:
            tamanho_lote = 15000
            nomes_lote = random.choices(nomes, k=tamanho_lote)
            setores_lote = random.choices(setores, k=tamanho_lote)
            linhas = []
            for i in range(tamanho_lote):
                salario = 3000 + (contador % 50) * 100
                linhas.append(f"{contador},{nomes_lote[i]},{setores_lote[i]},{salario:.2f},202{contador%6}-0{1+(contador%9)}-10\n")
                contador += 1
            bloco_bytes = "".join(linhas).encode('utf-8')
            escrever = min(len(bloco_bytes), tamanho_alvo - bytes_escritos)
            f.write(bloco_bytes[:escrever])
            bytes_escritos += escrever

def gerar_json_repetitivo(nome_arquivo, tamanho_alvo):
    caminho = os.path.join(PASTA_SAIDA, nome_arquivo)
    registro = {"usuario": {"id": "1001", "nome": "Usuario_Teste", "permissoes": ["leitura", "escrita"], "metadados": {"ativo": True, "regiao": "BR-MT"}}}
    linha_json = json.dumps(registro) + ",\n"
    linha_bytes = linha_json.encode('utf-8')
    bytes_escritos = 0
    with open(caminho, 'wb') as f:
        cabecalho = b"[\n"
        f.write(cabecalho)
        bytes_escritos += len(cabecalho)
        while bytes_escritos < tamanho_alvo - 2:
            escrever = min(TAMANHO_CHUNK, tamanho_alvo - bytes_escritos - 2)
            multiplicador = escrever // len(linha_bytes) + 1
            f.write((linha_bytes * multiplicador)[:escrever])
            bytes_escritos += escrever
        f.write(b"]")

def gerar_bmp_padrao(nome_arquivo, tamanho_alvo_aproximado):
    caminho = os.path.join(PASTA_SAIDA, nome_arquivo)
    pixels_totais = tamanho_alvo_aproximado // 3
    lado = int(np.sqrt(pixels_totais))
    matriz = np.zeros((lado, lado, 3), dtype=np.uint8)
    for i in range(lado):
        if i % 20 < 10:
            matriz[i, :] = [255, 0, 0]
        else:
            matriz[i, :] = [0, 0, 255]
    img = Image.fromarray(matriz)
    img.save(caminho, format='BMP')