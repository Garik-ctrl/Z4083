"""
Hodina Basic Python
14.12.2024
Skupina Z4083
"""

"""
Př. 1
pomocí funkce průměr spočítáte průměr tří čísel zadaných v listu
"""
def prumer(hodnoty):
    prumer = sum(hodnoty) / len(hodnoty)
    print(f"Průměr z čísel {cisla} je {round(prumer, 2)}")
    # print(f"Průměr z čísel {cisla} je {prumer:.2f}")  alternativně lze využít :.2f
cisla = [2, 3, 5]
prumer(cisla)

"""
for cyklus
FOR proměnná IN podmínka:
    tělo cyklu

"""
def prumer2(hodnoty): #Př. 1 za pomocí FOR cyklu
    suma=0
    pocet=0
    for cislo in hodnoty:
        suma+=cislo #ekvivalentní k suma=suma+cislo
        pocet+=1 #ekvivalentní k pocet=pocet+cislo
    prumer = suma/pocet
    print(f"Průměr z čísel {cisla} je {round(prumer, 2)}")

cisla = [2, 3, 5]
prumer2(cisla)

"""
Př. 2
počet "a" ve větě
"""

veta="Ahoj, jak se máš?"
pocet=0
for pismeno in veta:
    if pismeno=="a":
        pocet+=1
print(pocet)

"""
Př. 3
počet samohlásek (a,e,i,o,u) ve větě
"""

veta="AhOj, jAk se máš?"
print(veta)
print(veta.upper()) #AHOJ, JAK SE MÁŠ?
print(veta.lower()) #ahoj, jak se máš?
print(veta.capitalize()) #Ahoj, jak se máš?
pocet=0
for pismeno in veta.lower():
    if pismeno=="a" or pismeno=="e" or pismeno=="i" or pismeno=="o" or pismeno=="u":
        pocet+=1
print(pocet)

"""
Př. 4
počet nul v zadaném seznamu
"""

seznam = [2, 46, 38, 49, 23, 28, 38, 27, 44, 8, 39, 2, 27, 31, 5, 3, 47, 17, 10, 3, 17, 40, 6, 49, 27, 40, 49, 34, 13,
          18, 10, 29, 39, 14, 7, 40, 11, 34, 20, 32, 12, 10, 44, 9, 41, 16, 1, 33, 44, 1, 1, 40, 26, 31, 10, 28, 7, 24,
          46, 23, 30, 1, 43, 18, 23, 1, 30, 21, 47, 34, 19, 46, 30, 27, 26, 49, 34, 18, 46, 15, 20, 47, 49, 0, 22, 13,
          10, 30, 15, 18, 31, 48, 27, 35, 17, 13, 40, 18, 0, 46]
seznam2 = [46, 0, 41, 27, 38, 48, 41, 43, 0, 1, 16, 29, 23, 10, 26, 22, 19, 39, 30, 4, 44, 20, 11, 22, 18, 47, 13, 37,
           8, 35, 45, 16, 43, 26, 50, 49, 42, 34, 0, 40, 38, 23, 24, 30, 38, 46, 31, 50, 6, 5, 4, 19, 5, 19, 20, 31, 7,
           24, 7, 37, 36, 17, 21, 31, 10, 23, 11, 35, 11, 17, 33, 42, 8, 3, 43, 48, 22, 10, 13, 2, 25, 38, 1, 31, 35,
           19, 16, 37, 32, 16, 32, 9, 47, 25, 32, 24, 46, 32, 1, 18]

def pocet_nul(a):
    pocet=0
    for i in a:
        if i==0:
            pocet+=1
    return pocet

print(pocet_nul(seznam))

def pocet_nul2(a): #rychlejší řešení
    return sum([1 for i in a if i==0])
print(pocet_nul2(seznam))

"""
Př. 5
počet čísel dělitelných třemi v zadaném seznamu
"""

def delitelne_tremi(a):  # definování funkce pocet čísel dělitelných třemi
    pocet = 0
    for i in a:
        if i % 3 == 0:
            pocet += 1
    return pocet
print(delitelne_tremi(seznam))

def delitelne_tremi2(a):  # rychlejší řešení
    return sum([1 for i in a if i%3==0])
print(delitelne_tremi2(seznam))

