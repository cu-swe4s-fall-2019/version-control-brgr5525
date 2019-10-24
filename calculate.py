import math_lib as ml
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                description='Input variables to be added and divided',
                prog='get_column_stats')

    parser.add_argument('--a',
                        type=int,
                        help='First number',
                        required=True)

    parser.add_argument('--b',
                        type=int,
                        help='Second number',
                        required=True)

    args = parser.parse_args()

    a = args.a
    b = args.b

    print('calculating: ', a, '+', b)
    print(ml.add(a, b))

    print('calculating: ', a, '/', b)
    print(ml.div(a, b), '\n')
