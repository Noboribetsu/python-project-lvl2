## Description:
Вычислитель отличий – программа, определяющая разницу между двумя структурами данных. Это популярная задача, для решения которой существует множество онлайн-сервисов http://www.jsondiff.com/. Подобный механизм, например, используется при выводе тестов или при автоматическом отслеживании изменении в конфигурационных файлах.

Возможности утилиты:
Поддержка разных входных форматов: yaml, json
Генерация отчета в виде plain text, stylish и json

Требование:
Без использования классов.

### Usage:
```bash
gendiff -h
usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output: stylish, plain, json (default: stylish)
```
### Install:
```bash
make install
make build
make package-install
```

### Check codestyle
```bash
make lint
```

### Run tests
```bash
make test
make test-coverage
```

### Hexlet tests and linter status:
[![Actions Status](https://github.com/Noboribetsu/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/Noboribetsu/python-project-lvl2/actions)

[![build&test](https://github.com/Noboribetsu/python-project-lvl2/actions/workflows/build&test.yml/badge.svg)](https://github.com/Noboribetsu/python-project-lvl2/actions/workflows/build&test.yml)

[![Maintainability](https://api.codeclimate.com/v1/badges/ca31f8d69abfb4353a82/maintainability)](https://codeclimate.com/github/Noboribetsu/python-project-lvl2/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/ca31f8d69abfb4353a82/test_coverage)](https://codeclimate.com/github/Noboribetsu/python-project-lvl2/test_coverage)

## Step 3 progress:
[![asciicast](https://asciinema.org/a/5ZkEvfFfOU9nlfDgjU8QoczYl.svg)](https://asciinema.org/a/5ZkEvfFfOU9nlfDgjU8QoczYl)

## Step 5 progress(add yaml format support):
[![asciicast](https://asciinema.org/a/ewyriF8csLUTxrn0uN1KQPoKy.svg)](https://asciinema.org/a/ewyriF8csLUTxrn0uN1KQPoKy)

## Step 6 progress(add nested data support, add formater stylish(tree view))
[![asciicast](https://asciinema.org/a/rPGuDnWdsaQZaXo52QR3Ebkj2.svg)](https://asciinema.org/a/rPGuDnWdsaQZaXo52QR3Ebkj2)

## Step 7 progress(add plain formater)
[![asciicast](https://asciinema.org/a/J303sMzaALtfSkUVY8QaciEtq.svg)](https://asciinema.org/a/J303sMzaALtfSkUVY8QaciEtq)

## Step 8 progress(add json formater)
[![asciicast](https://asciinema.org/a/wPEc20zmiJ1zrY1Ae67GtXNSZ.svg)](https://asciinema.org/a/wPEc20zmiJ1zrY1Ae67GtXNSZ)
