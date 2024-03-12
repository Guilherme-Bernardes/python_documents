import requests
from acesso_cep import BuscaEndereco
api=requests.get("https://viacep.com.br/ws/01001000/json/")
cep=28943522
cep=BuscaEndereco(cep)
bairro,cidade,uf=cep.acesso_cep_api()
print(bairro,"-",cidade,"-",uf)
