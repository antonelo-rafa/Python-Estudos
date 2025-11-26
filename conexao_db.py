import mysql.connector
import os

def conexao_banco():
    conexaodb = mysql.connector.connect(
        host ='localhost',
        database='totvs',
        user='root',
        password='',
        port='3306'
        )
    return conexaodb

def insert():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    os.system('clear')
    id = int(input('Id:'))
    nome = input('Nome:')
    idade = int(input('Idade:'))

    query = 'INSERT INTO teste VALUES (%s, %s, %s)'

    cursor.execute(query,(id, nome, idade))

    conexao.commit()
    return 'Registro inserido com sucesso na base'

def select():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    os.system('clear')
    query = 'SELECT * FROM teste'
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado

operacao = int(input(('Escolha a operação 1-Insert ou 2-Select:')))

while operacao not in (1, 2):
    operacao = int(input(('Escolha a operação 1-Insert ou 2-Select:')))

if operacao == 1:
    resultado = insert()
    print (resultado)
else:
    resultado = select()
    print (resultado)





