def atacar_fis(atacante, defensor):
    dano = atacante.atacar()
    defensor.tomar_dano(dano)
    defesa = defensor.defesa
    print(f"{atacante.nome} atacou {defensor.nome} causando {dano[0] - defesa} de dano")
