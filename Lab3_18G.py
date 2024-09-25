import re
import json

def task_1():
    # Открытие файла F1 для записи данных
    with open("F1.txt", "w") as f1:
        print("Введите строки для записи в файл (пустая строка завершает ввод):")
        while True:
            line = input()
            if line == "":
                break  # Пустая строка завершает ввод
            f1.write(line + "\n")
    # Открытие файлов F1 для чтения и F2 для записи
    with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
        for line in f1:
            if line.strip().endswith("А"):  # Проверка, заканчивается ли строка на 'А'
                f2.write(line)
                
    print("Данные успешно записаны в F2.txt, если строки заканчивались на 'А'.")


def task_2():
    with open('students.txt', 'r') as f:
        students = []
        for line in f:
            name, grade = line.split()
            grade = float(grade)
            students.append((name, grade))

    grades_4_6 = []
    grades_6_8 = []
    grades_above_8 = []

    for name, grade in students:
        if 4 <= grade <= 6:
            grades_4_6.append(name)
        elif 6 < grade <= 8:
            grades_6_8.append(name)
        elif grade > 8:
            grades_above_8.append(name)

    max_student = max(students, key=lambda x: x[1])

    print("Студенты с баллом от 4 до 6:", ", ".join(grades_4_6))
    print("Студенты с баллом от 6 до 8:", ", ".join(grades_6_8))
    print("Студенты с баллом выше 8:", ", ".join(grades_above_8))
    print(f"Студент с максимальным баллом: {max_student[0]} с баллом {max_student[1]:.2f}")


def task_3():
    with open('subjects.txt', 'r') as f:
        subject_dict = {}

        for line in f:
            subject, lessons = line.split(': ')

            lesson_numbers = re.findall(r'(\d+)\s*\(.*?\)', lessons)
            total_lessons = sum(map(int, lesson_numbers))

            subject_dict[subject] = total_lessons

    print(subject_dict)


def task_4():
    firms_data = []
    profit_dict = {}
    average_profit_dict = {}
    total_profit = 0
    profit_firms_count = 0

    with open('firms.txt', 'r') as file:
        for line in file:
            name, form, revenue, costs = line.split()
            revenue, costs = int(revenue), int(costs)
            # Прибыль
            profit = revenue - costs
            profit_dict[name] = profit
            # Прибыль только для положительных значений
            if profit >= 0:
                total_profit += profit
                profit_firms_count += 1

    # Подсчет средней прибыли (если были прибыльные фирмы)
    if profit_firms_count > 0:
        average_profit_dict["average_profit"] = total_profit / profit_firms_count
    else:
        average_profit_dict["average_profit"] = 0

    # Формирование итогового списка
    firms_data.append(profit_dict)
    firms_data.append(average_profit_dict)

    # Сохранение в JSON
    with open('firms_data.json', 'w') as json_file:
        json.dump(firms_data, json_file, ensure_ascii=False, indent=4)

    print("Данные о фирмах сохранены в 'firms_data.json'.")

    

def main():
    while True:
        print("\nМеню:")
        print("1. Задание 1")
        print("2. Задание 2")
        print("3. Задание 3")
        print("4. Задание 4")
        print("5. Выход")

        choice = input("Введите номер пункта меню: ")

        match choice:
            case '1':
                task_1()
            case '2':
                task_2()
            case '3':
                task_3()
            case '4':
                task_4()
            case '5':
                print("Завершение программы")
                break

if __name__ == "__main__":
    main()