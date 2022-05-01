from random import randint as rdt
from random import randrange as rdg
from datetime import datetime as dt

import psycopg2

bd_password = input("Введите пароль от Базы Данных: ")

connection = psycopg2.connect(
    dbname='markets', 
    user='beks', 
    password=f'{bd_password}', 
    host='localhost'
)

cursor = connection.cursor()


# categories_table = '''CREATE TABLE categories(
#     category_id SERIAL PRIMARY KEY,
#     category_name VARCHAR(50),
#     created_at DATE DEFAULT CURRENT_TIMESTAMP
# );'''

# produsers_table = '''CREATE TABLE produsers(
#     produser_id SERIAL PRIMARY KEY,
#     produser_country VARCHAR(50),
#     produser_company VARCHAR(50),
#     prodused_date DATE,
#     created_at DATE DEFAULT CURRENT_TIMESTAMP
# );'''

# kivano_table = '''CREATE TABLE kivano(
#     item_id SERIAL PRIMARY KEY,
#     category_id SMALLINT,
#     produser_id SMALLINT,
#     product_name VARCHAR(50),
#     price INT,
#     CONSTRAINT fk_category_id
#     FOREIGN KEY (category_id)
#         REFERENCES categories(category_id),
#     FOREIGN KEY (produser_id)
#         REFERENCES produsers(produser_id)
# );'''

# sulpak_table = '''CREATE TABLE sulpak(
#     item_id SERIAL PRIMARY KEY,
#     category_id SMALLINT,
#     produser_id SMALLINT,
#     product_name VARCHAR(50),
#     price INT,
#     CONSTRAINT fk_category_id
#     FOREIGN KEY (category_id)
#         REFERENCES categories(category_id),
#     FOREIGN KEY (produser_id)
#         REFERENCES produsers(produser_id)
# );'''


# produsers_insert = 'INSERT INTO produsers (produser_country,produser_company,prodused_date) VALUES '
# categories_insert = 'INSERT INTO categories (category_name) VALUES '
# kivano_insert = 'INSERT INTO kivano (category_id, produser_id, product_name, price) VALUES '
# sulpak_insert = 'INSERT INTO sulpak (category_id, produser_id, product_name, price) VALUES '

# SIZE = 100

# countries = (
#     'Brazil',
#     'China',
#     'Argentina',
#     'Korea',
#     'Germany',
#     'USA',
#     'UK',
#     'Russia',
#     'Japan'
# )


# smartphones = (
#     ('Iphone 4','Iphone 5','Iphone 6','Iphone 7','Iphone 10','Iphone 12'),
#     ('Samsung Galaxy A71','Samsung Galaxy A71','Samsung Galaxy S10 8','Samsung Galaxy S10 10','Samsung Galaxy S9','Samsung Galaxy A21s','Samsung Galaxy A10','Samsung Galaxy Note 8','Samsung Galaxy Note 10'),
#     ('OnePlus 1', 'OnePlus 2', 'OnePlus Zero', 'OnePlus 3'),
#     ('Xiaomi Mi A2','Xiaomi Redmi Note 8','Xiaomi Poco X3 NFC','Xiaomi Redmi 9A','Xiaomi Mi Note 10 Lite','Xiaomi Redmi Note 8T','Xiaomi Redmi 7A','Xiaomi Redmi Note 8T','Xiaomi Redmi 9','Xiaomi Redmi 9C'),
#     ('ASUS ZenFone 4 Selfie ZD553KL','ASUS PadFone mini','ASUS Fonepad Note 6 16Gb'),
#     ('Nokia 3310 Dual Sim','Nokia 3310 Dual Sim','Nokia 3310 Dual Sim','Nokia 150 Dual sim','Nokia 105 Dual sim','Nokia 106','Nokia 110','Nokia 150','Nokia 230 Dual Sim'),
#     ('Huawei P smart Z ','Huawei P30 lite','Huawei Y6s','Huawei P smart Z','Huawei Y9 Prime','Huawei P40 Pro','Huawei Y6p'),
# )

