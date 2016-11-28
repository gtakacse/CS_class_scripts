# ==========================================
#  OTTHONI FELADAT - STRING & LIST METHODS, FOR LOOPS
# ==========================================
# A megoldásokkal kitöltött Python fájlt mentsd el úgy, hogy a fájl neve 'hw6_vezetéknév_keresztnév.py' legyen.
# A fájlokat az email címemre küldjétek november 28. éjfélig.

# SZÖVEG MANIPULÁCIÓJA
# ====================
# Az s változó értéke Jókai egyik regényének bevezetőjében található. A következőkben string methodok segítségével ezt a részletet kell az instrukciók alapján átalakítanotok.
s = 'Nem nekünk való az. Mi gazdagok vagyunk és főrangúak. Atyám zászlósúr, s a magyarországi három leggazdagabb birtokosok egyike. Az ő egyetlen leányának más pályát nyitott a sors vágyai kielégítésére. Ott a high life tündérvilága, az udvar Olympja. Ez a mi versenypiacunk.'

# 1)
# Az s változót alkítsd át kisbetűsre, az eredményt pedig mentsd el az s2 változóban.

# 2)
# A split method segítségével bontsd az s2 változóban szereplő szöveget mondatokra. Az eredményt mentsd el a sentences változóban.

# 3)
# A split miatt marad egy üres string a sentences lista végén. Ezt próbáljuk kiküszöbölnöm a sentences2 váltözóban.
# Lent inicializáltam a sentences2 változót üres listaként. A feladatod az lesz, hogy menj végig for loop
# segítségével sentences minden egyes elemén és ha valamelyik elem értéke nem üres string (i.e. ''), akkor azt az
# elemet fűzd hozzá a sentences2 listához.
sentences2 = []

# 4)
# Bonstd a sentences2 változó mondatait szavakra, és az eredményt mentsd el a words_sents változóba. A words_sents tehát egy lista, amely mondatoknak megfelelő listákat tartalmaz, amelyekben az egyes szavak vannak.
# Tehát a következő absztrakt feladatot kell végrehajtani:
# ['első mondat', 'második modat'] -> [['első', 'mondat], ['második', 'mondat]]
# Hint: minden a listában szereplő mondaton for ciklussal tudsz végigmenni, a split method segítségével pedig szavakra tudok őket szedni.

# 5)
# Ha megnézed a words_sents változó értékét, láthatod, hogy a vesszők a szóalak részeként kerültek bele. Javítsuk ezt
#  úgy ki, hogy a words_sents2 új változóhoz hozzáadjuk a vessző szempontjából már kijavított mondatokat.
# Hint: Mivel a replace method csak stringeken és nem listákon működik, ezért két for ciklust kell használni,
# amiből az egyik végigmegy az összes mondaton, a másik pedig a mondat összes szaván. Ennek a következő a templateje:

l1 = [[1,2], [3,4]] #lista, ami listákat tartalmaz
l2 = [] # új lista inicializálása, ami kérsőbb majd a módosított elemeket fogja tartalmazni
for sublist in l1:
    new_sublist = [] # a belső listákat helyettesítő új lista inicializálása
    for item in sublist:
        new_sublist.append(item+1) # az allistához hozzáadom a módosított elemet, jelen esetben hozzáadok 1-et
    l2.append(new_sublist) # az új listához hozzáadom az új allistát, miután minden módosított elemet hozzáadtam
print(l2) # a folyamat végén l2 értéke: [[2, 3], [4, 5]]

# Ha nem vagy biztos abban, hogy az egyes sorban mit csinál a gép, a kódvizalizációs eszköz segíteni tud (http://www.pythontutor.com/visualize.html#mode=edit).

words_sents2 = []

# 6)
# Csinálj egy egyszerű szótárt az s2 váltzóból (egy listát, amely a szövegben előforduló szavakat tartalmazza egyetlen egyszer). A szólistát mentsd el a vocab változóban, amelyet lent üres listaként inicializáltam neked. A
# szóalakokat úgy add hozzá a vocab változóhoz, hogy nem tartalmaz vesszőt vagy pontot.
# Hint: Az in (tagadása a not in) operátor segítségével tudod megnézni, hogy egy elem része-e egy listának. Tehát ha a szöveg egy szava nem része a vocab listának, akkor és csakis akkor kell hozzáadni a vocab listához.
vocab = []



