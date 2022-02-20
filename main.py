from pprint import pprint

def cool_cook_book(input_file_name):

    # 1. Читаем файл.
    # 2. Проходим циклом по спискам со значениями равными строкам до двух пустых строк.
    # 3. В каждом списке присваиваем переменной name - значение первого элемента : Название блюда,
    #      переменной number - значение второго элемента: Количество ингридиентов
    #      переменной args - список с элементами соответствующими ингридиентам блюд.
    # 4. Создаем пустой список, в который будем добавлять словари с данными по ингридиентам
    # 5. Циклом из каждого элемента args создаем список элементов разделенных '|' ;
    #    объединяем c словарём, заданных в задаче ключей, в словарь методом zip().
    # 6. Добавляем полученные словари в список temp
    # 7. Записываем в словрь cook_book списаки словарей для каждого name.

    with open(input_file_name, encoding='utf-8') as file:
        cook_book = {}
        for txt in file.read().split('\n\n'):
            name, number, *args = txt.split('\n')
            tmp = []
            for arg in args:
                tmp.append(dict(zip(['ingredient_name', 'quantity', 'measure'], arg.split('|'))))
            cook_book[name] = tmp
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    # 1. Создаем словрь функцией из задания №1.
    # 2. Создаем пустой словарь для добавления ингидиентов и количества.
    # 3. Циклом ищем блюдо из заданного параметра функции в созданом словаре, если такое блюдо уже есть в словаре,
    #    то добавляет к значению количества, еще каличество необходимого ингридиента, расчитаного на заданное
    #    количество персон и перезаписывает значение количества ингридиентов;
    #    если не находит, то добавляем ингридиенты и количество заданного в параметрах функции блюда, расчиатанное
    #    на заданное количество персон.
    # 4. функция возвращает словарь с добаленными ингридентами и количестовм.


    cook_book = cool_cook_book('recipes.txt')
    cook_dict = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingredient in cook_book[dish]:
                dict_ing = {}
                if ingredient['ingredient_name'] in cook_dict:
                    quantity = cook_dict[ingredient['ingredient_name']].get('quantity') + \
                               int(ingredient['quantity']) * person_count
                    cook_dict[ingredient['ingredient_name']].update(quantity=quantity)
                else:
                    dict_ing['measure'] = ingredient['measure']
                    dict_ing['quantity'] = int(ingredient['quantity']) * person_count
                    cook_dict[ingredient['ingredient_name']] = dict_ing
    return cook_dict


pprint(cool_cook_book('recipes.txt'))
print('\n')
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 3))
