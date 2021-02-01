import sys
import time

input_file = sys.argv[1]


def decipher():
    letters = {}
    with open(input_file, 'r') as f:
        string = f.read()

    for i in string:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1

    return ''.join([x for x, y in letters.items() if y % 2 != 0])


if __name__ == '__main__':
    print(decipher())
