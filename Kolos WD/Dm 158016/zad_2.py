
# Przygotuj  funkcję toSamoPole, która przyjmuje 2 argumenty: typu Robaczek oraz
# Owoc, która ma sprawdzać czy znajdują się na tym samym polu

def toSamoPole(rob, ow):
    if int(rob.x) == int(ow['x']) and int(ow['y']) == int(rob.y):
        return True
    return False