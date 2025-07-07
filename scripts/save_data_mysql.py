import os
from dotenv import load_dotenv
import mysql.connector
import pandas as pd

load_dotenv()

def connection (hostname, username, passwordinfo):
    cnx = mysql.connector.connect(
        host= hostname,
        user=username,
        password=passwordinfo
    )
    print("mysql successfully connected!")
    return cnx


def tool (cnx):
    cursor = cnx.cursor()
    print("cursor successfully opened!")
    return cursor


def creating_database(cursor, databasename):
    query = f"CREATE DATABASE IF NOT EXISTS {databasename};"
    cursor.execute(query)
    print(f"\nDatabase {databasename} created!")

def show_databases (cursor):
    cursor.execute("SHOW DATABASES;")

    for db in cursor:
        print(db)

def read_csv(path):
    df = pd.read_csv(path)
    return df

def creating_table (cursor, databasename, tablename, columnsinfo):
    query = f"""
        CREATE TABLE IF NOT EXISTS {databasename}.{tablename} (
            {columnsinfo}
        );             
    """
    cursor.execute(query)

def show_tables (cursor, databasename):
    cursor.execute(f"USE {databasename}")
    cursor.execute("SHOW TABLES;")

    for db in cursor:
        print(db)

def insert_values (cursor, cnx, df, databasename, tablename, valuesplace):
    lista_dados = [tuple(row) for _, row in df.iterrows()]
    sql = f"INSERT INTO {databasename}.{tablename} VALUES ({valuesplace});"
    cursor.executemany(sql, lista_dados)
    print(f"\n{cursor.rowcount}, dados inseridos na tabela {tablename}.")
    cnx.commit()

def closing_connection(cursor, cnx):
    cursor.close()
    cnx.close()

if __name__ == "__main__":

    # pegando as variáveis de ambiente
    hostname = os.getenv("HOSTNAME")
    username = os.getenv("USERNAME")
    passwordinfo = os.getenv("PASSWORD")
    
    # estabelecendo a conexão:
    cnx = connection(hostname, username, passwordinfo)
    cursor = tool(cnx)

    # criando base de dados:
    creating_database(cursor,"dbprodutos2") 
    show_databases(cursor)

    # subindo o arquivo para dataframe:
    df = read_csv("/home/jessica/pipeline-python-mongo-mysql/data/tabela_2021_em_diante.csv")

    # criando tabela e informando colunas:
    creating_table(cursor, "dbprodutos2", "tabela_2021_em_diante", 
    "id VARCHAR(100), " \
    "Produto VARCHAR(100), " \
    "Categoria_Produto VARCHAR(100), " \
    "Preco FLOAT(10,2), Frete FLOAT(10,2), " \
    "Data_Compra DATE, Vendedor VARCHAR(100), " \
    "Local_Compra VARCHAR(100), " \
    "Avaliação_Compra INT, " \
    "Tipo_Pagamento VARCHAR(100), " \
    "Qtde_Parcelas INT, " \
    "Latitude FLOAT(10,2), " \
    "Longitude FLOAT(10,2), " \
    "" \
    "PRIMARY KEY (id)"
    )

    show_tables (cursor, "dbprodutos2")

    # subindo os valores:
    
    insert_values (cursor, cnx, df, "dbprodutos2", "tabela_2021_em_diante", "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s")
   
    closing_connection(cursor, cnx)
