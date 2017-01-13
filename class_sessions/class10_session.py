# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 12:54:53 2017

@author: ASUS
"""
# Összefoglalás és kitekintés

# Főbb adattípusok
# 1. Integer - int
1
# 2. Floating point number - float
1.0
# 3. String - str
'text'
# 4. Boolean - bool
False or True
# 5. List - list
[1, False, 5.6]
# 6. Dictionary - dict
my_dict = {'a': 1, 'b':2}

# Ciklusok
# 1. For ciklus
for item in range(1,6,1):
    print(item)

# 2. While ciklus
count = 1    
while count <= 5:
    print(count)
    count = count + 1

# REGEX modul
import re

text = 'How do you call a pig with 3 eye? Piiig.'
match = re.search(r'do', text)
match.group()
match.span()

# i összes előfordulása
re.findall(r'i', text)
# i első előfordulása
re.search(r'i', text)

# minimum 2 i
re.search(r'ii+', text)

# 2 akármilyen karakter a g előtt
re.search(r'..g', text)

# A a string elején
re.search(r'^A', text)

# a, b, vagy c cseréje X-re
re.sub(r'[abc]', 'X', text)

# a és z között az összes betű cseréje x-re
re.sub(r'[a-z]', 'x', text)

# Komplexebb példa, az összes e-mail cím kinyerése egy szövegből
example = 'Az email címem kaloska45@gmail.com vagy kalos.ka54@freemail.hu.'
pattern = r'\S*@\w+\.\w+'

matches = re.findall(pattern, example)

# HTML letöltése
url = 'http://www.origo.hu/gazdasag/20170111-igy-hasznalja-fel-a-cafeteria-keretet-2017-ben.html'

from urllib import request
html = request.urlopen(url).read().decode('iso-8859-2')

# a letöltött HTML feldolgozása
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())

# az oldal címe
soup.title
# a title tagben szereplő szöveg
soup.title.string

# az összeg bekezdés (ebben a példában a p tagek tárolják a cikk szövegét)
paragraphs = soup.body.find_all('p')
paragraphs[4] # az eredmény indexelhető

# class attribútumú tagek (figyelj rá, hogy a class egy Python parancs, így a html attributumra class_ kulcsszóval lehet)
soup.find(class_='article-lead')

# a weblapon lévő összes link
links = soup.find_all('a')
# a linkhez tartozó url
links[0].get('href')

# NLTK - Natural Language Toolkit
from nltk.corpus.reader import plaintext
# txt formátumú szöveg beolvasása korpszként
reader = plaintext.PlaintextCorpusReader('jokai', fileids='a_ciganybaro.txt')

# a szöveg fodolgozása
from nltk.text import Text
# Text változó létrehozása a szöveg szavaiból, hogy megkönnyítsük a konkordancia stb. készítését
textList = Text(reader.words())

# A szövegben szereplő szavak és az előfordulásaik száma
textList.vocab()

# Konkordencia
textList.concordance('báró')

# Eloszlási ábra
textList.dispersion_plot(['báró', 'bárónő', 'úr'])

# Konstrukciók kis xy és nagy xy formában
textList.findall('<kis> <.*>')
textList.findall('<nagy> <.*>')

# Lemmatizálás magyar nyelvre
from nltk.stem.snowball import HungarianStemmer
stemmer = HungarianStemmer()
stemmer.stem('pirosat')
# Nem tökéletes, a kivételeket nem tudja kezelni, de a szabályos formákat jól kezeli.

# XML fájlok kezelése
import xml.etree.ElementTree as ET
# a példa egy MNSZ2-ről letöltött találati lista
tree = ET.parse('mnsz2.xml')
root = tree.getroot()

# összes találat
hits = root[1]
for line in hits:
	# az összes találat bal kontextusa
	print(line.find('left_context').text)

# az összes találati szó a root vagyis az xml legfelsőbb szintjéről
for kwic in root.iter('kwic'):
	print(kwic.text)

