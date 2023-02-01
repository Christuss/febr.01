
# megoldas
def eredmeny(jatekosLapok: [int], gepLapok: [int]):
    if osszegzes(jatekosLapok) > 21:
        return "A játékos vesztett!"
    elif osszegzes(gepLapok) > 21:
        return "A gép vesztett!"

def osszegzes(lista):
    osszeg = 0
    for i in range(len(lista)):
        osszeg += lista[i]
    return osszeg
# teszt
