# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 20:53:38 2016

@author: GTAKACSE
"""

# CLASS SESSION No.4

# Defining Functions
def greet1(name):
    '''
    Prints out a greeting with name.
    '''
    print('hello', name)
 
x = greet1('Edit')

def greet2(name):
    '''
    Returns a greeting with name.
    '''
    return 'hello ' + name
 
y = greet2('Edit')

#Hogyan lehetne a print() és return parancsokat úgy kombinálni, hogy a funkció értéket is visszaadjon és a kiszámított értéket ki is nyomtassa a felhasználónak?

# buggy version, mert számít a sorrend: a Python interpreter a return statement utáni sorokat nem hajtja végre
def greet3(name):
    '''
    (str) -> str
    Print and return greeting with name.'''
    greet = 'hello' + name
    return greet
    print(greet)

gr = greet3('Maria')

# version no.2
def greet3b(name):
    '''
    (str) -> None
    Print and return greeting with name.'''
    greet = 'hello' + name
    print(greet)
    return greet

# A funkció nyomtat és értéket is visszaad.
gr2 = greet3b('Emese')
    
#Írj egy olyan funkciót, amely visszaadja a háromszög területét!

def haromszogT(height, side):
    '''
    (number, number) -> flaot
    Returns the area of a triangle with given side and height.
    Visszaadja a side oldalú és height magasságú háromszög területét'''
    return (height * side) / 2


t = haromszogT(2,5)