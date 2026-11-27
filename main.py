import pandas as pd

df = pd.read_csv('./sales.csv')

# Сперва проверяем изначальные данные на аномалии (пропуски, дубли, некорректные значения)
df.info()