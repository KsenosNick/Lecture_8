from pprint import pprint

with open("recipes.txt", encoding="utf-8") as file:
    cook_book = {}
    for line in file:
        ingredients = []
        dish_name = line.strip()
        ingredients_amount = int(file.readline().strip())
        for i in range(ingredients_amount):
            name, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append({'ingredient_name': name, 'quantity': int(quantity), 'measure': measure})
            cook_book[dish_name] = ingredients
        file.readline()


def dish_add():
    dish_list = input('Введите название блюд (через запятую): ').split(', ')
    return dish_list


def person_count_input():
    count = int(input('Введите количество персон: '))
    return count


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish.capitalize() in list(cook_book.keys()):
            for ingredient in cook_book[dish.capitalize()]:
                if ingredient['ingredient_name'] in list(shop_list.keys()):
                    ingredient['quantity'] += shop_list[ingredient['ingredient_name']]['quantity'] / person_count
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                            'quantity': round(ingredient['quantity']) * person_count}
        else:
            print('Рецепт не известен')
    pprint(shop_list)


dishes = dish_add()

person_count = person_count_input()

get_shop_list_by_dishes(dishes, person_count)
