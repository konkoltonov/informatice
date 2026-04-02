import json  # импортируем библиотеку

FILENAME = "input.json"  # указываем имя нашего файла


def task(file_name: str) -> float:
    total = 0  # вводим переменную для суммы

    with open(file_name, encoding="utf-8") as file:  # открываем файл в указанной кодировке
        inf = json.load(file)  # загружаем информацию из файла

    for i in inf:  # перебираем каждый словарь из списка
        score = i.get("score", 0)  # получаем значение ключа score
        weight = i.get("weight", 0)  # получаем значение ключа weight
        total += score * weight  # прибавляем к сумме произведение двух значений

    return round(total, 3)  # возвращаем результат, округлённый до трёх


if __name__ == '__main__':
    print(task(FILENAME))
