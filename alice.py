import sys
import time
import re
from itertools import groupby

input_file = sys.argv[1]


def decipher(string):
    while re.search(r'(.)\1', string) != None:
        string = ''.join(letter for letter, group in groupby(
            string) if len(tuple(group)) != 2)
    return string


def open_file():
    with open(input_file, 'r') as f:
        content = f.read()
    return decipher(content)


if __name__ == '__main__':
    print(open_file())
