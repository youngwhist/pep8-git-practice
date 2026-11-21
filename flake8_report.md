# Отчёт о проверке стиля кода (flake8)

Инструмент: flake8 7.5.0 (pycodestyle 2.15.0, pyflakes 4.1.0).

## До исправлений

Найдено замечаний: **35**.

| Код | Количество | Описание | Исправление |
|---|---|---|---|
| E203 | 1 | whitespace before ':' | убран пробел перед «:» |
| E225 | 9 | missing whitespace around operator | пробелы вокруг операторов |
| E231 | 10 | missing whitespace after ',' | пробел после запятой и двоеточия |
| E302 | 4 | expected 2 blank lines, found 0 | 2 пустые строки перед функциями |
| E305 | 1 | expected 2 blank lines after class or function definition, found 0 | 2 пустые строки после функций |
| E401 | 1 | multiple imports on one line | по одному импорту в строке |
| E701 | 3 | multiple statements on one line (colon) | тело if — на отдельной строке |
| F401 | 2 | 'os' imported but unused | удалены неиспользуемые импорты os, sys |
| F403 | 1 | 'from utils import *' used; unable to detect undefined names | «import *» заменён явным импортом |
| F405 | 3 | 'average' may be undefined, or defined from star imports: utils | имена импортированы явно |

<details><summary>Полный список</summary>

```text
./main.py:1:1 F403 'from utils import *' used; unable to detect undefined names
./main.py:2:1 E302 expected 2 blank lines, found 0
./main.py:3:11 E225 missing whitespace around operator
./main.py:3:15 E231 missing whitespace after ','
./main.py:3:18 E231 missing whitespace after ','
./main.py:3:21 E231 missing whitespace after ','
./main.py:3:24 E231 missing whitespace after ','
./main.py:4:26 E231 missing whitespace after ','
./main.py:4:38 F405 'average' may be undefined, or defined from star imports: utils
./main.py:5:30 E231 missing whitespace after ','
./main.py:5:46 F405 'max_value' may be undefined, or defined from star imports: utils
./main.py:6:30 E231 missing whitespace after ','
./main.py:6:46 F405 'min_value' may be undefined, or defined from star imports: utils
./main.py:7:1 E305 expected 2 blank lines after class or function definition, found 0
./main.py:7:12 E225 missing whitespace around operator
./utils.py:1:1 F401 'os' imported but unused
./utils.py:1:1 F401 'sys' imported but unused
./utils.py:1:10 E401 multiple imports on one line
./utils.py:1:10 E231 missing whitespace after ','
./utils.py:2:1 E302 expected 2 blank lines, found 0
./utils.py:3:20 E225 missing whitespace around operator
./utils.py:3:23 E701 multiple statements on one line (colon)
./utils.py:5:1 E302 expected 2 blank lines, found 0
./utils.py:5:23 E203 whitespace before ':'
./utils.py:6:11 E225 missing whitespace around operator
./utils.py:8:13 E225 missing whitespace around operator
./utils.py:8:20 E701 multiple statements on one line (colon)
./utils.py:8:20 E231 missing whitespace after ':'
./utils.py:8:27 E225 missing whitespace around operator
./utils.py:10:1 E302 expected 2 blank lines, found 0
./utils.py:11:11 E225 missing whitespace around operator
./utils.py:13:13 E225 missing whitespace around operator
./utils.py:13:20 E701 multiple statements on one line (colon)
./utils.py:13:20 E231 missing whitespace after ':'
./utils.py:13:27 E225 missing whitespace around operator
```

</details>

## После исправлений

```text
$ flake8 .
$ echo $?
0
```

Замечаний: **0**.
