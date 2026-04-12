import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

def gerar_chave(tamanho_bits):
    return RSA.generate(tamanho_bits)

def get_tamanhos(chave_rsa):
    tamanho_bits = chave_rsa.size_in_bits()
    tam_output = tamanho_bits // 8
    tam_input = tam_output - 42 # Overhead do PKCS1_OAEP
    return tam_input, tam_output

def xor_bytes(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))

def cifrar_arquivo_rsa(arquivo_entrada, arquivo_saida, modo_nome, chave_rsa):
    chave_pub = PKCS1_OAEP.new(chave_rsa.publickey())
    tam_input, _ = get_tamanhos(chave_rsa)

    with open(arquivo_entrada, 'rb') as f_in, open(arquivo_saida, 'wb') as f_out:
        
        if modo_nome == "ECB":
            while True:
                chunk = f_in.read(tam_input)
                if not chunk: break
                f_out.write(chave_pub.encrypt(chunk))

        elif modo_nome == "CBC":
            iv = get_random_bytes(tam_input)
            f_out.write(iv) # O IV precisa ir no arquivo para o decifrador usar
            ultimo_bloco_cifrado = iv
            
            while True:
                chunk = f_in.read(tam_input)
                if not chunk: break
            
                preparado = xor_bytes(chunk, ultimo_bloco_cifrado[:len(chunk)])
                cifrado = chave_pub.encrypt(preparado)
                f_out.write(cifrado)
                ultimo_bloco_cifrado = cifrado

        elif modo_nome == "CTR":
            contador = 0
            while True:
                chunk = f_in.read(tam_input) 
                if not chunk: break

                keystream = chave_pub.encrypt(contador.to_bytes(tam_input, 'big'))

                f_out.write(xor_bytes(chunk, keystream))
                contador += 1

def decifrar_arquivo_rsa(arquivo_entrada, arquivo_saida, modo_nome, chave_rsa):
    """Reverte o processo de cifragem."""
    chave_priv = PKCS1_OAEP.new(chave_rsa)
    tam_input, tam_output = get_tamanhos(chave_rsa)

    with open(arquivo_entrada, 'rb') as f_in, open(arquivo_saida, 'wb') as f_out:
        
        if modo_nome == "ECB":
            while True:
                chunk = f_in.read(tam_output)
                if not chunk: break
                f_out.write(chave_priv.decrypt(chunk))

        elif modo_nome == "CBC":
            iv = f_in.read(tam_input)
            ultimo_bloco_cifrado = iv
            while True:
                chunk = f_in.read(tam_output)
                if not chunk: break
                decifrado_pre = chave_priv.decrypt(chunk)
                f_out.write(xor_bytes(decifrado_pre, ultimo_bloco_cifrado))
                ultimo_bloco_cifrado = chunk

        elif modo_nome == "CTR":
            f_in.close() # Fecha para reabrir na função de cifrar
            f_out.close()
            cifrar_arquivo_rsa(arquivo_entrada, arquivo_saida, "CTR", chave_rsa)