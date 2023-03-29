from module import *

versenyzok:list[Versenyzo] = []
file = open(file='Eredmenyek.txt', mode='r', encoding='ansi')
for s in file: versenyzok.append(Versenyzo(s))

print(f'versenyzők száma: {len(versenyzok)}')

c_ej:int = 0
for v in versenyzok:
    if v.kategoria == 'elit junior':
        c_ej += 1
print(f'elit junior kategóriában indulók száma: {c_ej}')

s_ek:int = 0
for v in versenyzok:
    s_ek += (2014 - v.szul_ev)
a_ek:float = round(s_ek / len(versenyzok), 1)
print(f'átlagéletkor: {a_ek}')

k_kat:str = input('írj be egy kategóriát: ')
rszamok:list[int] = []
for v in versenyzok:
    if v.kategoria == k_kat:
        rszamok.append(v.rajt_szam)
if len(rszamok) == 0:
    print('\tnincs ilyen kategória!')
else:
    print('\tRajtszam(ok):', end=' ')
    for r in rszamok:
        print(r, end=' ')
    print(end='\n')

nok:list[Versenyzo] = []
for v in versenyzok:
    if not v.nem: nok.append(v)

mini:int = 0
for i in range(1, len(nok)):
    if nok[i].ossz_mp < nok[mini].ossz_mp:
        mini = i
print(f'legjobb női versenyző: {nok[mini].nev}')