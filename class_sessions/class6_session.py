# -*- coding: utf-8 -*-
"""
Class 6 - scripts used in class

Created on Wed Nov 23 2016

@author: ASUS
"""
    
# Methodok
# A complex adattípusok (pl. string, list) valójában Python osztályok, ezért vannak method-jaik.

# String methodok listája.
dir(str)

name = 'emese'
# nagybetűsít
name.upper()
# nagybetűvel kezd
name.capitalize()
# egy elem indexe
name.index('m')
name.index('e')
# a kölönböző methodok halmozhatók
name.upper().lower()
# értékltetni lehet, hogy egy string nagybetűs-e
name.islower()
# valamilyen elem vagy sorozat része-e egy szekvenciának
'se' in name
# string összes paraméternek megfelelő részét kicseréli egy másik elemre vagy elemsorra
name.replace('e', '3')
name.replace('e', 'E')

# string szétvágása bizonyos elemeknél, a végeredmény egy lista
s = 'Kezdetben volt az ige.'
sent1 = s.split()
s.split(sep='e')

# a split method ellentéte, egy stringeket elemként tartalmazó lista elemeit összefűzi egyetlen string változóvá, úgy hogy az elemek közé egy megadott string kerül

' '.join(sent1)
','.join(['alma', 'eper'])
' etc '.join(sent1)
sent2 = ' És mégis forog a Föld.\n'
sent2[0]
sent2[-1]
# a string végéről és elejéről eltávolítja a whitespace karaktereket (e.g. ' ', '\n', '\t', '\r')
sent2.strip()

# A listáknak is vannak methodjai.
dir(list)

list1 = [19,1,7,3,4]
list2 = ['Emma', 'Anna', 'Viola']

# megszámolja, hogy meghatározott elem hány alkalommal szerepel a listában
list1.count(1)
# visszaadja a megadott elem indexét
list1.index(7)

# A list methodok meg tudják változtatni a bemeneti változó értékét!!!
# A lent felsorolt list methodok mind megváltoztatják list1 értékét, erre érdemes nagyon figyelni.

# Listához hozzá lehet rendelni új elemeket
list1.append(10)
# és el is lehet távolítani elemket belőle
list1.remove(10)

# A listát ki is lehet bővíteni egy másik lista elemeivel.
list1.extend(list2)
# Az extend és az append methodok nem ugyanazt csinálják! Figyelj a különbségre!
list1.append(list2)

# A lista elemi rendezhetők is. A method itt is meváltoztatja list1 értékét és az eredeti sorrendet már nem lehet visszaállítani belőle.
list1.sort()


# ITERÁCIÓ - CIKLUSOK
# azaz hogyan menjünk végig egy szekvencia minden elemén?


# For ciklus 
# Variációk egy témára.

# 'Hajrá!!!' string kinyomtatása 5-ször.
for elem in [1,2,3,4,5]:
    print(elem)

for elem in range(5):
    print(elem)

for elem in ['Hajrá!!!','Hajrá!!!','Hajrá!!!','Hajrá!!!','Hajrá!!!']:
    print(elem)

for elem in [1,2,3,4,5]:
    print('Hajrá!!!')

for elem in range(100):
    print('Hajrá!!!')
    
s = 'ELTE'
for elem in range(4):
    print(s[elem])
    
for char in s:
    print(char)
    

