from gendiff.functions import to_low


def add_value(value):
    if isinstance(value, (bool, type(None))):
        return to_low(value)
    elif isinstance(value, str):
        return '"{0}"'.format(value)
    return value


def make_line(indent, key, value, depth):
    output = '{0}  "{1}": {2}'
    if value[0] in ['new', 'nested_value']:
        if value[2] == {}:
            return output.format(
                indent, key, add_value(value[1])
            )
        return output.format(
            indent, key, json_output(value[2], depth + 2)
        )
    elif value[0] == 'new_value':
        if isinstance(value[1][1], dict):
            return output.format(
                indent, key, json_output(value[1][1], depth + 2)
            )
        return output.format(indent, key, add_value(value[1][1]))
    elif value[0] == 'nested':
        return output.format(
            indent, key, json_output(value[2], depth + 2)
        )


def json_output(diff, depth=0):
    result = []
    indent = ' ' * depth
    for key, value in sorted(diff.items()):
        if value[0] in ['new', 'new_value', 'nested', 'nested_value']:
            line = make_line(indent, key, value, depth)
            result.append(line)
    return '{{\n{1}\n{0}}}'.format(indent, ',\n'.join(result))
