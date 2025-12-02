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

    os.system('cls')
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
    os.system('cls')
    query = 'SELECT * FROM teste'
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado

def select_especifico():
    conexao=conexao_banco()
    cursor = conexao.cursor()

    resultado = select()
    id_valido = []
    condicao = int(input('Digite qual id quer pesquisar:'))

    for x in resultado:
        id_valido.append(x[0])
    
    while condicao not in id_valido:
        condicao = int(input('Não existe esse ID na base de dados, digite outro ID:'))
    
    query = 'SELECT * FROM teste WHERE id = %s'

    condicao = (condicao,)
    cursor.execute(query, (condicao))

    resultado = cursor.fetchall()
    return resultado

def delete():
    conexao = conexao_banco()
    cursor = conexao.cursor()

    os.system('cls')
    opcoes = select()
    print(opcoes)
    condicao = int(input('Selecione o ID de quem quer apagar o Registro:'))

    lista = []

    for x in opcoes:
        lista.append(x[0])
        
    while condicao not in lista:
        condicao = int(input('Valor invalido, selecione o ID de quem quer apagar o Registro:'))
    condicao = (condicao, )
    query = 'DELETE FROM teste WHERE ID = %s'
    cursor.execute(query, condicao)
    conexao.commit()
    os.system('cls')
    print('Valor deletado com sucesso')

    return opcoes


    

os.system('cls')
print("VOCÊ ESTA CONECTADO AO BANCO DE DADOS TOTVS \n")
print("1 - Select")
print('2 - Select com condição')
print("3 - Insert")
print("4 - Update")
print("5 - Delete")
print("0 - Desconectar do banco de dados\n")
operacao = int(input("Digite a operação que deseja executar:"))


while operacao not in(0, 1, 2, 3, 4, 5):
    operacao = int(input("Operacao invalida, digite a operação que deseja executar:"))

if operacao == 0:
    os.system('cls')
    print('Desconectado com sucesso')

elif operacao == 1:
    resultado = select()
    print(resultado)

elif operacao == 2:
    resultado = select_especifico()
    print(resultado)

elif operacao == 3:
    resultado = insert()
    print(resultado)

elif operacao == 5:
    resultado = delete()
    print(resultado) 


delete()
