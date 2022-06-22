import json
import yaml
from yaml.loader import SafeLoader


def to_low(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def parse_file(file_path):
    if file_path.endswith(('.yaml', '.yml')):
        with open(file_path) as f:
            return yaml.load(f, Loader=SafeLoader)
    elif file_path.endswith('.json'):
        with open(file_path) as f:
            return json.load(f)


def compare(key, first_file, second_file):
    if key in first_file:
        if key in second_file:
            if first_file[key] == second_file[key]:
                return '    {0}: {1}'.format(key, to_low(first_file[key]))
            else:
                return '  - {0}: {1}\n  + {0}: {2}'.format(
                    key, to_low(first_file[key]), to_low(second_file[key])
                )
        else:
            return '  - {0}: {1}'.format(key, to_low(first_file[key]))
    else:
        return ('  + {0}: {1}'.format(key, to_low(second_file[key])))
