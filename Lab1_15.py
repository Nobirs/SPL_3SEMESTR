def convert_seconds():
    total_seconds = int(input("Введите количество секунд: "))
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    print(f"{days} дней, {hours:02}:{minutes:02}:{seconds:02}")


def extract_numbers_from_string():
    text = input("Введите строку: ")
    numbers = [int(num) for num in text.split() if num.isdigit()]
    print("Числа, встречающиеся в строке:", numbers)


def count_vowels_and_consonants_in_words():
    word_list = ['Python', 15442, 32, 'QweRty', 34, 19, 'love']
    vowels = "AEIOUYaeiouy"
    
    for word in word_list:
        if isinstance(word, str):
            vowels_count = sum(1 for char in word if char in vowels)
            consonants_count = len([char for char in word if char.isalpha() and char not in vowels])
            print(f"{word}: {vowels_count} гласных, {consonants_count} согласных")


def merge_dictionaries():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    dict3 = {'e': 5, 'f': 6}
    merged_dict = {**dict1, **dict2, **dict3}
    print("Слитый словарь:", merged_dict)


def jewelry_store():
    store = {
        'Кольцо': ['Золото', 1000, 10],
        'Браслет': ['Серебро', 500, 5],
        'Серьги': ['Платина', 1500, 2]
    }
    
    while True:
        print("""
        1. Просмотр описания
        2. Просмотр цены
        3. Просмотр количества
        4. Вся информация
        5. Покупка
        6. До свидания
        """)
        
        choice = input("Выберите пункт меню: ")
        
        if choice == '1':
            name = input("Введите название изделия: ")
            if name in store:
                print(f"{name}: Состав - {store[name][0]}")
            else:
                print("Такого изделия нет.")
        
        elif choice == '2':
            name = input("Введите название изделия: ")
            if name in store:
                print(f"{name}: Цена - {store[name][1]}")
            else:
                print("Такого изделия нет.")
        
        elif choice == '3':
            name = input("Введите название изделия: ")
            if name in store:
                print(f"{name}: Количество - {store[name][2]}")
            else:
                print("Такого изделия нет.")
        
        elif choice == '4':
            for name, details in store.items():
                print(f"{name}: Состав - {details[0]}, Цена - {details[1]}, Количество - {details[2]}")
        
        elif choice == '5':
            name = input("Введите название изделия: ")
            if name in store:
                qty = int(input("Введите количество: "))
                if qty <= store[name][2]:
                    total_price = qty * store[name][1]
                    store[name][2] -= qty
                    print(f"Вы купили {qty} {name}(ов) на сумму {total_price}. Осталось {store[name][2]}.")
                else:
                    print("Недостаточно товара.")
            else:
                print("Такого изделия нет.")
        
        elif choice == '6':
            print("До свидания!")
            break


def sum_until_negative():
    numbers = tuple(map(int, input("Введите числа через пробел: ").split()))
    total_sum = 0
    for num in numbers:
        if num < 0:
            break
        total_sum += num
    print("Сумма до первого отрицательного числа:", total_sum)


def menu():
    while True:
        print("""
        --------------------------------------------
        1. Дни:Часы:Минуты:Секунды
        2. Числа в строке
        3. Количество гласных и согласных
        4. Слияние словарей
        5. Ювелирный магазин
        6. Сумма до отрицательного
        7. Выход
        --------------------------------------------
        """)
        
        choice = input("Выберите задание: ")
        
        if choice == '1':
            convert_seconds()
        elif choice == '2':
            extract_numbers_from_string()
        elif choice == '3':
            count_vowels_and_consonants_in_words()
        elif choice == '4':
            merge_dictionaries()
        elif choice == '5':
            jewelry_store()
        elif choice == '6':
            sum_until_negative()
        elif choice == '7':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    menu()
