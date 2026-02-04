import random as rd
import os
import json

def gerar_personagem():

    file_path = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(file_path, "atributos.json")

    with open(json_path, 'r') as a:
        atributos = json.load(a)

    racas = atributos['racas'][:]
    elementos_disp= atributos['elementos'][:]
    while True:
        print(racas)
        ch1 = {
            'genero': str(input('Escolha o genero[ F , M ]')).lower().strip(),
            'raça': str(input(f'''escolha sua raça, digite rd para aleatório: ''')).capitalize().strip()
        }
        if ch1['genero'] in ['f', 'm']:
            if ch1['raça'] in atributos['racas'] or ch1['raça'] == 'Rd':
                break
            else:
                print('escolha uma raça da lista')
        else:
            print('entrada invalida, apenas f ou m')

    personagem = {}

    if ch1['genero'] == 'f':
        personagem['nome'] = f'{rd.choice(atributos["nomes_fem"])} {rd.choice(atributos["sobrenome"])}'
        personagem['genero'] = 'Feminino'
    else:
        personagem['nome'] = f'{rd.choice(atributos["nomes_mas"])} {rd.choice(atributos["sobrenome"])}'
        personagem['genero'] = 'Masculino'

    personagem['origem'] = rd.choice(list(atributos['origem'].keys()))
    personagem['classe'] = rd.choice(atributos['classe'])
    #personagem['classe'] = 'Feiticeiro'
    if ch1['raça'] == 'Rd':
        if ch1['genero'] == 'f':
            personagem['raça'] = rd.choice(racas)
        else:
            racas.remove('Sucubos')
            personagem['raça'] = rd.choice(racas)
            personagem['corpo'] = 'Humanoide'
    else:
        personagem['raça'] = ch1['raça']
        personagem['corpo'] = 'Humanoide'

    raca_funcs = {
        'Humano': humano,
        'Elfo': elfo,
        'Anão': anao,
        'Feline': feline,
        'Lupine': lupine,
        'Gigante': gigante,
        'Kobolt': kobolt,
        'Kitsune': kitsune,
        'Dragão': dragão,
        'Anjo': anjo,
        'Sucubos': sucubos,
        'Slime': slime,
        'Elemental': elemental
    }

    raca_escolhida = personagem['raça']
    if raca_escolhida in raca_funcs:
        raca_funcs[raca_escolhida](personagem, atributos, ch1, elementos_disp)



    return (personagem, atributos, ch1, elementos_disp)

def humano(personagem, atributos, ch1, elementos_disp):
    if ch1['genero'] == 'f':
        personagem['seios'] = rd.choice(atributos['seios'])
    personagem['alt_m'] = rd.choice([ 1, 2])
    if personagem['alt_m'] == 2:
        personagem['alt_cm'] = rd.randint(0, 50)
    else:
        personagem['alt_cm'] = rd.randint(0, 99)
    personagem['fisico'] = rd.choice(atributos['fisico'])
    personagem['idade'] = rd.randint(8, 80)
    personagem['cor_olhos'] = rd.choice(atributos['cores'])
    personagem['cor_pele'] = rd.choice(atributos['pele'])
    personagem['cabelo'] = rd.choice(atributos['cabelo'])
    personagem['tip_cabelo'] = rd.choice(atributos['tip_cabelo'])
    personagem['cor_cabelo'] = rd.choice(atributos['cores'])
    personagem['estatisticas'] = {'força': rd.randint(10, 50),
                                    'constituicao': rd.randint(10, 50),
                                    'agilidade': rd.randint(10, 50),
                                    'resistencia': rd.randint(10, 50),
                                    'inteligencia': rd.randint(10, 50),
                                    'sabedoria': rd.randint(10, 50),
                                    'percepcao': rd.randint(10, 50),
                                    'arcano': rd.randint(10, 50),
                                    'fé': rd.randint(10, 100),
                                    'sorte': rd.randint(10, 100),
                                    'carisma': rd.randint(10, 100)}
    
    if personagem['idade'] < 18:
        personagem['estatisticas']['força'] *= 0.8
        personagem['estatisticas']['sabedoria'] *= 0.7
    elif personagem['idade'] > 60:
        personagem['estatisticas']['agilidade'] *= 0.7
        personagem['estatisticas']['sabedoria'] *= 1.2

    modificadores(personagem, atributos, ch1, elementos_disp)

def elfo(personagem, atributos, ch1, elementos_disp):
    personagem['especie'] = rd.choice(['Alto elfo', 'Elfo negro', 'Elfo da floresta', 'Elfo lunar'])
    if ch1['genero'] == 'f':
        personagem['seios'] = rd.choice(atributos['seios'])
    personagem['alt_m'] = rd.choice([ 1, 2, 3])
    if personagem['alt_m'] == 3:
        personagem['alt_cm'] = rd.randint(0, 50)
    else:
        personagem['alt_cm'] = rd.randint(0, 99)
    personagem['fisico'] = rd.choice(atributos['fisico'])
    personagem['idade'] = rd.randint(8, 1000)
    personagem['cor_olhos'] = rd.choice(atributos['cores'])
    personagem['cabelo'] = rd.choice(atributos['cabelo'])
    personagem['tip_cabelo'] = rd.choice(atributos['tip_cabelo'])
    personagem['cor_cabelo'] = rd.choice(atributos['cores'])
    personagem['estatisticas'] = {'força': rd.randint(10, 60),
                                    'constituicao': rd.randint(10, 60),
                                    'agilidade': rd.randint(10, 60),
                                    'resistencia': rd.randint(10, 60),
                                    'inteligencia': rd.randint(10, 60),
                                    'sabedoria': rd.randint(10, 60),
                                    'percepcao': rd.randint(10, 60),
                                    'arcano': rd.randint(10, 60),
                                    'fé': rd.randint(10, 100),
                                    'sorte': rd.randint(10, 100),
                                    'carisma': rd.randint(10, 100)}
    match personagem['especie']:
        
        case 'Alto elfo':
            personagem['cor_pele'] = 'Palida'
            for i in personagem['estatisticas']:
                personagem['estatisticas'][i] *= 1.5
        
        case 'Elfo negro':
            personagem['cor_pele'] = 'Morena'
            personagem['estatisticas']['arcano'] *= 1.3
            personagem['estatisticas']['inteligencia'] *= 1.2
            personagem['estatisticas']['sabedoria'] *= 1.3
            personagem['estatisticas']['fé'] *= 1.5

        case 'Elfo da floresta':
            personagem['cor_pele'] = rd.choice(atributos['pele'])
            personagem['estatisticas']['força'] *= 1.15
            personagem['estatisticas']['constituicao'] *= 1.15
            personagem['estatisticas']['agilidade'] *= 1.15
            personagem['estatisticas']['resistencia'] *= 1.15
            personagem['estatisticas']['percepcao'] *= 1.15

        case 'Elfo lunar':
            personagem['cor_pele'] = 'Branca'
            personagem['cor_olhos'] = 'Azul lunar'
            personagem['cor_cabelo'] = 'Prata lunar'
            personagem['elemento inato'] = rd.choice(['Alma', 'Luz', 'Gelo', 'Agua'])
            personagem['estatisticas']['arcano'] *= 1.4
            personagem['estatisticas']['inteligencia'] *= 1.4
            personagem['estatisticas']['sabedoria'] *= 1.4
            personagem['estatisticas']['fé'] *= 1.5

    modificadores(personagem, atributos, ch1, elementos_disp)

