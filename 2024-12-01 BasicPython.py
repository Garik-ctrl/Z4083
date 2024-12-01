
"""
Hodina Basic Python
01.12.2024
Skupina Z4083
"""
#Datový typ BOOLEAN - 1/0 - TRUE/False
a=20
b=int(input("Zadej číslo od 1 do 100: ")) # input - string
print(a==b)

#Datový typ STRING - text
Prvni_promenna="Ahoj Gariku, " # ukládání do proměnné1
DruhaPromenna="TEST" # ukládání do proměnné2
print(Prvni_promenna + DruhaPromenna) #vytisknutí
print("jak se máš?" + "3+2" + "+")
print("neděle")


#input - vstup od uživatele, zachovává se je to, co zadá uživatel
a=input("Ahoj, zadej své jméno ") #Garik
Ahoj="Ahoj, " # Ahoj,
print(Ahoj + a + "u")
c=a+Ahoj
print(c)

# práce s matematickými operacemi INTEGER
print(3+2) # sčítání čísel výsledek 5
print("3+2") # text výsledek 3+2
print("3"+"2") # text výsledek 32
print("3"+2) # text+číslo výsledek error

"""
Datový typ integer - jsou celá čísla 1,2,-100,-5000
Datový typ float - desetinná čísla 1.0,2.0,-100.0,-5000.0
"""

a=int(5)
b=int(2)
c=a/b
print(c)

#Základní matematické operátory
print(5+2) #sčítání
print(5-2) #odčítání
print(5*2) #násobení
print(5/2) #dělení
print(5**2) #mocnina
print(5%2) #modulo 5/2 = 2 a zbytek 1
print(6%3) #modulo 6/3 = 2 a zbytek 0
print(5//2) #dělení beze zbytku

print(round(6/4,0)) # zaokrohlení
d=float(6/4)
print(type(d))

"""
#Pole: 
list, tuple,set,
dictionary 
 list: 
 
 Pole1 = [5, 3, 2, 11, 13]
indexy polí - od 0 do nekonečna

"""
Pole3=[5, 3, 2, 11, 13, (3,2), "Ahoj", [5,3]] # list s různými typy
print(Pole3)


Pole1 = [5, 3, 2, 11, 13]
print(Pole1[0]) #vytisknutí listu na nulté pozici
print(Pole1[2]) #vytisknutí listu na druhé pozici
#print(Pole1[10]) #Index error - out of range

Pole1.append(999) #přidání jedné hodnoty
print(Pole1)
Pole1.extend([1,2,1,11,1,111]) #přidání více hodnot
print(Pole1)

Pole1.insert(2,-999) #vložení hodnoty na druhou pozici
print(Pole1)

Pole1.pop(2) # smazání prvku na druhé pozici
print(Pole1)

Pole1[5]=0 #přepsání listu na páté pozici
print(Pole1[5])
print(Pole1)
"""
tuple 
"""
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[0])
#my_tuple[0]="chleba" # nelze měnit prvky
print(my_tuple[0])

my_tuple=my_tuple+("orange",)
print(my_tuple)

"""
Sety { }
všechny hodnoty jsou tam právě jednou

"""
Pole2=[5, 3, 2, 11, 13, 0, 1, 2, 1, 11, 1, 111, 1]
Set1=set(Pole2) #změna listu na set
print(Set1)
Set1.add(-15) #přidání prvku
print(Set1)
Set1.update([3,4,5]) #přidání více prvků
print(Set1)
Set1.remove(11) #odebrání prvku
print(Set1)
"""
Dictionary {Klíč:hodnota }
"""
Slovnik=[{
    "titul":"Moby Dick",
    "autor": "Herman Melville",
    "rok": 1851
},
{
    "titul":"Starověká Kréta",
    "autor": "Ludwika Pressová",
    "rok": 1978
}]

print(Slovnik[1]["titul"])


"""
If cyklus 
if Podmínka >,<,<=,>=,== Něco:
    Udělej příkaz 1
else:
    udělej něco jiného
"""
a=10
b=30

if a>b:
    print(a)
else:
    print(b)
"""
Příklad
 zjisti, zda zadané číslo je sudé, nebo liché
"""
cislo=int(input("Zadej číslo: "))

if cislo % 2==0:
    print(f"Zadané číslo {cislo} je sudé")
else:
    print(f"Zadané číslo {cislo} je liché")

"""
Příklad
výpočet budoucí mzdy
uživatel zadá svou mzdu a vy mu vypočítáte budoucí mzdu, 
když je aktuální mzda do 50.000Kč o 8% vyšší
když je aktuální mzda od 50.001Kč o 5% vyšší
"""
mzda=float(input("zadej svoji mzdu: "))

if mzda<=50000:
    print(f"Tvá mzda bude {mzda*1.05:.2f}")
else:
    print(f"Tvá mzda bude {mzda*1.08:.2f}")

"""
větvení if cyklu - mohu pidat nekonečně elif
if podmínka:
    něco
elif podmínka:
    něco2
elif podmínka:
    něco3
else:
    něco4
"""

"""
Příklad
zadej mzdu, pokud je do 20.000 - jsi nízkopříjmová osoba, do 40.000 středněpříjmová od 40.001 vysokopříjmová
"""

cislo=int(input("Zadej svou mzdu "))

if cislo <=20000:
    print("Jsi nízkopříjmová osoba")
elif cislo>20000 and cislo <=40000:
    print("Jsi středněpříjmová osoba")
else:
    print("Jsi vysokopříjmová osoba")

"""
Příklad
BMI
vstupy - Výška a váha
BMI=váha/(výška)^2
do 18,5 - podváha
od 18,6 do 25 - normální váha
od 25,1 - nadváha
"""
cislo = float(input("Zadej svou výšku v metrech"))
cislo2 = float(input("Zadej svou váhu"))
BMI=cislo2/(cislo)**2
if BMI <= 18.5:
    print(f"Máš podváhu {BMI}")
elif BMI > 18.6 and BMI<= 25:
    print(f"Máš normální váhu {BMI:.2f}")
else:
    print(f"Máš nadváhu {BMI}")


"""
Definování funkcí
def název_funkce(parametry)
    dělej něco
    vrať něco

vyvolání funkce
"""

def BMI_INDEX(vyska,vaha):
    BMI=vaha/(vyska)**2
    if BMI <= 18.5:
        vysledek="Máš podváhu"
    elif BMI > 18.6 and BMI<= 25:
        vysledek="Máš normální váhu"
    else:
        vysledek="Máš nadváhu"
    return vysledek

cislo = float(input("Zadej svou výšku v metrech"))
cislo2 = float(input("Zadej svou váhu"))
print(BMI_INDEX(cislo2,cislo))

"""
Příklad
udělej funkci sečti dvě čísla
"""
def secti(x,y):
    return x+y
a=5
b=3
print(secti(a,b))



"""
zadám dvě čísla a já je chci podělit
Pokud budeme dělit nulou, pak vypiš nejde, jinak vypiš podíl zaokrouhlený na 2 desetinná místa
"""
def podil(a,b):
    if b==0:
        return "Nelze dělit nulou"
    else:
        return a/b
a=float(input("Zadej první číslo "))
b=float(input("Zadej druhé číslo "))
print(podil(a,b))
