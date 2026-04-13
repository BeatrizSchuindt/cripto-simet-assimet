# Análise Comparativa de Algoritmos Criptográficos

**Autoras:** Ana Beatriz Schuindt do Amaral e Emmylly Maria dos Santos Oliveira  
**Ano:** 2026  

## 📌 Sobre o Projeto
Este projeto é uma esteira automatizada de testes desenvolvida em Python para avaliar o desempenho e a segurança de algoritmos criptográficos. O sistema realiza uma análise comparativa entre:
* **Criptografia Simétrica:** AES (128 e 256 bits), DES e 3DES.
* **Criptografia Assimétrica:** RSA (1024, 2048 e 4096 bits).
* **Modos de Operação:** ECB, CBC, CFB, OFB e CTR.

O programa gera sua própria massa de dados (arquivos TXT, CSV, JSON, XML e imagens BMP em várias escalas de tamanho), aplica as rotinas de cifragem e decifragem, e extrai métricas rigorosas. Os principais entregáveis gerados automaticamente são:
1. Tabelas de Throughput (MB/s) e Tempo de Execução.
2. Cálculo de **Entropia de Shannon** para detecção de vazamentos estatísticos.
3. Geração de relatórios em Markdown e gráficos comparativos.
4. **Matriz Visual de Imagens:** Comprovação prática da vulnerabilidade do modo ECB (preservação de padrões) em contraste com o ruído gerado pelos modos encadeados (CBC, CTR).

---

## 🚀 Como Executar

Para rodar o projeto localmente, é recomendado o uso de um ambiente virtual (venv) para isolar as dependências (como `PyCryptodome`, `Pillow` e `Matplotlib`). Siga os passos abaixo no seu terminal:

### 1. Criar o Ambiente Virtual
Na raiz do projeto, execute o comando para criar a venv:
```bash
python -m venv .venv
```

### 2. Ativar o Ambiente Virtual
No Windows:

```bash
.venv\Scripts\activate
```
No Linux/Mac:

```bash
source .venv/bin/activate
```
### 3. Instalar as Dependências
Com a venv ativada, instale as bibliotecas necessárias contidas no arquivo de requisitos:

```bash
pip install -r requirements.txt
```
### 4. Executar os Testes
Para iniciar a esteira de testes, basta rodar o arquivo principal:

```bash
python main.py
```
Siga as instruções no menu interativo do terminal para escolher os tamanhos e tipos de arquivos que deseja gerar e testar.

##  📁 Estrutura de Pastas
A arquitetura do projeto está organizada da seguinte forma:

```
CRIPTO-SIMET-ASSIMET/
│
├── algoritmos/                 # Módulos de criptografia
│   ├── __init__.py
│   ├── assimetricos.py         # Lógica de cifragem/decifragem RSA
│   └── simetricos.py           # Lógica de cifragem/decifragem AES, DES e 3DES
│
├── massa_de_teste/             # Arquivos originais gerados para os testes (TXT, CSV, BMP, etc.)
│
├── outputs/                    # Arquivos cifrados e decifrados gerados durante a execução
│
├── relatorios/                 # Entregáveis automáticos do sistema
│   ├── graficos/               # Gráficos PNG (Throughput, Entropia e Matrizes de Imagens)
│   └── md/                     # Relatórios consolidados em Markdown
│
├── gerador_massa.py            # Script responsável por criar os arquivos de teste em vários tamanhos
├── gerar_matriz_imagens.py     # Script que reconstrói cabeçalhos BMP e monta o painel visual
├── main.py                     # Ponto de entrada que orquestra a execução de todo o fluxo
├── metricas.py                 # Lógica de cálculo de tempo, throughput, entropia e geração de tabelas
├── requirements.txt            # Lista de dependências do Python
└── README.md                   # Documentação do projeto
```
