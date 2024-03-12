import requests


class BuscaEndereco:
    def __init__(self,cep):
        cep=str(cep)
        if self.valida_cep(cep):
            self.cep=cep
        else:
            raise ValueError("CEP Invalido!!")
        self.acesso_cep_api()

    def __str__(self):
        return self.formata_cep()
    def valida_cep(self,cep):
        if len(cep)==8:
            return True
        else:
            return False
    def formata_cep(self):
        cep_formatado=f"{self.cep[:5]}-{self.cep[5:]}"
        return cep_formatado
    def acesso_cep_api(self):
        url=(f"https://viacep.com.br/ws/{self.cep}/json/")
        site=requests.get(url)
        dados=site.json()
        return (dados["bairro"],dados["localidade"],dados["uf"])


