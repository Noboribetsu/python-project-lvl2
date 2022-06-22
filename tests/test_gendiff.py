from gendiff import generate_diff
import subprocess

json_file = ['tests/fixtures/file1.json', 'tests/fixtures/file2.json']
yaml_file = ['tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml']


def result():
    result_path = 'tests/fixtures/result'
    with open(result_path) as f:
        return f.read()


def test_generate_diff_with_json():
    assert generate_diff(json_file[0], json_file[1]) == result()


def test_gendiff_with_json():
    script_run = subprocess.run(['gendiff', json_file[0], json_file[1]], \
                                stdout=subprocess.PIPE, encoding='utf-8')
    assert script_run.stdout[:-1] == result()


def test_gendiff_with_yaml():
    script_run = subprocess.run(['gendiff', yaml_file[0], yaml_file[1]], \
                                stdout=subprocess.PIPE, encoding='utf-8')
    assert script_run.stdout[:-1] == result()