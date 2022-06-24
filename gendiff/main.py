"""Main file with function"""
import argparse
from gendiff.functions import make_diff, parse_file, stylish


def generate_diff(first_path, second_path):
    """
    The fucntion compares two configuration files and shows a difference.
    """
    dict_1 = parse_file(first_path)
    dict_2 = parse_file(second_path)
    return make_diff(dict_1, dict_2)


def gendiff():
    """
    CLI program compares two configuration files and shows a difference.
    """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', help='set format of output',
        metavar='FORMAT', default=stylish
    )
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(args.format(diff))
