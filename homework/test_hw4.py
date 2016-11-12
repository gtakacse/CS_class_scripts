import os
import re
import importlib
from io import StringIO
import sys

def main():
    file = find_file()
    #file = 'hw4_solutions.py'
    modul = load_modul(file)
    scores = 0
    scores += test_func1(modul)
    scores += test_func2(modul)
    scores += test_func3(modul)
    get_stats(scores)
    print('Checking longer function.')
    test_func4(modul)
    #print(get_print_output(modul.longer, ['macska', 'kutya']))

def find_file():
    files = os.listdir(os.curdir)
    for file in files:
        if re.search(r'^hw4.*py', file) is not None:
            return file

def load_modul(file):
    try:
        modul = importlib.import_module(file[:-3])
        print('Trying to load the homework file with the structure hw4_name.py\n' + '='*56)
        return modul
    except ImportError:
        print('The {} function cannot be found in {}'.format(file))

def function_exists(function):
    if function in dir():
        print('The function {} could be loaded.'.format(function))
    else:
        print('The function {} is not found.'.format(function))

def test_func1(modul):
    #function_exists('is_equal')
    test_cases = [(['abba', 'baba'], True),
                  (['az', 'azt'], False),
                  (['hosszu', 'rovid'], False)]
    mistakes = 0
    for t in test_cases:
        mistakes += func_test(t[0],t[1], modul.is_equal)
    if mistakes == 0:
        print('Good job. The is_equal function works as intended.')
        print('='*56)

    return len(test_cases)-mistakes

def test_func2(modul):
    #function_exists('fahr2celsius')
    test_cases = [([212],100),
                  ([32], 0),
                  ([100], 68*5/9)]
    mistakes = 0
    for t in test_cases:
        mistakes += func_test(t[0], t[1], modul.fahr2celsius)
    if mistakes == 0:
        print('Good job. The fahr2celsius function works as intended.')
        print('=' * 56)

    return len(test_cases) - mistakes


def test_func3(modul):
    #function_exists('last_n_char')
    test_cases = [(['hello Budapest',4], 'pest'),
                  (['',4], ''),
                  (['This house is not for sale.', 9], 'for sale.')]
    mistakes = 0
    for t in test_cases:
        mistakes += func_test(t[0], t[1], modul.last_n_char)
    if mistakes == 0:
        print('Good job. The last_n_char function works as intended.')
        print('=' * 56)
    return len(test_cases)-mistakes

def test_func4(modul):
    try:
        test_cases = [(['macska', 'kutya'], 'A(z) "macska" szó hosszabb, mint a(z) "kutya" szó.'),
                      (['bicska', 'kecske'], 'A megadott szavak egyenlő hosszúak.'),
                      (['python', 'anaconda'], 'A(z) "anaconda" szó hosszabb, mint a(z) "python" szó.')]
        mistakes = 0
        for t in test_cases:
            output = get_print_output(modul.longer, t[0])
            mistakes += feedback(t[0], t[1], output[0])

        if mistakes == 0:
            print('Superb! You are a real hacker! You have really mastered this matterial. Great job!')
        else:
            print('Almost there. Keep trying!')
    except AttributeError:
        print('Function of the optional exercise is not found.')



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
    return out.getvalue().strip().split('\n')

def hello():
    print('hello')

def feedback(input, output, got):
    print('Input: {}'.format(input))
    print('Expected: {}'.format(output))
    print('Got: {}'.format(got))

    if got == output:
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

def get_stats(scores):
    total = 9
    print('Summary:\n{} out of {}: {}%'.format(scores, 9, round(scores/total*100),2))
    print('='*56)
    print('*'*56)
    print('='*56)

if __name__ == '__main__':
    main()