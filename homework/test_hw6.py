import os
import re
import importlib

def main():
    s2_sol = 'nem nekünk való az. mi gazdagok vagyunk és főrangúak. atyám zászlósúr, s a magyarországi három leggazdagabb birtokosok egyike. az ő egyetlen leányának más pályát nyitott a sors vágyai kielégítésére. ott a high life tündérvilága, az udvar olympja. ez a mi versenypiacunk.'

    sentences_sol = ['nem nekünk való az',
                     ' mi gazdagok vagyunk és főrangúak',
                     ' atyám zászlósúr, s a magyarországi három leggazdagabb birtokosok egyike',
                     ' az ő egyetlen leányának más pályát nyitott a sors vágyai kielégítésére',
                     ' ott a high life tündérvilága, az udvar olympja',
                     ' ez a mi versenypiacunk',
                     '']

    sentences2_sol = ['nem nekünk való az',
                      ' mi gazdagok vagyunk és főrangúak',
                      ' atyám zászlósúr, s a magyarországi három leggazdagabb birtokosok egyike',
                      ' az ő egyetlen leányának más pályát nyitott a sors vágyai kielégítésére',
                      ' ott a high life tündérvilága, az udvar olympja',
                      ' ez a mi versenypiacunk']


    words_sents_sol = [['nem', 'nekünk', 'való', 'az'],
                       ['mi', 'gazdagok', 'vagyunk', 'és', 'főrangúak'],
                       ['atyám',
                        'zászlósúr,',
                        's',
                        'a',
                        'magyarországi',
                        'három',
                        'leggazdagabb',
                        'birtokosok',
                        'egyike'],
                       ['az',
                        'ő',
                        'egyetlen',
                        'leányának',
                        'más',
                        'pályát',
                        'nyitott',
                        'a',
                        'sors',
                        'vágyai',
                        'kielégítésére'],
                       ['ott', 'a', 'high', 'life', 'tündérvilága,', 'az', 'udvar', 'olympja'],
                       ['ez', 'a', 'mi', 'versenypiacunk']]

    words_sents2_sol = [['nem', 'nekünk', 'való', 'az'],
                        ['mi', 'gazdagok', 'vagyunk', 'és', 'főrangúak'],
                        ['atyám',
                         'zászlósúr',
                         's',
                         'a',
                         'magyarországi',
                         'három',
                         'leggazdagabb',
                         'birtokosok',
                         'egyike'],
                        ['az',
                         'ő',
                         'egyetlen',
                         'leányának',
                         'más',
                         'pályát',
                         'nyitott',
                         'a',
                         'sors',
                         'vágyai',
                         'kielégítésére'],
                        ['ott', 'a', 'high', 'life', 'tündérvilága', 'az', 'udvar', 'olympja'],
                        ['ez', 'a', 'mi', 'versenypiacunk']]

    vocab_sol = ['nem',
                 'nekünk',
                 'való',
                 'az',
                 'mi',
                 'gazdagok',
                 'vagyunk',
                 'és',
                 'főrangúak',
                 'atyám',
                 'zászlósúr',
                 's',
                 'a',
                 'magyarországi',
                 'három',
                 'leggazdagabb',
                 'birtokosok',
                 'egyike',
                 'ő',
                 'egyetlen',
                 'leányának',
                 'más',
                 'pályát',
                 'nyitott',
                 'sors',
                 'vágyai',
                 'kielégítésére',
                 'ott',
                 'high',
                 'life',
                 'tündérvilága',
                 'udvar',
                 'olympja',
                 'ez',
                 'versenypiacunk']

    file = find_file()
    modul = load_modul(file)
    scores = 0
    total_score=6
    scores += test_variables(modul.s2, s2_sol, 's2')
    scores += test_variables(modul.sentences, sentences_sol, 'sentences')
    scores += test_variables(modul.sentences2, sentences2_sol, 'sentences2')
    scores += test_variables(modul.words_sents, words_sents_sol, 'word_sents')
    scores += test_variables(modul.words_sents2, words_sents2_sol, 'words_sents2')
    scores += test_variables(modul.vocab, vocab_sol, 'vocab')
    get_stats(scores, total_score)

def find_file():
    files = os.listdir(os.curdir)
    for file in files:
        if re.search(r'^hw6.*py$', file) is not None and file != 'hw6_methods_forloop.py':
            return file

def load_modul(file):
    try:
        modul = importlib.import_module(file[:-3])
        print('Trying to load the homework file with the name hw6_name.py\n' + '='*56)
        return modul
    except ImportError:
        print('The {} function cannot be found in {}'.format(file))

def test_variables(stud_solution, expected, variable_name):
    print('For variable {}'.format(variable_name))
    print('Expected: {}'.format(expected))
    print('Received: {}'.format(stud_solution))
    if stud_solution == expected:
        print('The two match. Great job.')
        print('=' * 56)
        return 1
    else:
        print('The two DO NOT match. Keep trying.')
        print('=' * 56)
        return 0

def get_stats(scores, total):
    print('Summary:\n{} out of {}: {}%'.format(scores, total, round(scores / total * 100), 2))
    print('=' * 56)
    print('*' * 56)
    print('=' * 56)

if __name__ == '__main__':
    main()