# laptops = (
#     ('MacBook Pro 13','MacBook Pro 16','MacBook Pro 19','MacBook Air 13','MacBook Air 16'),
#     ('MSI Thin','MSI GL63 8RD','MSI GF65 Thin 9SD 9S7-16W112-252','MSI GL65 Leopard 10SCSR-051XRU 9S7-16U822-051','MSI GF72VR 7RF'),
#     ('Acer A315-55G','Acer A315-55G','Acer Aspire E5-576G-74W4','Acer Aspire E5-576G-74W4','Acer Aspire A315-55G','Acer Aspire E5-576G-56QV','Acer Aspire E5-576G-5121','Acer Aspire E5-576G-56QV','Acer Aspire A315-55G','Acer Extensa EX215-51-38HJ','Acer Aspire 3 A315-42-R14W','Acer Aspire E5-576G-56QV','Acer Aspire E5-576G-5121'),
#     ('Lenovo Ideapad S145-15IIL','Lenovo IdeaPad L3 15IML05','Lenovo V130-15IKB 81HN010YRU','Lenovo Ideapad 320-15ISK','Lenovo Flex 14 81SQ0000US','Lenovo ThinkPad X390 20Q1SCDR00','Lenovo V130-15IKB 81HN010YRU','Lenovo Ideapad 320-15ISK'),
# )

# company = {
#     'Mac': laptops[0],
#     'MSI': laptops[1],
#     'Aser': laptops[2],
#     'Lenovo': laptops[3],
#     'IPhone': smartphones[0],
#     'Samsung': smartphones[1],
#     'OnePlus': smartphones[2],
#     'Xiaomi': smartphones[3],
#     'Asus': smartphones[4],
#     'Nokia': smartphones[5],
#     'Huawei': smartphones[6],
# }


# comp_keys = tuple(company.keys())


# categories = (
#     "Smartphones",
#     "Laptops",
#     "Home Stuff",
#     "Clothes"
# )


# stuff = (laptops, smartphones)


# dates = tuple(
#     str(
#         dt.date(
#             dt.strptime(
#                 f'{rdt(1995,2023)}-{rdt(1,12)}-{rdt(1,29)}', '%Y-%M-%d'
#             )
#         )
#     )
#     for _ in range(SIZE)
# )

# prices = tuple(rdg(20000, 100000, 2500) for _ in range(SIZE))

# for i in range(SIZE):
#     n = rdt(0,1)
#     item = stuff[n]
#     cmp_n = rdt(0,len(comp_keys)-1)
#     l_s = item[rdt(0, len(item)-1)]
#     produsers_insert += f'(\'{countries[rdt(0, len(countries)-1)]}\',\'{comp_keys[cmp_n]}\',\'{dates[rdt(0, len(dates)-1)]}\'),'
#     kivano_insert += f'({n+1}, {rdt(1, SIZE)}, \'{company[comp_keys[cmp_n]][rdt(0, len(company[comp_keys[cmp_n]])-1)]}\', {prices[rdt(0, len(prices)-1)]}),'
#     sulpak_insert += f'({n+1}, {rdt(1, SIZE)}, \'{company[comp_keys[cmp_n]][rdt(0, len(company[comp_keys[cmp_n]])-1)]}\', {prices[rdt(0, len(prices)-1)]}),'
# else:
#     produsers_insert = produsers_insert[:-1] + ';'
#     kivano_insert = kivano_insert[:-1] + ';'
#     sulpak_insert = sulpak_insert[:-1] + ';'


# for category in categories:
#     categories_insert += f'(\'{category}\'),'
# else:
#     categories_insert = categories_insert[:-1] + ';'


# cursor.execute(categories_table)
# cursor.execute(produsers_table)
# connection.commit()
# cursor.execute(kivano_table)
# cursor.execute(sulpak_table)
# connection.commit()

# cursor.execute(produsers_insert)
# cursor.execute(categories_insert)
# connection.commit()
# cursor.execute(kivano_insert)
# connection.commit()
# cursor.execute(sulpak_insert)
# connection.commit()
 



