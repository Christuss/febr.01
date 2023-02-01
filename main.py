
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
    kapott = eredmeny(jatekos, gep)
    vart = "A gép vesztett!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")

def gep_vesztett_teszt():
    jatekos = [8, 6]
    gep = [5, 5, 5, 5, 5]
    kapott = eredmeny(jatekos, gep)
    vart = "A gép vesztett!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")

def tesztek():
    jatekos_vesztett_teszt()
    gep_vesztett_teszt()


tesztek()