"""
Př. 6
počet čísel dělitelných třemi nebo pěti, ale ne patnácti v zadaném seznamu
"""

def vypis_delitelne_tremi_nebo_peti_nedelitelne_patnacti(a):
    # definování funkce, která vypíše počet čísel, která jsou dělitelná třemi, nebo 5, ale nejsou dělitelná 15
    pocet = 0
    for i in a:
        if (i % 3 == 0 or i % 5 == 0) and i %15 != 0: #i=2 False
            pocet += 1
    return pocet
print(vypis_delitelne_tremi_nebo_peti_nedelitelne_patnacti(seznam))

def vypis_delitelne_tremi_nebo_peti_nedelitelne_patnacti2(a): # efektivnější řešení
    # definování funkce, která vypíše počet čísel, která jsou dělitelná třemi, nebo 5, ale nejsou dělitelná 15
    return sum([1 for i in a if ((i % 3 == 0 or i % 5 == 0) and i %15 != 0)])
print(vypis_delitelne_tremi_nebo_peti_nedelitelne_patnacti2(seznam))

"""
Př. 7
funkce je_prvocislo
prvočíslo >1 a je dělitelné pouze sebou samým a jedničkou
"""

def prvocislo(cislo):
    if cislo <= 1:
        return False
    for i in range(2, cislo):
        if cislo % i == 0:
            return f"{cislo} není prvočíslo."
    return f"{cislo} je prvočíslo."

cislo = int(input("Zadejte číslo: "))

print(prvocislo(cislo))

"""
WHILE cyklus

while podminka:
    tělo 
    
Důležité je se nezacyklit, neboli jsme si jisti, že algoritmus skončí 
"""

i=10
while i>0: # cyklus tiskne čísla tak dlouho, dokud i >0
    print(i)
    i-=1

"""
Příklad špatného while cyklu, podmínka z>0 je vždy platná, pokud spustím, tak se mi kód zacyklí!!!
"""
i=10
z=10
while z>0:
    print(i)
    i-=1

"""
Př. 8
Faktoriál
5!=5*4*3*2*1 =120
3!=3*2*1
"""
vstup=int(input("zadej kladné číslo: "))

if vstup<1:
    print("číslo není kladné")
else:
    pomoc=vstup
    while pomoc>1:
        pomoc -= 1
        vstup*=pomoc
    print("Výsledek je ", vstup)


"""
Př. 9
Na vstupu zadáváme křestní jména a výstup je "Ahoj" + jméno. Jakmile uživatel zadá "XXX". Program skončí  
"""

pomoc=True
while pomoc==True:
    jmeno=input("zadej své jméno: ")
    if jmeno=="XXX":
        pomoc=False
    else:
        print(f"Ahoj {jmeno}!")

"""
Př. 10
Největší společný dělitel dvou čísel
16,12 
NSD=4
NSD
"""

def NSD(a, b):
    pomoc=min(a,b)
    while pomoc >1:
        if a%pomoc==0 and b% pomoc==0:
            return pomoc
        pomoc-=1
    return 1

print(NSD(16, 19))


"""
Opakování polí
"""
Pole1 = [5, 3, 2, 11, 13]
print(Pole1[0])  # vytisknutí listu na nulté pozici
print(Pole1[2])  # vytisknutí listu na druhé pozici
print(Pole1[10]) #Index error - out of range - chci vytisknout něco na místě, pro které nemám nic definováno

Pole1.append(999)  # přidání jedné hodnoty
Pole1.extend([1, 2, 1, 11, 1, 111])  # přidání více hodnot
Pole1.insert(2, -999)  # vložení hodnoty na druhou pozici
Pole1.pop(2)  # smazání prvku na druhé pozici
Pole1[5] = 0  # přepsání listu na páté pozici

"""
Př. 11
comprehensive functions - snaha o kratší zápis viz výše
"""
seznam = [2, 46, 38, 49, 23, 28, 38, 27, 44, 8, 39, 2, 27, 31, 5, 3, 47, 17, 10, 3, 17, 40, 6, 49, 27, 40, 49, 34, 13,
          18, 10, 29, 39, 14, 7, 40, 11, 34, 20, 32, 12, 10, 44, 9, 41, 16, 1, 33, 44, 1, 1, 40, 26, 31, 10, 28, 7, 24,
          46, 23, 30, 1, 43, 18, 23, 1, 30, 21, 47, 34, 19, 46, 30, 27, 26, 49, 34, 18, 46, 15, 20, 47, 49, 0, 22, 13,
          10, 30, 15, 18, 31, 48, 27, 35, 17, 13, 40, 18, 0, 46]

