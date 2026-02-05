class Arma():
    def __init__(self, nome, tipo, dano, mod= 1.0):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano * mod

    def __str__(self):
        return f"Nome: {self.nome} | Tipo: {self.tipo} | Ataque: {self.dano}"

class Armadura():
    def __init__(self, nome, tipo, defesa_fis, defesa_mag, mod= 1.0):
        self.nome = nome
        self.tipo = tipo
        self.protecao_fis = defesa_fis * mod
        self.protecao_mag = defesa_mag * mod

    def __str__(self):
        return f"Nome: {self.nome} | Tipo: {self.tipo} | Defesa Fisica: {self.protecao_fis} | Defesa Magica: {self.protecao_mag}"