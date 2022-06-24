import json
import yaml
from yaml.loader import SafeLoader
from gendiff.data import STYLISH, BOOL


def to_low(value):
    return BOOL.get(value, value)


def parse_file(file_path):
    if file_path.endswith(('.yaml', '.yml')):
        with open(file_path) as f:
            return yaml.load(f, Loader=SafeLoader)
    elif file_path.endswith('.json'):
        with open(file_path) as f:
            return json.load(f)


def check_nested(key, type, arg1, arg2):
    if isinstance(arg1[key], dict):
        return ['same' if arg2 == {} else type, [], make_diff(arg1[key], {})]
    return ['same' if arg2 == {} else type, arg1[key], {}]


def check_value(value, arg, function):
    return function(value, arg) if isinstance(value, dict) else value


def make_diff(dict_1, dict_2):
    diff = {}
    keys_diff = dict_2.keys() - dict_1.keys()
    keys = list(dict_1.keys()) + list(keys_diff)
    for key in keys:
        if key in dict_1 and key not in dict_2:
            diff[key] = check_nested(key, 'del_nested', dict_1, dict_2)
        elif key in dict_2 and key not in dict_1:
            diff[key] = check_nested(key, 'new_nested', dict_2, dict_1)
        elif isinstance(dict_1[key], dict) and isinstance(dict_2[key], dict):
            diff[key] = ['nested', [], make_diff(dict_1[key], dict_2[key])]
        elif dict_1[key] == dict_2[key]:
            diff[key] = ['same', dict_1[key], {}]
        else:
            diff[key] = [
                'new_value',
                [check_value(dict_1[key], {}, make_diff),
                    check_value(dict_2[key], {}, make_diff)],
                {}
            ]
    return diff


def stylish(diff, depth=0):
    result = []
    indent = ' ' * depth
    for key, value in sorted(diff.items()):
        if value[1] == []:
            line = STYLISH[value[0]].format(indent, key, stylish(
                value[2], depth + 4)
            )
            result.append(line)
        elif isinstance(value[1], list):
            old_value = to_low(
                check_value(value[1][0], depth + 4, stylish)
            )
            new_value = to_low(
                check_value(value[1][1], depth + 4, stylish)
            )
            line = STYLISH[value[0]].format(indent, key, old_value, new_value)
            result.append(line)
        else:
            line = STYLISH[value[0]].format(indent, key, to_low(value[1]))
            result.append(line)
    return '{{\n{1}\n{0}}}'.format(indent, '\n'.join(result))
