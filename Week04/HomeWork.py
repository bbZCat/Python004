import numpy as np
import pandas as pd
import time
import random

def dash(str=''):
    print()
    print(str)
    print("="*75)

def random_date():
    s = (1990, 1, 1, 0, 0, 0, 0, 0, 0)
    e = (2020, 1, 1, 0, 0, 0, 0, 0, 0)
    start = time.mktime(s)
    end = time.mktime(e)
    t = random.randint(start, end)
    return time.strftime("%Y-%m-%d", time.localtime(t))

id = list(np.arange(500, 2000, 100))

age = []
salary = []
names = ['Bob', 'John', 'Tom', 'Jack', 'Mike', 'Eric', 'Richard', 'Robin', 'Lee', 'Henry',\
        'James', 'Jacob', 'Ben', 'Alan', 'Carl']
for _ in range(15):
    age.append(random.randint(18,60))
    salary.append(random.randint(2000, 10000))

table1 = pd.DataFrame({
    "id":id, 
    "name":names,
    "age":age, 
    "salary":salary
}) 

sales_id = []
order_id = list(np.arange(10000, 20000, 100))
order_date = []
clients = ["IBM", "HP", "SUN", "APPLE", "LENOVO", "HUAWEI", "ASUS"]
client_name = []

for _ in range(15):
    sales_id.append(random.choice(id)),
    order_date.append(random_date()),
    client_name.append(random.choice(clients))

table2 = pd.DataFrame({
    "id":sales_id,
    "client_name":client_name,
    "order_id": random.sample(order_id, 15),
    "order_date": order_date,
    #"contract_amount":
})

#dash('Origin Data')
dash('Table1')
print(table1)
dash('Table2')
print(table2)

# 1. SELECT * FROM data;
dash('1. SELECT * FROM data;')
print(table1)

# 2. SELECT * FROM data LIMIT 10;
dash('2. SELECT * FROM data LIMIT 10;')
print(table1[0:10])

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
dash('3. SELECT id FROM data;  //id 是 data 表的特定一列')
print(table1['id'])

#4. SELECT COUNT(id) FROM data;
dash('4. SELECT COUNT(id) FROM data;')
print(table1['id'].count())
 
# 5. SELECT * FROM data WHERE id<1000 AND age>30;
dash('5. SELECT * FROM data WHERE id<1000 AND age>30;')
print(table1.loc[(table1['id'] < 1000) & (table1['age'] > 30), ['id', 'name', 'age']])

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
dash('6. SELECT id,COUNT(DISTINCT order_id) FROM table2 GROUP BY id;')
print(table2['id'].value_counts())

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
dash('7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;') 
print(pd.merge(table1, table2, how='inner', on='id'))

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
dash('8. SELECT * FROM table1 UNION SELECT * FROM table2;') 
print(pd.concat([table1, table2], ignore_index=True, sort=True))

# 9. DELETE FROM table1 WHERE id=10;
dash('9. DELETE FROM table1 WHERE id=1000') 
table1.drop(table1[table1['id'].isin([1000])].index, axis=0, inplace=True)
print(table1)

# 10. ALTER TABLE table1 DROP COLUMN column_name;
dash('ALTER TABLE table1 DROP COLUMN salary;')
table1.drop(['salary'], axis=1, inplace=True)
print(table1)
