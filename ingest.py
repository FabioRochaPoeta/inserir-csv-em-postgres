import pandas as pd
import os
from tqdm import tqdm
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from decouple import config

# HOST     = config('HOST')
# DATABASE = config('DATABASE')
# USER     = config('USER')
# PASSWORD = config('PASSWORD')
# PORT     = config('PORT')


# string_conexao = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
string_conexao = 'postgresql://postgres:postgres@localhost:5432/olist'
conn_olist     = create_engine(string_conexao)

if not database_exists(conn_olist.url):
    create_database(conn_olist.url)
    
files = os.listdir('data')
for file in tqdm(files):
    if 'olist' in file:
        df     = pd.read_csv(f'data/{file}')
        tabela = file.replace('olist_','').replace('_dataset.csv', '')
        df.to_sql(tabela, conn_olist, if_exists='replace', index=False)
