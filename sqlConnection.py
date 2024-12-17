import mysql.connector

db_config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "TiAGO.2006",
    "database": "lista"
}

def connect_db():
    try:
        conexao = mysql.connector.connect(**db_config)
        return conexao
    except mysql.connector.Error as error:
        print(f"Erro ao conectar ao banco de dados: {error}")
        return None

def select(query, params=None):
    conexao = connect_db()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(query, params)
            resultados = cursor.fetchall()
            return resultados
        except mysql.connector.Error as error:
            print(f"Erro ao executar SELECT: {error}")
        finally:
            cursor.close()
            conexao.close()

def insert(query, params):
    conexao = connect_db()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(query, params)
            conexao.commit()
            print("Inserção realizada com sucesso!")
        except mysql.connector.Error as error:
            print(f"Erro ao executar INSERT: {error}")
        finally:
            cursor.close()
            conexao.close()

def update(query, params):
    conexao = connect_db()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(query, params)
            conexao.commit()
            print("Atualização realizada com sucesso!")
        except mysql.connector.Error as error:
            print(f"Erro ao executar UPDATE: {error}")
        finally:
            cursor.close()
            conexao.close()

def delete(query, params):
    conexao = connect_db()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(query, params)
            conexao.commit()
            print("Remoção realizada com sucesso!")
        except mysql.connector.Error as error:
            print(f"Erro ao executar DELETE: {error}")
        finally:
            cursor.close()
            conexao.close()