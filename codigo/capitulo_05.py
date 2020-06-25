# Exemplos de reflection - Criacao de opbetos SQLAlchemy a partir de um
# banco de dados pre-existent
from pprint import pprint
from sqlalchemy import MetaData, create_engine, Table, select

metadata = MetaData()
engine = create_engine('sqlite:///chinook.db')

tables = []
table_names = [
    'artists', 'media_types', 'genres',
    'playlists', 'albums', 'employees',
    'customers', 'tracks', 'playlist_track',
    'invoices', 'invoice_items',
]

# Table reflections
for tab_name in table_names:
    tables.append(Table(tab_name, metadata, autoload=True, autoload_with=engine))

connection = engine.connect()

for tab in tables:
    s = select([tab]).limit(10)
    print(f"== Tabela: {tab.name:<10} ======================================")
    print(f">>> Colunas: {[col.name for col in tab.columns]} ")
    print('=' * 60)
    for rec in engine.execute(s).fetchall():
        print(rec)
        print('-' * 60)
