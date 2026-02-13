from hub import *

camara = Sala(10, 15)
grama = Tile("grama")
parede = Tile("parede", passavel= False)

player = Personagem('Luis', 'Ronin', 'Lupinoi', 10, 35, 25, 25, 28, 30, 52, 10, 10, 10)


inimigo = Monstro("Calamity", 'grande', 'Dragão', 100, 150, 200, 100, 50, 300, 250, 500, 50, 50)

print(inimigo)

katana = Arma("Ruptura da alma", 'fis', 100, 6.0)

player.equipar_arma(katana, 'destra')
player.equipar_arma(katana, 'canhota')
print(player)
atacar_fis(player, inimigo)

print(inimigo)