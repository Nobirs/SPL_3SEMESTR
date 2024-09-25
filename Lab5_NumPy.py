import numpy as np

# 1. Создать вектор размера 10, заполненный нулями
vector_zeros = np.zeros(10)
print("Vector of zeros:", vector_zeros)

# 2. Создать вектор размера 10, заполненный числом 2.5
vector_2_5 = np.full(10, 2.5)
print("Vector filled with 2.5:", vector_2_5)

# 3. Создать вектор размера 10, заполненный нулями, но пятый элемент равен 1
vector_custom = np.zeros(10)
vector_custom[4] = 1
print("Custom vector:", vector_custom)

# 4. Создать вектор со значениями от 10 до 49
vector_range = np.arange(10, 50)
print("Vector from 10 to 49:", vector_range)

# 5. Найти индексы ненулевых элементов в [1,2,0,0,4,0]
array = np.array([1, 2, 0, 0, 4, 0])
non_zero_indices = np.nonzero(array)
print("Non-zero indices:", non_zero_indices)

# 6. Создать 3x3 единичную матрицу
identity_matrix = np.eye(3)
print("3x3 Identity Matrix:\n", identity_matrix)

# 7. Создать массив 10x10 со случайными значениями, найти минимум и максимум
random_matrix = np.random.random((10, 10))
matrix_min = random_matrix.min()
matrix_max = random_matrix.max()
print("Random 10x10 matrix:\n", random_matrix)
print("Min value:", matrix_min)
print("Max value:", matrix_max)

# 8. Создать случайный вектор размера 30 и найти среднее значение всех элементов
random_vector = np.random.random(30)
mean_value = random_vector.mean()
print("Random vector of 30 elements:", random_vector)
print("Mean value:", mean_value)

# 9. Создать 8x8 матрицу и заполнить ее в шахматном порядке
chess_matrix = np.zeros((8, 8), dtype=int)
chess_matrix[1::2, ::2] = 1
chess_matrix[::2, 1::2] = 1
print("Chessboard pattern:\n", chess_matrix)

# 10. Перемножить матрицы 5x3 и 3x2
matrix_5x3 = np.random.random((5, 3))
matrix_3x2 = np.random.random((3, 2))
product_matrix = np.dot(matrix_5x3, matrix_3x2)
print("Product of 5x3 and 3x2 matrices:\n", product_matrix)

# 11. Проверить, одинаковы ли 2 numpy массива
array1 = np.array([1, 2, 3])
array2 = np.array([1, 2, 3])
arrays_equal = np.array_equal(array1, array2)
print("Are the arrays equal?", arrays_equal)

# 12. Заменить максимальный элемент на ноль
random_array = np.random.random(10)
random_array[random_array.argmax()] = 0
print("Array after replacing max with zero:", random_array)

# 13. Найти наиболее частое значение в массиве
array_with_duplicates = np.random.randint(0, 10, 20)
most_frequent_value = np.bincount(array_with_duplicates).argmax()
print("Array:", array_with_duplicates)
print("Most frequent value:", most_frequent_value)

# 14. Найти n наибольших значений в массиве
n = 3
large_values = np.sort(array_with_duplicates)[-n:]
print(f"{n} largest values:", large_values)
