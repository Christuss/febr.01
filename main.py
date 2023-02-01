
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
def jatekos_vesztett_teszt():
    jatekos = [5, 5, 5, 5, 5]
    gep = [8, 6]
    print(eredmeny(jatekos, gep))

def tesztek():
    jatekos_vesztett_teszt()


tesztek()