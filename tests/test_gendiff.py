from gendiff import generate_diff

first_file = 'tests/fixtures/file1.json'
second_file = 'tests/fixtures/file2.json'
result_path = 'tests/fixtures/result'

def test_print():
    result = open(result_path)
    assert generate_diff(first_file, second_file) == result.read()