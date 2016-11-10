# ==========================================
#  OTTHONI FELADAT - DEFINING FUNCTIONS, IF STATEMENTS
# ==========================================
# A megoldásokkal kitöltött Python fájlt mentsd el úgy, hogy a fájl neve 'hw4_vezetéknév_keresztnév.py' legyen.
# A fájlokat az email címemre küldjétek. 
# Határidő: november 14. éjfél


# DEFINING FUNCTIONS
#==============================

# 1. Írj egy funkciót, amely az alapján ad vissza True/False értéket, hogy a bemeneti két string paraméter hossza
# egyenlő vagy sem!
# A funkció neve legyen is_equal!
# A funkciónak tartalmaznia kell egy konvencionális docstring-et is, illetve ne felejtsd el a funkciódat tesztelni sem!


# Ide írd a kódodat!



# 2. Írj egy olyan funkciót, amely fahrenheitről vált celsiusra!
# A funkció neve legyen fahr2celsius!
# A funkciónak tartalmaznia kell egy konvencionális docstring-et is, illetve ne felejtsd el a funkciódat tesztelni sem!


# Ide írd a kódodat!


# 3. Írj egy olyan funkciót, amely egy string utolsó x karakterét adja vissza! Az x egy olyan szám,
# amit a felhasználó inputkét ad meg. Tehát ha a funkció a 'hello Budapest' string-et és a 4-es számot kapja,
# akkor a 'pest' értéket adja vissza!
# A funkció neve legyen last_n_char!
# A funkciónak tartalmaznia kell egy konvencionális docstring-et is, illetve ne felejtsd el a funkciódat tesztelni sem!


# Ide írd a kódodat!

# +++ Opcionális feladat heckereknek. 
# Az órán az if else struktúrákra már nem jutott idő, de egy kis ízelítőként a következő órához itt egy példa az if struktúrákhoz.

# ha a hőmérséklet 0 fok alatt van, akkor fagy
temp = 5
if temp <= 0:
    print('Fagy.')
# egyébként ha a hőmérséklet 15 fok alatt van, akkor hideg van
elif temp <= 15:
     print('Hideg van.')
# minden más esetben, ha a fentiek egyike sem teljesül, akkor meleg van
else:
    print('Meleg van.')
    
# a fenti struktúra akár funkcióba is foglalható például így:

def temp_feedback(celsius):
    '''(number)-> None
    Prints out a message according to how the temperature feels.
    Üzentet nyomtat ki a funkció annak függvényében, hogy a celsius értéket milyennek érezzük.
    
    >>>temp_feedback(-4)
    Fagy.
    >>>temp_feedback(30)
    Meleg van.
    '''
    if celsius <= 0:
        print('Fagy.')
    elif celsius <= 15:
        print('Hideg van.')
    else:
        print('Meleg van.')
        
temp_feedback(-4)
temp_feedback(30)
temp_feedback(10.5)
        
# A fentiek alapják, aki elég kedvet érez magában, az próbálkozhat az 5. feladattal is. DE EZ TERMÉSZETESEN NEM KÖTELEZŐ!

# 4. Írj egy olyan funkciót, amely két string bemeneti paraméterről megállapítja, hogy melyik a hosszabb és annak
# megfelő feedback-et ad a felhasználónak.
# Például ha a funkció a "kutya" és a "macska" szavakat kapja, a következőt nyomtatja a konzolra: 'A(z) "macska" szó
# hosszabb mint a(z) "kutya" szó.'
# Ha funkció egyenlő hosszú szavakat kap, a következő üzenetet nyomtatja: 'A megadott szavak egyenlő hosszúak.'
# Ha a megadott input-ok bármelyike nem string típusú, a következő üzenetet adja vissza: 'A funkció két string típusú
#  argumentumot követel. Kérem string értékeket adjon meg!'
# A funkció neve legyen longer!
# A funkciónak tartalmaznia kell egy konvencionális docstring-et is, illetve ne felejtsd el a funkciódat tesztelni sem!



# Ide írd a kódodat!
