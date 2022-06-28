"""Internal fuctions for gendiff/generate_diff."""
import json
import yaml
from yaml.loader import SafeLoader

BOOL = {
    True: 'true',
    False: 'false',
    None: 'null'
}


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
        return [
            'nested_value' if arg2 == {} else type,
            [], make_diff(arg1[key], {})
        ]
    return ['nested_value' if arg2 == {} else type, arg1[key], {}]


def isnested(value):
    """Check if a new added value is nested or not"""
    return make_diff(value, {}) if isinstance(value, dict) else value


def in_both(key, dict_1, dict_2):
    """Check dictionary value, return formated value for difference."""
    if isinstance(dict_1[key], dict) and isinstance(dict_2[key], dict):
        return ['nested', [], make_diff(dict_1[key], dict_2[key])]
    if dict_1[key] == dict_2[key]:
        return ['same', dict_1[key], {}]
    return ['new_value', [isnested(dict_1[key]), isnested(dict_2[key])], {}]


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
            diff[key] = check_nested(key, 'del', dict_1, dict_2)
        elif key in dict_2 and key not in dict_1:
            diff[key] = check_nested(key, 'new', dict_2, dict_1)
        else:
            diff[key] = in_both(key, dict_1, dict_2)
    return diff
