import string

# =================================================================================
class List:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(f"Элемент '{item}' добавлен в список.")

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Элемент '{item}' удален из списка.")
        else:
            print(f"Элемент '{item}' не найден.")

    def find(self, item):
        if item in self.items:
            return self.items.index(item)
        return -1

    def sort(self):
        self.items.sort()
        print("Список отсортирован.")

    def display(self):
        print("Содержимое списка:", self.items)

def task_1():
    # Пример использования List:
    my_list = List()

    my_list.add(10)
    my_list.add(5)
    my_list.add(20)

    my_list.remove(5)
    index = my_list.find(10)
    print(f"Элемент 10 находится по индексу: {index}")
    my_list.sort()
    my_list.display()

# =================================================================================
# Класс алфавита
class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(f"Буквы алфавита ({self.lang}):", ''.join(self.letters))

    def letters_num(self):
        return len(self.letters)

# Класс английского алфавита
class EngAlphabet(Alphabet):
    __letters_num = 26  # кол-во букв в английском алфавите

    def __init__(self):
        super().__init__('En', list(string.ascii_uppercase))

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        return "The quick brown fox jumps over the lazy dog."


def task_2():
    eng_alphabet = EngAlphabet()
    eng_alphabet.print()

    print(f"Количество букв в английском алфавите: {eng_alphabet.letters_num()}")
    print(f"Буква 'F' является английской: {eng_alphabet.is_en_letter('F')}")
    print("Пример текста:", EngAlphabet.example())
# =================================================================================

class Animal:
    def __init__(self, breed, price):
        self.breed = breed
        self.price = price

    def move(self):
        pass

class Fish(Animal):
    def __init__(self, breed, price):
        super().__init__(breed, price)

    def move(self):
        return f"Рыба {self.breed} плавает."

class Bird(Animal):
    def __init__(self, breed, price):
        super().__init__(breed, price)

    def move(self):
        return f"Птица {self.breed} летает."

class PetShop:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def most_expensive_animal(self):
        if not self.animals:
            return "В зоомагазине нет животных."
        expensive_animal = max(self.animals, key=lambda x: x.price)
        return f"Самое дорогое животное: {expensive_animal.breed}, стоимость: {expensive_animal.price}"

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for animal in self.animals:
                file.write(f"Порода: {animal.breed}, Цена: {animal.price}, Способ передвижения: {animal.move()}\n")

def task_3():
    shop = PetShop()

    shop.add_animal(Fish("Золотая рыбка", 50))
    shop.add_animal(Bird("Попугай", 150))
    shop.add_animal(Fish("Акула", 1000))
    shop.add_animal(Bird("Орёл", 500))

    print(shop.most_expensive_animal())
    shop.save_to_file("animals.txt")
# =================================================================================

class Car:
    # статическая переменная
    total_cars = 0

    def __init__(self, brand, model, year, mileage):
        """Метод экземпляра"""
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        Car.total_cars += 1

    def start_engine(self):
        """Метод экземпляра"""
        print(f"Двигатель {self.brand} {self.model} запущен.")

    def drive(self, distance):
        """Метод экземпляра"""
        self.mileage += distance
        print(f"{self.brand} {self.model} проехал {distance} км. Общий пробег: {self.mileage} км.")

    @staticmethod
    def is_vintage(year):
        """Статический метод"""
        current_year = 2024
        return current_year - year > 30

    @classmethod
    def from_string(cls, car_str):
        """
        Метод класса
            - создание экземпляра из строки формата 
            - 'brand,model,year,mileage'. 
        """
        brand, model, year, mileage = car_str.split(',')
        try:
            return cls(brand, model, int(year), int(mileage))
        except ValueError as e:
            print(e)

    @classmethod
    def get_total_cars(cls):
        """Метод класса"""
        return f"Общее количество автомобилей: {cls.total_cars}"


def task_4():
    car1 = Car("Toyota", "Camry", 2020, 15000)
    car1.start_engine()
    car1.drive(200)

    print(f"Toyota Camry 2020 является раритетным? {'Да' if Car.is_vintage(2020) else 'Нет'}")

    car2 = Car.from_string("Ford,Mustang,1990,75000")
    print(f"{car2.brand} {car2.model} - пробег: {car2.mileage} км.")

    print(Car.get_total_cars())

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