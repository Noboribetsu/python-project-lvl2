"""Main file with function"""

import argparse
import json


def to_json(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(first_path, second_path):
    """
    The fucntion compares two configuration files and shows a difference.
    """
    diff = []
    first_file = json.load(open(first_path))
    second_file = json.load(open(second_path))
    keys_diff = second_file.keys() - first_file.keys()
    keys = list(first_file.keys())
    keys.extend(keys_diff)
    keys = sorted(keys)
    for key in keys:
        if key in first_file and key in second_file:
            if first_file[key] == second_file[key]:
                diff.append('    {0}: {1}'.format(
                    key, to_json(first_file[key])
                )
                )
            else:
                diff.append('  - {0}: {1}'.format(
                    key, to_json(first_file[key])
                ))
                diff.append('  + {0}: {1}'.format(
                    key, to_json(second_file[key])
                ))
            continue
        elif key in first_file:
            diff.append('  - {0}: {1}'.format(key, to_json(first_file[key])))
        elif key in second_file:
            diff.append('  + {0}: {1}'.format(key, to_json(second_file[key])))
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
