from capitulo_01 import *
from sqlalchemy import select, insert, update

from sqlalchemy.exc import IntegrityError

# ------------------------------------------
# ------------------------------------------
# Populating the database

# Adding users
ins = insert(users).values(
    username='cookiemon',
    email_address='mon@cookie.com',
    phone='111-111-1111',
    password='password'
)
result = connection.execute(ins)

# Adding cookies
ins = cookies.insert()
inventory_list = [
    {
        'cookie_name': 'chocolate chip',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/recipe.html',
        'cookie_sku': 'CC01',
        'quantity': '12',
        'unit_cost': '0.50',
    },
    {
        'cookie_name': 'dark chocolate chip',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/recipe_dark.html',
        'cookie_sku': 'CC02',
        'quantity': '1',
        'unit_cost': '0.75',
    },
]
result = connection.execute(ins, inventory_list)

# Adding orders
ins = insert(orders).values(user_id=1, order_id='1')
result = connection.execute(ins)
ins = insert(line_items)
order_items = [
    {
        'order_id': 1,
        'cookie_id': 1,
        'quantity': 9,
        'extended_cost': 4.50,
    },
]
result = connection.execute(ins, order_items)

ins = insert(orders).values(user_id=1, order_id='2')
result = connection.execute(ins)
ins = insert(line_items)
order_items = [
    {
        'order_id': 2,
        'cookie_id': 1,
        'quantity': 4,  # This order should fail (only 3 cookies left)
        'extended_cost': 1.50,
    },
    {
        'order_id': 2,
        'cookie_id': 2,
        'quantity': 1,
        'extended_cost': 4.50,
    },
]
result = connection.execute(ins, order_items)

# -- SHIP function --------------------------------------------------
def ship_it(order_id):
    s = select([line_items.c.cookie_id, line_items.c.quantity])
    s = s.where(line_items.c.order_id == order_id)
    transaction = connection.begin()   # Opening the transaction block
    cookies_to_ship = connection.execute(s).fetchall()

    try:
        for cookie in cookies_to_ship:
            u = update(cookies).where(cookies.c.cookie_id == cookie.cookie_id)
            u = u.values(quantity = cookies.c.quantity - cookie.quantity)
            result = connection.execute(u)
        u = update(orders).where(orders.c.order_id == order_id)
        u = u.values(shipped = True)
        result = connection.execute(u)
        transaction.commit()  # Closing the transaction block
        print(f"Shipped order ID: {order_id}")
    except IntegrityError as error:
        transaction.rollback()
        print(error)
        print(f"Order ID: {order_id} won't be shipped")
# -------------------------------------------------------------------

# First query - shows initial stock
print('Estoque inicial')
print('=' * 50)
s = select([cookies.c.cookie_name, cookies.c.quantity])
print(connection.execute(s).fetchall())
print()

print('Estoque após order #1')
print('=' * 50)
ship_it(1)  # Executes the first connection.execute(s)order
s = select([cookies.c.cookie_name, cookies.c.quantity])
print(connection.execute(s).fetchall())
print()

print('Tabela orders')
print('=' * 50)
s = select([orders])
result = connection.execute(s)
for r in result.fetchall():
    for k, v in r.items():
        print(f"{k:>15}: {v}")
    print('-' * 30)


# Trying to process order #2
print('Estoque após order #2')
print('=' * 50)
ship_it(2)  # Executes the first connection.execute(s)order
s = select([cookies.c.cookie_name, cookies.c.quantity])
print(connection.execute(s).fetchall())
print()
