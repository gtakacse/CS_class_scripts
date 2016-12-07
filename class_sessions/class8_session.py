# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:12:44 2016

@author: ASUS
"""

path = 'C:\\Users\\ASUS\\Desktop\\szilagyi_hajnal.txt'
path2 = 'C:/Users/ASUS/Desktop/szilagyi_hajnal.txt'

f = open(path2, encoding='utf-8')
data = f.read()
f.close()

f = open(path2, encoding='utf-8')
data2 = f.readlines()
f.close()

for line in data2:
    print(line)
    
f = open(path2, encoding='utf-8')
elso = f.readline()
masodik = f.readline()
f.close()

with open(path2, encoding='utf-8') as f:
    data = f.read()


import os
os.getcwd()

path3 = 'szilagyi_hajnal.txt'
f = open(path3, encoding='utf-8')
d = f.read()
print(d)
f.close()

new_path = 'C:/Users/ASUS/Desktop'
os.chdir(new_path)
os.getcwd()


f = open('test.txt', 'w')
f.write('hello\n')
f.write('könnyű fájlba írni Pythonnal\n')
f.close()

f = open('test.txt', 'a')
for i in range(6):
    f.write('ELTE\n')
f.close()

# A DIÁN SZEREPLŐ FELADAT KÉT LEHETSÉGES MEGOLDÁSA
    
#Olvasd be a 'szilagyi_hajnal.txt' nevű fájlt Python-ba.
path = 'szilagyi_hajnal.txt'
f = open(path, encoding='utf-8')
data = f.read()
f.close()

# Opcionális: a szöveg megtisztítása (írásjelek eltüntetése, kisbetűsítés)
clean_data = data.lower()
punc = ';.,!'
for p in punc:
    clean_data = clean_data.replace(p,'')

#Keresd meg a szöveg leghosszab szavát vagy szavait.
#1. megoldás string típussal, ha csak egy stringet akarunk visszaadni
leghosszabb = ''
words = clean_data.split()

for word in words:
    if len(word) > len(leghosszabb):
        leghosszabb = word

# Viszont, ha a leghosszabb n karakter hosszú, és több n karakter hosszú szó is lenne a szövegben, az első megoldás nem tudja visszaadni az összeset
# 2. megoldás lista változóval
leghosszabb_lista = []
hossz = 0

for word in words:
    # ha word hosszabb mint bármelyik korábban látott szó
    if len(word) > hossz:
        # update leghosszabb_lista és hossz értékét
        leghosszabb_lista = [] # még nem láttunk olyan hosszú szót, mint word, így a leghosszabb_lista változóban csak word értékét akarjuk látni
        leghosszabb_lista.append(word)
        hossz = len(word)
    # ha word ugyanolyan hosszú, mint az eddig látott leghosszabb szó
    elif len(word) == hossz:
        # adjuk hozzá az új szót a leghosszab_lista változóhoz
        leghosszabb_lista.append(word)
    # egyéb esetben nem kell semmit csinálnunk, így azt nem kell specifikálni

#Hozz létre egy új txt fájlt 'leghosszabb_szo.txt' címmel.
f  = open('leghosszabb_szo.txt','w')
#A fájl tartalma legyen a következő:
#név
f.write('Takács Edit\n')
#dátum
f.write('2016. december 7.\n')
# 
f.write('\n')
#leghosszabb szó (ha van több ugyanolyan hosszú szó, szavak kerüljenek új sorokba)
# 1. változatban
f.write(leghosszabb)
# 2. változatban
for word in leghosszabb_lista:
    f.write(word)
    f.write('\n')
    
# Ne felejtsük el becsukni a fájlt
f.close()



