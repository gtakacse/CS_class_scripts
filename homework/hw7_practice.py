# -*- coding: utf-8 -*-

# ==========================================
#  OTTHONI FELADAT - ISMÉTLÉS
# ==========================================
# A megoldásokkal kitöltött Python fájlt mentsd el úgy, hogy a fájl neve 'hw7_vezetéknév_keresztnév.py' legyen.
# A fájlokat az email címemre küldjétek december 6. (kedd) éjfélig.

# 1)
# Írj egy olyan funkciót, amely egy megadott szám számjegyeit adja össze, pl. az 1234 számjegyeinek összege 1 + 2 + 3 + 4, azaz 10. 
# A funkció neve legyen add_digits.


# 2)
# Írj egy for ciklust a range funkció felhasználásával, ami a következő sorozatot nyomtatja ki a Console-ra.
# 0
# 1
# 4
# 9
# 16
# 25

# 3)
# Írj egy olyan funkciót, amely egy megadott szó mássalhangzóit adja vissza a következő formában! (A  három nyíl a Console promptját jelöli, vagyis a remove_vowels('apple') parancsot a funkció implementálása után a Pythonnak a 'ppl' stringet kell visszadnia.)
#
#'''
#>>> remove_vowels('apple')
#ppl
#>>> remove_vowels('pillangó')
#pllng
#>>> remove_vowels('fülolaj')
#fllj
#>>> remove_vowels('i')
#
#'''

# A sent változó és a korábban inicializált remove_vowels funkció felhasználásával hozz létre egy olyan változót, amely listában sent szavait tárolja magánhangzók nélkül. A lista neve legyen msh_szavak.
# Vigyázz arra, hogy írásjelek ne kerüljenek az msh_szavak elemei között, illetve hogy a listában csak kisbetűs alakok szerepeljenek. A kötőjeles alakokat az egyszerűség kedvéért kezeld külön szavakként, pl. a 'végre-valahára' szó 'vgr' és 'vlhr' stringekként kerüljön be a listába.

sent = 'Háromnegyed egykor, épp abban a pillanatban, mikor a természetrajzi terem katedraasztalán hosszú és sikertelen kísérletek után végre-valahára, nagy nehezen, izgatott várakozás jutalmául a Bunsen-lámpa színtelen lángjában fellobbant egy gyönyörű, smaragdzöld csík, annak jeléül, hogy az a vegyület, melyről a tanár úr be akarta bizonyítani, hogy zöldre festi a lángot, a lángot csakugyan zöldre festette, mondom: pont háromnegyed egykor, épp abban a diadalmas minutumban megpendült a szomszéd ház udvarán egy zongora-verkli, s ezzel minden komolyságnak vége szakadt. Az ablakok tárva-nyitva voltak a meleg márciusi napon, s a friss tavaszi szellő szárnyán berepült a muzsika a tanterembe. Valami vidám magyar nóta volt, ami a verkliből indulónak hangzott, s olyan csinnadrattásan, olyan bécsiesen pengett, hogy az egész osztály mosolyogni szeretett volna, sőt voltak, akik valóban mosolyogtak is rajta. A Bunsen-lámpában vígan lobogott a zöld csík, s ezt valahogyan még csak bámulta az első padból néhány fiú.'

# OPCIONÁLIS HACKER FELADAT
# ==================================
# Márió piramis
# A funkció egy jobbra dőlő félpiramist nyomtat ki, melynek magassága a felhasználó által megadott számtól függ. Tehát a funkciónak így kell működnie:

#>>>mario_piramis(5)
    ##
   ###
  ####
 #####
######

# A piramis magassága tehát a felhasználó által megadott szám. A piramis testét hashtag-ek alkotják, a piramis tetején pedig két hashtag van.
# A felhasználó által megadott számnak 3 és 25 között kell lennie.

#>>>mario_piramis(2)
#'A számnak 3 és 25 kell lennie!'

#>>>mario_piramis(26)
#'A számnak 3 és 25 kell lennie!'