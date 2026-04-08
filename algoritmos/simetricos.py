import os
from Crypto.Cipher import AES, DES, DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

ALGORITMOS = {
    "AES-128": {"module": AES, "key_size": 16, "block_size": 16},
    "AES-256": {"module": AES, "key_size": 32, "block_size": 16},
    "DES": {"module": DES, "key_size": 8, "block_size": 8},
    "3DES": {"module": DES3, "key_size": 24, "block_size": 8}
}

MODOS = {
    "ECB": AES.MODE_ECB,
    "CBC": AES.MODE_CBC,
    "CFB": AES.MODE_CFB,
    "OFB": AES.MODE_OFB,
    "CTR": AES.MODE_CTR
}

TAMANHO_CHUNK = 64 * 1024

def gerar_chave(algoritmo_nome):
    key_size = ALGORITMOS[algoritmo_nome]["key_size"]
    return get_random_bytes(key_size)

def cifrar_arquivo(arquivo_entrada, arquivo_saida, algoritmo_nome, modo_nome, chave=None):
    alg_info = ALGORITMOS[algoritmo_nome]
    CipherModule = alg_info["module"]
    block_size = alg_info["block_size"]
    
    if chave is None:
        chave = gerar_chave(algoritmo_nome)
        
    modo = MODOS[modo_nome]
    
    if modo == CipherModule.MODE_ECB:
        cipher = CipherModule.new(chave, modo)
        iv_nonce = b''
    elif modo == CipherModule.MODE_CTR:
        nonce_tamanho = block_size // 2
        iv_nonce = get_random_bytes(nonce_tamanho)
        cipher = CipherModule.new(chave, modo, nonce=iv_nonce)
    else:
        iv_nonce = get_random_bytes(block_size)
        cipher = CipherModule.new(chave, modo, iv_nonce)
        
    needs_padding = modo in [CipherModule.MODE_ECB, CipherModule.MODE_CBC]
    file_size = os.path.getsize(arquivo_entrada)
    
    with open(arquivo_entrada, 'rb') as f_in, open(arquivo_saida, 'wb') as f_out:
        f_out.write(iv_nonce)
        
        bytes_lidos = 0
        while bytes_lidos < file_size:
            chunk = f_in.read(TAMANHO_CHUNK)
            bytes_lidos += len(chunk)
            
            if bytes_lidos == file_size and needs_padding:
                chunk = pad(chunk, block_size)
                
            f_out.write(cipher.encrypt(chunk))

def decifrar_arquivo(arquivo_entrada, arquivo_saida, algoritmo_nome, modo_nome, chave):
    alg_info = ALGORITMOS[algoritmo_nome]
    CipherModule = alg_info["module"]
    block_size = alg_info["block_size"]
    modo = MODOS[modo_nome]
    
    with open(arquivo_entrada, 'rb') as f_in, open(arquivo_saida, 'wb') as f_out:
        if modo == CipherModule.MODE_ECB:
            cipher = CipherModule.new(chave, modo)
        elif modo == CipherModule.MODE_CTR:
            nonce_tamanho = block_size // 2
            nonce = f_in.read(nonce_tamanho)
            cipher = CipherModule.new(chave, modo, nonce=nonce)
        else:
            iv = f_in.read(block_size)
            cipher = CipherModule.new(chave, modo, iv)
            
        needs_padding = modo in [CipherModule.MODE_ECB, CipherModule.MODE_CBC]
        file_size = os.path.getsize(arquivo_entrada)
        bytes_lidos = f_in.tell()
        
        while bytes_lidos < file_size:
            chunk = f_in.read(TAMANHO_CHUNK)
            bytes_lidos += len(chunk)
            
            decrypted_chunk = cipher.decrypt(chunk)
            
            if bytes_lidos == file_size and needs_padding:
                decrypted_chunk = unpad(decrypted_chunk, block_size)
                
            f_out.write(decrypted_chunk)