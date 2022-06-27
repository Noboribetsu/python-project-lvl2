"""
Main file with CLI function and libary fucntion
to compare two configuration files.
"""
import argparse
from gendiff.formaters.plain import plain
from gendiff.formaters.stylish import stylish
from gendiff.functions import make_diff, parse_file


def generate_diff(first_path, second_path, format_name='stylish'):
    """
    The fucntion compares two configuration files and shows a difference.
    Libary function.
    """
    dict_1 = parse_file(first_path)
    dict_2 = parse_file(second_path)
    diff = make_diff(dict_1, dict_2)
    if format_name == 'stylish':
        return stylish(diff)
    elif format_name == 'plain':
        return plain(diff)


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
        metavar='FORMAT', default='stylish', choices=['stylish', 'plain']
    )
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)
