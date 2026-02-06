class Personagem():
	SLOTS_ARMADURA = { 
		'elmo': 'cabeça', 
		'peitoral': 'torso', 
		'manoplas': 'luvas', 
		'grevas': 'calças', 
		'botas': 'botas'
		}

	def __init__(self, nome, classe, raca, forca, agilidade, resistencia, constituicao, carisma, inteligencia, sabedoria, arcano, fe, sorte):
		self.nome = nome
		self.nivel = 1
		self.raca = raca
		self.vida_max = constituicao * 10
		self.vida = self.vida_max
		self.mana_max = arcano * (inteligencia / 4)
		self.mana = self.mana_max
		self.estamina_max = 10 * resistencia
		self.estamina = self.estamina_max
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
			'calças': 'nenhum',
			'luvas' : 'nenhum',
			'botas' : 'nenhum',
			'mão dir' : 'punho',
			'mão esq' : 'punho'
		}
		self.habilidades = {}
		self.magias = {}
		self.inventario = None
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

	def atualizar_ataque(self):
		self.ataque_fis = 10 * self.forca
		self.ataque_m = 10 * (self.arcano + (self.inteligencia / 2))
		for slot in ["mão dir", "mão esq"]: 
			arma = self.equipamento[slot] 
			if arma != "punho":
				if arma.tipo == "fis":
					self.ataque_fis += arma.dano
				elif arma.tipo == 'mag':
					self.ataque_m += arma.dano

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
		slot = self.SLOTS_ARMADURA.get(tipo)
		if slot and self.equipamento[slot] != 'nenhum': 
			armadura = self.equipamento[slot] 
			self.defesa -= armadura.protecao_fis
			self.defesa_m -= armadura.protecao_mag
			self.equipamento[slot] = 'nenhum'

	def equipar_armadura(self, armadura):
		slot = self.SLOTS_ARMADURA.get(armadura.tipo)
		if slot:
			if self.equipamento[slot] != 'nenhum':
				antiga = self.equipamento[slot]
				self.defesa_m -= antiga.protecao_mag
				self.defesa -= antiga.protecao_fis

			self.equipamento[slot] = armadura
			self.defesa_m += armadura.protecao_mag
			self.defesa += armadura.protecao_fis

	def usar_habilidade(self, nome):
		habilidade = self.habilidades.get(nome)
		if not habilidade:
			return f"Habilidade {nome} não encontrada"

		if self.estamina < habilidade.custo:
			return f"estamina insuficiente para usar {habilidade.nome}"

		# Consome estamina
		self.estamina -= habilidade.custo

		if habilidade.tipo == "ofensiva":
			return self.atacar(mod=habilidade.dano)

		elif habilidade.tipo == "cura":
			self.curar(habilidade.dano)
			return f"{self.nome} recuperou {habilidade.dano * self.vida_max} de vida com {habilidade.nome}"

	def usar_magia(self, nome):
		magia = self.magias.get(nome)
		if not magia:
			return f"Magia {nome} não encontrada"

		if self.mana < magia.custo:
			return f"mana insuficiente para usar {magia.nome}"

		# Consome mana
		self.mana -= magia.custo

		if magia.tipo == "ofensiva":
			return self.atacar(mod=magia.dano)

		elif magia.tipo == "cura":
			self.curar(magia.dano)
			return f"{self.nome} recuperou {magia.dano * self.vida_max} de vida com {magia.nome}"

	def recuperar_mana(self):
		regen = self.mana_max / 100 + ((self.arcano + self.inteligencia) / 100)
		if self.mana < self.mana_max:
			self.mana += regen
		else:
			self.mana = self.mana_max

	def recuperar_estamina(self):
		regen = self.estamina_max / 100 + ((self.resistencia + self.constituicao + self.agilidade) / 100)
		
		if self.estamina < self.estamina_max:
			self.estamina += regen

		else:
			self.estamina = self.estamina_max
	
	def __str__(self):
		equipamentos = ", ".join( 
            f"{slot}: {str(item) if item else 'Nenhum'}" 
        for slot, item in self.equipamento.items() )
		return (
			f"Nome: {self.nome} | Classe: {self.classe} | Nivel: {self.nivel}"
			f"Vida: {self.vida} | Mana: {self.mana} | Estamina: {self.estamina}"
			f"Ataque Fisico: {self.ataque_fis} | Ataque Magico: {self.ataque_m}"
			f"Defesa Fisica: {self.defesa} | Defesa Magica: {self.defesa_m}"
			f"Equipamento: {equipamentos}" 
		)

