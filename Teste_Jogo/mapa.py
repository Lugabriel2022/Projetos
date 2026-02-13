class Sala():
    def __init__(self, largura, comprimento):
        self.largura = largura
        self.comprimento = comprimento
        self.sala = {}  # inicializa vazio
        
    def gerar_sala(self):
        # cria um grid de coordenadas com valor "vazio"
        self.sala = {(x, y): "vazio" 
                     for x in range(self.largura) 
                     for y in range(self.comprimento)}
        return self.sala
        
    def preencher_ponto(self, x, y, objeto):
        if (x, y) in self.sala:
            self.sala[(x, y)] = objeto
        else:
            print("Coordenada fora da sala!")

    def preencher_area(self, x, y, largura, altura, objeto):
         """Preenche uma área retangular com o mesmo objeto""" 
         for i in range(x, x + largura): 
            for j in range(y, y + altura): 
                if (i, j) in self.sala: 
                    self.sala[(i, j)] = objeto

    def mostrar_sala(self): 
        for y in range(self.comprimento): 
            linha = "" 
            for x in range(self.largura):
                try: 
                    linha += f"{self.sala[(x, y)].nome:^7}"

                except Exception as e:
                    linha += f"{self.sala[(x, y)]:^7}"

            print(linha)

class Tile():
    def __init__(self, nome, custo= 1, passavel= True, dano= 0):
        self.nome = nome
        self.custo = custo
        self.passavel = passavel
        self.dano = dano

    def __str__(self):
        return f"Nome: {self.nome}"