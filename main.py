import gerador_massa

TAMANHOS = {
    "1KB": 1024,
    "10KB": 10 * 1024,
    "100KB": 100 * 1024,
    "1MB": 1024 * 1024,
    "10MB": 10 * 1024 * 1024,
    "100MB": 100 * 1024 * 1024,
    "500MB": 500 * 1024 * 1024,
    "1GB": 1024 * 1024 * 1024
}

if __name__ == "__main__":
    print("Iniciando geração de massa de testes...\n")
    gerador_massa.garantir_pasta()
    
    for nome_tamanho, tamanho_bytes in TAMANHOS.items():
        print(f"Gerando lote: {nome_tamanho}...")
        
        # Arquivos de Texto
        gerador_massa.gerar_txt_aleatorio(f"texto_aleatorio_{nome_tamanho}.txt", tamanho_bytes)
        gerador_massa.gerar_txt_repetitivo(f"texto_repetitivo_{nome_tamanho}.txt", tamanho_bytes)
        gerador_massa.gerar_txt_natural(f"texto_natural_{nome_tamanho}.txt", tamanho_bytes)
        
        # Arquivos CSV
        gerador_massa.gerar_csv_repetitivo(f"csv_repetitivo_{nome_tamanho}.csv", tamanho_bytes)
        gerador_massa.gerar_csv_incremental(f"csv_incremental_{nome_tamanho}.csv", tamanho_bytes)
        gerador_massa.gerar_csv_categorico(f"csv_categorico_{nome_tamanho}.csv", tamanho_bytes)
        gerador_massa.gerar_csv_realista(f"csv_realista_{nome_tamanho}.csv", tamanho_bytes)
        
        # Outros formatos
        gerador_massa.gerar_json_repetitivo(f"dados_aninhados_{nome_tamanho}.json", tamanho_bytes)
        gerador_massa.gerar_bmp_padrao(f"imagem_padrao_{nome_tamanho}.bmp", tamanho_bytes)
        
    print("\n[+] Geração concluída! Verifique a pasta 'massa_de_teste'.")