# 1. Узнайте какие телефоны из Kivano стоят столько же сколько и компьютеры из Sulpak.
# cursor.execute("""SELECT DISTINCT kivano.product_name, kivano.price, sulpak.product_name, sulpak.price 
# FROM kivano 
# RIGHt JOIN sulpak ON kivano.price = sulpak.price 
# WHERE sulpak.category_id = 1 AND kivano.category_id = 1;
# """)
# print(cursor.fetchall())
# connection.commit()

######################### 2. Узнайте самую последнюю модель Iphone в магазинах. ########################
# cursor.execute("")
# print(cursor.fetchall())
# connection.commit()


######################### 3. Выведите на экран список всех ноутбуков из sulpak и только тех телефонов которые имеют одинаковую дату выхода с компьютером из таблицы kivano.########################
# cursor.execute("")
# print(cursor.fetchall())
# connection.commit()


# 4. Выведите все китайские продукты.
# cursor.execute("""SELECT DISTINCT kivano.item_id ,kivano.product_name, produsers.produser_country FROM kivano  
# INNER JOIN produsers  ON produser_country = 'China' AND kivano.item_id = produsers.produser_id;
# """)
# cursor.execute(""" SELECT DISTINCT sulpak.item_id ,sulpak.product_name, produsers.produser_country FROM sulpak  
# INNER JOIN produsers  ON produser_country = 'China' AND sulpak.item_id = produsers.produser_id;
# """)

# print(cursor.fetchall())
# connection.commit()


# 5. Напишите запрос, который выводит продукты любого магазина в порядке их добавления.
# cursor.execute("")
# print(cursor.fetchall())
# connection.commit()


# 6. Найдите товары, которые есть в kivano но нет в sulpak.
# cursor.execute(""" SELECT DISTINCT k.product_name, s.product_name 
# FROM kivano k, sulpak s 
# WHERE k.product_name != s.product_name
# """)
# print(cursor.fetchall())
# connection.commit()


# 7. Найдите все товары в магазине sulpak, где компания-производитель содержит букву "m" в имени.
# cursor.execute("""SELECT product_name, produsers.produser_company FROM sulpak
# INNER JOIN produsers ON sulpak.produser_id = produsers.produser_id 
# WHERE produser_company LIKE '%m%'""")
# print(cursor.fetchall())
# connection.commit()


# 8. Найдите товары, которые есть и в kivano u sulpak.
# cursor.execute("""SELECT DISTINCT k.product_name, s.product_name 
# FROM kivano k, sulpak s 
# WHERE k.product_name = s.product_name
# """)
# print(cursor.fetchall())
# connection.commit()


# 9. Найдите китайские товары из kivano, которые в названии содержат "k". 
# cursor.execute("SELECT product_name,produsers.produser_country FROM kivano INNER JOIN produsers ON produsers.produser_id = kivano.produser_id where produsers.produser_country = 'China' and kivano.product_name LIKE '%k%';")
# print(cursor.fetchall())
# connection.commit()


# 10. Найдите самый последний добавленный товар в таблице produsers, и поменяйте компанию на Apple, и страну на kyrgyzstan.
# cursor.execute("SELECT * FROM produsers where prodused_date = (select MAX(prodused_date) from produsers);")

# print(cursor.fetchall())
# cursor.execute("UPDATE produsers SET produser_company = 'Apple', produser_country = 'Kyrgyzstan' where prodused_date = (select MAX(prodused_date) from produsers);")

# connection.commit()


# 11. Нужно объеденить 2 магазина по product_name и вывести на экран имя продукта и его цену из обоих магазинов, однако не факт что в обоих магазинах будут одинаковые товары, поэтому нужно joinить по полной.
# cursor.execute("SELECT kivano.product_name, sulpak.product_name FROM kivano FULL OUTER JOIN sulpak ON kivano.produser_id = sulpak.produser_id;")
# print(cursor.fetchall())
# connection.commit()


# 12. Найдите самый последний японский товар который был добавлен в produsers.
# cursor.execute("""select product_name,produsers.produser_country,produsers.prodused_date from sulpak inner join produsers on produsers.produser_id = sulpak.produser_id
# where sulpak.produser_id = (select produser_id from produsers where prodused_date = (SELECT MAX(prodused_date) FROM produsers where produser_country = 'Japan')
# and produser_country = 'Japan');""")
# print(cursor.fetchall())
# connection.commit()


