import pandas as pd

df = pd.read_csv('./sales.csv')

# Сперва проверяем изначальные данные на аномалии (пропуски, дубли, некорректные значения)
df.info()

# Видим, что в столбце quantity есть пропуски. Надо проверить, как они выглядят
print(df[df['quantity'].isna()])

# По условию задачи мы строки со статусом 'cancelled' все равно не считаем, поэтому данные можно оставить как есть, но лучше заменю пропуски на 0
df = df.fillna(0)

# Еще раз чекнем общую инфу
df.info()

# Пропуски заполнены, теперь удовлетворим условие задачи, по которому считается только один заказ, даже если есть дубли, убрав эти дубли по order_id
# Но сперва проверим, полные ли это дубли или есть аномалии
duplicate_orders = df[df['order_id'].duplicated(keep=False)].sort_values('order_id')
print(duplicate_orders.to_string())

# Выяснили, что дубли полные, поэтому можно их дропать
df = df.drop_duplicates()

# Смотрим уникальные значения в остальных столбцах, чтобы найти приколы в данных
print(df['order_date'].unique())
print(df['sku'].unique())
print(df['quantity'].unique())
print(df['price'].unique())
print(df['status'].unique())

# Проблемы остались со статусами, помимо 'delivered' и 'cancelled' видим значения с опечатками, некорректными регистрами и пробелами в рандомных местах. Приводим к нужному виду.
df['status'] = df['status'].astype(str).str.strip().str.lower().replace({'canceled': 'cancelled'})

# Проверяем статусы повторно
print(df['status'].unique())