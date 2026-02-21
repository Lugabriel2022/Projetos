from hub import *

jogador = Personagem('Hugo')

jogador.add_module(RacaModule('humano', 'humano'))

jogador.add_module(InventoryModule('mochila', 100))

jogador.add_module(EquipModule('equipamento'))

jogador.add_module(HealthModule('Hp'))

jogador.add_module(StaminaModule('Fp'))

jogador.add_module(ManaModule('Mp'))

health = jogador.get('humano').vitalidade()
mana = jogador.get('humano').magia()
stamina = jogador.get('humano').stamina()

jogador.get('Hp').calcular_vida(health)

jogador.get('Mp').calcular_mana(mana)

jogador.get('Fp').calcular_stamina(stamina)

jogador.get('equipamento').equipar_arma(FireweaponObjeto('Ares', 'mosquete', 40, 20, 30, 50, 100, 1, 100, "uma arma de fogo forjada pelas mãos do deus daguerra", 5.0).set_tags("two-handed", "heavy", "divine")
, 'destra')

print(jogador.get('humano').expor_stats())
print(jogador.get('Hp').expor_dados())
print(jogador.get('Mp').expor_dados())
print(jogador.get('Fp').expor_dados())
print(jogador.get('equipamento').expor_dados())



