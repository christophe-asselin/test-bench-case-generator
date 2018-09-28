from random import randint
import sys


def generate_line(n_bits):
    a = randint(0, (2 ** n_bits) - 1)
    b = randint(0, (2 ** n_bits) - 1)

    a_binary = bin(a)[2:].zfill(n_bits)  # removes 0b prefix and fills with zeroes
    b_binary = bin(b)[2:].zfill(n_bits)
    f_binary = bin(a * b)[2:].zfill(2 * n_bits)

    return '{} {} {}\n'.format(a_binary, b_binary, f_binary)


def write_to_file(filename, data):
    with open(filename, 'w') as fout:
        for line in data:
            fout.write(line)


def main():
    try:
        n_bits = int(sys.argv[1])  # number of bits for multiplication
        n_tests = int(sys.argv[2])  # number of tests to generate
    except IndexError:
        print('Please enter the number of bits for the multiplication as the first argument and the number of test '
              'cases to generate as the second argument.')
    else:
        data = []

        for i in range(n_tests):
            data.append(generate_line(n_bits))

        write_to_file('input.txt', data)


if __name__ == '__main__':
    main()
