import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

KEY = RSA.generate(2048)
CHAVE_PUB = PKCS1_OAEP.new(KEY.publickey())
CHAVE_PRIV = PKCS1_OAEP.new(KEY)

TAM_INPUT = 214  # O que lemos do arquivo original
TAM_OUTPUT = 256 # O que o RSA gera (bloco cifrado)

def xor_bytes(b1, b2):
    """Realiza XOR entre dois conjuntos de bytes."""
    return bytes(a ^ b for a, b in zip(b1, b2))

def cifrar_arquivo_rsa(arquivo_entrada, arquivo_saida, modo_nome):
    """Implementação acadêmica de modos de operação para RSA."""
    with open(arquivo_entrada, 'rb') as f_in, open(arquivo_saida, 'wb') as f_out:
        
        if modo_nome == "ECB":
            while True:
                chunk = f_in.read(TAM_INPUT)
                if not chunk: break
                f_out.write(CHAVE_PUB.encrypt(chunk))

        elif modo_nome == "CBC":
            iv = get_random_bytes(TAM_INPUT)
            f_out.write(iv) # O IV precisa ir no arquivo para o decifrador usar
            ultimo_bloco_cifrado = iv
            
            while True:
                chunk = f_in.read(TAM_INPUT)
                if not chunk: break
            
                preparado = xor_bytes(chunk, ultimo_bloco_cifrado[:len(chunk)])
                cifrado = CHAVE_PUB.encrypt(preparado)
                f_out.write(cifrado)
                ultimo_bloco_cifrado = cifrado

        elif modo_nome == "CTR":
            contador = 0
            while True:
                chunk = f_in.read(TAM_INPUT) 
                if not chunk: break

                keystream = CHAVE_PUB.encrypt(contador.to_bytes(TAM_INPUT, 'big'))

                f_out.write(xor_bytes(chunk, keystream))
                contador += 1

def decifrar_arquivo_rsa(arquivo_entrada, arquivo_saida, modo_nome):
    """Reverte o processo de cifragem."""
    with open(arquivo_entrada, 'rb') as f_in, open(arquivo_saida, 'wb') as f_out:
        
        if modo_nome == "ECB":
            while True:
                chunk = f_in.read(TAM_OUTPUT) # Lemos o bloco "cheio" do RSA
                if not chunk: break
                f_out.write(CHAVE_PRIV.decrypt(chunk))

        elif modo_nome == "CBC":
            iv = f_in.read(TAM_INPUT)
            ultimo_bloco_cifrado = iv
            while True:
                chunk = f_in.read(TAM_OUTPUT)
                if not chunk: break
                decifrado_pre = CHAVE_PRIV.decrypt(chunk)
                f_out.write(xor_bytes(decifrado_pre, ultimo_bloco_cifrado))
                ultimo_bloco_cifrado = chunk

        elif modo_nome == "CTR":
            f_in.close() # Fecha para reabrir na função de cifrar
            cifrar_arquivo_rsa(arquivo_entrada, arquivo_saida, "CTR")