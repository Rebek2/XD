
s="""
..........
..sssss...
..........
.s........
.s..s..s..
....s..s..
....s..s..
..s.......
......s...
.........."""
wiersz = 10
kolumna = 10
s=s.splitlines()
s=s[1:]
tab=[]
for i in s:
    tab.append(list(i))
p = [" "] * wiersz

pg = []
for i in p:
    pg.append(list(i*kolumna))
suma = 0
def wypisz(tab):
    print("   0 1 2 3 4 5 6 7 8 9")
    print("   -------------------")
    for i in range(len(tab)):
        print("{}|".format(i),end=" ")
        for j in tab[i]:
                print(j,end=' ')
        print()

    print()

wypisz(tab)
def wstaw(tab,pg):
    w=int(input("Wstaw numer wiersza: "))
    k=int(input("Wstaw numer kolumny: "))
    if tab[w][k] == "s":
        pg[w][k] = "s"
    elif tab[w][k] == '.':
        pg[w][k] = '.'
def koniec(pg):
    w = 0
    for i in pg:
        for j in i:
            if j =="s":
                w = w+1
    return w
while True:
    wypisz(pg)
    wstaw(tab,pg)
    koniec1 = koniec(pg)

    if koniec1 == 15:
        print("Excellent you won!")
        wypisz(tab)
        break
