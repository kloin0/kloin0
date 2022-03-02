from hashlib import sha256
import time 
def apli_sha256(texto): 
    return sha256("abc".encode("ascii")).hexdigest()

def mine(bloco,trans,hash_a,qtd_z):
    nonce = 0 
    while True:
        texto = str(bloco) + trans + hash_a + str(nonce)
        m_hash = apli_sha256(texto)
        if m_hash.startswith("0"*qtd_z):
            return nonce, m_hash 
        nonce += 1

if __name__ == "__main__":
    bloco = 15
    trans = '''
    Gustavo-> Henrique
    Alves-> Silva
    Carlos-> João'''
    qtd_z = 0
    hash_a = "abc"
    resultado = mine(bloco,trans,hash_a,qtd_z)
    print(resultado)
