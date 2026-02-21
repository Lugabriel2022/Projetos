class ArmaObjeto():
    def __init__(self, nome, dano_fisico, dano_magico, dano_elemental, valor, desc, mod=1.0):
        self.nome = nome
        self.dano_fisico = dano_fisico
        self.dano_magico = dano_magico
        self.dano_elemental = dano_elemental
        self.dano = 0
        self.mod = mod
        self.valor = valor
        self.desc = desc # descrição
        self.tags = []
        self.calcular_dano()

    def calcular_dano(self):
        self.dano = self.dano_magico + self.dano_fisico + self.dano_elemental * self.mod

    def set_tags(self, *tags):
        self.tags.extend(tags)

    def expor_dados(self):
        return {'dano_fisico': self.dano_fisico, 'dano_magico': self.dano_magico, 'dano_elemental': self.dano_elemental, 'dano_total': self.dano}

class ArmaduraObjeto():
    def __init__(self, nome, tipo, defesa_fis, defesa_mag, valor, desc, mod= 1.0):
        self.nome = nome
        self.tipo = tipo
        self.protecao_fis = defesa_fis * mod
        self.protecao_mag = defesa_mag * mod
        self.defesa_abs = 0
        self.valor = valor
        self.mod = mod
        self.desc = desc # descrição
        self.calcular_defesa()

    def calcular_defesa(self):
        self.defesa_abs = self.protecao_fis + self.protecao_mag * self.mod

    def __str__(self):
        return f"Nome: {self.nome} | Tipo: {self.tipo} | Defesa Fisica: {self.protecao_fis} | Defesa Magica: {self.protecao_mag}"

class FireweaponObjeto():
    def __init__(self, nome, tipo, dano_fisico, dano_magico, dano_elemental, alcance, custo, municao, precisao, desc, mod= 1.0):
        self.nome = nome
        self.tipo = tipo
        self.dano_fisico = dano_fisico
        self.dano_magico = dano_magico
        self.dano_elemental = dano_elemental
        self.mod = mod
        self.municao_max = municao
        self.municao = self.municao_max
        self.custo = custo
        self.alcance = alcance
        self.dano = 0
        self.desc = desc # descrição[
        self.precisao = max(0, min(precisao, 100))
        self.tags = []
        self.calcular_dano()

    def calcular_dano(self):
        self.dano = self.dano_fisico + self.dano_magico + self.dano_elemental * self.mod

    def set_tags(self, *tags):
        self.tags.extend(tags)
        return self

    def expor_dados(self):
        return {
            'dano_fisico': self.dano_fisico, 'dano_magico': self.dano_magico, 'dano_elemental': self.dano_elemental, 'dano_total': self.dano, 'precisao': self.precisao,
            'municao': self.municao, 'carregador': self.municao_max
            }

class ConsumivelObjeto():
    def __init__(self, nome, valor_rec, att_target, valor_buy, desc):
        self.nome = nome
        self.valor_rec = valor_rec # Valor Recuperado
        self.att_target = att_target # Atributo Alvo
        self.valor_buy = valor_buy # Valor em ouro do item
        self.desc = desc # descrição do item

    def usar_item(self):
        return self.nome, self.valor_rec, self.att_target, 1 
