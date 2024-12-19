"""
Hodina Basic Python
15.12.2024
Skupina Z4083
"""

"""
Opakování
globální proměnná - v hlavní struktuře programu
lokální proměnná - v dané funkci

Př. 1 
Příkaz vyvolej jméno a vytiskni
"""
def pozdrav():
    def vnitrni_funkce(): #vnitřní funkce uvnitř jiné funkce vnitrni_funkce()
        print("Toto je funkce uvnitř jiné funkce ")

    lok_prom="1234"
    print("Toto je lokální proměnná: ", lok_prom)
    print("Toto je globální proměnná: ", glob_prom)
    vnitrni_funkce() #uvnitř funkce mohu volat jinou funkci uvnitř sočasné, nebo v dalším těle
    jmeno= input("Zadej své jméno: ") # ve funkci mohu standardně využívat příkazy jako je input
    return jmeno

def another_function(): #Vytvoříme funkci another_function(), která bude volat funkci pozdrav
    return pozdrav() #volám jinou funkcifunkci

glob_prom="Ahoj SDA"
print("Ahoj ",another_function())

"""
Př. 2
pomocí rekurzivní funce - tj. funkce která volá samu sebe
Faktoriál číslo, které je >1
5!=5*4*3*2*1 =120
6!=6*5*4*3*2*1 =720
"""
def rekurze(x):
    if x==1:
        return 1
    else:
        return x*rekurze(x-1) #volám stejnou funkci ale s o jedno nižším argumentem.

print(rekurze(5))

"""
vrať mi výsledek rekurze(x=5) -> 5*rekurze(4)
rekurze(4)=4*rekurze(3)
rekurze(3)=3*rekurze(2)
rekurze(2)=2*rekurze(1)
rekurze(1)=1 - konec programu

rekurze(1)=1
rekurze(2)=2*rekurze(1)=2*1=2
rekurze(3)=3*rekurze(2)=3*2*rekurze(1)=3*2*1
rekurze(4)=4*rekurze(3)=4*3*rekurze(2)=4*3*2*rekurze(1)=4*3*2*1
rekurze(5)=5*rekurze(4)=5*4*rekurze(3)=5*4*3*rekurze(2)=5*4*3*2*rekurze(1)=5*4*3*2*1
vrať mi výsledek rekurze(x=5) -> 5*4*3*2*1=120
"""

"""
Opakování
def soucet_cisel(a,b=0,*c,**d): 
a - povinný parametr, 
b - nepovinný parametr, 
*c - všechna ostatní čísla, 
**d - přidávání do dictionary
"""

"""
Př. 3
Uživatel mi bude dávat čísla a já budu tisknout mezivýpočty  

5 -> mezivýpočet je roven 5
7 -> mezivýpočet je roven 12
10-> mezivýpočet je roven 22
XXX-> celkový součet je roven 22
"""

def count():
    total = 0
    while True:
        user_input = input("Zadejte číslo nebo 'XXX' pro ukončení: ")
        if user_input.upper() == "XXX":
            break
        if user_input.isdigit():
            #isdigit nám dává hodnotu True/False a hodnotí, zdali je zadaný údaj číslo
            total += int(user_input)
            print(f"Mezivýpočet je roven {total}")
        else:
            print("Zadali jste neplatnou hodnotu, zkuste to prosím znovu.")
    print(f"Celkový součet je roven {total}")

count()

def count2(): #2. alternativa
    total = 0
    while (user_input := input("Zadejte číslo nebo 'XXX' pro ukončení: ").upper()) != "XXX":
        if user_input.isdigit():
            total += int(user_input)
            print(f"Mezivýpočet je roven {total}")
        else:
            print("Neplatná hodnota, zkuste to znovu.")
    print(f"Celkový součet je roven {total}")

count()
"""
Př. 4
"""
def say_hello_to_user(name, surname):
    _name = " ".join([name, surname]).title() #propojení pomocí funkce .join
    print(_name)
    def greet_user():
        print(f"Hello {_name}, nice to meet you!")

    greet_user()

    # outer function body
say_hello_to_user('harry', 'pOtter')






