import sys
import re

input_file = sys.argv[1]


def decipher(string):
    while re.search(r'([a-z])\1', string) != None:
        string = re.sub(r'([a-z])\1', '', string)
    return string


def open_file():
    with open(input_file, 'r') as f:
        content = f.read()
    return decipher(re.sub(r'\s', '', content))


if __name__ == '__main__':
    print(open_file())
