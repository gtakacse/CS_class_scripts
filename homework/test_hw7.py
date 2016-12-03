import re
import os
import importlib
import sys
from io import StringIO

def main():
    file = find_file()
    modul = load_modul(file)
    scores = 0
    scores += test_add_digits(modul)
    scores += test_remove_vowels(modul)
    msh_szavak_sol = ['hrmngyd', 'gykr', 'pp', 'bbn', '', 'pllntbn', 'mkr', '', 'trmsztrjz', 'trm', 'ktdrsztln', 'hssz', 's', 'skrtln', 'ksrltk', 'tn', 'vgr', 'vlhr', 'ngy', 'nhzn', 'zgttt', 'vrkzs', 'jtlml', '', 'bnsn', 'lmp', 'szntln', 'lngjbn', 'fllbbnt', 'gy', 'gynyr', 'smrgdzld', 'csk', 'nnk', 'jll', 'hgy', 'z', '', 'vgylt', 'mlyrl', '', 'tnr', 'r', 'b', 'krt', 'bznytn', 'hgy', 'zldr', 'fst', '', 'lngt', '', 'lngt', 'cskgyn', 'zldr', 'fsttt', 'mndm', 'pnt', 'hrmngyd', 'gykr', 'pp', 'bbn', '', 'ddlms', 'mntmbn', 'mgpndlt', '', 'szmszd', 'hz', 'dvrn', 'gy', 'zngr', 'vrkl', 's', 'zzl', 'mndn', 'kmlysgnk', 'vg', 'szkdt', 'z', 'blkk', 'trv', 'nytv', 'vltk', '', 'mlg', 'mrcs', 'npn', 's', '', 'frss', 'tvsz', 'szll', 'szrnyn', 'brplt', '', 'mzsk', '', 'tntrmb', 'vlm', 'vdm', 'mgyr', 'nt', 'vlt', 'm', '', 'vrklbl', 'ndlnk', 'hngztt', 's', 'lyn', 'csnndrttsn', 'lyn', 'bcssn', 'pngtt', 'hgy', 'z', 'gsz', 'sztly', 'mslygn', 'szrttt', 'vln', 'st', 'vltk', 'kk', 'vlbn', 'mslygtk', 's', 'rjt', '', 'bnsn', 'lmpbn', 'vgn', 'lbgtt', '', 'zld', 'csk', 's', 'zt', 'vlhgyn', 'mg', 'csk', 'bmlt', 'z', 'ls', 'pdbl', 'nhny', 'f']
    scores += test_msh_sent_list(modul, msh_szavak_sol)
    get_stats(scores, 10)
    try:
        test_mario(modul)
    except AttributeError:
        print('The mario_piramis function is not found.')



def find_file():
    files = os.listdir(os.curdir)
    for file in files:
        if re.search(r'^hw7.*py', file) is not None:
            return file

def load_modul(file):
    try:
        modul = importlib.import_module(file[:-3])
        print('Trying to load the homework file with the structure hw5_name.py\n' + '='*56)
        return modul
    except ImportError:
        print('The {} function cannot be found in {}'.format(file))

def get_print_output(function, input=None):
    backup = sys.stdout
    out = StringIO()
    sys.stdout = out
    if input is None:
        function()
    else:
        function(*input)
    #sys.stdout.close()
    sys.stdout = backup
    return out.getvalue().split('\n')[:-1]
    
def pretty_print(text_list):
    for line in text_list:
        print(line)
        
def feedback(input, expected_output, got, pprint=False):
    if pprint == False:
        print('Input: {}'.format(input))
        print('Expected: {}'.format(expected_output))
        print('Got: {}'.format(got))
    else:
        print('Input: {}'.format(input))
        print('Expected:')
        pretty_print(expected_output)
        print('Got:')
        pretty_print(got)

    if got == expected_output:
        print('Test passed.')
        print('=' * 56)
        return 0
    else:
        print('Test failed. Check your function.')
        print('=' * 56)
        return 1
        
def func_test(input, output, function):

    got = function(*input)
    mistake = feedback(input, output, got)

    return mistake

def get_stats(scores, total):
    print('Summary:\n{} out of {}: {}%'.format(scores, total, round(scores/total*100),2))
    print('='*56)
    print('*'*56)
    print('='*56)
    
def test_add_digits(modul):
    print('*'*56)
    print('TESTING ADD_DIGITS FUNCTION')
    print('*'*56)
    test_cases = [([1234], 10),
([-123],6), ([123456], 21), ([290], 11)]
    mistakes = 0
    for t in test_cases:
        mistakes += func_test(t[0], t[1], modul.add_digits)
    if mistakes == 0:
        print('Great job! Test passed. The function works as intended.')
        print('=' * 56)
    return len(test_cases)-mistakes
    
def test_remove_vowels(modul):
    print('*'*56)
    print('TESTING REMOVE_VOWELS FUNCTION')
    print('*'*56)
    test_cases = [(['apple'], 'ppl'),
(['pillangó'], 'pllng'), (['fülolaj'], 'fllj'), (['i'], ''), (['megadott'], 'mgdtt')]
    mistakes = 0
    for t in test_cases:
        mistakes += func_test(t[0], t[1], modul.remove_vowels)
    if mistakes == 0:
        print('Great job! Test passed. The function works as intended.')
        print('=' * 56)
    return len(test_cases)-mistakes
    
def test_msh_sent_list(modul, solution):
    print('*'*56)
    print('TESTING MSH_SENT_LIST VARIABLE')
    print('*'*56)
    print('Expected msh_szavak value: {}'.format(solution))
    print('Got: {}'.format(modul.msh_szavak))
    
    if modul.msh_szavak == solution:
            print('Test passed.')
            print('=' * 56)
            return 1
    else:
            print('Test failed. Check your function.')
            print('=' * 56)
            return 0
            
def test_mario(modul):
    print('*'*56)
    print('TESTING OPTIONAL MARIO_PIRAMIS FUNCTION')
    print('*'*56)
    test_cases = [([5], ['    ##', '   ###', '  ####', ' #####', '######']), 
    ([17], ['                ##', '               ###', '              ####', '             #####', '            ######', '           #######', '          ########', '         #########', '        ##########', '       ###########', '      ############', '     #############', '    ##############', '   ###############', '  ################', ' #################', '##################']), 
    ([3], ['  ##', ' ###', '####']), 
    ([2], ['A számnak 3 és 25 kell lennie!']), 
    ([25], ['                        ##', '                       ###', '                      ####', '                     #####', '                    ######', '                   #######', '                  ########', '                 #########', '                ##########', '               ###########', '              ############', '             #############', '            ##############', '           ###############', '          ################', '         #################', '        ##################', '       ###################', '      ####################', '     #####################', '    ######################', '   #######################', '  ########################', ' #########################', '##########################'] ), 
    ([65], ['A számnak 3 és 25 kell lennie!'])]
    mistakes = 0
    for t in test_cases:
        printed = get_print_output(modul.mario_piramis, t[0])
        mistakes += feedback(t[0], t[1], printed, pprint=True)
        
    if mistakes == 0:
        'Great job! Your mario pyramids look awesome. Your function works as intended!'
    else:
        'Keep trying!'
            
if __name__ == '__main__':
    main()
