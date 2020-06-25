

from sqlalchemy.sql import func
from sqlalchemy.sql import select
from sqlalchemy import insert
from capitulo_01 import *


# ================================================
# INSERINDO DADOS
# ================================================

# # ==>Função insert() como método da tabela 'cookies'
# ins = cookies.insert().values(
#     cookie_name = 'chocolate chip',
#     cookie_recipe_url = 'http://some.aweso.me/cookie/recipe.html',
#     cookie_sku = 'CC01',
#     quantity = '12',
#     unit_cost = '0.50'
# )

# Função genérica insert(), cujo parametro é a tabela onde os dados serão inseridos
ins = insert(cookies).values(
    cookie_name='chocolate chip',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
    cookie_sku='CC01',
    quantity='12',
    unit_cost='0.50'
)
# print(ins)

result = connection.execute(ins)
# print(result.inserted_primary_key)

# Inserção múltipla
inventory_list = [
    {
        'cookie_name': 'oatmeal raisin',
        'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
        'cookie_sku': 'EWW01',
        'quantity': '100',
        'unit_cost': '1.00'
    },
    {
        'cookie_name': 'peanut butter',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
        'cookie_sku': 'PB01',
        'quantity': '24',
        'unit_cost': '0.25'
    },
    {
        'cookie_name': 'dark chocolate chip',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/recipe_dark.html',
        'cookie_sku': 'CC02',
        'quantity': '1',
        'unit_cost': '0.75'
    },
]
result = connection.execute(ins, inventory_list)  # Exibir se dados estão corretos

# ================================================
# REALIZANDO CONSULTAS
# ================================================

# s = cookies.select()    # Usando o método select() do objeto Table
# s = select([cookies])   # Usando a função genérica select()

# result_proxy = connection.execute(s)
# results = result_proxy.fetchall()

# Formas de manipular os dados de resultado
# first_row = results[0]
# first_row[1]
# first_row.cookie_name
# first_row[cookies.c.cookie_namee]

# for record in results:
#     print(f"{record.cookie_name:>22} => {record.keys()!r}")

# print(record)

# from sqlalchemy import desc
# s = select([cookies.c.cookie_name, cookies.c.quantity])
# s = s.order_by(cookies.c.quantity)         # crescente
# # s = s.order_by(desc(cookies.c.quantity))   # decrescente (como função)
# # s = s.order_by(cookies.c.quantity.desc())  # decrescente (como método)
# s = s.limit(2)

# result_proxy = connection.execute(s)
# print([result.cookie_name for result in result_proxy])

# for cookie in result_proxy:
#     print(f"{cookie.quantity:03} - {cookie.cookie_name}")

# from sqlalchemy.sql import func
# USO DA FUNÇÃO SUM()
# s = select([func.sum(cookies.c.quantity)])
# result_proxy = connection.execute(s)
# print(result_proxy.scalar())

# USO DA FUNÇÃO COUNT()
# s = select([func.count(cookies.c.cookie_name).label('inventory_count')])
# result_proxy = connection.execute(s)
# record = result_proxy.first()
# print(record.keys())
# print(record.inventory_count)

# ================================================
# REALIZANDO CONSULTAS COM FILTROS - WHERE
# ================================================
# s = select([cookies]).where(cookies.c.cookie_name == 'chocolate chip')  # Busca exata
# s = select([cookies]).where(cookies.c.cookie_name.like(r'%chocolate%'))  # Busca palavra-chave
# result_proxy = connection.execute(s)
# # print(record.items())
# for record in result_proxy.fetchall():
#     print(record)

# s = select([cookies.c.cookie_name, 'SKU-' + cookies.c.cookie_sku])
# for row in connection.execute(s):
# print(row)


# from sqlalchemy import cast
# s = select([cookies.c.cookie_name,
#         cast((cookies.c.quantity * cookies.c.unit_cost),
#         Numeric(12, 2)).label('inv_cost')])
# for row in connection.execute(s):
#     print(f"{row.cookie_name} - {row.inv_cost}")


# from sqlalchemy import and_, or_, not_
# s = select([cookies]).where(
#     and_(
#         cookies.c.quantity > 23,
#         cookies.c.unit_cost < 0.40
#     )
# )
# for row in connection.execute(s):
#     print(row.cookie_name)


# s = select([cookies]).where(
#     or_(
#         cookies.c.quantity.between(10, 50),
#         cookies.c.cookie_name.contains('chip')
#     )
# )
# for row in connection.execute(s):
#     print(row.cookie_name)

# ================================================
# ATUALIZANDO DADOS - UPDATE
# ================================================
# from sqlalchemy import update

# u = update(cookies).where(cookies.c.cookie_name == 'chocolate chip')
# u = u.values(quantity=(cookies.c.quantity + 120))
# result = connection.execute(u)
# print(result.rowcount)

# s = select([cookies]).where(cookies.c.cookie_name == 'chocolate chip')
# result = connection.execute(s).first()
# for key in result.keys():
#     print(f"{key:>20}: {result[key]}")

