class Feitiço():
    def __init__(self, nome, classe, dano_fisico, dano_magico, dano_elemental, custo, cooldown, preparacao, elemento, msg):
        self.nome = nome
        self.classe = classe
        self.custo = custo
        self.elemento = elemento
        self.preparacao = preparacao
        self.dano_fisico = dano_fisico
        self.dano_magico = dano_magico
        self.dano_elemental = dano_elemental
        self.cooldown = cooldown
        self.dano = 0
        self.msg_use = msg
        self.calcular_dano()

    def calcular_dano(self):
        match self.elemento:
            case 'fogo' | 'agua' | 'ar':
                self.dano = self.dano_magico + self.dano_elemental

            case 'terra' | 'fisico':
                self.dano = self.dano_magico + self.dano_fisico

            case _:
                self.dano = self.dano_magico
        
    def __str__(self):
        return f'''
            Nome: {self.nome} | Classe: {self.classe} | Custo: {self.custo}
            Elemento: {self.elemento} | Dano: {self.dano} | Preparação: {self.preparacao}
        '''
        
class Habilidade():
    def __init__(self, nome, dano_fisico, dano_elemental, custo, cooldown, msg):
        self.nome = nome
        self.dano_fisico = dano_fisico
        self.dano_elemental = dano_elemental
        self.custo = custo
        self.cooldown = cooldown
        self.dano = 0
        self.msg_use = msg
        self.calcular_dano()

    def calcular_dano(self):
        self.dano = self.dano_fisico + self.dano_elemental

    def __str__(self):
        return f'''
            Nome: {self.nome} | Custo: {self.custo}
            Dano: {self.dano} 
        '''

