all_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"] # исходный список


ceredina = len(all_players) // 2 #получаем индекс середины

pervyu_team = all_players[:ceredina] #срез исходного списка до середины = первой команде
vtorouy_team = all_players[ceredina:] #срез после середины = второй команде


print(pervyu_team) # выводим первую команду
print(vtorouy_team) # выводим вторую команду
