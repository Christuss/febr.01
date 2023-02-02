
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
    vart = "A játékos vesztett!"
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


def jatekos_vesztett_teszt_2():
    jatekos = [8, 6]
    gep = [5, 5, 5, 5]
    kapott = eredmeny(jatekos, gep)
    if osszegzes(jatekos) > osszegzes(gep):
        kapott = "A játékos nyert!"
    elif osszegzes(gep) > osszegzes(jatekos):
        kapott = "A játékos vesztett!"
    vart = "A játékos vesztett!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")


def gep_vesztett_teszt_2():
    jatekos = [8, 8]
    gep = [5, 5, 9]
    kapott = eredmeny(jatekos, gep)
    if osszegzes(jatekos) > osszegzes(gep):
        kapott = "A játékos nyert!"
    elif osszegzes(gep) > osszegzes(jatekos):
        kapott = "A gép nyert!"
    vart = "A gép nyert!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")


def gep_vesztett_teszt_3():
    jatekos = [8, 8]
    gep = [5, 5, 6]
    kapott = eredmeny(jatekos, gep)
    if osszegzes(jatekos) == osszegzes(gep):
        if len(jatekos) > len(gep):
            kapott = "A gép nyert!"
        elif len(gep) > len(jatekos):
            kapott = "A játékos nyert!"
    vart = "A játékos nyert!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")


def jatekos_vesztett_teszt_3():
    jatekos = [4, 6, 6]
    gep = [8, 8]
    kapott = eredmeny(jatekos, gep)
    if osszegzes(jatekos) == osszegzes(gep):
        if len(jatekos) > len(gep):
            kapott = "A gép nyert!"
        elif len(gep) > len(jatekos):
            kapott = "A játékos nyert!"
    vart = "A gép nyert!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")


def dontetlen_vesztettek_teszt():
    jatekos = [11, 11]
    gep = [11, 11]
    kapott = eredmeny(jatekos, gep)
    if osszegzes(jatekos) == osszegzes(gep):
        if len(jatekos) > len(gep):
            kapott = "A gép nyert!"
        elif len(gep) > len(jatekos):
            kapott = "A játékos nyert!"
        elif osszegzes(jatekos) > 21:
            kapott = "Döntetlen, vesztettetek!"
    vart = "Döntetlen, vesztettetek!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")


def dontetlen_nyertek_teszt():
    jatekos = [11, 9]
    gep = [11, 9]
    kapott = eredmeny(jatekos, gep)
    if osszegzes(jatekos) == osszegzes(gep):
        if len(jatekos) > len(gep):
            kapott = "A gép nyert!"
        elif len(gep) > len(jatekos):
            kapott = "A játékos nyert!"
        elif osszegzes(jatekos) > 21:
            kapott = "Döntetlen, vesztettetek!"
        else:
            kapott = "Döntetlen, nyertetek!"
    vart = "Döntetlen, nyertetek!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")



def tesztek():
    jatekos_vesztett_teszt()
    gep_vesztett_teszt()
    jatekos_vesztett_teszt_2()
    gep_vesztett_teszt_2()
    jatekos_vesztett_teszt_3()
    gep_vesztett_teszt_3()
    dontetlen_vesztettek_teszt()
    dontetlen_nyertek_teszt()


tesztek()