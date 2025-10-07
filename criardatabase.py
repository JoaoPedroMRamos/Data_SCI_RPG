import sqlite3

#criando conexão
try:
    con=sqlite3.connect('data_sci.db')
    print("Conexão com banco de dados autorizada")
except sqlite3.Error  as e:
    print("Falha ao conectar com o banco de dados:",e)

#criando tabela de Funções
try:
    with con: 
        cur=con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS divisao(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_area TEXT,
            diretor TEXT   
        )""")
        print("Tabela áreas criada com sucesso")
except sqlite3.Error  as e:
    print("Falha ao criar a tabela de funções:",e)
#Criando tabela de agentes
try:
    with con: 
        cur=con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS agentes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            nascimento TEXT,
            patente TEXT,
            area TEXT,   
            contato TEXT,
            registro TEXT,
            status TEXT,
            descricao TEXT,
            foto BLOB,
            FOREIGN KEY (area) REFERENCES divisao(nome_area) ON UPDATE CASCADE ON DELETE CASCADE       
        )""")  
        print("Tabela agentes criada com sucesso")
except sqlite3.Error  as e:
    print("Falha ao criar a tabela de agentes:",e)
#Criando tabela de equipes
try:
    with con: 
        cur=con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS teams(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_equipe TEXT,
            registro REAL,  
            membros TEXT,
            operador TEXT,
            status TEXT,
            FOREIGN KEY (membros) REFERENCES agentes(nome) ON UPDATE CASCADE ON DELETE CASCADE       
        )""")  
        print("Tabela equipes criada com sucesso")
except sqlite3.Error  as e:
    print("Falha ao criar a tabela de equipes:",e)
#Criando tabela de missões
try:
    with con: 
        cur=con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS missoes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT,
            local TEXT,  
            equipe_associada TEXT,
            inicio TEXT,
            fim TEXT,
            status TEXT,
            descricao TEXT,
            FOREIGN KEY (equipe_associada) REFERENCES teams(nome_equipe) ON UPDATE CASCADE ON DELETE CASCADE       
        )""")  
        print("Tabela missões criada com sucesso")
except sqlite3.Error  as e:
    print("Falha ao criar a tabela de missões:",e)