def delitelne_tremi(a):  # definování funkce pocet čísel dělitelných třemi
    pocet = 0
    pocet2=sum([1 for i in a if i%3==0])
    seznam2=[i for i in a if i%3==0]
    seznam=[]
    for i in a:
        if i % 3 == 0:
            pocet += 1
            seznam.append(i)
    return seznam2, pocet2
print(delitelne_tremi(seznam))

"""
Př. 12
Rozklad na prvočísla
120
120/2?
60
30
15
5
1
2,2,2,3,5
120=2*2*2*3*5
"""
def rozklad_na_prvocisla(n):
    delitele=[]
    if n<=1:
        return "Špatný vstup"
    else:
        pomoc=2
        while n>1:
            if n%pomoc==0:
                delitele.append(pomoc)
                n/=pomoc
            else:
                pomoc+=1
    return delitele

print(rozklad_na_prvocisla(int(input("zadej číslo větší než jedna: "))))

"""
Rozklad na prvočísla
120
120/2?
60
30
15
5
1
2,2,2,3,5
120=2*2*2*3*5
"""
def rozklad_na_prvocisla2(n):
    ciselnik=[]
    if n<2:
        return "Špatný vstup"
    else:
        pomoc=2
        while n>1:
            if n%pomoc==0:
                ciselnik.append(pomoc)
                n/=pomoc
            else:
                pomoc+=1
    return ciselnik
uzivatel=int(input("Zadej číslo větší než 1"))

print(rozklad_na_prvocisla2(uzivatel))

"""
Opakování práce se seznamy
"""
print(seznam)
print(seznam[::2]) #Tisknu každý druhý prvek
print(seznam[::-2]) #Tisknu každý druhý prvek odzadu
print(seznam[1:10:3]) # tisknu každý třetí prvek od indexu jedna do indexu 10

dir(seznam) #funkce pro daný datový typ

"""
Př. 13
palindrom 
level - palindrom
Garik - není palindrom
"""

slova = ["oko", "radar", "python", "madam", "level", "auto" ]

def palindrom(slova):
    palindromy = []
    for slovo in slova:
        if slovo == slovo[::-1]:
            palindromy.append(slovo)
    return print(palindromy)
palindrom(slova)

def palindrom2(slova): #efektivnější řešení
    palindromy2 = [slovo for slovo in slova if slovo == slovo[::-1]]
    return print(palindromy2)
palindrom2(slova)


"""
standardní jednoduchá funkce
"""
def pozdrav():
    print("Ahoj světe")

pozdrav()


"""
standardní jednoduchá funkce - pomocí funkce lambda
"""
pozdrav2=lambda : print("Ahoj světe")
pozdrav2()

"""
*args - umožňuje mi mít nekonečně mnoho proměnných do funkce
"""

def soucet_cisel(*cisla):
    pomoc=0
    for i in cisla:
        pomoc+=i
    return pomoc

print(soucet_cisel(5,4,5,6,8,9))
print(soucet_cisel(5))
print(soucet_cisel())
"""
**kwargs
používáme to na slovníky

slovník={
        klíč:hodnota,
        klíč2:hodnota2,
        klíč3:hodnota3}
"""

def vytvor_slovnik(**kwargs):
    print(kwargs,type(kwargs))
    for klic, hodnota in kwargs.items():
        print(klic, hodnota)

vytvor_slovnik(titul="Starověká Kréta", autor="Ludwika Pressová")

"""
globální a lokální proměnné

globální proměnná je definována v hlavním těle programu
lokální proměnná v dané funkci
"""

def global_local_promenna():
    global_text="Ahoj Alfréde"
    localni_text="Dnes je středa"
    print("Toto je globální proměnná: ", global_text)
    print("Toto je lokální proměnná: ", localni_text)

global_text="Ahoj Gariku"
global_local_promenna()
print("Toto je globální proměnná: ", global_text)
print("Toto je lokální proměnná: ", localni_text)