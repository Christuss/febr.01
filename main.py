
#megoldas
def eredmeny(jatekosPont, gepPont):

    if osszegzes(jatekosPont) > 21:
        print("A játékos vesztett!")
    elif osszegzes(gepPont) > 21:
        print("A gép vesztett!")

def osszegzes(lista):
    osszeg = 0
    for i in range(len(lista)):
        osszeg += lista[i]
    return osszeg
#teszt