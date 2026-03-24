def poisk(items_list,tovar):  # функция поиска предложенного товара в предложенном списке
    if tovar in items_list:  # проверка наличия товара в списке
        return items_list.index(tovar)  # возвращение значения первого индекса с помощью метода .index
    return None  # возвращение None, если товара нет в списке

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']  # исходный список продуктов

for find_item in ['банан', 'груша', 'персик']:
    index_item = poisk(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
