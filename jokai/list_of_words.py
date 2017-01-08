# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 12:24:49 2016

@author: ASUS
"""
import os
import re
import string


files = os.listdir()

vocab = set()
punc = '[' + string.punctuation + ']'
tokens = 0
for file in files:
    with open(file, encoding ='utf-8') as f:
        print('Processing {}'.format(file))
        for line in f:
            words = re.sub(punc, '', line)
            words_list= words.strip().lower().split()
            tokens += len(words_list) 
            new_set = set(words_list)
            vocab.update(new_set)
                
print('Jókai Mór {} különböző szót írt le a regényeiben.'.format(len(vocab)))
print('Összes szó: {}\n'.format(tokens))
print('Néhány szó amelyet Jókai használt.')
count = 0
for item in iter(vocab):
    print(item)
    if count > 25:
        break
    count += 1