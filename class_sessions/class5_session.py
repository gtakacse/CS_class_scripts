# -*- coding: utf-8 -*-
"""
Scripts for class 5

Created on Wed Nov 16 11:06:19 2016

@author: GTAKACSE
"""

#1. Házi feladat megbeszélése - DEBUGGING TECHNIQUES


#2. IF - ELSE kontrollstruktúrák

def temp_feedback(celsius):
    '''(number)-> None
    Prints out a message according to how the temperature feels.
    Üzentet nyomtat ki a funkció annak függvényében, hogy a celsius értéket milyennek érezzük.
    
    >>>temp_feedback(-4)
    Fagy.
    >>>temp_feedback(30)
    Meleg van.
    '''
    if 0 < celsius <= 15:
        print('Fagy.')
    elif celsius <= 0:
        print('Hideg van.')
    else:
        print('Meleg van.')
        
temp_feedback(-4)
temp_feedback(0)
temp_feedback(15)
temp_feedback(10)
temp_feedback(40)


# Különbség IF - ELSE és IF - IF között
celsius = 0
if celsius <= 0:
    print('Fagy.')
if celsius <= 15:
    print('Hideg van.')
if celsius > 15:
    print('Meleg van.')

# Információ kérése a felhasználótól az input() funkcióval.

name = input('Mi a neved?\n')

num1 = input('Mondj egy számot: ')
num1 = int(num1) # Mert az input funkció mindig strig-et ad vissza.

# Kérjünk még egy számot!
num2 = input('Mondj egy másik számot: ')
num2 = int(num2)


# Írjunk egy funkciót, ami eldönti, hogy két szám az közül az első a második többszöröse-e?

def multi(number1, number2):
    '''
    (number, number) -> Bool
    Első a második többszöröse?
    '''
    result = number1 % number2
    if result == 0:
        return True
    else:
        return False


# Feladat a diáról
# Páros?

# Instrukciók:
#Írj egy olyan funkciót, amely eldönti egy számról, hogy páros-e!
#A funkció boolean (igaz/hamis) értéket adjon vissza!

def is_even(num):
    '''
    (number) -> Bool
    Returns whether num is even or not.
    Visszaadja, hogy num páros-e vagy sem.
    >>>is_even(6)
    True
    >>>is_even(3)
    False
    >>>is_even(0)
    True
    '''
    remainder = num % 2
    if remainder == 0:
        return True
    else:
        return False

is_even(6.0)
is_even(3)
is_even(0)
is_even(-3)

# LIST PYTHON ADATTÍPUS

# Python list = elemek sorozata

list1 = [19,1,7,3,4]
list2 = ['Emma', 'Anna', 'Viola']
list3 = [3.14, 5, 'Emma', num1, [1,2], len]

# Rengeteg mindent lehet Python listákkal csinálni
# Indexelni
list1[0]
list1[-1]

# Meghatározni a benne lévő elemek számát.
len(list2)

# Bizonyos indexszel rendelkező elemek értékét módosítani. (mutable)
list1[0] = 99
list1

# Keresni benne elemeket
1 in [4,3,2,1]
'Emma' in list2

#Mi list1 harmadik eleme?
list1[2]
#Igaz-e: list1 hosszabb mint list2?
len(list1) > len(list2)
#A max() funkcióval állpítsd meg melyik a list1 lista legnagyobb eleme?
max(list1)
#Hozz létre egy új listát, amelynek tartalma legyen list1 első három elemének és list2 utolsó elemének az együttese!
my_list = list1[:3] + list2[-1]
#list1 4. eleme legyen a list2 változó értékével azonos!
list1[2] = list2

# Bónusz. Kód, ami a felhasználó együttműködését teszteli.
x = input('Give me a number: ')
try:
    x = int(x)
except ValueError:
    print('Give me a number!')