def anao(personagem, atributos, ch1, elementos_disp):
    if ch1['genero'] == 'f':
        personagem['seios'] = rd.choice(atributos['seios'])
    personagem['alt_m'] = 1
    personagem['alt_cm'] = rd.randint(0, 50)
    personagem['fisico'] = rd.choice(atributos['fisico'])
    personagem['idade'] = rd.randint(8, 500)
    personagem['cor_olhos'] = rd.choice(atributos['cores'])
    personagem['cor_pele'] = rd.choice(atributos['pele'])
    personagem['cabelo'] = rd.choice(atributos['cabelo'])
    personagem['tip_cabelo'] = rd.choice(atributos['tip_cabelo'])
    personagem['cor_cabelo'] = rd.choice(atributos['cores'])
    personagem['estatisticas'] = {'força': rd.randint(10, 70),
                                    'constituicao': rd.randint(10, 70),
                                    'agilidade': rd.randint(10, 40),
                                    'resistencia': rd.randint(10, 70),
                                    'inteligencia': rd.randint(10, 40),
                                    'sabedoria': rd.randint(10, 40),
                                    'percepcao': rd.randint(10, 40),
                                    'arcano': rd.randint(10, 40),
                                    'fé': rd.randint(10, 100),
                                    'sorte': rd.randint(10, 100),
                                    'carisma': rd.randint(10, 100)}

    modificadores(personagem, atributos, ch1, elementos_disp)

def feline(personagem, atributos, ch1, elementos_disp):
    personagem['especie'] = rd.choice(['Tigre', 'Pantera', 'Gato', 'Jaguar', 'Leão', 'Jaguatirica', 'Hyena'])
    personagem['corpo'] = rd.choice(atributos['corpo'])
    if ch1['genero'] == 'f':
        if personagem['corpo'] in ['Humanoide', 'Antropomorfico']:
            personagem['seios'] = rd.choice(atributos['seios'])
    if personagem['corpo'] == 'Bestial':
        personagem['alt_m'] = rd.choice([1, 2])
    else:
        personagem['alt_m'] = rd.choice([ 1, 2, 3])
    if personagem['alt_m'] == 3:
        personagem['alt_cm'] = rd.randint(0, 50)
    else:
        personagem['alt_cm'] = rd.randint(0, 99)
    personagem['fisico'] = rd.choice(atributos['fisico'])
    personagem['idade'] = rd.randint(8, 80)
    personagem['cor_olhos'] = rd.choice(atributos['cores'])
    personagem['cor_pelos'] = rd.choice(atributos['cores'])
    if personagem['corpo'] in ['Humanoide', 'Antropomorfico']:
        personagem['cabelo'] = rd.choice(atributos['cabelo'])
        personagem['tip_cabelo'] = rd.choice(atributos['tip_cabelo'])
        personagem['cor_cabelo'] = rd.choice(atributos['cores'])
    personagem['estatisticas'] = {'força': rd.randint(10, 70),
                                    'constituicao': rd.randint(10, 70),
                                    'agilidade': rd.randint(10, 90),
                                    'resistencia': rd.randint(10, 70),
                                    'inteligencia': rd.randint(10, 50),
                                    'sabedoria': rd.randint(10, 50),
                                    'percepcao': rd.randint(10, 90),
                                    'arcano': rd.randint(10, 40),
                                    'fé': rd.randint(10, 100),
                                    'sorte': rd.randint(10, 100),
                                    'carisma': rd.randint(10, 100)}
    
    match personagem['especie']:
        case 'Tigre':
            personagem['estatisticas']['força'] *= 1.2
            personagem['estatisticas']['resistencia'] *= 1.15
        case 'Pantera':
            personagem['estatisticas']['agilidade'] *= 1.25
            personagem['estatisticas']['percepcao'] *= 1.2
        case 'Gato':
            personagem['estatisticas']['sorte'] *= 1.2
            personagem['estatisticas']['carisma'] *= 1.2
        case 'Jaguar':
            personagem['estatisticas']['força'] *= 1.15
            personagem['estatisticas']['percepcao'] *= 1.15
        case 'Leão':
            personagem['estatisticas']['constituicao'] *= 1.2
            personagem['estatisticas']['carisma'] *= 1.2
        case 'Jaguatirica':
            personagem['estatisticas']['agilidade'] *= 1.15
            personagem['estatisticas']['inteligencia'] *= 1.15
        case 'Hyena':
            personagem['estatisticas']['resistencia'] *= 1.2
            personagem['estatisticas']['sabedoria'] *= 1.2

    modificadores(personagem, atributos, ch1, elementos_disp)

def lupine(personagem, atributos, ch1, elementos_disp):
    personagem['especie'] = rd.choice(['Lobo', 'Pastor Alemão', 'Husky', 'Raposa', 'Dingo', 'Golden retiever', 'Chacal'])
    personagem['corpo'] = rd.choice(atributos['corpo'])
    if ch1['genero'] == 'f':
        if personagem['corpo'] in ['Humanoide', 'Antropomorfico']:
            personagem['seios'] = rd.choice(atributos['seios'])
    if personagem['corpo'] == 'Bestial':
        personagem['alt_m'] = rd.choice([1, 2])
    else:
        personagem['alt_m'] = rd.choice([ 1, 2, 3])
    if personagem['alt_m'] == 3:
        personagem['alt_cm'] = rd.randint(0, 50)
    else:
        personagem['alt_cm'] = rd.randint(00, 99)
    personagem['fisico'] = rd.choice(atributos['fisico'])
    personagem['idade'] = rd.randint(8, 80)
    personagem['cor_olhos'] = rd.choice(atributos['cores'])
    personagem['cor_pelos'] = rd.choice(atributos['cores'])
    if personagem['corpo'] in ['Humanoide', 'Antropomorfico']:
        personagem['cabelo'] = rd.choice(atributos['cabelo'])
        personagem['tip_cabelo'] = rd.choice(atributos['tip_cabelo'])
        personagem['cor_cabelo'] = rd.choice(atributos['cores'])
    personagem['estatisticas'] = {'força': rd.randint(10, 90),
                                    'constituicao': rd.randint(10, 90),
                                    'agilidade': rd.randint(10, 50),
                                    'resistencia': rd.randint(10, 90),
                                    'inteligencia': rd.randint(10, 60),
                                    'sabedoria': rd.randint(10, 50),
                                    'percepcao': rd.randint(10, 90),
                                    'arcano': rd.randint(10, 40),
                                    'fé': rd.randint(10, 100),
                                    'sorte': rd.randint(10, 100),
                                    'carisma': rd.randint(10, 100)}
    
    match personagem['especie']:
        case 'Lobo':
            personagem['estatisticas']['força'] *= 1.2
            personagem['estatisticas']['resistencia'] *= 1.15
        case 'Pastor Alemão':
            personagem['estatisticas']['constituicao'] *= 1.2
            personagem['estatisticas']['percepcao'] *= 1.15
        case 'Husky':
            personagem['estatisticas']['agilidade'] *= 1.2
            personagem['estatisticas']['carisma'] *= 1.15
        case 'Raposa':
            personagem['estatisticas']['inteligencia'] *= 1.2
            personagem['estatisticas']['sorte'] *= 1.2
        case 'Dingo':
            personagem['estatisticas']['força'] *= 1.15
            personagem['estatisticas']['sabedoria'] *= 1.2
        case 'Golden retiever':
            personagem['estatisticas']['carisma'] *= 1.2
            personagem['estatisticas']['fé'] *= 1.2
        case 'Chacal':
            personagem['estatisticas']['percepcao'] *= 1.2
            personagem['estatisticas']['agilidade'] *= 1.15

    modificadores(personagem, atributos, ch1, elementos_disp)

