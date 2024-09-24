import math

def triangle(side):
    perimeter = 3 * side
    area = (math.sqrt(3) / 4) * side ** 2
    return perimeter, area

def process_data(data):
    if isinstance(data, list):
        # Сумма после второго отрицательного элемента и вывод четных числел
        neg_count = 0
        total_sum = 0
        even_numbers = []
        for num in data:
            if num < 0 and neg_count < 2:
                neg_count += 1
                continue
            if neg_count >= 2:
                total_sum += num
            if num % 2 == 0:
                even_numbers.append(num)
        if neg_count >= 2:
            print(f"Сумма после второго отрицательного: {total_sum}")
        print(f"Четные числа: {even_numbers}")
    elif isinstance(data, set):
        print(f"Максимум: {max(data)}, Минимум: {min(data)}")
    elif isinstance(data, int):
        primes = []
        for num in range(2, data):
            if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
                primes.append(num)
        print(f"Простые числа до {data}: {primes}")
    elif isinstance(data, str):
        # Выводим все цифры в отдельный список
        digits = [char for char in data if char.isdigit()]
        print(f"Цифры в строке: {digits}")
    else:
        print("Неверный тип данных.")

def swap_columns(matrix, i, j):
    for row in matrix:
        row[i], row[j] = row[j], row[i]
    return matrix

def example_try_except():
    try:
        x = int(input("Введите число: "))
        result = 10 / x
        print(f"Результат деления: {result}")
    except ValueError:
        print("Ошибка: введено не число!")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
    finally:
        print("Завершение программы.")

def menu():
    while True:
        print("\nМеню:")
        print("1. Периметр и площадь треугольника")
        print("2. Универсальная обработка данных")
        print("3. Замена столбцов в двумерном массиве")
        print("4. Пример try/except/finally")
        print("5. Выход")

        choice = input("Выберите задание (1-5): ")

        if choice == '1':
            try:
                side = float(input("Введите длину стороны треугольника: "))
                if side < 0:
                    raise ValueError("Число отрицательное")
                perimeter, area = triangle(side)
                print(f"Периметр: {perimeter}, Площадь: {area}")
            except ValueError as e:
                print(f"Введено не число или {e}")
                continue
        elif choice == '2':
            data_type = input("Введите тип данных (list, set, int, str): ")
            if data_type == 'list':
                data = list(map(int, input("Введите элементы списка через пробел: ").split()))
            elif data_type == 'set':
                data = set(map(int, input("Введите элементы множества через пробел: ").split()))
            elif data_type == 'int':
                try:
                    data = int(input("Введите число: "))
                except ValueError:
                    print(f"Введено не число")
                    continue
            elif data_type == 'str':
                data = input("Введите строку: ")
            else:
                print("Неверный тип данных.")
                continue
            process_data(data)
        elif choice == '3':
            try:
                n, m = map(int, input("размеры массива (n m): ").split())
                matrix = [list(map(int, input().split())) for _ in range(n)]
                matrix_full = all(len(row) == m for row in matrix)
                if not matrix_full:
                    raise Exception("Матрица не заполнена")
                i, j = map(int, input("индексы столбцов для замены (i j): ").split())
                if i > m - 1 or j > m - 1:
                    raise Exception("индексы столбцов для замены выходят за границы")
                swapped_matrix = swap_columns(matrix, i, j)
                print("Изменённый массив:")
                for row in swapped_matrix:
                    print(row)
            except ValueError:
                print(f"Введено не число")
                continue
            except Exception as e:
                print(f"{e}")
                continue
        elif choice == '4':
            example_try_except()
        elif choice == '5':
            print("Конец")
            break
        else:
            print("Неправильный выбор")

# Запуск программы
if __name__ == "__main__":
    menu()