class Monstro():
	def __init__(self, nome, tamanho, raca, forca, agilidade, resistencia, constituicao, carisma, inteligencia, sabedoria, arcano, fe, sorte):
		size = {'minusculo': 0.8,'pequeno': 1.0, 'medio': 2.3, 'grande': 3.0, 'colossal': 3.5, 'gargantua': 4.0, 'cosmico': 10.0}
		self.nome = nome
		self.raca = raca
		self.forca = forca * size[tamanho]
		self.resistencia = resistencia * size[tamanho]
		self.constituicao = constituicao
		self.carisma = carisma * size[tamanho]
		self.inteligencia = inteligencia * size[tamanho]
		self.sabedoria = sabedoria * size[tamanho]
		self.arcano = arcano * size[tamanho]
		self.fe = fe
		self.sorte = sorte
		self.vida_max = constituicao * 10
		self.vida = self.vida_max
		self.mana_max = arcano * (inteligencia / 4)
		self.mana = self.mana_max
		self.estamina_max = 10 * resistencia
		self.estamina = self.estamina_max
		self.ataque_fis = 10 * forca
		self.defesa = 10 * ((constituicao * 50 / 100) + (resistencia * 25 / 100))
		self.ataque_m = 10 * (arcano + (inteligencia / 2))
		self.defesa_m = 10 * (arcano * 1.2 + (inteligencia / 4))
		self.inventario = None
		self.habilidades = {}
		self.magias = {}
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

	def recuperar_mana(self):
		regen = self.mana_max / 100 + ((self.arcano + self.inteligencia) / 100)
		if self.mana < self.mana_max:
			self.mana += regen
		else:
			self.mana = self.mana_max

	def recuperar_estamina(self):
		regen = self.estamina_max / 100 + ((self.resistencia + self.constituicao + self.agilidade) / 100)
		
		if self.estamina < self.estamina_max:
			self.estamina += regen

		else:
			self.estamina = self.estamina_max

	def mover(self, dir):
		if dir == 'frente':
			self.posy += 1
		elif dir == 'trás':
			self.posy -= 1
		elif dir == 'direita':
			self.posx += 1
		elif dir == 'esquerda':
			self.posx -= 1
		
	def usar_habilidade(self, nome):
		habilidade = self.habilidades.get(nome)
		if not habilidade:
			return f"Habilidade {nome} não encontrada"

		if self.estamina < habilidade.custo:
			return f"estamina insuficiente para usar {habilidade.nome}"

		# Consome estamina
		self.estamina -= habilidade.custo

		if habilidade.tipo == "ofensiva":
			return self.atacar(mod=habilidade.dano)

		elif habilidade.tipo == "cura":
			self.curar(habilidade.dano)
			return f"{self.nome} recuperou {habilidade.dano * self.vida_max} de vida com {habilidade.nome}"

	def usar_magia(self, nome):
		magia = self.magias.get(nome)
		if not magia:
			return f"Magia {nome} não encontrada"

		if self.mana < magia.custo:
			return f"mana insuficiente para usar {magia.nome}"

		# Consome mana
		self.mana -= magia.custo

		if magia.tipo == "ofensiva":
			return self.atacar(mod=magia.dano)

		elif magia.tipo == "cura":
			self.curar(magia.dano)
			return f"{self.nome} recuperou {magia.dano * self.vida_max} de vida com {magia.nome}"

	def __str__(self):
		return (
			f"Nome: {self.nome} | Raça: {self.raca}"
			f"Vida: {self.vida} | Mana: {self.mana} | Estamina: {self.estamina}"
			f"Ataque Fisico: {self.ataque_fis} | Ataque Magico: {self.ataque_m}"
			f"Defesa Fisica: {self.defesa} | Defesa Magica: {self.defesa_m}" 
		)
