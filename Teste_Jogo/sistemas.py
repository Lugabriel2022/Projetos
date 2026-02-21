import random as rd

class InventoryModule():
	def __init__(self, name, slots):
		self.name = name
		self.inventario = {}
		self.slots_max = slots
		self.slots_livres = 0
		self.calcular_slots()

	def add_item(self, id, item, quantidade, tipo, valor):
		if id in self.inventario.keys():
			return 'id repetido'

		else:
			if self.slots_livres > 0:
				self.inventario[id] = {
					'item': item, 'quant': quantidade, 'tipo': tipo, 'valor': f'{valor} G, Desc: {item.desc}'
				}
				
				self.calcular_slots()
				return 'item adcionado com sucesso'

			else:
				return 'inventario lotado'
		
	def calcular_slots(self):
		self.slots_livres = self.slots_max - len(self.inventario.keys())

	def upgrade_slots(self, slots):
		self.slots_max += slots

	def remove_item(self, nome, quant):
		for id_chave, dados in self.inventario.items():
			if dados['item'].nome == nome:
				id_encontrado = id_chave
				break

		if id_encontrado:
			item_atual = self.inventario[id_encontrado]

			if item_atual['quant'] > quant:
				item_atual['quant'] -= quant
				print(f"Removido {quant}x {nome}. Restam {item_atual['quant']}.")
				return item_atual

			elif item_atual['quant'] == quant:
				item_removido = self.inventario.pop(id_encontrado)
				print(f"Item {nome} esgotado e removido do inventário.")
				self.calcular_slots()
				return 
				
			else:
				print(f"Erro: Você tenta remover {quant}, mas só tem {item_atual['quant']}.")
				return None

		else:
			print(f"Item {nome} não encontrado na mochila.")
			return None

	def exibir_inventario(self):
		print(self.inventario)

class EquipModule():
	SLOTS_ARMADURA = { 
		'elmo': 'cabeça', 
		'peitoral': 'torso', 
		'manoplas': 'luvas', 
		'grevas': 'calças', 
		'botas': 'botas'
		}

	def __init__(self, name):
		self.name = name
		self.equipamento = {
			'cabeça' : 'nenhum',
			'torso' : 'nenhum',
			'calças': 'nenhum',
			'luvas' : 'nenhum',
			'botas' : 'nenhum',
			'mão dir' : 'punho',
			'mão esq' : 'punho'
		}

	def equipar_arma(self, arma, slot):
		slots = {
			'destra': 'mão dir',
			'canhota' : 'mão esq'
		}
		if 'two-handed' in arma.tags:
			# Se for duas mãos, ocupa ambos ou limpa o outro antes
			self.equipamento['mão dir'] = arma
			self.equipamento['mão esq'] = arma # A arma ocupa os dois slots
			print(f"{arma.nome} equipada em ambas as mãos.")
		else:
			match slot:
				case 'destra':
					self.equipamento[slots[slot]] = arma
				case 'canhota':
					self.equipamento[slots[slot]] = arma
	
	def desequipar_arma(self, slot):
		slots = {
			'destra': 'mão dir',
			'canhota' : 'mão esq'
		}
		
		# Identificamos o que está no slot antes de apagar
		item_atual = self.equipamento[slots[slot]]

		# Se for uma arma de duas mãos, ela ocupa ambos, então limpamos ambos
		if hasattr(item_atual, 'tags') and 'two-handed' in item_atual.tags:
			self.equipamento['mão dir'] = 'punho'
			self.equipamento['mão esq'] = 'punho'
			print(f"{item_atual.nome} removida de ambas as mãos.")
		else:
			# Se for uma mão só (ou já for 'punho'), limpa só o escolhido
			self.equipamento[slots[slot]] = 'punho'

	def equipar_armadura(self, armadura):
		slot = self.SLOTS_ARMADURA.get(armadura.tipo)
		if slot:
			self.equipamento[slot] = armadura

	def desequipar_armadura(self, armadura):
		slot = self.SLOTS_ARMADURA.get(armadura.tipo)
		if slot and self.equipamento[slot] != 'nenhum': 
			armadura = self.equipamento[slot] 
			self.equipamento[slot] = 'nenhum'

	def expor_dados(self):
		return self.equipamento
		
class HealthModule():
	def __init__(self, name):
		self.name = name
		self.vida_max = 10
		self.modificador = 0
		self.regen_tax = 0.1
		self.vida = self.vida_max

	def calcular_vida(self, mod):
		self.modificador = mod
		self.vida_max += self.modificador
		self.vida = self.vida_max

	def regenerar_vida(self):
		if self.vida < self.vida_max:
			regen = self.vida_max * self.regen_tax
			# Garante que não ultrapasse o máximo
			self.vida = min(self.vida_max, self.vida + regen)

	def set_regen(self, new_regen):
		self.regen_tax = new_regen

	def get(self, dano):
		self.vida -= max(0, dano)
		if self.vida <= 0:
			self.vida = 0

	def morreu(self):
		return self.vida <= 0

	def restaurar(self, valor):
		self.vida = min(self.vida_max, self.vida + valor)

	def expor_dados(self):
		"""A função contra a blasfêmia!"""
		Health_rel = {
			"atual": self.vida,
			"max": self.vida_max,
			"percentual": self.vida / self.vida_max if self.vida_max > 0 else 0,
			"status": "morto" if self.morreu() else "vivo"
		}

		return  Health_rel

