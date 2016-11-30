# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30, 2016

@author: ASUS
"""

# CLASS 7 SESSION - SOLUTIONS

# FOR LOOP GYAKORLÁSA

sent = 'The quick. brown. fox. jumps over the lazy dog.'
print(sent)

# 1) kisbetűsítsd sent értékét
sent = sent.lower()
print(sent)

# 2) a sent változóból töröld ki a pontot
#sent = sent.replace(sent, sent[:-1])
new_sent= ''
for char in sent:
    if char != '.':
        #csinalj valamit
        new_sent = new_sent + char

sent = sent.replace('.', '')
print('new_sent értéke: {}'.format(new_sent))
        

# 3) bontsd a sent változót szavakra és az eredményt mentsd el a words váltzozóban

words = sent.split()
print(words)
'  hello   '.split()

# 4) írj egy for loop-ot, amely kinyomtatja words minden elemét egyenként, külön sorban

# menj végig words minden elemén
for elem in words:
#   nyomtasd ki az elemet
    print(elem)
    
words.index('the')

for word in words:
    index = words.index(word)
    print('{}\t{}'.format(index, word))
    
range(len(words))

for index in range(len(words)):
    word = words[index]
    print('{}\t{}'.format(index, word))
# 5) írj egy olyan for loop-ot, amely indexelés segítségével megy végig a words lista elemein és a következőt nyomtatja ki: a szó indexe TAB a szó értéke

# 6) hozz létre egy új listát, amely a words változó egyedi elemeit tartalmazza, a változó neve legyen vocab

vocab = []
# menj vegig words elemein
for word in words:
#   nincs benne az elem vocab-ben?
    if word not in vocab:
#       add hozza
        vocab = vocab + [word]

# 7) a vocab lista elemeit nyomtasd ki egyenként úgy, hogy csak mássalhangzók szerepeljenek bennük

# menj vegig vocab elemein
#   uj_alak valtozo letrehozasa
#   menj vegig a szo betuin
#       mgh = 'aeoui'
#       if betu not in mgh
#           uj_alak = uj_alak + betu

