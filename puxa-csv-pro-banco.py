import sqlite3
import pandas as pd
from sqlalchemy import create_engine

# roteiro de inicialização
# criar readme.md
# !pip freeze > requirements.txt
# criar .gitignore e .env

tabela1 = 'data/olist_customers_dataset.csv'
tabela2 = 'data/olist_geolocation_dataset.csv'
tabela3 = 'data/olist_order_items_dataset.csv'
tabela4 = 'data/olist_order_payments_dataset.csv'
tabela5 = 'data/olist_order_reviews_dataset.csv'
tabela6 = 'data/olist_orders_dataset.csv'
tabela7 = 'data/olist_products_dataset.csv'
tabela8 = 'data/olist_sellers_dataset.csv'
tabela9 = 'data/product_category_name_translation.csv'

string_conexao = 'postgresql://postgres:postgres@localhost:5432/olist'
conn = create_engine(string_conexao)

# for N in range (1,10): - deu erro
#  tabelaN = (f'tabela{N}')

df = pd.read_csv(tabela1)

try:
    df.to_sql('tabela1', conn, if_exists= 'replace', index= False)

except Exception as e:
    print("Sorry, some error has occurred!", e)

finally:
    conn.dispose()


df = pd.read_csv(tabela2)

try:
    df.to_sql('tabela2', conn, if_exists= 'replace', index= False)

except Exception as e:
    print("Sorry, some error has occurred!", e)

finally:
    conn.dispose()


df = pd.read_csv(tabela3)

try:
    df.to_sql('tabela3', conn, if_exists= 'replace', index= False)

except Exception as e:
    print("Sorry, some error has occurred!", e)

finally:
    conn.dispose()


df = pd.read_csv(tabela4)

try:
    df.to_sql('tabela4', conn, if_exists= 'replace', index= False)

except Exception as e:
    print("Sorry, some error has occurred!", e)

finally:
    conn.dispose()


df = pd.read_csv(tabela5)

try:
    df.to_sql('tabela5', conn, if_exists= 'replace', index= False)

except Exception as e:
    print("Sorry, some error has occurred!", e)

finally:
    conn.dispose()


df = pd.read_csv(tabela6)

try:
    df.to_sql('tabela6', conn, if_exists= 'replace', index= False)

except Exception as e:
    print("Sorry, some error has occurred!", e)

finally:
    conn.dispose()


df = pd.read_csv(tabela7)

try:
    df.to_sql('tabela7', conn, if_exists= 'replace', index= False)

except Exception as e:
    print("Sorry, some error has occurred!", e)

finally:
    conn.dispose()


df = pd.read_csv(tabela8)

try:
    df.to_sql('tabela8', conn, if_exists= 'replace', index= False)

except Exception as e:
    print("Sorry, some error has occurred!", e)

finally:
    conn.dispose()


df = pd.read_csv(tabela9)

try:
    df.to_sql('tabela9', conn, if_exists= 'replace', index= False)

except Exception as e:
    print("Sorry, some error has occurred!", e)

finally:
    conn.dispose()
