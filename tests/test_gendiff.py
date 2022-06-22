from gendiff import generate_diff
import subprocess

first_file = 'tests/fixtures/file1.json'
second_file = 'tests/fixtures/file2.json'
result_path = 'tests/fixtures/result'


def test_generate_diff():
    result = open(result_path)
    assert generate_diff(first_file, second_file) == result.read()


def test_gendiff():
    result = open(result_path)
    script_run = subprocess.run(['gendiff', first_file, second_file], \
                                stdout=subprocess.PIPE, encoding='utf-8')
    assert script_run.stdout[:-1] == result.read()
