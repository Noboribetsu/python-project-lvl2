from gendiff.functions import to_low


STYLISH = {
    'del': '{0}  - {1}: {2}',
    'new': '{0}  + {1}: {2}',
    'same': '{0}    {1}: {2}',
    'nested': '{0}    {1}: {2}',
    'new_nested': '{0}    {1}: {2}',
    'del_nested': '{0}    {1}: {2}',
    'new_value': '{0}  - {1}: {2}\n{0}  + {1}: {3}'
}


def check_value(value, depth):
    """Normalize nested value for stylish function."""
    return stylish(value, depth) if isinstance(value, dict) else to_low(value)


def make_line(key, value, indent, depth):
    """Check diff value, return formated line for stylish."""
    if value[1] == []:
        return STYLISH[value[0]].format(indent, key, stylish(
            value[2], depth + 4)
        )
    if isinstance(value[1], list):
        old_value = check_value(value[1][0], depth + 4)
        new_value = check_value(value[1][1], depth + 4)
        return STYLISH[value[0]].format(indent, key, old_value, new_value)


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
