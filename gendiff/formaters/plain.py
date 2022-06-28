from gendiff.functions import to_low


PLAIN = {
    'del': "Property '{0}' was removed",
    'new': "Property '{0}' was added with value: {1}",
    'new_value': "Property '{0}' was updated. From {1} to {2}"
}


def plain_value(value):
    if value == [] or isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, (bool, type(None))):
        return to_low(value)
    return '{0}'.format(value) \
        if isinstance(value, int) else "'{0}'".format(value)


def plain(diff, path=[]):
    result = []
    for key, value in sorted(diff.items()):
        path.append(key)
        if value[0] in ['new', 'del', 'new_value', 'new_nested']:
            if value[0] == 'new':
                line = PLAIN[value[0]].format(
                    '.'.join(path), plain_value(value[1])
                )
                result.append(line)
            elif value[0] == 'del':
                line = PLAIN[value[0]].format('.'.join(path))
                result.append(line)
            else:
                line = PLAIN[value[0]].format(
                    '.'.join(path),
                    plain_value(value[1][0]),
                    plain_value(value[1][1])
                )
                result.append(line)
        elif value[0] == 'nested':
            line = plain(value[2], path)
            result.append(line)
        path.remove(key)
    return '\n'.join(result)