# 13. Напишите запрос, который прибавит 1000 к цене всех продуктов в sulpak.
# cursor.execute("SELECT price+1000 as added_1000_price FROM sulpak;")
# print(cursor.fetchall())
# connection.commit()


# 14. Узнать разницу между самой высокой ценой в sulpak и самой низкой ценой товар в kivano.
# cursor.execute("select DISTINCT (sulpak.price - kivano.price) as difference from sulpak,kivano where sulpak.price = (select max(price) from sulpak) AND kivano.price =  (select MIN(price) from kivano);")
# print(cursor.fetchall())
# connection.commit()


# 15. Выведите на экран цены самых дешёвых телефонов из обоих магазинов.
# cursor.execute("""SELECT product_name, categories.category_name FROM kivano INNER JOIN categories ON categories.category_id = kivano.category_id
# WHERE categories.category_name = 'Smartphones' and price = (SELECT MIN(price) FROM kivano)
# UNION
# SELECT product_name, categories.category_name FROM sulpak INNER JOIN categories ON categories.category_id = sulpak.category_id 
# WHERE categories.category_name = 'Smartphones' and price = (SELECT MIN(price) FROM sulpak)
# ORDER BY product_name, category_name;
# """)
# print(cursor.fetchall())
# connection.commit()


# 16. Удалить все записи где есть NULL в product_name в обоих магазинах.
# cursor.execute("DELETE FROM kivano WHERE product_name IS NULL;")
# cursor.execute("DELETE FROM sulpak WHERE product_name IS NULL;")

# connection.commit()



######################### 17. Все телефоны у которых год меньше 1998 изменить на 2000 (Выполнить с помощью psycopg2).########################
# cursor.execute("update produsers set prodused_date = '2000-01-01' where prodused_date < '1998-01-01';")
# connection.commit()

# 18. Acer закрыл свою фабрику в Бразилии после 2012 года и переехал в Германию, у всех записей в produsers где Acer был произведен в Brazil после 2012 поставьте Germany.
# cursor.execute("update produsers set produser_country = 'Germany' where produser_country = 'Brazil' and prodused_date >'2012-01-01' and produser_company = 'Aser';")
# connection.commit()

# 19. Выведите первые 16 записей без id, из kivano.
# cursor.execute("select product_name,price from kivano where item_id<=16;")
# print(cursor.fetchall())
# connection.commit()

# 20. Выведите на экран все product_name которые относятся к категории laptops в kivano.
# cursor.execute("select product_name,categories.category_name from kivano inner join categories on categories.category_id = kivano.category_id where categories.category_name = 'Laptops';")
# print(cursor.fetchall())
# connection.commit()


# 21. Найдите товары в sulpak, цена которых больше среднего на 2000 и меньше средний на 2000
# cursor.execute("select product_name,price from sulpak where price = (select floor(avg(price))+2000 from sulpak) or price =(select floor(avg(price))-2000 from sulpak);")
# print(cursor.fetchall())
# connection.commit()

# 22. Найдите product_company, чьи товары дороже среднего в kivano.
# cursor.execute("select produser_company,price from produsers inner join kivano on kivano.produser_id = produsers.produser_id where kivano.price < (select avg(price) from kivano);")
# print(cursor.fetchall())
# connection.commit()

# 23. Найдите товар который лежит посередине в таблице sulpak.
# cursor.execute("select item_id, product_name from sulpak where item_id = (select floor(count(*)/2) from sulpak);")
# print(cursor.fetchall())
# connection.commit()

# 24. Поменяйте страну на South Korea везде где страна Korea и компания Asus.
# cursor.execute("update  produsers set produser_country = 'South Korea' where produser_country = 'Korea' and produser_company = 'Aser'")
# connection.commit()

# 25. В producers поменяйте Nokia на Microsoft везде где у компании Nokia указана страна USA.
# cursor.execute("update  produsers set produser_company = 'Microsoft' where produser_company = 'Nokia' and produser_country = 'USA';")
# connection.commit()


