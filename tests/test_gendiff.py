import subprocess

json_file = ['tests/fixtures/file1.json', 'tests/fixtures/file2.json']
yaml_file = ['tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml']


def result_stylish():
    result_path = 'tests/fixtures/result_stylish'
    with open(result_path) as f:
        return f.read()

def result_plain():
    result_path = 'tests/fixtures/result_plain'
    with open(result_path) as f:
        return f.read()

def test_gendiff_json_stylish():
    script_run = subprocess.run(['gendiff', json_file[0], json_file[1]], \
                                stdout=subprocess.PIPE, encoding='utf-8')
    assert script_run.stdout[:-1] == result_stylish()


def test_gendiff_yaml_stylish():
    script_run = subprocess.run(['gendiff', yaml_file[0], yaml_file[1]], \
                                stdout=subprocess.PIPE, encoding='utf-8')
    assert script_run.stdout[:-1] == result_stylish()

def test_gendiff_json_plain():
    script_run = subprocess.run(['gendiff','-f', 'plain', json_file[0], json_file[1]], \
                                stdout=subprocess.PIPE, encoding='utf-8')
    assert script_run.stdout[:-1] == result_plain()

def test_gendiff_yaml_plain():
    script_run = subprocess.run(['gendiff','-f', 'plain', yaml_file[0], yaml_file[1]], \
                                stdout=subprocess.PIPE, encoding='utf-8')
    assert script_run.stdout[:-1] == result_plain()    