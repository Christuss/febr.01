
# megoldas
def eredmeny(jatekosLista, gepLista):
    jatekosPont = osszegzes(jatekosLista)
    gepPont = osszegzes(gepLista)
    jatekosDarab = len(jatekosLista)
    gepDarab = len(gepLista)
    if jatekosPont <= 21 and gepPont <= 21:
        if jatekosPont > gepPont:
            s = "A játékos nyert"
        elif gepPont > jatekosPont:
            s = "A gép nyert"
        elif gepPont == jatekosPont:
            if jatekosDarab < gepDarab:
                s = "A játékos nyert"
            elif jatekosDarab > gepDarab:
                s = "A gép nyert"
            else:
                s = "Döntetlen, osztoztok a nyereségen"
    elif jatekosPont > 21:
        s = "A játékos vesztett"
    if gepPont > 21:
        s = "A gép vesztett"
    if jatekosPont > 21 and gepPont > 21:
        s = "döntetlen, a Ház nyert!"
    return s

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
    vart = "A játékos vesztett"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")

def gep_vesztett_teszt():
    jatekos = [8, 6]
    gep = [5, 5, 5, 5, 5]
    kapott = eredmeny(jatekos, gep)
    vart = "A gép vesztett"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")


def jatekos_vesztett_teszt_2():
    jatekos = [8, 6]
    gep = [5, 5, 5, 5]
    kapott = eredmeny(jatekos, gep)
    vart = "A gép nyert"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")


def gep_vesztett_teszt_2():
    jatekos = [8, 8]
    gep = [5, 5, 9]
    kapott = eredmeny(jatekos, gep)
    vart = "A gép nyert"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")


def gep_vesztett_teszt_3():
    jatekos = [8, 8]
    gep = [5, 5, 6]
    kapott = eredmeny(jatekos, gep)
    vart = "A játékos nyert"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")


def jatekos_vesztett_teszt_3():
    jatekos = [4, 6, 6]
    gep = [8, 8]
    kapott = eredmeny(jatekos, gep)
    vart = "A gép nyert"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")


def dontetlen_vesztettek_teszt():
    jatekos = [11, 11]
    gep = [11, 11]
    kapott = eredmeny(jatekos, gep)
    vart = "döntetlen, a Ház nyert!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott!")


def dontetlen_nyertek_teszt():
    jatekos = [11, 9]
    gep = [11, 9]
    kapott = eredmeny(jatekos, gep)
    vart = "Döntetlen, osztoztok a nyereségen"
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