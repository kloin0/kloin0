import requests 
import json 
# não vai funcionar pq o site ta fora do ar !!!!!!!
link = 'https://api.kloin.repl.co/pagarVendas'
requisicao = requests.get(link)
#print(requisicao.json())
dicionario = requisicao.json()
print(dicionario['totalDeVendas'])

