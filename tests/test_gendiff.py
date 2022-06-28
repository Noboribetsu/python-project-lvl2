import subprocess

RESULT = {
    'stylish': 'tests/fixtures/result_stylish',
    'plain': 'tests/fixtures/result_plain',
    'json': 'tests/fixtures/result_json'
}

json_file = ['tests/fixtures/file1.json', 'tests/fixtures/file2.json']
yaml_file = ['tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml']


def result(key):
    with open(RESULT[key]) as f:
        return f.read()


def test_gendiff_json_stylish():
    script_run = subprocess.run(
        ['gendiff', json_file[0], json_file[1]],
        stdout=subprocess.PIPE, encoding='utf-8')
    assert script_run.stdout[:-1] == result('stylish')


def test_gendiff_yaml_stylish():
    script_run = subprocess.run(
        ['gendiff', yaml_file[0], yaml_file[1]],
        stdout=subprocess.PIPE, encoding='utf-8')
    assert script_run.stdout[:-1] == result('stylish')


def test_gendiff_json_plain():
    script_run = subprocess.run(
        ['gendiff', '-f', 'plain', json_file[0],
            json_file[1]], stdout=subprocess.PIPE, encoding='utf-8')
    assert script_run.stdout[:-1] == result('plain')


def test_gendiff_yaml_plain():
    script_run = subprocess.run(
        ['gendiff', '-f', 'plain', yaml_file[0], yaml_file[1]],
        stdout=subprocess.PIPE, encoding='utf-8')
    assert script_run.stdout[:-1] == result('plain')


def test_gendiff_json_to_json():
    script_run = subprocess.run(
        ['gendiff', '-f', 'json', json_file[0], json_file[1]],
        stdout=subprocess.PIPE, encoding='utf-8')
    assert script_run.stdout[:-1] == result('json')


def test_gendiff_yaml_to_json():
    script_run = subprocess.run(
        ['gendiff', '-f', 'json', yaml_file[0], yaml_file[1]],
        stdout=subprocess.PIPE, encoding='utf-8')
    assert script_run.stdout[:-1] == result('json')
