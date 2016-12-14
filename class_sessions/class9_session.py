# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 15:10:43 2016

@author: ASUS
"""

# While ciklus

# Számoljunk 5-től visszafelé
# For loop-pal így néz ki
for i in range(5,0,-1):
    print(i)
print('Boom!')

# While loop-pal is elérhető
count = 5
while count > -3:
    print(count)
    count = count -1
print('Boom!')
    
# Szótár (dict) struktúra Pythonban

# dict létrehozása
my_dict = {'Emma': 159, 'Anna': 176}
# értékek elérése kulcsok segítségével
my_dict['Anna']
# új kulcs-érték pár hozzáadása
my_dict['Laci'] = 190
my_dict['Laci']
# szótár elemének törlése
del my_dict['Anna']

my_dict
# szótár hossza
len(my_dict)

# szótár kulcsai
my_dict.keys()
# szótár értékei
my_dict.values()
# szótár kulcs-érték párjai
my_dict.items()

katalog= {
'eper' : 'növény', 
'asztal': 'tárgy', 
'kutya': 'állat', 
'fa' : 'növény', 
'macska': 'állat'
}

# szótár kulcs-érték párjainak kinyomtatása egyenként
for item in katalog.items():
    print(item)

# szótár kulcs-érték párjainak kinyomtatása egyenként, a kulcsok segítségével
for key in katalog.keys():
    print(key, katalog[key])

# egy kulcs meglétét tesztelni a szótárban
'elefánt' in katalog.keys()
    
# inverz szótár készítése, A:B párokból, ahol A a kulcs, B az érték, B:A párokat csinálunk, ahol B a kulcs és A az érték
    
inv_katalog = {}

# egyenként végigmenni a kulcsokon
for key in katalog.keys():  
    # az új kulcs a régi értéke
    new_key = katalog[key]
    # az új érték a régi kulcsa    
    new_value = key
    # nem akarunk információt elveszteni, így teszteljük, hogy new_key értéke már szerepel-e az inverz szótárban    
    if new_key in inv_katalog.keys():
        # ha szerepel, hozzáadjuk a már meglévő értékhez az újat
        inv_katalog[new_key].append(new_value)
    else:
        # ha nem, létrehozunk egy szótári recordot, amelyben az érték típusa lista, hogy könnyen új elemeket lehessen hozzáadni
        inv_katalog[new_key] = [new_value]
    
# ellenőrizzük inv_katalog értékét
inv_katalog

# CSV fájlok beolvasása - veszélyeztetett nyelvek

# Elérési útvonal beállítása
#import os
#os.getcwd()
#os.chdir('C:\\Users\\ASUS\\Desktop')

f = open('end_lang.csv', 'r', encoding='utf-8')
# hozz létre egy változót az eredményeknek
lang_dict = {}
# olvass be egy sort
line = f.readline()
# menj végig a fájl minden során, amíg üres string nem lesz line értéke
while line != '':
    # a sorok végéről távolítsd el a newline karaktereket és vágd szét őket a vesszőknél
    data = line.strip().split(',')
    # az első elem a nyelv
    lang = data[0]
    # az utolsó a beszélők száma
    speakers = data[-1]
    # adjuk hozzá őket a szótárhoz, úgy hogy a nyelv legyen a kulcs, a beszélők száma pedig az érték integerként
    lang_dict[lang] = int(speakers)
    # line értékét frissítsük, olvassuk be a következő sort
    line = f.readline()
# miután végeztünk zárjuk be a fájlt
f.close()

# opcionális vizualizáció
import matplotlib.pyplot as plt
x= list(lang_dict.values())
bins=100
plt.hist(x,bins,range=[0,100])
plt.title('Number of speakers of endangered languages')
plt.xlabel('number of speakers')
plt.show()


f.close()