def gigante(personagem, atributos, ch1, elementos_disp):
    if ch1['genero'] == 'f':
        personagem['seios'] = rd.choice(atributos['seios'])
    personagem['alt_m'] = rd.choice([5, 6, 7, 8, 9])
    if personagem['alt_m'] == 9:
        personagem['alt_cm'] = rd.randint(0, 50)
    else:
        personagem['alt_cm'] = rd.randint(0, 95)
    personagem['fisico'] = rd.choice(atributos['fisico'])
    personagem['idade'] = rd.randint(8, 80)
    personagem['cor_olhos'] = rd.choice(atributos['cores'])
    personagem['cor_pele'] = rd.choice(atributos['pele'])
    personagem['cabelo'] = rd.choice(atributos['cabelo'])
    personagem['tip_cabelo'] = rd.choice(atributos['tip_cabelo'])
    personagem['cor_cabelo'] = rd.choice(atributos['cores'])
    personagem['estatisticas'] = {'força': rd.randint(10, 100),
                                  'constituicao': rd.randint(10, 100),
                                  'agilidade': rd.randint(10, 100),
                                  'resistencia': rd.randint(10, 100),
                                  'inteligencia': rd.randint(10, 50),
                                  'sabedoria': rd.randint(10, 50),
                                  'percepcao': rd.randint(10, 40),
                                  'arcano': rd.randint(10, 50),
                                  'fé': rd.randint(10, 100),
                                  'sorte': rd.randint(10, 100),
                                  'carisma': rd.randint(10, 100)}

    modificadores(personagem, atributos, ch1, elementos_disp)

def kobolt(personagem, atributos, ch1, elementos_disp):
    if ch1['genero'] == 'f':
        personagem['seios'] = rd.choice(atributos['seios'])
    personagem['alt_m'] = 1
    personagem['alt_cm'] = rd.randint(00, 50)
    personagem['fisico'] = rd.choice(atributos['fisico'])
    personagem['idade'] = rd.randint(8, 500)
    personagem['afinidade_draconica'] = rd.choice(['Fogo', 'Gelo', 'Terra', 'Sombra', 'Relâmpago'])
    personagem['chifres'] = rd.choice(atributos['chifres'])
    personagem['cor_olhos'] = rd.choice(atributos['cores'])
    personagem['cor_escamas'] = rd.choice(atributos['cores'])
    personagem['estatisticas'] = {'força': rd.randint(10, 40),
                                  'constituicao': rd.randint(10, 40),
                                  'agilidade': rd.randint(10, 40),
                                  'resistencia': rd.randint(10, 40),
                                  'inteligencia': rd.randint(10, 40),
                                  'sabedoria': rd.randint(10, 40),
                                  'percepcao': rd.randint(10, 40),
                                  'arcano': rd.randint(10, 40),
                                  'fé': rd.randint(10, 100),
                                  'sorte': rd.randint(10, 100),
                                  'carisma': rd.randint(10, 100)}
    match personagem['afinidade_draconica']:
        case 'Fogo':
            personagem['estatisticas']['força'] *= 1.1
        case 'Gelo':
            personagem['estatisticas']['resistencia'] *= 1.1
        case 'Terra':
            personagem['estatisticas']['constituição'] *= 1.1
        case 'Sombra':
            personagem['estatisticas']['sabedoria'] *= 1.1
        case 'Relâmpago':
            personagem['estatisticas']['agilidade'] *= 1.1
    

    modificadores(personagem, atributos, ch1, elementos_disp)

