import csv  # импортируем библиотеки
import json

INPUT_FILENAME = "input.csv"  # глобальные переменные
OUTPUT_FILENAME = "output.json"


def task(input_filename, output_filename) -> None:  # создаём функцию, которая принимает названия файлов
    with open(input_filename, encoding="utf-8") as in_file:  # открываем исходный файл
        read = csv.DictReader(in_file)  # считываем файл в формате словарей
        data = [row for row in read]  # записываем данные как список словарей
    with open(output_filename, "w", encoding="utf-8") as out_file:  # открываем выходной файл для записи
        json.dump(data, out_file, indent=4, ensure_ascii=False)  # записываем список словарей


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
