import mysql.connector
from mysql.connector import errorcode

print('Conectando...')
connector = None
try:
    connector = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='K21h3fI5X!!'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(err)

# criando o banco para sermos felizes
cursor = connector.cursor()

cursor.execute("DROP DATABASE IF EXISTS library;")

cursor.execute("CREATE DATABASE library;")

cursor.execute("USE library;")

# criando tabelas
TABLES = {}
TABLES['Books'] = ('''
    CREATE TABLE books (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    author varchar(50) NOT NULL,
    category varchar(50) NOT NULL,
    PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print('Criando tabela {}:'.format(tabela_nome), end=' ')
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Já existe')
        else:
            print(err.msg)
    else:
        print('OK')

# inserindo livros
books_sql = 'INSERT INTO books (name, author, category) VALUES (%s, %s, %s)'
books = [
    ('Duna', 'Frank Hebert', 'Ficção Científica'),
    ('O Chamado de Cthulhu', 'H.P. Lovecraft', 'Ficção Científica'),
    ('Elantris', 'Brandon Sanderson', 'Ficção Científica'),
    ('Crepúsculo', 'Stephenie Meyer', 'Romance')
]
cursor.executemany(books_sql, books)

cursor.execute('select * from library.books')
print(' ------------- Livros  ------------- ')
for books in cursor.fetchall():
    print(books[1])

# commitando se não nada tem efeito
connector.commit()

cursor.close()
connector.close()