class ManaModule():
	def __init__(self, name):
		self.name = name
		self.mana_max = 10
		self.mana = self.mana_max
		self.modificador = 0
		self.regen_tax = 0.1

	def calcular_mana(self, mod):
		self.modificador = mod
		self.mana_max += self.modificador
		self.mana = self.mana_max

	def regenerar_mana(self):
		if self.mana < self.mana_max:
			regen = self.mana_max * self.regen_tax
			self.mana = min(self.mana_max, self.mana + regen)

	def set_regen(self, new_regen):
		self.regen_tax = new_regen

	def get(self, mana):
		self.mana -= max(0, mana)
		if self.mana <= 0:
			self.mana = 0

	def restaurar(self, valor):
		self.mana = min(self.mana_max, self.mana + valor)

	def expor_dados(self):
		mana_rel = {
			'mana_max': self.mana_max,
			'atual': self.mana,
		}

		return mana_rel

class StaminaModule():
	def __init__(self, name):
		self.name = name
		self.stamina_max = 10
		self.stamina = self.stamina_max
		self.modificador = 0
		self.regen_tax = 0.1

	def calcular_stamina(self, mod):
		self.modificador = mod
		self.stamina_max += self.modificador
		self.stamina = self.stamina_max

	def regenerar_stamina(self):
		regen = self.stamina_max * self.regen_tax
		self.stamina = min(self.stamina_max, self.stamina + regen)

	def set_regen(self, new_regen):
		self.regen_tax = new_regen

	def get(self, stamina):
		self.stamina -= max(0, stamina)
		if self.stamina <= 0:
			self.stamina = 0

	def restaurar(self, valor):
		self.stamina = min(self.stamina_max, self.stamina + valor)

	def expor_dados(self):
		stamina_rel = {
			'stamina_max': self.stamina_max,
			'stamina': self.stamina
		}

		return stamina_rel

class RacaModule():
	Raca = {
		'humano': [10, 50],
		'elfo': [10, 60],
		'anão': [15, 60],
		'kobolt': [10, 40],
		'Feline': [15, 70],
		'Lupine': [15, 90],
		'gigante': [20, 100],
		'dragão': [1000, 15000],
		'kitsune': [50, 800],
		'anjo': [1000, 10000],
		'sucubos': [20, 80],
		'slime': [10, 50],
		'elemental': [20, 150],
		'custom': [0, 0]
	}
	def __init__(self, name, raca, top=0 , down=0):
		self.name = name
		self.raca = raca
		self.top = top
		self.down = down
		self.forca = 10
		self.constituicao = 10
		self.agilidade = 10
		self.resistencia = 10
		self.inteligencia = 10
		self.sabedoria = 10
		self.percepcao = 10
		self.arcano = 10
		self.fe = rd.randint(10, 100)
		self.carisma = rd.randint(10, 100)
		self.sorte = rd.randint(10, 100)
		self.calcular_stats()

	def calcular_stats(self):
		if self.raca != 'custom':
			padrao = (self.Raca[self.raca][0], self.Raca[self.raca][1])
		else:
			padrao = (self.down, self.top)
		self.forca = rd.randint(padrao[0], padrao[1])
		self.constituicao = rd.randint(padrao[0], padrao[1])
		self.agilidade = rd.randint(padrao[0], padrao[1])
		self.resistencia = rd.randint(padrao[0], padrao[1])
		self.inteligencia = rd.randint(padrao[0], padrao[1])
		self.sabedoria = rd.randint(padrao[0], padrao[1])
		self.percepcao = rd.randint(padrao[0], padrao[1])
		self.arcano = rd.randint(padrao[0], padrao[1])

	def vitalidade(self):
		vitalidade = (self.constituicao * 0.3) + (self.resistencia * 0.3)
		return vitalidade

	def magia(self):
		astral = (self.arcano * 0.5) + (self.sabedoria * 0.2) + (self.inteligencia * 0.25)
		return astral

	def stamina(self):
		stamina = (self.constituicao * 0.3) + (self.agilidade * 0.5)
		return stamina

	def expor_stats(self):
		stats = {
			'for':self.forca,
			'con':self.constituicao,
			'agi':self.agilidade,
			'res':self.resistencia,
			'int':self.inteligencia,
			'sab':self.sabedoria,
			'per':self.percepcao,
			'arc':self.arcano,
			'car':self.carisma,
			'fe':self.fe,
			'sor':self.sorte
		}
		return stats

class RangeCombatModule():
	def __init__(self, name):
		self.name = name

	def get(self, dano, presisao, municao):
		pass
	pass

class MeleeCombatModule():
	pass

class CastModule():
	pass

class CoreModule():
	pass
