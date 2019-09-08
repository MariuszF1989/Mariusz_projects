import random
class Mapa():
    def __init__(self,szerokosc, dlugosc):
        self.szerokosc = szerokosc
        self.dlugosc = dlugosc
        self.mur = []
        self.poczatek = (0,0)
        self.koniec = (szerokosc-1, dlugosc-1)
        self.bohater = (0,0)

    def poruszanie(self, kierunek):
        x = self.bohater[0]
        y = self.bohater[1]
        pozycja = None

        if kierunek[0] == 'd':
            pozycja = (x + 1, y)
        if kierunek[0] == 'a':
            pozycja = (x - 1, y)
        if kierunek[0] == 'w':
            pozycja = (x, y - 1)
        if kierunek[0] == 's':
            pozycja = (x, y + 1)

        if pozycja not in self.mur:
            self.bohater = pozycja

        if pozycja == self.koniec:
            print(f'VICTORY!!!')


def obiekty(gra, sep=' '):
    for y in range(gra.dlugosc):
        for x in range(gra.szerokosc):
            if (x, y) in gra.mur:
                symbol = 'R'
            elif (x, y) == gra.bohater:
                symbol = 'O'
            elif (x, y) == gra.poczatek:
                symbol = '<'
            elif (x, y) == gra.koniec:
                symbol = '>'
            else:
                symbol = '.'
            print(f'{sep} {symbol}', end="")
        print()

def dodaj_mur(gra: Mapa, pct=0.25):
        out = []
        for i in range(int(gra.dlugosc * gra.szerokosc*pct)//2):

            x = random.randint(1, gra.szerokosc-2)
            y = random.randint(1, gra.dlugosc-2)

            out.append((x, y))
            out.append((x + random.choice([-1, 0, 1]), y + random.choice([-1, 0, 1])))
        return out

def main():
    gra = Mapa(10, 10)
    gra.mur = dodaj_mur(gra)

    while gra.bohater != gra.koniec:
        obiekty(gra)
        kierunek = input("Przyciśnij 'a, w, s, d' aby przemieścić")
        print(chr(27) + '[2j')
        gra.poruszanie(kierunek)


if __name__ == '__main__':
    main()


