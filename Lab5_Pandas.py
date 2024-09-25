import pandas as pd

# 2.1 Импортировать датасет
df = pd.read_csv('Real_Estate_Sales_2001-2022_GL.csv')

# 2.2 Взять 1000 значений из выбранного датасета
df_sample = df.sample(1000, random_state=42)

# 2.3 Проверить данные на пропуски
missing_data = df_sample.isnull().sum()
print("Пропуски в данных:\n", missing_data)

# 2.4 Заполнить пропуски (в зависимости от типа данных можно использовать разные методы)
df_sample.fillna(method='ffill', inplace=True)  # заполнение пропусков предыдущим значением

# Пример обработки аномальных значений (например, удаление квартир с количеством комнат > 10)
df_sample = df_sample[df_sample['Sales Ratio'] <= 10]

# 2.5 Определить количество квартир по количеству комнат
year_counts = df_sample['List Year'].value_counts()
print("Количество по годам:\n", year_counts)

# 2.6 Сохранение в CSV
df_sample.to_csv('processed_surname.csv', index=False)
