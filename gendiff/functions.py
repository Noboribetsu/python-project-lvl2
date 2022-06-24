"""Internal fuctions for gendiff/generate_diff."""
import json
import yaml
from yaml.loader import SafeLoader
from gendiff.data import STYLISH, BOOL


def to_low(value):
    """
    Fuctions to_low bring a value to a correct while printing difference.
    Example: True(Python style) -> true(JSON, yaml style).
    """
    return BOOL.get(value, value)


def parse_file(file_path):
    """Check file format, open and revert data(dictionaries)."""
    if file_path.endswith(('.yaml', '.yml')):
        with open(file_path) as f:
            return yaml.load(f, Loader=SafeLoader)
    elif file_path.endswith('.json'):
        with open(file_path) as f:
            return json.load(f)


def check_nested(key, type, arg1, arg2):
    """Check if a value is nested, make it plain"""
    if isinstance(arg1[key], dict):
        return ['same' if arg2 == {} else type, [], make_diff(arg1[key], {})]
    return ['same' if arg2 == {} else type, arg1[key], {}]


def check_value(value, arg, function):
    """Normalize nested value for stylish function."""
    return function(value, arg) if isinstance(value, dict) else to_low(value)


def in_both(key, dict_1, dict_2):
    """Check dictionary value, return formated value for difference."""
    if isinstance(dict_1[key], dict) and isinstance(dict_2[key], dict):
        return ['nested', [], make_diff(dict_1[key], dict_2[key])]
    if dict_1[key] == dict_2[key]:
        return ['same', dict_1[key], {}]
    return ['new_value', [
            check_value(dict_1[key], {}, make_diff),
            check_value(dict_2[key], {}, make_diff)
            ],
            {}]


def make_line(key, value, indent, depth):
    """Check diff value, return formated line for stylish."""
    if value[1] == []:
        return STYLISH[value[0]].format(indent, key, stylish(
            value[2], depth + 4)
        )
    if isinstance(value[1], list):
        old_value = check_value(value[1][0], depth + 4, stylish)
        new_value = check_value(value[1][1], depth + 4, stylish)
        return STYLISH[value[0]].format(indent, key, old_value, new_value)


def make_diff(dict_1, dict_2):
    """
    Make difference between two dictionaries readed from files.
    Return diff which can be printed in different styles.
    """
    diff = {}
    keys_diff = dict_2.keys() - dict_1.keys()
    keys = list(dict_1.keys()) + list(keys_diff)
    for key in keys:
        if key in dict_1 and key not in dict_2:
            diff[key] = check_nested(key, 'del_nested', dict_1, dict_2)
        elif key in dict_2 and key not in dict_1:
            diff[key] = check_nested(key, 'new_nested', dict_2, dict_1)
        else:
            diff[key] = in_both(key, dict_1, dict_2)
    return diff


def stylish(diff, depth=0):
    """
    Print diff in tree style.
    Default formater for gendiff.
    """
    result = []
    indent = ' ' * depth
    for key, value in sorted(diff.items()):
        if not isinstance(value[1], list):
            line = STYLISH[value[0]].format(indent, key, to_low(value[1]))
            result.append(line)
        else:
            result.append(make_line(key, value, indent, depth))
    return '{{\n{1}\n{0}}}'.format(indent, '\n'.join(result))
