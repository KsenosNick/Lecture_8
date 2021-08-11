
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
    file.close()


def dish_add():
    dish_list = input('Введите название блюд (через запятую): ').split(', ')
    return dish_list


def person_count_input():
    count = int(input('Введите количество персон: '))
    return count


def get_shop_list_by_dishes(dishes, persons):
    ingredient_list = {}
    for dish in dishes:
        if dish.capitalize() in list(cook_book.keys()):
            for ingredient in cook_book[dish.capitalize()]:
                if ingredient['ingredient_name'] in list(ingredient_list.keys()):
                    ingredient['quantity'] += ingredient_list[ingredient['ingredient_name']]['quantity'] / persons
                ingredient_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                  'quantity': round(ingredient['quantity']) * persons}

        else:
            print(f'Рецепт {dish.capitalize()} не известен')
            return
    return ingredient_list


dishes_to_cooking = dish_add()

person_count = person_count_input()

shop_list = get_shop_list_by_dishes(dishes_to_cooking, person_count)

print(shop_list)
