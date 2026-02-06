def validar_genero(genero: str) -> bool:
    return genero in [ 'f', 'm']

def validar_raca(raca: str, racas: list) -> bool:
    return raca.lower() == 'rd' or raca in racas

def validar_classe(classe: str, classes: list) -> bool:
    return classe.lower() == 'rd' or classe in classes

def validar_mod(mod: str) -> bool:
    return mod in ['s', 'y', 'sim', 'yep', 'n', 'não', 'nop']

def normalizar_mod(mod: str) -> bool:
    return mod in ['s', 'y', 'sim', 'yep']