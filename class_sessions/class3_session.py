# -*- coding: utf-8 -*-
"""
Class session created on Wed Oct 19 14:40:15 2016

@author: ASUS
"""

# CLASS SESSION No.3

# String ismétlés
#==================================
x  = 'hello'
city = 'Budapest'
#Add vissza az x változó utolsó két karakterét!
x[3:]
x[-2:]
#Add vissza a city változó első és utolsó karakterét!
city[0]+city[-1]

city[0:len(city):7]
#Add vissza az x változó első, második és harmadik karakterét!
x[:3]
#Add vissza a city változó 3-tól 6. karakterét.
city[2:6]
#Add vissza a city változó minden harmadik karakterét!
city[::3]
city[2::3]
#Hozzd létre az x és city változók felhasználásával a következő string-et: ‘hello Budapest’


# Boolean demonstration
#==================================
x = 'hello'
num = 5

len(x) == num

(num**2) >= 100

True == False

3 == 3.0

type(3) != type(3.0)

'b' <= 'a'

not(True) == False

len(x*2) == num + 4

type(False) == bool

type(x) != type('77')

int('77')

x == num

x <= num


#Boolean excercises
#==================================
x = 4.5
y = 'ELTE'
z = False

#Az y változó hosszabb, mint az x változó értéke?
len(y) > x
#Az Y változó típusa string?
type(y) == str
#Ha az Y változó 2. elemét megszorozzuk X egész szám részével, a kifejezés értéke ‘EEEE’ lesz?
(y[1]*int(x))=='EEEE'
#Az X típusa megegyezik Y típusával kifejezés értéke megegyezik Z változó értékével?
(type(x) == type(y)) == z
#Nem (Z változó értéke megegyezik Z értékével)?
not(z == z)

dir(__builtins__)
help(len)