# ================================================
# APAGANDO DADOS - DELETE
# ================================================
# from sqlalchemy import delete

# u = delete(cookies).where(cookies.c.cookie_name == 'dark chocolate chip')
# result = connection.execute(u)
# print(result.rowcount)

# s = select([cookies]).where(cookies.c.cookie_name == 'dark chocolate chip')
# result = connection.execute(s).fetchall()
# print(len(result))


# TESTES DE INSERÇÃO
customer_list = [
    {
        'username': 'cookiemon',
        'email_address': 'mon@cookie.com',
        'phone': '111-111-1111',
        'password': 'password'
    },
    {
        'username': 'pieguy',
        'email_address': 'guy@pie.com',
        'phone': '333-333-3333',
        'password': 'password'
    }
]

ins = users.insert()
result = connection.execute(ins, customer_list)
result = connection.execute(select([users]))
# for user in result.fetchall():
#     for k, v in user.items():
#         print(f"{k:>20} -> {v}")
#     print('-' * 50)

ins = insert(orders).values(user_id=1, order_id=1)
result = connection.execute(ins)
# result = connection.execute(select([orders]))
# for order in result.fetchall():
#     print(order.items())


# ins = line_items.insert()
ins = insert(line_items)
order_items = [
    {
        'order_id': 1,
        'cookie_id': 1,
        'quantity': 2,
        'extended_cost': 1.00
    },
    {
        'order_id': 1,
        'cookie_id': 3,
        'quantity': 12,
        'extended_cost': 3.00
    }
]
result = connection.execute(ins, order_items)
# result = connection.execute(select([line_items]))
# for item in result.fetchall():
#     print(item.items())


ins = insert(orders).values(user_id=2, order_id=2)
result = connection.execute(ins)
ins = insert(line_items)
order_items = [
    {
        'order_id': 2,
        'cookie_id': 1,
        'quantity': 24,
        'extended_cost': 12.00
    },
    {
        'order_id': 2,
        'cookie_id': 4,
        'quantity': 6,
        'extended_cost': 6.00
    }
]
result = connection.execute(ins, order_items)
# result = connection.execute(select([orders]))
# for order in result.fetchall():
#     print(order.items())


# ================================================
# JOIN
# ================================================

# columns = [
#     orders.c.order_id, users.c.username, users.c.phone,
#     cookies.c.cookie_name, line_items.c.quantity, line_items.c.extended_cost
# ]
# cookiemon_orders = select(columns)
# cookiemon_orders = cookiemon_orders.select_from(
#     orders.join(users).join(line_items).join(cookies)
# ).where(users.c.username == 'cookiemon')
# # print(cookiemon_orders)    # Exibe a consulta SQL equivamente
# result = connection.execute(cookiemon_orders)
# # for r in result.fetchall():
# #     print(r.items())
#
# columns = [users.c.username, func.count(orders.c.order_id)]
# all_orders = select(columns)
# all_orders = all_orders.select_from(users.outerjoin(orders))
# all_orders = all_orders.group_by(users.c.username)
# result = connection.execute(all_orders)
# print(result.fetchall())

# ================================================
# GROUPING
# ================================================

# columns = [users.c.username, func.count(orders.c.order_id)]
#
# all_orders = select(columns)
# all_orders = all_orders.select_from(users.outerjoin(orders))
# all_orders = all_orders.group_by(users.c.username)
# # print(all_orders)
#
# result = connection.execute(all_orders).fetchall()
# for row in result:
#     print(row)

# ================================================
# CHAINING
# ================================================
#
# def get_orders_by_customer(cust_name):
#     columns = [orders.c.order_id, users.c.username,
#         users.c.phone, cookies.c.cookie_name,
#         line_items.c.quantity, line_items.c.extended_cost
#     ]
#     cust_orders = select(columns)
#     cust_orders = cust_orders.select_from(
#         users.join(orders).join(line_items).join(cookies)
#     )
#     cust_orders = cust_orders.where(users.c.username == cust_name)
#     print(cust_orders)
#     result = connection.execute(cust_orders).fetchall()
#     return result
#
# get_orders_by_customer('cakeeater')

# ================================================
# CHAINING AND IF
# ================================================
#
# def get_orders_by_customer(cust_name, shipped=None, details=False):
#     columns = [orders.c.order_id, users.c.username, users.c.phone]
#     joins = users.join(orders)
#     if details:
#         columns.extend([
#             cookies.c.cookie_name, line_items.c.quantity,
#             line_items.c.extended_cost
#         ])
#         joins = joins.join(line_items).join(cookies)
#     cust_orders = select(columns)
#     cust_orders = cust_orders.where(users.c.username == cust_name)
#     if shipped is not None:
#         cust_orders = cust_orders.where(orders.c.shipped == shipped)
#     result = connection.execute(cust_orders).fetchall()
#     print(cust_orders)
#     return result
#
# get_orders_by_customer('cakeeater', details=True, shipped=True)

# ================================================
# RAW SQL
# ================================================

from sqlalchemy import text
stmt = select([users]).where(text("username='cookiemon'"))
print(connection.execute(stmt).fetchall())
