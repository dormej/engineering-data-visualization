def wczytaj(path):
    lista = []
    dict = {}
    with open(path) as file:
        lines = [line.strip() for line in file]

    aftersplit = lines[0].split(',')
    dict['robaczek'] = {'x':int(aftersplit[0]), 'y':int(aftersplit[1])}

    for linia in lines:
        if linia != lines[0]:
            linia = linia[::-1]
            donazwy = linia.split(' ')
            dodanych = donazwy[1].split(',')
            slownik = {'x':int(dodanych[1]), 'y':int(dodanych[2]), 'jedzenie':int(dodanych[0]), 'nazwa':donazwy[0]}
            lista.append(slownik)


    dict['owoce'] = lista
    return dict
