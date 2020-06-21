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
from sqlalchemy import insert
ins = insert(cookies).values(
    cookie_name = 'chocolate chip',
    cookie_recipe_url = 'http://some.aweso.me/cookie/recipe.html',
    cookie_sku = 'CC01',
    quantity = '12',
    unit_cost = '0.50'
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
from sqlalchemy.sql import select

# s = cookies.select()    # Usando o método select() do objeto Table
# s = select([cookies])   # Usando a função genérica select()

# print(s)e

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

from sqlalchemy.sql import func
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
# REALIZANDO CONSULTAS COM FILTROS
# ================================================
# s = select([cookies]).where(cookies.c.cookie_name == 'chocolate chip')  # Busca exata
s = select([cookies]).where(cookies.c.cookie_name.like(r'%chocolate%'))  # Busca palavra-chave
result_proxy = connection.execute(s)
# print(record.items())
for record in result_proxy.fetchall():
    print(record)





