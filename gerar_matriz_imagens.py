import os
import io
from PIL import Image, ImageDraw, ImageFont

def recuperar_imagem_cifrada(caminho_original, caminho_cifrado):
    try:
        with open(caminho_original, 'rb') as f_orig:
            cabecalho = f_orig.read(54)
            
        with open(caminho_cifrado, 'rb') as f_cif:
            dados_cifrados = f_cif.read()
        
        img_bytes = cabecalho + dados_cifrados[54:]
        
        return Image.open(io.BytesIO(img_bytes)).convert('RGB')
    except Exception as e:
        print(f"Erro ao recuperar {caminho_cifrado}: {e}")
        return None

def gerar_matrizes(pasta_massa, pasta_outputs, pasta_graficos):
    if not os.path.exists(pasta_graficos):
        os.makedirs(pasta_graficos)

    arquivos_massa = [f for f in os.listdir(pasta_massa) if f.lower().endswith('.bmp')]
    if not arquivos_massa:
        return

    algoritmos = ["AES-128", "DES"] 
    modos = ["ECB", "CBC", "CTR"]
    
    # Tamanho padrão para que as imagens fiquem visíveis no relatório
    TAMANHO_CELULA = (256, 256)

    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()

    for arquivo_bmp in arquivos_massa:
        caminho_original = os.path.join(pasta_massa, arquivo_bmp)
        
        for alg in algoritmos:
            # Carrega a original e dá o "zoom" preservando os pixels duros (NEAREST)
            img_original = Image.open(caminho_original).convert('RGB')
            img_original = img_original.resize(TAMANHO_CELULA, Image.NEAREST)
            celulas = [(img_original, "ORIGINAL")]
            
            for modo in modos:
                nome_cifrado = f"cifrado_{alg}_{modo}_{arquivo_bmp}"
                caminho_cifrado = os.path.join(pasta_outputs, nome_cifrado)
                
                if os.path.exists(caminho_cifrado):
                    img_cifrada = recuperar_imagem_cifrada(caminho_original, caminho_cifrado)
                    if img_cifrada:
                        # Redimensiona a cifrada do mesmo jeito
                        img_cifrada = img_cifrada.resize(TAMANHO_CELULA, Image.NEAREST)
                        celulas.append((img_cifrada, f"{alg} ({modo})"))
            
            if len(celulas) > 1:
                # Agora usamos o tamanho fixo da célula
                largura_img, altura_img = TAMANHO_CELULA
                espaco_texto = 40
                largura_total = largura_img * len(celulas)
                altura_total = altura_img + espaco_texto
                
                matriz = Image.new('RGB', (largura_total, altura_total), (255, 255, 255))
                draw = ImageDraw.Draw(matriz)
                
                for i, (img, legenda) in enumerate(celulas):
                    x_offset = i * largura_img
                    matriz.paste(img, (x_offset, espaco_texto))
                    
                    try:
                        w_texto = draw.textlength(legenda, font=font)
                    except AttributeError:
                        w_texto = len(legenda) * 10
                        
                    # Centraliza o texto no topo de cada imagem
                    draw.text((x_offset + (largura_img - w_texto)//2, 10), legenda, fill=(0, 0, 0), font=font)

                nome_saida = f"matriz_visual_{alg}_{arquivo_bmp.replace('.bmp', '.png')}"
                caminho_saida = os.path.join(pasta_graficos, nome_saida)
                matriz.save(caminho_saida)
                print(f"[+] Matriz visual comparativa gerada: {caminho_saida}")

if __name__ == "__main__":
    gerar_matrizes("massa_de_teste", "outputs", "relatorios/graficos")