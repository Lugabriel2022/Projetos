class Personagem():
	def __init__(self, nome, classe, forca, agilidade, resistencia, constituicao, carisma, inteligencia, sabedoria, arcano, fe, sorte):
		self.nome = nome
		self.nivel = 1
		self.vida_max = constituicao * 10
		self.vida = self.vida_max
		self.mana_max = arcano * (inteligencia / 4)
		self.mana = self.mana_max
		self.ataque_fis = 10 * forca
		self.defesa = 10 * ((constituicao * 50 / 100) + (resistencia * 25 / 100))
		self.ataque_m = 10 * (arcano + (inteligencia / 2))
		self.defesa_m = 10 * (arcano * 1.2 + (inteligencia / 4))
		self.classe = classe
		self.forca = forca
		self.resistencia = resistencia
		self.constituicao = constituicao
		self.carisma = carisma
		self.inteligencia = inteligencia
		self.sabedoria = sabedoria
		self.arcano = arcano
		self.fe = fe
		self.sorte = sorte
		self.equipamento = {
			'cabeça' : 'nenhum',
			'torso' : 'nenhum',
			'mãos' : 'nenhum',
			'calças': 'nenhum',
			'luvas' : 'nenhum',
			'botas' : 'nenhum',
			'mão dir' : 'punho',
			'mão esq' : 'punho'
		}
		self.habilidades = {}
		self.posx = 0
		self.posy = 0


	def atacar(self, type= 'fis',mod=1.0):
		if type == 'fis':
			return self.ataque_fis * mod, type

		elif type == 'mag':	
			return self.ataque_m * mod, type

	def tomar_dano(self, dano):
		if dano[1] == 'fis':
			dano_final = max(0, dano[0] - self.defesa)
		elif dano[1] == 'mag':
			dano_final = max(0, dano[0] - self.defesa_m)
		self.vida = max(0, self.vida - dano_final)

	def curar(self, pot):
		cura = self.vida_max * pot
		self.vida = min(self.vida_max, self.vida + cura)

	def equipar_arma(self, arma, slot):
		slots = {
			'dominant': 'mão dir',
			'canhota' : 'mão esq'
		}
		match slot:
			case 'dominant':
				self.equipamento[slots[slot]] = arma
			case 'canhota':
				self.equipamento[slots[slot]] = arma
		self.atualizar_ataque()
	
	def desequipar_arma(self, slot):
		slots = {
			'dominant': 'mão dir',
			'canhota' : 'mão esq'
		}
		self.equipamento[slots[slot]] = 'punho'
		self.atualizar_ataque()
		self.atualizar_ataque()

	def atualizar_ataque(self):
		total = 5
		for slot in ["mão dir", "mão esq"]: 
			arma = self.equipamento[slot] 
			if arma != "punho": total += arma.dano 
		self.ataque = total

	def mover(self, dir):
		if dir == 'frente':
			self.posy += 1
		elif dir == 'trás':
			self.posy -= 1
		elif dir == 'direita':
			self.posx += 1
		elif dir == 'esquerda':
			self.posx -= 1

	def desequipar_armadura(self, armadura):
		slots ={
			'elmo': 'cabeça',
			'peitoral': 'torso',
			'manoplas': 'mãos',
			'grevas': 'calças',
			'botas': 'pés'
		}
		if armadura in slots and self.equipamento[slots[armadura]] != 'Nenhum': 
			slot = slots[armadura] 
			self.defesa -= self.equipamento[slot].defesa 
			self.equipamento[slot] = 'Nenhum'

	def equipar_armadura(self, armadura):
		slots ={
			'elmo': 'cabeça',
			'peitoral': 'torso',
			'manoplas': 'mãos',
			'grevas': 'calças',
			'botas': 'pés'
		}
		if armadura.tipo in slots: 
			slot = slots[armadura.tipo] 
			self.equipamento[slot] = armadura 
			self.defesa += armadura.defesa
			
		pass