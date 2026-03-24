def find_common_participants(first, second, razdelitel=","):  # вводим функцию со значением разделителя по умолчанию
    list1 = first.split(razdelitel)  # Преобразуем строки в списки
    list2 = second.split(razdelitel)  # Преобразуем строки в списки
    spisok = []   # Создаём пустой список
    for last_name in list1:   # цикл перебора первого списка
        if last_name in list2:   # условия нахождения участника в двух списках сразу
            spisok.append(last_name)   # добавляем участника в наш список
            list2.remove(last_name)   # удаляем его фамилию из второго списка, чтобы избежать дубликатов, если есть однофамильцы
    spisok.sort()  # сортируем список в алфавитном порядке
    return spisok  # возвращаем список

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group,"|"))