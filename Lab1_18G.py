from textwrap import dedent
import re


def task1():
    """1. На обработку поступает натуральное число. Нужно написать
        программу, которая выводит на экран сумму чётных цифр этого числа
        или 0, если чётных цифр в записи нет. – 2 балла"""
    num = input("Введите натуральное число: ")
    
    if not num.isdigit():
        print("Ошибка: Введите только натуральное число!")
        return
    
    even_sum = sum(int(digit) for digit in num if int(digit) % 2 == 0)
    print(even_sum if even_sum > 0 else 0)


def task2():
    """2.С клавиатуры вводится текст, определить, сколько в нём гласных,
        а сколько согласных. В случае равенства вывести на экран все гласные
        буквы. Посчитать количество слов в тексте. – 1 балл"""
    text = input("Введите текст: ").lower()
    
    if not text.isalpha() and ' ' not in text:
        print("Ошибка: Введите корректный текст!")
        return
    
    vowels = "аеёиоуыэюяaeiouy"
    consonants = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"
    
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char in consonants)
    words = re.findall(r'\b\w+\b', text)
    word_count = len(words)
    
    print(f"Гласных: {vowel_count}, Согласных: {consonant_count}, Слов: {word_count}")
    
    if vowel_count == consonant_count:
        print("Гласные в тексте:", ", ".join([char for char in text if char in vowels]))


def task3():
    """3.Дан список list=[12,511,'Python',311,122,'love’].
        Все числа этого списка проверить на чётность. Если число чётное, то
        посчитать сумму его цифр. Если нечётное, то заменить его на 1 в
        списке. – 1 балл"""
    lst = [ 12, 511, 'Python', 311, 122, 'love']
    for i in range(len(lst)):
        if isinstance(lst[i], int):
            if lst[i] % 2 == 0:
                print(f"Сумма цифр четного числа {lst[i]}: {sum(int(digit) for digit in str(lst[i]))}")
            else:
                lst[i] = 1
    
    print("Обновленный список:", lst)


def task4():
    """4.Найдите три ключа с самыми маленькими значениями в
        словаре my_dict = {'a':12, 'b':13, 'c': 56,'d':400, 'e':58, 'f': 20}– 2 балла"""
    my_dict = {'a': 12, 'b': 13, 'c': 56, 'd': 400, 'e': 58, 'f': 20}
    smallest_keys = sorted(my_dict, key=my_dict.get)[:3]
    print("Три ключа с самыми маленькими значениями:", smallest_keys)


def task5():
    """5.Реализуйте программу «Магазин игрушек», которая будет
        включать в себя шесть пунктов меню. У вас есть словарь, где ключ –
        название игрушки. Значение – список, который содержит состав
        игрушки, цену и кол-во (шт),которое есть в магазине.
        1.Просмотр описания: название – описание
        2.Просмотр цены: название – цена.
        3.Просмотр количества: название – количество.
        4.Всю информацию.
        5.Покупка
        В пункте «Покупка» необходимо совершить покупку,
        с
        клавиатуры вводите название игрушки и его кол-во, n – выход из
        программы. Посчитать цену выбранных товаров и сколько товаров
        осталось в изначальном списке.
        6.До свидания – 2 балла"""
    toys = {
        'Кукла': ['Пластик, текстиль', 500, 10],
        'Машинка': ['Металл, пластик', 300, 5],
        'Мяч': ['Резина', 100, 15]
    }
    
    while True:
        print(dedent("""\
              ----------------------------------------------
              1. Просмотр описания
              2. Просмотр цены
              3. Просмотр количества
              4. Вся информация
              5. Покупка
              6. До свидания
              ----------------------------------------------"""))
        choice = input("Выберите пункт меню: ")
        
        if choice not in {'1', '2', '3', '4', '5', '6'}:
            print("Ошибка: Некорректный выбор пункта меню!")
            continue
        
        match choice:
            case '1':
                toy = input("Введите название игрушки: ")
                if toy in toys:
                    print(f"{toy}: {toys[toy][0]}")
                else:
                    print("Игрушка не найдена.")
            case '2':
                toy = input("Введите название игрушки: ")
                if toy in toys:
                    print(f"Цена {toy}: {toys[toy][1]}")
                else:
                    print("Игрушка не найдена.")
            case '3':
                toy = input("Введите название игрушки: ")
                if toy in toys:
                    print(f"Количество {toy}: {toys[toy][2]}")
                else:
                    print("Игрушка не найдена.")
            case '4':
                for toy, info in toys.items():
                    print(f"{toy}: Описание - {info[0]}, Цена - {info[1]}, Количество - {info[2]}")
            case '5':
                toy = input("Введите название игрушки для покупки: ")
                if toy in toys:
                    try:
                        qty = int(input(f"Сколько {toy} вы хотите купить?: "))
                    except ValueError:
                        print("Ошибка: Введите числовое значение для количества.")
                        continue
                    
                    if qty <= toys[toy][2]:
                        total_price = toys[toy][1] * qty
                        toys[toy][2] -= qty
                        print(f"Покупка совершена! Итоговая цена: {total_price}. Осталось {toys[toy][2]} шт.")
                    else:
                        print("Недостаточно товара в магазине.")
                else:
                    print("Игрушка не найдена.")
            case '6':
                print("До свидания!")
                break


def task6():
    """6. Дан кортеж целых чисел. Найти индекс максимального элемента.
        – 1 балл"""
    numbers = (1, 20, 3, 50, 45, 99, 100)
    max_index = numbers.index(max(numbers))
    print(f"Индекс максимального элемента: {max_index}")


def main():
    while True:
        print(dedent("""\
                    --------------------------------------------
                    1. Сумма четных цифр числа
                    2. Гласные и согласные в тексте
                    3. Проверка четности в списке
                    4. Ключи с маленькими значениями
                    5. Магазин игрушек
                    6. Индекс максимального элемента
                    7. Выход
                    ---------------------------------------------"""))
        choice = input("--> ")
        
        if choice not in {'1', '2', '3', '4', '5', '6', '7'}:
            print("Ошибка: Некорректный выбор пункта меню!")
            continue
        match choice:
            case '1': task1()
            case '2': task2()
            case '3': task3()
            case '4': task4()
            case '5': task5()
            case '6': task6()
            case '7': break


if __name__ == "__main__":
    main()
