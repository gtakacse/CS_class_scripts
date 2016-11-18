import re
import os
import importlib
import sys
from io import StringIO
from unittest.mock import patch
from unittest import TestCase


def main():
    file = find_file()
    #file = 'hw5_solutions.py'
    modul = load_modul(file)
    scores = 0
    scores += test_one(modul)
    scores += test_two(modul)
    scores += test_three(modul)
    get_stats(scores)

def find_file():
    files = os.listdir(os.curdir)
    for file in files:
        if re.search(r'^hw5.*py', file) is not None:
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
    return out.getvalue().strip().split('\n')[0]


def feedback(input, expected_output, got):
    print('Input: {}'.format(input))
    print('Expected: {}'.format(expected_output))
    print('Got: {}'.format(got))

    if got == expected_output:
        print('Test passed.')
        print('=' * 56)
        return 0
    else:
        print('Test failed. Check your function.')
        print('=' * 56)
        return 1

def feedback_plus(user_input, expected_return, received_returned, expected_print, printed):
    print("User's input: {}".format(user_input))
    print('Expected return value: {}'.format(expected_return))
    print('Received return value: {}'.format(received_returned))
    print('Expected to print: {}'.format(expected_print))
    print('The function printed: {}'.format(printed))

    if expected_return == received_returned and expected_print == printed:
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
    total = 20
    print('Summary:\n{} out of {}: {}%'.format(scores, 9, round(scores/total*100),2))
    print('='*56)
    print('*'*56)
    print('='*56)


def test_one(modul):
    # 10, 34.5, 0, -99
    test_cases = [([10], True),
                  ([34.5], True),
                  ([0], False),
                  ([-99], False)]
    mistakes = 0
    for t in test_cases:
        mistakes += func_test(t[0], t[1], modul.is_positive)
    if mistakes == 0:
        print('Good job. The is_positive function works as intended.')
        print('=' * 56)
    return len(test_cases)-mistakes

def pwd_answer(modul):
    ans = modul.ask_pseudo_password()
    return ans


class MyTestCase(TestCase):
    def __init__(self, modul):
        self.modul = modul

    def runTest(self, given_answer):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
            return_val = pwd_answer(self.modul)
            print_out = fake_out.getvalue().strip()
            # self.assertEqual(fake_out.getvalue().strip(), expected_out)
            return (return_val, print_out)

def test_two(modul):
    # test cases: '232ldjfl', '', 'dsfal', 'password', 'FS34DFasf'
    # structure (input, returned, printed)
    test_cases = [('232ldjfl', '232ldjfl', ''),
                  ('', None, 'A jelszó nem megfelelő.'),
                  ('dsf', None, 'A jelszó nem megfelelő.'),
                  ('password', None, 'A jelszó nem megfelelő.'),
                  ('FS34DFasf', 'FS34DFasf', '')]
    mistakes = 0
    tester = MyTestCase(modul)

    for t in test_cases:
        returned, printed = tester.runTest(t[0])

        # get print output
        #printed = ''
        #printed = get_print_output(get_input_func_output(modul.ask_pseudo_password, t[0]))
        if returned != t[1]:
            mistakes += 1
        if printed != t[2]:
            mistakes += 1
        feedback_plus(t[0], t[1], returned, t[2], printed)

    if mistakes == 0:
        print('Good job. The ask_pseudo_password function works as intended.')
        print('=' * 56)
    return len(test_cases) * 2 - mistakes

def test_three(modul):
    # test cases: 2016, 2000, 1997, 1900, 2800, 2525
    test_cases = [([2016], '2016 szökőév volt.'),
                  ([2000], '2000 szökőév volt.'),
                  ([1997], '1997 nem volt szökőév.'),
                  ([1900], '1900 nem volt szökőév.'),
                  ([2800], '2800 szökőév lesz.'),
                  ([2525], '2525 nem lesz szökőév.')]
    mistakes = 0
    for t in test_cases:
        output = get_print_output(modul.is_leap_year, t[0])
        mistakes += feedback(t[0], t[1], output)
    if mistakes == 0:
        print('Congrats! You mastered the if-else control structure. Great job!')
    return len(test_cases)-mistakes

if __name__ == '__main__':
    main()