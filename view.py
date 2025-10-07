import sqlite3 as lite
import os

try:
    con=lite.connect('data_sci.db')
    print("Conexão com banco de dados autorizada")
except lite.Error  as e:
    print("Falha ao conectar com o banco de dados:",e)

#-----------------------------------------------------------Tabela Áreas-----------------------------------------------------------
#Inserir Áreas (criar)
def criar_areas(i):
    with con:
        cur=con.cursor()
        query="INSERT INTO divisao(nome_area, diretor) VALUES(?,?)"
        cur.execute(query,i)


#Ver areas(selecionar)
def ver_areas():
    lista =[]
    with con:
        cur=con.cursor()
        cur.execute('SELECT * FROM divisao')
        row= cur.fetchall()
        for i in row:
            lista.append(i)
    return lista

def ver_nome_areas():
    lista =[]
    with con:
        cur=con.cursor()
        cur.execute('SELECT nome_area FROM divisao')
        row= cur.fetchall()
        for i in row:
            lista.append(i)
    return lista


#Atualizar areas
def atualizar_areas(i):
    with con:
        cur=con.cursor()
        query="UPDATE divisao SET nome_area=?,diretor=? WHERE id=?"
        cur.execute(query,i)

#Deletar areas
def del_areas(i):
    with con:
        cur=con.cursor()
        query="DELETE FROM divisao WHERE id=?"
        cur.execute(query,i)
#-----------------------------------------------------------Tabela Agentes-----------------------------------------------------------
def criar_agentes(i):
    with con:
        cur=con.cursor()
        query="INSERT INTO agentes(nome,nascimento,patente,area,contato,registro,status,descricao,foto) VALUES(?,?,?,?,?,?,?,?,?)"
        cur.execute(query,i)


#Ver areas(selecionar)
def ver_agentes():
    lista =[]
    with con:
        cur=con.cursor()
        cur.execute('SELECT id,nome,area,patente,registro,status FROM agentes')
        row= cur.fetchall()
        for i in row:
            lista.append(i)
    return lista

def ver_agentes_completo():
    lista =[]
    with con:
        cur=con.cursor()
        cur.execute('SELECT * FROM agentes')
        row= cur.fetchall()
        for i in row:
            lista.append(i)
    return lista

#Atualizar agentes
def att_agentes(i):
    with con:
        cur=con.cursor()
        query="UPDATE agentes SET nome=?,nascimento=?, patente=?,area=?,contato=?,registro=?,status=?,descricao=?,foto=? WHERE id=?"
        cur.execute(query,i)

#Deletar agentes
def del_agentes(i):
    with con:
        cur=con.cursor()
        query="DELETE FROM agentes WHERE id=?"
        cur.execute(query,i)

def convert_pic(i):
    with open(i,'rb')as file:
        foto= file.read()
    return foto






#-----------------------------------------------------------Tabela Equipes-----------------------------------------------------------
def criar_equipes(i):
    with con:
        cur=con.cursor()
        query="INSERT INTO teams(nome_equipe,registro,membros,operador,status) VALUES(?,?,?,?,?)"
        cur.execute(query,i)


#Ver areas(selecionar)
def ver_equipes():
    lista =[]
    with con:
        cur=con.cursor()
        cur.execute('SELECT * FROM teams')
        row= cur.fetchall()
        for i in row:
            lista.append(i)
    return lista

def ver_nome_equipes():
    lista =[]
    with con:
        cur=con.cursor()
        cur.execute('SELECT nome_equipe FROM teams')
        row= cur.fetchall()
        for i in row:
            lista.append(i)
    return lista


#Atualizar agentes
def att_equipes(i):
    with con:
        cur=con.cursor()
        query="UPDATE teams SET nome_equipe=?,registro=?, membros=?,operador=?,status=? WHERE id=?"
        cur.execute(query,i)

#Deletar agentes
def del_equipes(i):
    with con:
        cur=con.cursor()
        query="DELETE FROM teams WHERE id=?"
        cur.execute(query,i)
#-----------------------------------------------------------Tabela Missões-----------------------------------------------------------
def criar_missao(i):
    with con:
        cur=con.cursor()
        query="INSERT INTO missoes(code,local,equipe_associada,inicio,fim,status,descricao) VALUES(?,?,?,?,?,?,?)"
        cur.execute(query,i)


#Ver areas(selecionar)
def ver_missao():
    lista =[]
    with con:
        cur=con.cursor()
        cur.execute('SELECT * FROM missoes')
        row= cur.fetchall()
        for i in row:
            lista.append(i)
    return lista


#Atualizar agentes
def att_missao(i):
    with con:
        cur=con.cursor()
        query="UPDATE missoes SET code=?,local=?,equipe_associada=?,inicio=?,fim=?,status=?,descricao=? WHERE id=?"
        cur.execute(query,i)

#Deletar agentes
def del_missao(i):
    with con:
        cur=con.cursor()
        query="DELETE FROM missoes WHERE id=?"
        cur.execute(query,i)