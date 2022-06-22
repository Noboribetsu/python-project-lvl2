"""Main file with function"""
import argparse
from gendiff.functions import compare, parse_file


def generate_diff(first_path, second_path):
    """
    The fucntion compares two configuration files and shows a difference.
    """
    diff = []
    dict_1 = parse_file(first_path)
    dict_2 = parse_file(second_path)
    keys_diff = dict_2.keys() - dict_1.keys()
    keys = list(dict_1.keys()) + list(keys_diff)
    diff = list(map(lambda x: compare(x, dict_1, dict_2), sorted(keys)))
    return '{{\n{0}\n}}'.format('\n'.join(diff))


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
        '-f', '--format', help='set format of output', metavar='FORMAT'
    )
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