def kitsune(personagem, atributos, ch1, elementos_disp):
    personagem['corpo'] = rd.choice(atributos['corpo'])
    if ch1['genero'] == 'f':
        if personagem['corpo'] in ['Humanoide', 'Antropomorfico']:
            personagem['seios'] = rd.choice(atributos['seios'])
    if personagem['corpo'] == 'Bestial':
        personagem['alt_m'] = rd.choice([1, 2, 3])
    else:
        personagem['alt_m'] = rd.choice([1, 2, 3, 4])
    if personagem['alt_m'] == 4:
        personagem['atl_cm'] = rd.randint(0, 50)
    else:
        personagem['alt_cm'] = rd.randint(0, 99)
    personagem['fisico'] = rd.choice(atributos['fisico'])
    personagem['idade'] = rd.randint(8, 5000)
    personagem['caudas'] = min(10, personagem['idade'] // 100)
    personagem['elemento inato'] = rd.choice(elementos_disp)
    elementos_disp.remove(personagem['elemento inato'])
    personagem['cor_olhos'] = rd.choice(atributos['cores'])
    personagem['cor_pelos'] = rd.choice(atributos['cores'])
    if personagem['corpo'] in ['Humanoide', 'Antropomorfico']:
        personagem['cabelo'] = rd.choice(atributos['cabelo'])
        personagem['tip_cabelo'] = rd.choice(atributos['tip_cabelo'])
        personagem['cor_cabelo'] = rd.choice(atributos['cores'])
    personagem['estatisticas'] = {'força': rd.randint(10, 200),
                                  'constituicao': rd.randint(10, 200),
                                  'agilidade': rd.randint(10, 200),
                                  'resistencia': rd.randint(10, 200),
                                  'inteligencia': rd.randint(10, 200),
                                  'sabedoria': rd.randint(10, 200),
                                  'percepcao': rd.randint(10, 200),
                                  'arcano': rd.randint(10, 200),
                                  'fé': rd.randint(10, 100),
                                  'sorte': rd.randint(10, 100),
                                  'carisma': rd.randint(10, 100)}
    
    multiplicador = 1 + (personagem['caudas'] * 0.3)
    personagem['estatisticas']['arcano'] *= multiplicador
    personagem['estatisticas']['sabedoria'] *= multiplicador
    personagem['estatisticas']['inteligencia'] *= multiplicador
    personagem['estatisticas']['percepcao'] *= multiplicador

    if personagem['caudas'] == 10:
        personagem['raça'] += ' Divino'
        personagem['titulo'] = 'Tenko'
        if rd.random() < 0.3:
            for i in personagem['estatisticas']:
                personagem['estatisticas'][i] *= 1.5
            personagem['titulo'] += ' Descendente de Amaterasu'
        personagem['estatisticas']['fé'] = 'Celestial'
        personagem['estatisticas']['arcano'] *= 10
        personagem['estatisticas']['sabedoria'] *= 10
        personagem['estatisticas']['carisma'] *= 10

    modificadores(personagem, atributos, ch1, elementos_disp)

def dragão(personagem, atributos, ch1, elementos_disp):
    personagem['especie'] = rd.choice(['Long', 'Drake', 'Europeu'])
    personagem['corpo'] = rd.choice(atributos['corpo'])
    personagem['stage'] = rd.choice(['jovem', 'jovem adulto', 'adulto', 'antigo', 'ancestral', 'ancião'])
    if ch1['genero'] == 'f':
        if personagem['corpo'] in ['Humanoide', 'Antropomorfico']:
            personagem['seios'] = rd.choice(atributos['seios'])
        if personagem['corpo'] == 'Bestial':
            personagem['alt_m'] = rd.randint(4, 35)
            if personagem['alt_m'] == 35:
                personagem['alt_cm'] = rd.randint(0, 50)
            else:
                personagem['alt_cm'] = rd.randint(0, 99)
        else:
            personagem['alt_m'] = rd.randint(2, 9)
            if personagem['alt_m'] == 9:
                personagem['alt_cm'] = rd.randint(00, 50)
            else:
                personagem['alt_cm'] = rd.randint(0, 99)
    personagem['fisico'] = rd.choice(atributos['fisico'])
    personagem['idade'] = rd.randint(100, 100000)
    personagem['chifres'] = rd.choice(atributos['chifres'])
    personagem['cor_olhos'] = rd.choice(atributos['cores'])
    personagem['cor_escamas'] = rd.choice(atributos['cores'])
    personagem['elemento inato'] = rd.choice(elementos_disp)
    if personagem['corpo'] in ['Humanoide', 'Antropomorfico']:
        personagem['cabelo'] = rd.choice(atributos['cabelo'])
        personagem['tip_cabelo'] = rd.choice(atributos['tip_cabelo'])
        personagem['cor_cabelo'] = rd.choice(atributos['cores'])
    elementos_disp.remove(personagem['elemento inato'])
    personagem['estatisticas'] = {'força': rd.randint(10, 15000),
                                  'constituicao': rd.randint(10, 15000),
                                  'agilidade': rd.randint(10, 15000),
                                  'resistencia': rd.randint(10, 15000),
                                  'inteligencia': rd.randint(10, 15000),
                                  'sabedoria': rd.randint(10, 15000),
                                  'percepcao': rd.randint(10, 15000),
                                  'arcano': rd.randint(10, 15000),
                                  'fé': rd.randint(10, 100),
                                  'sorte': rd.randint(10, 100),
                                  'carisma': rd.randint(10, 100)}
    match personagem['stage']:
        case 'jovem':
            personagem['estatisticas']['força'] *= 1.15
            personagem['estatisticas']['constituicao'] *= 1.15
            personagem['estatisticas']['agilidade'] *= 1.15
            personagem['estatisticas']['resistencia'] *= 1.15
            personagem['estatisticas']['inteligencia'] *= 1.15
            personagem['estatisticas']['sabedoria'] *= 1.15
            personagem['estatisticas']['percepcao'] *= 1.15
            personagem['estatisticas']['arcano'] *= 1.15
        case 'jovem adulto':
            personagem['estatisticas']['força'] *= 1.30
            personagem['estatisticas']['constituicao'] *= 1.30
            personagem['estatisticas']['agilidade'] *= 1.30
            personagem['estatisticas']['resistencia'] *= 1.30
            personagem['estatisticas']['inteligencia'] *= 1.30
            personagem['estatisticas']['sabedoria'] *= 1.30
            personagem['estatisticas']['percepcao'] *= 1.30
            personagem['estatisticas']['arcano'] *= 1.30
        case 'adulto':
            personagem['estatisticas']['força'] *= 1.45
            personagem['estatisticas']['constituicao'] *= 1.45
            personagem['estatisticas']['agilidade'] *= 1.45
            personagem['estatisticas']['resistencia'] *= 1.45
            personagem['estatisticas']['inteligencia'] *= 1.45
            personagem['estatisticas']['sabedoria'] *= 1.45
            personagem['estatisticas']['percepcao'] *= 1.45
            personagem['estatisticas']['arcano'] *= 1.45
        case 'antigo':
            personagem['estatisticas']['força'] *= 1.60
            personagem['estatisticas']['constituicao'] *= 1.60
            personagem['estatisticas']['agilidade'] *= 1.60
            personagem['estatisticas']['resistencia'] *= 1.60
            personagem['estatisticas']['inteligencia'] *= 1.60
            personagem['estatisticas']['sabedoria'] *= 1.60
            personagem['estatisticas']['percepcao'] *= 1.60
            personagem['estatisticas']['arcano'] *= 1.60
        case 'ancestral':
            personagem['estatisticas']['força'] *= 1.75
            personagem['estatisticas']['constituicao'] *= 1.75
            personagem['estatisticas']['agilidade'] *= 1.75
            personagem['estatisticas']['resistencia'] *= 1.75
            personagem['estatisticas']['inteligencia'] *= 1.75
            personagem['estatisticas']['sabedoria'] *= 1.75
            personagem['estatisticas']['percepcao'] *= 1.75
            personagem['estatisticas']['arcano'] *= 1.75
        case 'ancião':
            personagem['estatisticas']['força'] *= 2
            personagem['estatisticas']['constituicao'] *= 2
            personagem['estatisticas']['agilidade'] *= 2
            personagem['estatisticas']['resistencia'] *= 2
            personagem['estatisticas']['inteligencia'] *= 2
            personagem['estatisticas']['sabedoria'] *= 2
            personagem['estatisticas']['percepcao'] *= 2
            personagem['estatisticas']['arcano'] *= 2

    match personagem['especie']:
        case 'Long':
            personagem['estatisticas']['sabedoria'] *= 1.2
            personagem['estatisticas']['arcano'] *= 1.2
        case 'Drake':
            personagem['estatisticas']['agilidade'] *= 1.2
            personagem['estatisticas']['força'] *= 1.2
        case 'Europeu':
            personagem['estatisticas']['resistencia'] *= 1.2
            personagem['estatisticas']['constituição'] *= 1.2
            

    modificadores(personagem, atributos, ch1, elementos_disp)

def anjo(personagem, atributos, ch1, elementos_disp):
    personagem['ordem'] = rd.choice(['Anjo', 'Arcanjo', 'Seraphin'])
    if ch1['genero'] == 'f':
        personagem['seios'] = rd.choice(atributos['seios'])
    personagem['alt_m'] = rd.randint(1, 6)
    if personagem['alt_m'] == 6:
        personagem['alt_cm'] = rd.randint(0, 50)
    else:
        personagem['alt_cm'] = rd.randint(0, 99)
    personagem['fisico'] = rd.choice(atributos['fisico'])
    personagem['idade'] = rd.randint(100, 100000)
    personagem['cor_olhos'] = rd.choice(atributos['cores'])
    personagem['cor_pele'] = rd.choice(atributos['pele'])
    personagem['cabelo'] = rd.choice(atributos['cabelo'])
    personagem['tip_cabelo'] = rd.choice(atributos['tip_cabelo'])
    personagem['cor_cabelo'] = rd.choice(atributos['cores'])
    personagem['elemento inato'] = rd.choice(['Luz', 'Justiça', 'Esperança', 'Sabedoria', 'Guerra', 'Proteção'])
    personagem['estatisticas'] = {'força': rd.randint(10, 15000),
                                  'constituicao': rd.randint(10, 15000),
                                  'agilidade': rd.randint(10, 15000),
                                  'resistencia': rd.randint(10, 15000),
                                  'inteligencia': rd.randint(10, 15000),
                                  'sabedoria': rd.randint(10, 15000),
                                  'percepcao': rd.randint(10, 15000),
                                  'arcano': rd.randint(10, 15000),
                                  'fé': 'infinity',
                                  'sorte': rd.randint(10, 100),
                                  'carisma': rd.randint(10, 100)}
    
    match personagem['ordem']:
        case 'Anjo':
            personagem['asas'] = 2
            multiplicador = 1.15
        case 'Arcanjo':
            personagem['asas'] = 4
            multiplicador = 1.3
        case 'Seraphin':
            personagem['asas'] = 6
            multiplicador = 1.5

    for stat in personagem['estatisticas']:
        if stat != 'fé' and isinstance(personagem['estatisticas'][stat], (int, float)):
            personagem['estatisticas'][stat] *= multiplicador

    modificadores(personagem, atributos, ch1, elementos_disp)

def sucubos(personagem, atributos, ch1, elementos_disp):
    personagem['ordem'] = rd.choice(['Sedutora', 'Manipuladora', 'Dominadora', 'Ilusionista'])
    personagem['genero'] = 'Feminino'
    personagem['seios'] = rd.choice(atributos['seios'])
    personagem['alt_m'] = rd.choice([1 , 2])
    if personagem['alt_m'] == 2:
        personagem['alt_cm'] = rd.randint(0, 50)
    else:
        personagem['alt_cm'] = rd.randint(0, 95)
    personagem['fisico'] = rd.choice(atributos['fisico'])
    personagem['idade'] = rd.randint(100, 100000)
    personagem['chifres'] = rd.choice(atributos['chifres'])
    personagem['cor_olhos'] = rd.choice(atributos['cores'])
    personagem['cor_pele'] = rd.choice(atributos['pele'])
    personagem['cabelo'] = rd.choice(atributos['cabelo'])
    personagem['tip_cabelo'] = rd.choice(atributos['tip_cabelo'])
    personagem['cor_cabelo'] = rd.choice(atributos['cores'])
    personagem['estatisticas'] = {'força': rd.randint(100, 1000),
                                  'constituicao': rd.randint(100, 1000),
                                  'agilidade': rd.randint(100, 1000),
                                  'resistencia': rd.randint(100, 1000),
                                  'inteligencia': rd.randint(100, 1000),
                                  'sabedoria': rd.randint(100, 1000),
                                  'percepcao': rd.randint(100, 1000),
                                  'arcano': rd.randint(100, 1000),
                                  'fé': rd.randint(10, 100),
                                  'sorte': rd.randint(10, 100),
                                  'carisma': rd.randint(10, 100)}
    
    match personagem['ordem']:
        case 'Sedutora':
            personagem['estatisticas']['carisma'] *= 1.3
            personagem['estatisticas']['percepcao'] *= 1.2
        case 'Manipuladora':
            personagem['estatisticas']['inteligencia'] *= 1.25
            personagem['estatisticas']['sabedoria'] *= 1.25
        case 'Dominadora':
            personagem['estatisticas']['força'] *= 1.2
            personagem['estatisticas']['resistencia'] *= 1.2
        case 'Ilusionista':
            personagem['estatisticas']['arcano'] *= 1.25
            personagem['estatisticas']['sorte'] *= 1.25
        
    modificadores(personagem, atributos, ch1, elementos_disp)

def slime(personagem, atributos, ch1, elementos_disp):
    personagem['especie'] = rd.choice([
    'Slime Ácido', 'Slime Elemental', 'Slime Metálico',
    'Slime Espiritual', 'Slime Parasítico', 'Slime Real'])

    personagem['corpo'] = rd.choice(atributos['corpo'])
    if personagem['corpo'] in ['Humanoide', 'Antropomorfico']:
        if ch1['genero'] == 'f':
            personagem['seios'] = rd.choice(atributos['seios'])
        personagem['alt_m'] = rd.choice([1, 2, 3])
        if personagem['alt_m'] == 3:
            personagem['alt_cm'] = rd.randint(0, 50)
        else:
            personagem['alt_cm'] = rd.randint(0, 90)
        personagem['fisico'] = rd.choice(atributos['fisico'])
        personagem['idade'] = rd.randint(1, 100)
        personagem['cor_olhos'] = rd.choice(atributos['cores'])
        personagem['cor_corpo'] = rd.choice(atributos['cores'])
        personagem['cabelo'] = rd.choice(atributos['cabelo'])
        personagem['tip_cabelo'] = rd.choice(atributos['tip_cabelo'])
        personagem['cor_cabelo'] = rd.choice(atributos['cores'])
    else:
        personagem['alt_m'] = rd.randint(0, 2)
        if personagem['alt_m'] == 2:
            personagem['alt_cm'] = rd.randint(0, 50)
        else:
            personagem['alt_cm'] = rd.randint(0, 90)
        personagem['fisico'] = rd.choice(atributos['fisico'])
        personagem['idade'] = rd.randint(1, 100)
        personagem['cor_olhos'] = rd.choice(atributos['cores'])
        personagem['cor_corpo'] = rd.choice(atributos['cores'])
    personagem['estatisticas'] = {'força': rd.randint(10, 50),
                                    'constituicao': rd.randint(10, 50),
                                    'agilidade': rd.randint(10, 50),
                                    'resistencia': rd.randint(10, 50),
                                    'inteligencia': rd.randint(10, 30),
                                    'sabedoria': rd.randint(10, 50),
                                    'percepcao': rd.randint(10, 50),
                                    'arcano': rd.randint(10, 30),
                                    'fé': rd.randint(10, 100),
                                    'sorte': rd.randint(10, 100),
                                    'carisma': rd.randint(10, 100)}
    match personagem['especie']:
        case 'Slime Ácido':
            personagem['estatisticas']['agilidade'] *= 1.2
            personagem['estatisticas']['percepcao'] *= 1.2
        case 'Slime Elemental':
            personagem['estatisticas']['arcano'] *= 1.25
            personagem['estatisticas']['resistencia'] *= 1.2
        case 'Slime Metálico':
            personagem['estatisticas']['constituicao'] *= 1.25
            personagem['estatisticas']['força'] *= 1.2
        case 'Slime Espiritual':
            personagem['estatisticas']['fé'] *= 1.3
            personagem['estatisticas']['sabedoria'] *= 1.2
        case 'Slime Parasítico':
            personagem['estatisticas']['inteligencia'] *= 1.25
            personagem['estatisticas']['sorte'] *= 1.25
        case 'Slime Real':
            personagem['estatisticas']['carisma'] *= 1.3
            personagem['estatisticas']['resistencia'] *= 1.2
        
    modificadores(personagem, atributos, ch1, elementos_disp)

def elemental(personagem, atributos, ch1, elementos_disp):
    personagem['elemento'] = rd.choice(['Fogo', 'Agua', 'Ar', 'Terra', 'Metal', 'Madeira', 'Vapor', 'Raio', 'Pedra'])
    if ch1['genero'] == 'f':
        personagem['seios'] = rd.choice(atributos['seios'])
    personagem['alt_m'] = rd.choice([ 1, 2])
    if personagem['alt_m'] == 2:
        personagem['alt_cm'] = rd.randint(0, 50)
    else:
        personagem['alt_cm'] = rd.randint(0, 99)
    personagem['fisico'] = rd.choice(atributos['fisico'])
    personagem['idade'] = rd.randint(100, 1000)
    personagem['cor_olhos'] = rd.choice(atributos['cores'])
    match personagem['elemento']:
        case 'Fogo':
            personagem['cor_corpo'] = rd.choice(['Vermelho', 'Branco', 'Azul'])
            personagem['cor_cabelo'] = personagem['cor_corpo']
            personagem['estatisticas'] = {
                'força': rd.randint(80, 120),
                'constituicao': rd.randint(50, 90),
                'agilidade': rd.randint(100, 150),
                'arcano': rd.randint(60, 100),
                'resistencia': rd.randint(50, 90),
                'inteligencia': rd.randint(40, 80),
                'sabedoria': rd.randint(30, 70),
                'percepcao': rd.randint(50, 100),
                'fé': rd.randint(10, 50),
                'sorte': rd.randint(10, 100),
                'carisma': rd.randint(10, 100)
            }

        case 'Agua':
            personagem['cor_corpo'] = rd.choice(['Azul', 'Ciano', 'Turquesa'])
            personagem['cor_cabelo'] = rd.choice(['Azul', 'Branco'])
            personagem['estatisticas'] = {
                'força': rd.randint(30, 70),
                'constituicao': rd.randint(60, 100),
                'agilidade': rd.randint(80, 120),
                'arcano': rd.randint(90, 150),
                'resistencia': rd.randint(60, 100),
                'inteligencia': rd.randint(80, 130),
                'sabedoria': rd.randint(90, 140),
                'percepcao': rd.randint(70, 120),
                'fé': rd.randint(20, 80),
                'sorte': rd.randint(10, 100),
                'carisma': rd.randint(10, 100)
            }
        
        case 'Ar':
            personagem['cor_corpo'] = rd.choice(['Translúcido', 'Cinza Claro', 'Branco'])
            personagem['cor_cabelo'] = rd.choice(['Branco', 'Cinza', 'Prateado'])
            personagem['estatisticas'] = {
                'força': rd.randint(20, 60),
                'constituicao': rd.randint(30, 70),
                'agilidade': rd.randint(130, 180),
                'arcano': rd.randint(90, 140),
                'resistencia': rd.randint(30, 70),
                'inteligencia': rd.randint(80, 120),
                'sabedoria': rd.randint(70, 110),
                'percepcao': rd.randint(100, 160),
                'fé': rd.randint(10, 100),
                'sorte': rd.randint(10, 100),
                'carisma': rd.randint(10, 100)
        }

        case 'Terra':
            personagem['cor_corpo'] = rd.choice(['Marrom', 'Castanho', 'Cinza'])
            personagem['cor_cabelo'] = rd.choice(['Preto', 'Castanho'])
            personagem['estatisticas'] = {
                'força': rd.randint(100, 150),
                'constituicao': rd.randint(100, 150),
                'agilidade': rd.randint(30, 70),
                'arcano': rd.randint(40, 80),
                'resistencia': rd.randint(100, 150),
                'inteligencia': rd.randint(50, 90),
                'sabedoria': rd.randint(60, 100),
                'percepcao': rd.randint(40, 80),
                'fé': rd.randint(10, 100),
                'sorte': rd.randint(10, 100),
                'carisma': rd.randint(10, 100)
            }

        case 'Metal':
            personagem['cor_corpo'] = rd.choice(['Prata', 'Bronze', 'Ouro'])
            personagem['cor_cabelo'] = rd.choice(['Prata', 'Preto'])
            personagem['estatisticas'] = {
                'força': rd.randint(90, 130),
                'constituicao': rd.randint(110, 160),
                'agilidade': rd.randint(40, 80),
                'arcano': rd.randint(50, 90),
                'resistencia': rd.randint(110, 160),
                'inteligencia': rd.randint(60, 100),
                'sabedoria': rd.randint(50, 90),
                'percepcao': rd.randint(40, 80),
                'fé': rd.randint(10, 100),
                'sorte': rd.randint(10, 100),
                'carisma': rd.randint(10, 100)
            }

        case 'Madeira':
            personagem['cor_corpo'] = rd.choice(['Castanho', 'Verde Musgo'])
            personagem['cor_cabelo'] = rd.choice(['Verde', 'Castanho'])
            personagem['estatisticas'] = {
                'força': rd.randint(60, 100),
                'constituicao': rd.randint(60, 100),
                'agilidade': rd.randint(70, 110),
                'arcano': rd.randint(70, 120),
                'resistencia': rd.randint(60, 100),
                'inteligencia': rd.randint(70, 110),
                'sabedoria': rd.randint(80, 130),
                'percepcao': rd.randint(60, 100),
                'fé': rd.randint(10, 100),
                'sorte': rd.randint(10, 100),
                'carisma': rd.randint(10, 100)
            }

        case 'Vapor':
            personagem['cor_corpo'] = 'Nebuloso'
            personagem['cor_cabelo'] = 'Cinza Claro'
            personagem['estatisticas'] = {
                'força': rd.randint(20, 60),
                'constituicao': rd.randint(40, 80),
                'agilidade': rd.randint(100, 160),
                'arcano': rd.randint(80, 140),
                'resistencia': rd.randint(40, 80),
                'inteligencia': rd.randint(90, 140),
                'sabedoria': rd.randint(100, 150),
                'percepcao': rd.randint(120, 180),
                'fé': rd.randint(10, 100),
                'sorte': rd.randint(10, 100),
                'carisma': rd.randint(10, 100)
            }

        case 'Raio':
            personagem['cor_corpo'] = rd.choice(['Amarelo', 'Branco', 'Azul Elétrico'])
            personagem['cor_cabelo'] = rd.choice(['Azul', 'Amarelo'])
            personagem['estatisticas'] = {
                'força': rd.randint(70, 110),
                'constituicao': rd.randint(60, 100),
                'agilidade': rd.randint(120, 180),
                'arcano': rd.randint(100, 160),
                'resistencia': rd.randint(60, 100),
                'inteligencia': rd.randint(80, 120),
                'sabedoria': rd.randint(60, 100),
                'percepcao': rd.randint(100, 150),
                'fé': rd.randint(10, 100),
                'sorte': rd.randint(10, 100),
                'carisma': rd.randint(10, 100)
            }

        case 'Pedra':
            personagem['cor_corpo'] = rd.choice(['Cinza', 'Granito', 'Basalto'])
            personagem['cor_cabelo'] = rd.choice(['Cinza', 'Preto'])
            personagem['estatisticas'] = {
                'força': rd.randint(110, 160),
                'constituicao': rd.randint(130, 180),
                'agilidade': rd.randint(20, 60),
                'arcano': rd.randint(30, 70),
                'resistencia': rd.randint(130, 180),
                'inteligencia': rd.randint(50, 90),
                'sabedoria': rd.randint(60, 100),
                'percepcao': rd.randint(40, 80),
                'fé': rd.randint(10, 100),
                'sorte': rd.randint(10, 100),
                'carisma': rd.randint(10, 100)
            }

    modificadores(personagem, atributos, ch1, elementos_disp)

def modificadores(personagem, atributos, ch1, elementos_disp):
    # controle origem
    if personagem['origem'] == 'Orfão':
        personagem['estatisticas']['agilidade'] *= atributos['origem']['Orfão'][0]
        personagem['estatisticas']['constituicao'] *= atributos['origem']['Orfão'][0]
        personagem['estatisticas']['percepcao'] *= atributos['origem']['Orfão'][0]
        personagem['estatisticas']['inteligencia'] *= atributos['origem']['Orfão'][1]
        personagem['estatisticas']['sabedoria'] *= atributos['origem']['Orfão'][0]

    elif personagem['origem'] == 'Nobre':
        personagem['estatisticas']['carisma'] *= atributos['origem']['Nobre'][0]
        personagem['estatisticas']['inteligencia'] *= atributos['origem']['Nobre'][0]
        personagem['estatisticas']['sabedoria'] *= atributos['origem']['Nobre'][1]

    elif personagem['origem'] == 'Aprendiz de Mago':
        personagem['classe'] = rd.choice(['Mago', 'Feiticeiro', 'Artifice'])
        personagem['estatisticas']['inteligencia'] *= atributos['origem']['Aprendiz de Mago']
        personagem['estatisticas']['arcano'] *= atributos['origem']['Aprendiz de Mago']
        personagem['estatisticas']['percepcao'] *= atributos['origem']['Aprendiz de Mago']
        personagem['estatisticas']['sabedoria'] *= atributos['origem']['Aprendiz de Mago']

    elif personagem['origem'] == 'Semideus':
        personagem['estatisticas']['força'] *= atributos['origem']['Semideus']
        personagem['estatisticas']['constituicao'] *= atributos['origem']['Semideus']
        personagem['estatisticas']['agilidade'] *= atributos['origem']['Semideus']
        personagem['estatisticas']['resistencia'] *= atributos['origem']['Semideus']
        personagem['estatisticas']['inteligencia'] *= atributos['origem']['Semideus']
        personagem['estatisticas']['sabedoria'] *= atributos['origem']['Semideus']
        personagem['estatisticas']['percepcao'] *= atributos['origem']['Semideus']
        personagem['estatisticas']['arcano'] *= atributos['origem']['Semideus']
        personagem['estatisticas']['carisma'] *= atributos['origem']['Semideus']
        if isinstance(personagem['estatisticas']['fé'], (int, float)):
            personagem['estatisticas']['fé'] *= atributos['origem']['Semideus']

    elif personagem['origem'] == 'Divindade':
        if 'Divino' not in personagem['raça']:
            personagem['raça'] += ' Divino'
        personagem['estatisticas']['força'] *= atributos['origem']['Divindade']
        personagem['estatisticas']['constituicao'] *= atributos['origem']['Divindade']
        personagem['estatisticas']['agilidade'] *= atributos['origem']['Divindade']
        personagem['estatisticas']['resistencia'] *= atributos['origem']['Divindade']
        personagem['estatisticas']['inteligencia'] *= atributos['origem']['Divindade']
        personagem['estatisticas']['sabedoria'] *= atributos['origem']['Divindade']
        personagem['estatisticas']['percepcao'] *= atributos['origem']['Divindade']
        personagem['estatisticas']['arcano'] *= atributos['origem']['Divindade']
        personagem['estatisticas']['carisma'] *= atributos['origem']['Divindade']
        personagem['estatisticas']['fé'] = "Ominipotent"

    # modificador Classe:
    if personagem['classe'] in ['Clérico', 'Cultista', 'Paladino']:
        personagem['credo'] = rd.choice(atributos['divindades'])
        if personagem['classe'] == 'Paladino':
            if isinstance(personagem['estatisticas']['fé'], (int, float)):
                personagem['estatisticas']['fé'] *= 1.4
            personagem['estatisticas']['força'] *= 1.4
            personagem['estatisticas']['constituicao'] *= 1.4
            personagem['estatisticas']['resistencia'] *= 1.4
            personagem['estatisticas']['carisma'] *= 1.4
        else:
            if isinstance(personagem['estatisticas']['fé'], (int, float)):
                personagem['estatisticas']['fé'] *= 1.4
            personagem['estatisticas']['inteligencia'] *= 1.4
            personagem['estatisticas']['sabedoria'] *= 1.4
        personagem['proeficiencias'] = rd.sample(atributos['proef_div'], rd.randint(1, 6)) + \
                                       rd.sample(atributos['proef_fis'], rd.randint(1, 3)) + \
                                       rd.sample(atributos['proef_ger'], rd.randint(1, 7))

    elif personagem['classe'] in ['Feiticeiro', 'Mago', 'Artifice']:
        personagem['estatisticas']['arcano'] *= 1.4
        personagem['estatisticas']['inteligencia'] *= 1.4
        personagem['estatisticas']['percepcao'] *= 1.4
        personagem['estatisticas']['sabedoria'] *= 1.4
        personagem['elemento magico 1'] = rd.choice(elementos_disp)
        elementos_disp.remove(personagem['elemento magico 1'])
        if personagem['estatisticas']['arcano'] > 35:
            personagem['elemento magico 2'] = rd.choice(elementos_disp)
            elementos_disp.remove(personagem['elemento magico 2'])
            if personagem['estatisticas']['arcano'] > 50:
                personagem['elemento magico 3'] = rd.choice(elementos_disp)
        personagem['proeficiencias'] = rd.sample(atributos['proef_mag'], rd.randint(1, 6)) + \
                                       rd.sample(atributos['proef_fis'], rd.randint(1, 3)) + \
                                       rd.sample(atributos['proef_ger'], rd.randint(1, 7))

    elif personagem['classe'] in ['Cavaleiro', 'Guerreiro']:
        personagem['estatisticas']['força'] *= 1.4
        personagem['estatisticas']['constituicao'] *= 1.4
        personagem['estatisticas']['resistencia'] *= 1.4
        personagem['proeficiencias'] = rd.sample(atributos['proef_fis'], rd.randint(1, 6)) + \
                                       rd.sample(atributos['proef_ger'], rd.randint(1, 7))

    elif personagem['classe'] in ['Arqueiro', 'Ladino']:
        personagem['estatisticas']['agilidade'] *= 1.4
        personagem['estatisticas']['percepcao'] *= 1.4
        personagem['estatisticas']['inteligencia'] *= 1.4
        personagem['proeficiencias'] = rd.sample(atributos['proef_fis'], rd.randint(1, 6)) + \
                                       rd.sample(atributos['proef_ger'], rd.randint(1, 7))


    elif personagem['classe'] == 'Alquimista':
        personagem['estatisticas']['inteligencia'] *= 1.4
        personagem['estatisticas']['percepcao'] *= 1.4
        personagem['estatisticas']['sabedoria'] *= 1.4
        personagem['proeficiencias'] = rd.sample(atributos['proef_fis'], rd.randint(1, 6)) + \
                                       rd.sample(atributos['proef_ger'], rd.randint(1, 7))


    #modficador fisico
    match personagem['fisico']:
        case 'musculoso':
            personagem['estatisticas']['força'] *= 1.4

        case 'esguio':
            personagem['estatisticas']['agilidade'] *= 1.4

        case 'robusto':
            personagem['estatisticas']['constituicao'] *= 1.4
            personagem['estatisticas']['resistencia'] *= 1.4

def exibir_personagem(personagem):
    print('_-_-_ Ficha do Personagem _-_-_')
    if 'nome' in personagem:
        print(f'Nome: {personagem["nome"]}')
    if 'genero' in personagem:
        print(f'Genero: {personagem["genero"]}')
    if 'raça' in personagem:
        print(f'Raça: {personagem["raça"]}')
    if 'stage' in personagem:
        print(f'Estagio: {personagem["stage"]}')
    if 'caudas' in personagem:
        print(f'Caudas: {personagem["caudas"]}')
    if 'titulo' in personagem:
        print(f'Titulo: {personagem["titulo"]}')
    if 'idade' in personagem:
        print(f'Idade: {personagem["idade"]}')
    if 'especie' in personagem:
        print(f'Espécie: {personagem["especie"]}')
    if 'ordem' in personagem:
        print(f'Ordem: {personagem["ordem"]}')
    if 'asas' in personagem:
        print(f'Asas: {personagem["asas"]}')
    if 'elemento' in personagem:
        print(f'Elemento: {personagem["elemento"]}')
    if 'origem' in personagem:
        print(f'Origem: {personagem["origem"]}')
    if 'classe' in personagem:
        print(f'Classe: {personagem["classe"]}')
    if 'credo' in personagem:
        print(f'Credo: {personagem["credo"]}')
    if 'afinidade_dragonica' in personagem:
        print(f'Afinidade: {personagem["afinidade_dragonica"]}')
    if 'elemento inato' in personagem:
        print(f'Elemento Inato: {personagem["elemento inato"]}')
    if 'elemento magico 1' in personagem:    
        print(f'Elemento Magico 1: {personagem["elemento magico 1"]}')
    if 'elemento magico 2' in personagem:
        print(f'Elemento Magico 2: {personagem["elemento magico 2"]}')
    if 'elemento magico 3' in personagem:            
        print(f'Elemento Magico 3: {personagem["elemento magico 3"]}')
    if 'alt_m' in personagem and 'alt_cm' in personagem:
        print(f'Altura: {personagem["alt_m"]}.{personagem["alt_cm"]} m')
    if 'fisico' in personagem:
        print(f'Fisico: {personagem["fisico"]}')
    if 'cor_pele' in personagem:
        print(f'Cor de Pele: {personagem["cor_pele"]}')
    if 'cor_pelos' in personagem:
        print(f'Cor Pelo: {personagem["cor_pelos"]}')
    if 'cor_corpo' in personagem:
        print(f'Cor Corpo: {personagem["cor_corpo"]}')
    if 'corpo' in personagem:
        print(f'Corpo: {personagem["corpo"]}')
    if 'chifres' in personagem:
        print(f'Chifres: {personagem["chifres"]}')
    if 'cor_escamas' in personagem:
        print(f'Cor Escamas: {personagem["cor_escamas"]}')
    if 'cor_cabelo' in personagem:
        print(f'Cor Cabelo: {personagem["cor_cabelo"]}')
    if 'tip_cabelo' in personagem:
        print(f'Tipo Cabelo: {personagem["tip_cabelo"]}')
    if 'cabelo' in personagem:
        print(f'Comprimento cabelo: {personagem["cabelo"]}')
    if 'seios' in personagem:
        print(f'Busto: {personagem["seios"]}')
    if 'cor_olhos' in personagem:
        print(f'Cor Olhos: {personagem["cor_olhos"]}')
    if 'proeficiencias' in personagem:
        print('Proeficiencias:')
        for i in personagem['proeficiencias']:
            print(f'-> {i}')
    print(f'''--- Stats ---
    Força: {round(personagem["estatisticas"]["força"])}
    Sabedoria: {round(personagem["estatisticas"]["sabedoria"])}
    Constituição: {round(personagem["estatisticas"]["constituicao"])}
    Percepção: {round(personagem["estatisticas"]["percepcao"])}
    Agilidade: {round(personagem["estatisticas"]["agilidade"])}
    Arcano: {round(personagem["estatisticas"]["arcano"])}
    Resistencia: {round(personagem["estatisticas"]["resistencia"])}
    Sorte: {round(personagem["estatisticas"]["sorte"])}
    Inteligencia: {round(personagem["estatisticas"]["inteligencia"])}
    Fé: {round(personagem["estatisticas"]["fé"]) if isinstance(personagem["estatisticas"]["fé"], (int, float)) else personagem["estatisticas"]["fé"]}
    Carisma: {round(personagem["estatisticas"]["carisma"])}''')

if __name__ == '__main__':
    personagem_gerado = gerar_personagem()[0]
    exibir_personagem(personagem_gerado)