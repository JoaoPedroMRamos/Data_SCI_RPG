from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import  ImageTk, Image
from view import *


cbg="#010601" #Verde Escuro do background
ctx="#13a10e" #Verde dos textos

#Criando janela
janela = Tk()
janela.title("Database SCI 91")
janela.geometry("1280x980")
janela.configure(background=cbg)
janela.resizable(width=False, height=False)

style=Style(janela)
style.theme_use("default")

#Criando frames
frame_version = Frame(janela,width=650, height=15,bg=cbg)
frame_version.grid(row=0, column=0, pady=0, padx=10, sticky=NSEW)

frame_title = Frame(janela, width=350, height=75, bg=cbg)
frame_title.grid(row=1, column=0, pady=5, padx=460, sticky=NSEW)

separator1 = Frame(janela,width=1280, height=2,bg=ctx)
separator1.grid(row =2, column=0, pady=0, padx=0, sticky=NSEW)

frame_adicionar= Frame(janela, width=1280,height=65, bg=cbg )
frame_adicionar.grid(row =3, column=0, pady=0, padx=0, sticky=NSEW)

separator2 = Frame(janela,width=1280, height=2,bg=ctx)
separator2.grid(row =4, column=0, pady=0, padx=0, sticky=NSEW)

frame_deco = Frame(janela, width=400, height=550,bg=cbg)
frame_deco.grid(row=5, column=0,pady=0,padx=10, sticky=NSEW)

separator3 = Frame(janela,width=1, height=550,bg=ctx)
separator3.grid(row =5, column=0, pady=0, padx=410, sticky=NSEW)


frame_info = Frame(janela, width=870, height=550,bg=cbg)
frame_info.grid(row=5, column=0,pady=0,padx=411, sticky=NSEW)

separator4 = Frame(janela,width=1280, height=1,bg=ctx)
separator4.grid(row =6, column=0, pady=0, padx=0, sticky=NSEW)

frame_tabela = Frame(janela, width=1270, height=267, bg=cbg)
frame_tabela.grid(row=7, column=0, pady=0, padx=10, sticky=NSEW)

#Trabalhando no frame titulo-----------------------------------------------------
app_version=Label(frame_version, text="V 1.3.21", width=350, compound=CENTER, anchor=NW, font=('{Lucida console} 10'),bg=cbg,fg=ctx)
app_version.place(x=0,y=0)
app_title=Label(frame_title, text="Database S.C.I.91", width=350, compound=CENTER, anchor=NW, font=('{Lucida console} 25'),bg=cbg,fg=ctx)
app_title.place(x=0,y=0)




agnt_string=''
nome_save='*'
nascimento_save='*'
patente_save='*'
divisao_save='*'
contato_save='*'
registro_save='*'
status_save='*'
descrip_save='*'


def mostrar_divisoes():
    app_nome= Label(frame_tabela,text='Divisões',height=1,pady=0,padx=0,relief='flat',anchor=NW, font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    app_nome.grid(row=0,column=0,padx=0,pady=10,sticky=NSEW)

    list_header=['id','Nome','Diretor']

    df_list=ver_areas()

    global tree_divisao

    style=ttk.Style()
    style.theme_use('clam')
    style.configure('Treeview',
            background_color='#010601',
            foreground_color='#13a10e',
            fieldbackground='#010601'
                    )
    style.map('Treeview',
            background=[('selected','#13a10e')],
            foreground=[('selected','#010601')]
              )
    style.configure('Treeview.Heading',
                   background='#010601', 
                   foreground='#13a10e',
                   relief='flat'
                        )


    tree_divisao=ttk.Treeview(frame_tabela,selectmode='extended',columns=list_header, show='headings')
    vsb=ttk.Scrollbar(frame_tabela, orient='vertical',command=tree_divisao.yview)
    hsb=ttk.Scrollbar(frame_tabela, orient='horizontal',command=tree_divisao.xview)
    
    tree_divisao.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_divisao.grid(column=0,row=1,sticky=NSEW)
    vsb.grid(column=1,row=1,sticky=NS)
    hsb.grid(column=0,row=2,sticky=EW)
    frame_tabela.grid_rowconfigure(0,weight=12)

    hd=['nw','nw','nw']
    h=[20,370,850]
    n=0

    for col in list_header:
        tree_divisao.heading(col, text=col.title(),anchor=NW)
        tree_divisao.column(col,width=h[n],anchor=hd[n])
        n=n+1
    for item in df_list:
        tree_divisao.insert('','end',values=item)

def mostrar_agentes():
    app_nome= Label(frame_tabela,text='Agentes',height=1,pady=0,padx=0,relief='flat',anchor=NW, font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    app_nome.grid(row=0,column=0,padx=0,pady=10,sticky=NSEW)

    style=ttk.Style()
    style.theme_use('clam')
    style.configure('Treeview',
            background_color='#010601',
            foreground_color='#13a10e',
            fieldbackground='#010601'
                    )
    style.map('Treeview',
            background=[('selected','#13a10e')],
            foreground=[('selected','#010601')]
              )
    style.configure('Treeview.Heading',
                   background='#010601', 
                   foreground='#13a10e',
                   relief='flat'
                        )
    
    list_header=['id','Nome','Divisão','Patente','Registro','Status']

    df_list=ver_agentes()

    global tree_agentes

    style=ttk.Style()
    style.theme_use('clam')
    style.configure('Treeview',
            background_color='#010601',
            foreground_color='#13a10e',
            fieldbackground='#010601'
                    )
    style.map('Treeview',
            background=[('selected','#13a10e')],
            foreground=[('selected','#010601')]
              )
    style.configure('Treeview.Heading',
                   background='#13a10e', 
                   foreground='#010601',
                   relief='flat'
                        )


    tree_agentes=ttk.Treeview(frame_tabela,selectmode='extended',columns=list_header, show='headings')
    vsb=ttk.Scrollbar(frame_tabela, orient='vertical',command=tree_agentes.yview)
    hsb=ttk.Scrollbar(frame_tabela, orient='horizontal',command=tree_agentes.xview)
    
    tree_agentes.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_agentes.grid(column=0,row=1,sticky=NSEW)
    vsb.grid(column=1,row=1,sticky=NS)
    hsb.grid(column=0,row=2,sticky=EW)
    frame_tabela.grid_rowconfigure(0,weight=12)

    hd=['nw','nw','nw','nw','nw','nw']
    h=[40,480,100,80,460,80]
    n=0

    for col in list_header:
        tree_agentes.heading(col, text=col.title(),anchor=NW)
        tree_agentes.column(col,width=h[n],anchor=hd[n])
        n=n+1
    
    for item in df_list:
            tree_agentes.insert('','end',values=item)
            
def mostrar_agentes_completo():
    app_nome= Label(frame_tabela,text='Agentes',height=1,pady=0,padx=0,relief='flat',anchor=NW, font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    app_nome.grid(row=0,column=0,padx=0,pady=10,sticky=NSEW)

    style=ttk.Style()
    style.theme_use('clam')
    style.configure('Treeview',
            background_color='#010601',
            foreground_color='#13a10e',
            fieldbackground='#010601'
                    )
    style.map('Treeview',
            background=[('selected','#13a10e')],
            foreground=[('selected','#010601')]
              )
    style.configure('Treeview.Heading',
                   background='#010601', 
                   foreground='#13a10e',
                   relief='flat'
                        )
    
    list_header_c=['id','Nome','Nascimento','Patente','Divisão','Contato','Registro','Status']

    df_list_c=ver_agentes_completo()

    global tree_agentes_completo

    tree_agentes_completo=ttk.Treeview(frame_tabela,selectmode='extended',columns=list_header_c, show='headings')
    vsb=ttk.Scrollbar(frame_tabela, orient='vertical',command=tree_agentes_completo.yview)
    hsb=ttk.Scrollbar(frame_tabela, orient='horizontal',command=tree_agentes_completo.xview)
    
    tree_agentes_completo.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_agentes_completo.grid(column=0,row=1,sticky=NSEW)
    vsb.grid(column=1,row=1,sticky=NS)
    hsb.grid(column=0,row=2,sticky=EW)
    frame_tabela.grid_rowconfigure(0,weight=12)

    hd=['nw','nw','nw','nw','nw','nw','nw','nw']
    h=[40,280,90,150,150,100,280,150]
    n=0

    for col in list_header_c:
        tree_agentes_completo.heading(col, text=col.title(),anchor=NW)
        tree_agentes_completo.column(col,width=h[n],anchor=hd[n])
        n=n+1
    
    for item in df_list_c:
            tree_agentes_completo.insert('','end',values=item)
def mostrar_equipes():
    app_nome= Label(frame_tabela,text='Equipes',height=1,pady=0,padx=0,relief='flat',anchor=NW, font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    app_nome.grid(row=0,column=0,padx=0,pady=10,sticky=NSEW)

    style=ttk.Style()
    style.theme_use('clam')
    style.configure('Treeview',
            background_color='#010601',
            foreground_color='#13a10e',
            fieldbackground='#010601'
                    )
    style.map('Treeview',
            background=[('selected','#13a10e')],
            foreground=[('selected','#010601')]
              )
    style.configure('Treeview.Heading',
                   background='#010601', 
                   foreground='#13a10e',
                   relief='flat'
                        )
    
    list_header=['id','Nome','Registro','Membros','Operador','Status']

    df_list_equipe=ver_equipes()

    global tree_equipes

    tree_equipes=ttk.Treeview(frame_tabela,selectmode='extended',columns=list_header, show='headings')
    vsb=ttk.Scrollbar(frame_tabela, orient='vertical',command=tree_equipes.yview)
    hsb=ttk.Scrollbar(frame_tabela, orient='horizontal',command=tree_equipes.xview)
    
    tree_equipes.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_equipes.grid(column=0,row=1,sticky=NSEW)
    vsb.grid(column=1,row=1,sticky=NS)
    hsb.grid(column=0,row=2,sticky=EW)
    frame_tabela.grid_rowconfigure(0,weight=12)
    hd=['nw','nw','nw','nw','nw','nw']
    h=[40,350,110,410,250,80]
    n=0

    for col in list_header:
        tree_equipes.heading(col, text=col.title(),anchor=NW)
        tree_equipes.column(col,width=h[n],anchor=hd[n])
        n=n+1
    for item in df_list_equipe:
        tree_equipes.insert('','end',values=item)

def mostrar_missoes():
    app_nome= Label(frame_tabela,text='Missões',height=1,pady=0,padx=0,relief='flat',anchor=NW, font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    app_nome.grid(row=0,column=0,padx=0,pady=10,sticky=NSEW)


    list_header=['id','Código','Local','Equipe','Início','Fim','Status']

    df_list_equipe=ver_missao()

    global tree_missoes

    style=ttk.Style()
    style.theme_use('clam')
    style.configure('Treeview',
            background_color='#010601',
            foreground_color='#13a10e',
            fieldbackground='#010601'
                    )
    style.map('Treeview',
            background=[('selected','#13a10e')],
            foreground=[('selected','#010601')]
              )
    style.configure('Treeview.Heading',
                   background='#010601', 
                   foreground='#13a10e',
                   relief='flat'
                        )


    tree_missoes=ttk.Treeview(frame_tabela,selectmode='extended',columns=list_header, show='headings')
    vsb=ttk.Scrollbar(frame_tabela, orient='vertical',command=tree_missoes.yview)
    hsb=ttk.Scrollbar(frame_tabela, orient='horizontal',command=tree_missoes.xview)
    
    tree_missoes.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_missoes.grid(column=0,row=1,sticky=NSEW)
    vsb.grid(column=1,row=1,sticky=NS)
    hsb.grid(column=0,row=2,sticky=EW)
    frame_tabela.grid_rowconfigure(0,weight=12)

    hd=['nw','nw','nw','nw','nw','nw','nw']
    h=[40,100,450,310,120,120,100]
    n=0

    for col in list_header:
        tree_missoes.heading(col, text=col.title(),anchor=NW)
        tree_missoes.column(col,width=h[n],anchor=hd[n])
        n=n+1
    for item in df_list_equipe:
        tree_missoes.insert('','end',values=item)

#Cadastro de Agente
def agentes():
    def mudar_tabela():
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        mostrar_agentes()
        botao_mudar_tabela.destroy()
        botao_voltar_tabela=Button(frame_info,anchor=CENTER,command=voltar_tabela,text='Voltar Tabela'.upper(), overrelief=RIDGE,relief=RAISED,font=('{Lucida console} 10'),bg=ctx,fg=cbg)
        botao_voltar_tabela.place(x=700,y=480)
        
    def voltar_tabela():
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        mostrar_agentes_completo()
        botao_voltar_tabela.destroy()
        botao_mudar_tabela=Button(frame_info,anchor=CENTER,command=mudar_tabela,text='Mudar  Tabela'.upper(), overrelief=RIDGE,relief=RAISED,font=('{Lucida console} 10'),bg=ctx,fg=cbg)
        botao_mudar_tabela.place(x=700,y=480)

    def add_agente():
        def confirmar_add():
            descricao_agente=e_descrip.get('1.0',END)
            lista_agente=[nome_agente,nascimento_agente,patente_agente,divisao_agente,contato_agente,registro_agente,stats_agente,descricao_agente,imagem_agente]
            for i in lista_agente:
                if i=='':
                    messagebox.showerror('Error','Complete todos os Campos')
                    return
            criar_agentes(lista_agente)
            messagebox.showinfo('Concluído','Dados adicionados com sucesso')
            control('agente')

        nome_agente=e_nome.get()
        nascimento_agente=e_nascimento.get()
        patente_agente=c_pat_agente.get()
        divisao_agente=c_divis_agente.get()
        contato_agente=e_contato.get()
        registro_agente=e_registro.get()
        stats_agente=c_stats_agente.get()
        imagem_agente=agnt_string

        for widget in frame_info.winfo_children():
            widget.destroy()
        
        l_descrip=Label(frame_info,anchor=NW,text='Descrição:',font=('{Lucida console} 10'),bg=cbg,fg=ctx)
        l_descrip.place(x=3, y=20)

        e_descrip=Text(frame_info,width=71,height=24,font=('{Lucida console} 15'),bg=ctx,fg=cbg)
        e_descrip.place(x=5,y=60)

        botao_salvaragnt=Button(frame_info,anchor=CENTER,command=confirmar_add,text='Salvar'.upper(),width=9, overrelief=RIDGE,relief=RAISED,font=('{Lucida console} 10'),bg=ctx,fg=cbg)
        botao_salvaragnt.place(x=750,y=20)
        mostrar_agentes_completo()

    def update_agente():
        
        try:
            tree_itens= tree_agentes_completo.focus()
            tree_dicionario_agentes=tree_agentes_completo.item(tree_itens)
            tree_lista=tree_dicionario_agentes['values']
            valor_id_agente=tree_lista[0]
            e_nome.insert(0,tree_lista[1])
            e_nascimento.insert(0,tree_lista[2])
            c_pat_agente.insert(0,tree_lista[3])
            c_divis_agente.insert(0,tree_lista[4])
            e_contato.insert(0,tree_lista[5])
            e_registro.insert(0,tree_lista[6])
            c_stats_agente.insert(0,tree_lista[7])
            
            def update_agnt():
                def confirmar_att():
                    descricao_agente=e_descrip.get('1.0',END)
                    lista_agente=[nome_agente, nascimento_agente, patente_agente,divisao_agente,contato_agente,registro_agente,stats_agente,descricao_agente,agnt_string,valor_id_agente]
                    for i in lista_agente:
                        if i=='':
                            messagebox.showerror('Error','Complete todos os Campos')
                            return
                    att_agentes(lista_agente)
                    messagebox.showinfo('Cocluído','Dados atualizadoss com sucesso')
                    e_descrip.delete(1.0,END)
                    control('agente')
                
                nome_agente=e_nome.get()
                nascimento_agente=e_nascimento.get()
                patente_agente=c_pat_agente.get()
                divisao_agente=c_divis_agente.get()
                contato_agente=e_contato.get()
                registro_agente=e_registro.get()
                stats_agente=c_stats_agente.get()
                escolher_imagem()
    
                for widget in frame_info.winfo_children():
                    widget.destroy()

                l_descrip=Label(frame_info,anchor=NW,text='Descrição:',font=('{Lucida console} 10'),bg=cbg,fg=ctx)
                l_descrip.place(x=3, y=20)

                e_descrip=Text(frame_info,width=71,height=24,font=('{Lucida console} 15'),bg=ctx,fg=cbg)
                e_descrip.place(x=5,y=60)
                e_descrip.insert('1.0',tree_lista[8])

                botao_salvaragnt=Button(frame_info,anchor=CENTER,command=confirmar_att,text='Salvar'.upper(),width=9, overrelief=RIDGE,relief=RAISED,font=('{Lucida console} 10'),bg=ctx,fg=cbg)
                botao_salvaragnt.place(x=750,y=20)
                mostrar_agentes_completo()


            botao_confirmar_divisao=Button(frame_info,anchor=CENTER,command=update_agnt, text='Próxima Página'.upper(),overrelief=RIDGE,relief=RAISED,font=('{Lucida console Bold} 9'),bg=ctx,fg=cbg)
            botao_confirmar_divisao.place(x=403,y=480)
        except IndexError:
            messagebox.showerror('Error','Selecione um dos agentes')

    def detalhes_agente():
        try:
            for widget in frame_info.winfo_children():
                widget.destroy()
            def description():
                for widget in frame_info.winfo_children():
                    widget.destroy()
                l_descrip=Label(frame_info,anchor=NW,text='Descrição:',font=('{Lucida console} 14'),bg=cbg,fg=ctx)
                l_descrip.place(x=3,y=10)
                l_sdescrip=Label(frame_info,anchor=NW,height=24,width=71,text=tree_lista[8],font=('{Lucida console} 14'),bg=cbg,fg=ctx)
                l_sdescrip.place(x=3,y=50)
                prev_pag=Button(frame_info, command=detalhes_agente,anchor=NW, text='<-',font=('{Lucida console} 14'),bg=ctx,fg=cbg)
                prev_pag.place(x=800,y=20)
        
            tree_itens= tree_agentes_completo.focus()
            tree_dicionario_agentes=tree_agentes_completo.item(tree_itens)
            tree_lista=tree_dicionario_agentes['values']

            title_ver=Label(frame_info,anchor=NW,text='Informações de Agente'.upper(),font=('{Lucida console} 25'), bg=cbg, fg=ctx)
            title_ver.place(x=3,y=20)

            nome_completo=tree_lista[1].split()
            primeironome=nome_completo[0]+' '+nome_completo[1]
            nome_completo.pop(0)
            nome_completo.pop(0)
            sobrenome=' '.join(nome_completo)
            l_nome=Label(frame_info,text="Nome:",height=1,anchor=NW,font=('{Lucida console} 14'),bg=cbg,fg=ctx)
            l_nome.place(x=3,y=100)
            l_snome=Label(frame_info,text=primeironome,anchor=NW,font=('{Lucida console} 14'),bg=cbg,fg=ctx)
            l_snome.place(x=3,y=130)
            l_ssobrenome=Label(frame_info,text=sobrenome,anchor=NW,font=('{Lucida console} 14'),bg=cbg,fg=ctx)
            l_ssobrenome.place(x=3,y=150)

            l_nascimento=Label(frame_info,text="Nascimento:",height=1,anchor=NW,font=('{Lucida console} 14'),bg=cbg,fg=ctx)
            l_nascimento.place(x=3,y=200)
            l_snascimento=Label(frame_info,text=tree_lista[2],anchor=NW,font=('{Lucida console} 14'),bg=cbg,fg=ctx)
            l_snascimento.place(x=3,y=230)

            l_contato=Label(frame_info,anchor=NW,text='Contato:',font=('{Lucida console} 14'),bg=cbg,fg=ctx)
            l_contato.place(x=3,y=300)
            l_scontato=Label(frame_info,anchor=NW,text=tree_lista[5],font=('{Lucida console} 14'),bg=cbg,fg=ctx)
            l_scontato.place(x=3,y=330)

            l_patente=Label(frame_info,text="Patente:",height=1,anchor=NW,font=('{Lucida console} 14'),bg=cbg,fg=ctx)
            l_patente.place(x=303,y=100)
            l_spatente=Label(frame_info,text=tree_lista[3],anchor=NW,font=('{Lucida console} 14'),bg=cbg,fg=ctx)
            l_spatente.place(x=303,y=130)

            l_divisao=Label(frame_info,text="Divisão:",height=1,anchor=NW,font=('{Lucida console} 14'),bg=cbg,fg=ctx)
            l_divisao.place(x=303,y=200)
            l_sdivisao=Label(frame_info,text=tree_lista[4],anchor=NW,font=('{Lucida console} 14'),bg=cbg,fg=ctx)
            l_sdivisao.place(x=303,y=230)

            l_registro=Label(frame_info,anchor=NW,text='Registro:',font=('{Lucida console} 14'),bg=cbg,fg=ctx)
            l_registro.place(x=303,y=300)
            l_sregistro=Label(frame_info,anchor=NW,text=tree_lista[6],font=('{Lucida console} 14'),bg=cbg,fg=ctx)
            l_sregistro.place(x=303,y=330)

            l_stats=Label(frame_info,anchor=NW,text='['+tree_lista[7]+']',font=('{Lucida console} 16'),bg=cbg,fg=ctx)
            l_stats.place(x=3,y=430)

            
            global agnt_simg,agnt_fimg,imagem

            imagem=tree_lista[9]
            agnt_simg= Image.open(imagem)
            agnt_simg= agnt_simg.resize((250,250))
            agnt_fimg=ImageTk.PhotoImage(agnt_simg)

            l_agntimg=Label(frame_info, image=agnt_fimg,compound=CENTER,bg=cbg)
            l_agntimg.place(x=553, y=100)

            proxima_pag=Button(frame_info, anchor=NW,command=description, text='->',font=('{Lucida console} 14'),bg=ctx,fg=cbg)
            proxima_pag.place(x=800,y=20)

        except IndexError:
            messagebox.showerror("Error",'Selecione Agente')
            control('agente')
    
    lista_divisao=ver_nome_areas()
    l_nome=Label(frame_info,text="Nome",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_nome.place(x=3,y=0)
    e_nome=Entry(frame_info, width=30, justify=LEFT, relief='solid',font=('{Lucida console} 15'),bg=ctx)
    e_nome.place(x=3,y=20)
    

    l_nascimento=Label(frame_info,text="Nascimento",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_nascimento.place(x=3,y=50)
    e_nascimento=Entry(frame_info, width=11, justify=LEFT, relief='solid',font=('{Lucida console} 15'),bg=ctx)
    e_nascimento.place(x=3,y=70)
    

    l_patente=Label(frame_info,text="Patente",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_patente.place(x=3,y=100)
    patente=['Recruta','Afiliado','Agente','Operador','Diretor']
    pat=[]
    for i in patente:
        pat.append(i)
    c_pat_agente= ttk.Combobox(frame_info,width=20,font=('{Lucida console} 10'))
    c_pat_agente['values']=(pat)
    c_pat_agente.place(x=3,y=120)
    


    l_divisao=Label(frame_info,text="Divisão",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_divisao.place(x=3,y=150)
    divisao=lista_divisao
    divis=[]
    for i in divisao:
        divis.append(i)
    c_divis_agente= ttk.Combobox(frame_info,width=20,font=('{Lucida console} 10'))
    c_divis_agente['values']=(divis)
    c_divis_agente.place(x=3,y=170)
    

    l_contato=Label(frame_info,text="Contato",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_contato.place(x=3,y=200)
    e_contato=Entry(frame_info, width=25, justify=LEFT, relief='solid',font=('{Lucida console} 15'),bg=ctx)
    e_contato.place(x=3,y=220)
    

    l_registro=Label(frame_info,text="Registro",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_registro.place(x=3,y=250)
    e_registro=Entry(frame_info, width=25, justify=LEFT, relief='solid',font=('{Lucida console} 15'),bg=ctx)
    e_registro.place(x=3,y=270)
    

    l_status=Label(frame_info,text="Status",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_status.place(x=3,y=300)
    status=['Ativo','Afastado','Inativo','RIP']
    stats=[]
    for i in status:
        stats.append(i)
    c_stats_agente= ttk.Combobox(frame_info,width=20,font=('{Lucida console} 10'))
    c_stats_agente['values']=(stats)
    c_stats_agente.place(x=3,y=320)
    

    global agnt_img,agnt_string,l_agntimg
    def escolher_imagem():
        global agnt_img,agnt_string,l_agntimg

        agnt_img= fd.askopenfilename()

        agnt_string=agnt_img

        agnt_img= Image.open(agnt_img)
        agnt_img= agnt_img.resize((250,250))
        agnt_img=ImageTk.PhotoImage(agnt_img)
        l_agntimg=Label(frame_info, image=agnt_img, bg=cbg)
        l_agntimg.place(x=465, y=0)

        botao_carregar['text']='Trocar de Foto'.upper()

    botao_carregar= Button(frame_info,command=escolher_imagem,text='Carregar Foto'.upper(), width=20, compound=CENTER,anchor=CENTER,overrelief=RIDGE,relief=RAISED, font=('{Lucida console} 7'))
    botao_carregar.place(x=537, y=260)

    botao_salvaragnt=Button(frame_info,anchor=CENTER,command=add_agente,text='Salvar'.upper(),width=9, overrelief=RIDGE,relief=RAISED,font=('{Lucida console} 10'),bg=ctx,fg=cbg)
    botao_salvaragnt.place(x=3,y=480)

    botao_attagnt=Button(frame_info,anchor=CENTER,command=update_agente,text='Atualizar'.upper(),width=9, overrelief=RIDGE,relief=RAISED,font=('{Lucida console} 10'),bg=ctx,fg=cbg)
    botao_attagnt.place(x=103,y=480)

    botao_veragnt=Button(frame_info,anchor=CENTER,command=detalhes_agente,text='Ver'.upper(),width=9, overrelief=RIDGE,relief=RAISED,font=('{Lucida console} 10'),bg=ctx,fg=cbg)
    botao_veragnt.place(x=203,y=480)

    botao_mudar_tabela=Button(frame_info,anchor=CENTER,command=mudar_tabela,text='Mudar  Tabela'.upper(), overrelief=RIDGE,relief=RAISED,font=('{Lucida console} 10'),bg=ctx,fg=cbg)
    botao_mudar_tabela.place(x=700,y=480)

    botao_voltar_tabela=Button(frame_info,anchor=CENTER,command=voltar_tabela,text='Voltar Tabela'.upper(), overrelief=RIDGE,relief=RAISED,font=('{Lucida console} 10'),bg=ctx,fg=cbg)

def divisao():
    def nova_divisao():
        nome_area=e_nomearea.get()
        diretor=e_nomediretor.get()
        lista_divisao=[nome_area,diretor]
    #Verificação de espaços vazios
        for i in lista_divisao:
            if i=='':
                messagebox.showerror('Error','Preencha todos os campos')
                return
    #inserindo dados no database
        criar_areas(lista_divisao)
    #Confirmando recepção dos dados
        messagebox.showinfo('Cocluído','Dados adicionados com sucesso')
        e_nomearea.delete(0,END)
        e_nomediretor.delete(0,END)
    #mostrando dados na tabela
        mostrar_divisoes()

    def att_divisao():
        try:
            tree_itens= tree_divisao.focus()
            tree_dicionario_divisao=tree_divisao.item(tree_itens)
            tree_lista=tree_dicionario_divisao['values']
            valor_id_divisao=tree_lista[0]
            e_nomearea.insert(0,tree_lista[1])
            e_nomediretor.insert(0,tree_lista[2])
            def update():
                nome_area=e_nomearea.get()
                diretor=e_nomediretor.get()
                lista_divisao_att=[nome_area,diretor,valor_id_divisao]
                #Verificação de espaços vazios
                for i in lista_divisao_att:
                    if i=='':
                     messagebox.showerror('Error','Preencha todos os campos')
                     return
                #inserindo dados no database
                atualizar_areas(lista_divisao_att)
                #Confirmando recepção dos dados
                messagebox.showinfo('Cocluído','Dados atualizados com sucesso')
                e_nomearea.delete(0,END)
                e_nomediretor.delete(0,END)
                #mostrando dados na tabela
                botao_confirmar_divisao.destroy()
                mostrar_divisoes()

            botao_confirmar_divisao=Button(frame_info,anchor=CENTER,command=update, text='Salvar Atualização'.upper(),overrelief=RIDGE,relief=RAISED,font=('{Lucida console Bold} 9'),bg=ctx,fg=cbg)
            botao_confirmar_divisao.place(x=303,y=100)
        except IndexError:
            messagebox.showerror('Error','Selecione uma das divisões')

    def del_divisao():
        try:
            tree_itens= tree_divisao.focus()
            tree_dicionario_divisao=tree_divisao.item(tree_itens)
            tree_lista=tree_dicionario_divisao['values']
            valor_id=[tree_lista[0]]
            e_nomearea.insert(0,tree_lista[1])
            e_nomediretor.insert(0,tree_lista[2])
            def delete():
                del_areas(valor_id)
                messagebox.showinfo('Concluído','Dados excluídos com sucesso')
                e_nomearea.delete(0,END)
                e_nomediretor.delete(0,END)
                botao_del_divis.destroy()
                mostrar_divisoes()
            botao_del_divis=Button(frame_info,anchor=CENTER,command=delete, text='Deletar Divisão'.upper(),overrelief=RIDGE,relief=RAISED,font=('{Lucida console Bold} 9'),bg=ctx,fg=cbg)
            botao_del_divis.place(x=303,y=100)
        except IndexError:
            messagebox.showerror('Error','Selecione uma Divisão')
    
            


    l_nomearea=Label(frame_info,text="Nome",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_nomearea.place(x=3,y=0)
    e_nomearea=Entry(frame_info, width=30, justify=LEFT, relief='solid',font=('{Lucida console} 15'),bg=ctx)
    e_nomearea.place(x=3,y=20)

    l_nomediretor=Label(frame_info,text="Diretor",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_nomediretor.place(x=3,y=50)
    e_nomediretor=Entry(frame_info, width=30, justify=LEFT, relief='solid',font=('{Lucida console} 15'),bg=ctx)
    e_nomediretor.place(x=3,y=70)

    botao_save=Button(frame_info,anchor=CENTER,command=nova_divisao, text='Salvar'.upper(),width=10,overrelief=RIDGE,relief=RAISED,font=('{Lucida console Bold} 9'),bg=ctx,fg=cbg)
    botao_save.place(x=3,y=100)

    botao_cancel=Button(frame_info,anchor=CENTER,command=del_divisao, text='Apagar'.upper(),width=10,overrelief=RIDGE,relief=RAISED,font=('{Lucida console Bold} 9'),bg=ctx,fg=cbg)
    botao_cancel.place(x=103,y=100)

    botao_att=Button(frame_info,anchor=CENTER,command=att_divisao,text='Atualizar'.upper(),width=9, overrelief=RIDGE,relief=RAISED,font=('{Lucida console} 10'),bg=ctx,fg=cbg)
    botao_att.place(x=203,y=100)

def equipes():
    def adicionar_equipes():
        nome_equipe=e_nomeequipe.get()
        registro_equipe=e_registroequipe.get()
        membros=e_membrosequipe.get()
        operador=e_opequipe.get()
        status_equipe=c_statse.get()
        lista_equipe=[nome_equipe,registro_equipe,membros,operador,status_equipe]
        for i in lista_equipe:
            if i=='':
                messagebox.showerror('Error','Preencha todos os campos')
                return
        criar_equipes(lista_equipe)
        messagebox.showinfo('Concluído','Dados adicionados com sucesso')
        e_nomeequipe.delete(0,END)
        e_registroequipe.delete(0,END)
        e_membrosequipe.delete(0,END)
        e_opequipe.delete(0,END)
        c_statse.delete(0,END)
        mostrar_equipes()
    
    def atualizar_equipe():
        try:
            tree_itens=tree_equipes.focus()
            tree_dicionario_equipes=tree_equipes.item(tree_itens)
            tree_lista=tree_dicionario_equipes['values']
            valor_id_equipe=tree_lista[0]
            e_nomeequipe.insert(0,tree_lista[1])
            e_registroequipe.insert(0,tree_lista[2])
            e_membrosequipe.insert(0,tree_lista[3])
            e_opequipe.insert(0,tree_lista[4])
            c_statse.insert(0,tree_lista[5])
            def update_equipe():
                nome_equipe=e_nomeequipe.get()
                registro_equipe=e_registroequipe.get()
                membros=e_membrosequipe.get()
                operador=e_opequipe.get()
                status_equipe=c_statse.get()
                lista_equipe=[nome_equipe,registro_equipe,membros,operador,status_equipe,valor_id_equipe]
                for i in lista_equipe:
                    if i=='':
                        messagebox.showerror('Error','Preencha todos os campos')
                        return
                att_equipes(lista_equipe)
                messagebox.showinfo('Concluído','Dados atualizados com sucesso')
                e_nomeequipe.delete(0,END)
                e_registroequipe.delete(0,END)
                e_membrosequipe.delete(0,END)
                e_opequipe.delete(0,END)
                c_statse.delete(0,END)
                botao_confirmar_equipe.destroy()
                mostrar_equipes()
            botao_confirmar_equipe=Button(frame_info,command=update_equipe,text='Confirmar Atualização'.upper(),overrelief=RIDGE,relief=RAISED,font=('{Lucida console} 9'),bg=ctx,fg=cbg)
            botao_confirmar_equipe.place(x=203,y=200)
        except IndexError:
            messagebox.showerror('Error','Selecione uma das equipes')

    l_nomeequipe=Label(frame_info,text="Nome da Equipe",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_nomeequipe.place(x=3,y=0)
    e_nomeequipe=Entry(frame_info, width=20, justify=LEFT, relief='solid',font=('{Lucida console} 15'),bg=ctx)
    e_nomeequipe.place(x=3,y=20)

    l_resgistroequipe=Label(frame_info,text="Registro",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_resgistroequipe.place(x=3,y=50)
    e_registroequipe=Entry(frame_info, width=20, justify=LEFT, relief='solid',font=('{Lucida console} 15'),bg=ctx)
    e_registroequipe.place(x=3,y=70)

    l_membrosequipe=Label(frame_info,text="Membros",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_membrosequipe.place(x=3,y=100)
    e_membrosequipe=Entry(frame_info, width=30, justify=LEFT, relief='solid',font=('{Lucida console} 15'),bg=ctx)
    e_membrosequipe.place(x=3,y=120)

    l_opequipe=Label(frame_info,text="Operador",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_opequipe.place(x=3,y=150)
    e_opequipe=Entry(frame_info, width=30, justify=LEFT, relief='solid',font=('{Lucida console} 15'),bg=ctx)
    e_opequipe.place(x=3,y=170)

    l_statusequipe=Label(frame_info,text="Status",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_statusequipe.place(x=400,y=0)
    statuse=['Ativa','Inativa','Dissolvida']
    statse=[]
    for i in statuse:
        statse.append(i)
    c_statse= ttk.Combobox(frame_info,width=20,font=('{Lucida console} 10'))
    c_statse['values']=(statse)
    c_statse.place(x=400,y=20)

    botao_save=Button(frame_info,anchor=CENTER,command=adicionar_equipes, text='Salvar'.upper(),width=10,overrelief=RIDGE,relief=RAISED,font=('{Lucida console Bold} 9'),bg=ctx,fg=cbg)
    botao_save.place(x=3,y=200)

    botao_att=Button(frame_info,anchor=CENTER,command=atualizar_equipe, text='Atualizar'.upper(),width=10,overrelief=RIDGE,relief=RAISED,font=('{Lucida console Bold} 9'),bg=ctx,fg=cbg)
    botao_att.place(x=103,y=200)

def missoes():

    def add_missao():
        codigo_missao=e_code.get()
        local_missao=e_local.get()
        inicio_missao=e_inicio.get()
        fim_missao=e_fim.get()
        descricao_missao=e_descricao.get(1.0,END)
        equipe_missao=c_equipe.get()
        status_missao=c_statusm.get()
        lista_missao=[codigo_missao,local_missao,equipe_missao,inicio_missao,fim_missao,status_missao,descricao_missao]
        for i in lista_missao:
            if i=='':
                messagebox.showerror('Error','Complete todos os campos')
                return
        criar_missao(lista_missao)
        messagebox.showinfo('Concluído','Dados adicionados com sucesso')
        e_code.delete(0,END)
        e_local.delete(0,END)
        e_inicio.delete(0,END)
        e_fim.delete(0,END)
        e_descricao.delete(1.0,END)
        c_equipe.delete(0,END)
        c_statusm.delete(0,END)
        mostrar_missoes()

    def atualizar_missao():
        try:
            tree_itens=tree_missoes.focus()
            tree_dicionario_missoes=tree_missoes.item(tree_itens)
            tree_lista=tree_dicionario_missoes['values']
            valor_id_missoes=tree_lista[0]
            e_code.insert(0,tree_lista[1])
            e_local.insert(0,tree_lista[2])
            c_equipe.insert(0,tree_lista[3])
            e_inicio.insert(0,tree_lista[4])
            e_fim.insert(0,tree_lista[5])
            c_statusm.insert(0,tree_lista[6])
            e_descricao.insert(1.0,tree_lista[7])
            
            def confirmar_att():
                codigo_missao=e_code.get()
                local_missao=e_local.get()
                inicio_missao=e_inicio.get()
                fim_missao=e_fim.get()
                descricao_missao=e_descricao.get(1.0,END)
                equipe_missao=c_equipe.get()
                status_missao=c_statusm.get()
                lista_missao=[codigo_missao,local_missao,equipe_missao,inicio_missao,fim_missao,status_missao,descricao_missao,valor_id_missoes]
                for i in lista_missao:
                    if i=='':
                        messagebox.showerror('Error','Complete todos os campos')
                        return
                att_missao(lista_missao)
                messagebox.showinfo('Concluído','Dados atualizados com sucesso')
                e_code.delete(0,END)
                e_local.delete(0,END)
                e_inicio.delete(0,END)
                e_fim.delete(0,END)
                e_descricao.delete(1.0,END)
                c_equipe.delete(0,END)
                c_statusm.delete(0,END)
                botao_salvar_mudancas.destroy()
                mostrar_missoes()
            botao_salvar_mudancas=Button(frame_info,command=confirmar_att ,text='Confirmar Atualização'.upper(),font=('{Lucida console} 9'),bg=ctx,fg=cbg,overrelief=RIDGE,relief=RAISED)
            botao_salvar_mudancas.place(x=700,y=140)
        except IndexError:
            messagebox.showerror('Error','Selecione uma missão')
            
        

    def detalhes_missao():
        try:
            tree_itens=tree_missoes.focus()
            tree_dicionario_missoes=tree_missoes.item(tree_itens)
            tree_listam=tree_dicionario_missoes['values']


            for widget in frame_info.winfo_children():
                widget.destroy()
            l_code=Label(frame_info,text="Código",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
            l_code.place(x=3,y=0)
            e_scode=Label(frame_info,text=tree_listam[1],font=('{Lucida console} 15'),bg=cbg,fg=ctx)
            e_scode.place(x=3,y=20)
            
            l_local=Label(frame_info,text="Local",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
            l_local.place(x=3,y=50)
            e_slocal=Label(frame_info,text=tree_listam[2],font=('{Lucida console} 15'),bg=cbg,fg=ctx)
            e_slocal.place(x=3,y=70)

            l_inicio=Label(frame_info,text="Data de Expedição",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
            l_inicio.place(x=3,y=100)
            e_inicio=Label(frame_info, text=tree_listam[4],font=('{Lucida console} 15'),bg=cbg,fg=ctx)
            e_inicio.place(x=3,y=120)

            l_equipe=Label(frame_info, text='Equipe Associada',height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
            l_equipe.place(x=400,y=0)
            e_equipe=Label(frame_info,text=tree_listam[3],font=('{Lucida console} 15'),bg=cbg,fg=ctx)
            e_equipe.place(x=400,y=20)

            l_status=Label(frame_info,text='Status',height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
            l_status.place(x=400,y=50)
            e_status=Label(frame_info,text=tree_listam[6],font=('{Lucida console} 15'),bg=cbg,fg=ctx)
            e_status.place(x=400,y=70)

            l_fim=Label(frame_info,text="Data de Finalização",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
            l_fim.place(x=400,y=100)
            e_fim=Label(frame_info,text=tree_listam[5],font=('{Lucida console} 15'),bg=cbg,fg=ctx)
            e_fim.place(x=400,y=120)

            l_descricao=Label(frame_info,text="Descrição",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
            l_descricao.place(x=6,y=155)
            e_descricao=Label(frame_info,width=71,anchor=NW,height=18,text=tree_listam[7],font=('{Lucida console} 15'),bg=ctx,fg=cbg)
            e_descricao.place(x=6,y=177)
        except IndexError:
            messagebox.showerror('Error','Selecione uma missão')
            control('missao')

    lista_equipes=ver_nome_equipes()
    l_code=Label(frame_info,text="Código",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_code.place(x=3,y=0)
    e_code=Entry(frame_info, width=20, justify=LEFT, relief='solid',font=('{Lucida console} 15'),bg=ctx)
    e_code.place(x=3,y=20)
    
    l_local=Label(frame_info,text="Local",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_local.place(x=3,y=50)
    e_local=Entry(frame_info, width=20, justify=LEFT, relief='solid',font=('{Lucida console} 15'),bg=ctx)
    e_local.place(x=3,y=70)

    l_inicio=Label(frame_info,text="Data de Expedição",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_inicio.place(x=3,y=100)
    e_inicio=Entry(frame_info, width=11, justify=LEFT, relief='solid',font=('{Lucida console} 15'),bg=ctx)
    e_inicio.place(x=3,y=120)

    l_fim=Label(frame_info,text="Data de Finalização",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_fim.place(x=400,y=100)
    e_fim=Entry(frame_info, width=11, justify=LEFT, relief='solid',font=('{Lucida console} 15'),bg=ctx)
    e_fim.place(x=400,y=120)

    l_descricao=Label(frame_info,text="Descrição",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_descricao.place(x=6,y=155)
    e_descricao=Text(frame_info, width=71,height=18, relief='solid',font=('{Lucida console} 15'),bg=ctx,fg=cbg)
    e_descricao.place(x=6,y=177)

    l_missaoequipe=Label(frame_info,text="Equipe Atribuída",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_missaoequipe.place(x=400,y=0)
    equipem=lista_equipes
    equipm=[]
    for i in equipem:
        equipm.append(i)
    c_equipe= ttk.Combobox(frame_info,width=20,font=('{Lucida console} 10'))
    c_equipe['values']=(equipm)
    c_equipe.place(x=400,y=20)

    l_statusequipe=Label(frame_info,text="Status da Missão",height=1,anchor=NW,font=('{Lucida console} 10'),bg=cbg,fg=ctx)
    l_statusequipe.place(x=400,y=50)
    statusm=['Ativa','Sucesso','Fracasso']
    statsm=[]
    for i in statusm:
        statsm.append(i)
    c_statusm= ttk.Combobox(frame_info,width=20,font=('{Lucida console} 10'))
    c_statusm['values']=(statsm)
    c_statusm.place(x=400,y=70)

    botao_save=Button(frame_info,anchor=CENTER,command=add_missao, text='Salvar'.upper(),width=10,overrelief=RIDGE,relief=RAISED,font=('{Lucida console Bold} 9'),bg=ctx,fg=cbg)
    botao_save.place(x=700,y=20)

    botao_att=Button(frame_info,anchor=CENTER,command=atualizar_missao,text='Atualizar'.upper(),width=9, overrelief=RIDGE,relief=RAISED,font=('{Lucida console} 10'),bg=ctx,fg=cbg)
    botao_att.place(x=700,y=60)

    botao_ver=Button(frame_info,anchor=CENTER,command=detalhes_missao,text='Detalhes'.upper(),width=9, overrelief=RIDGE,relief=RAISED,font=('{Lucida console} 10'),bg=ctx,fg=cbg)
    botao_ver.place(x=700,y=100)

# Funções de controle
def control(i):
    #cadastro de agente
    if i == 'agente':
        for widget in frame_info.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        mostrar_agentes_completo()
        agentes()
    elif i == 'divisao':
        for widget in frame_info.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        mostrar_divisoes()
        divisao()   
    elif i == 'equipe':
        for widget in frame_info.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        mostrar_equipes()
        equipes() 
    elif i == 'missao':
        for widget in frame_info.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        mostrar_missoes()
        missoes()


#Criando botões de controle
app_add_img= Image.open('icone_mais.png')
app_add_img= app_add_img.resize((18,18))
app_add_img=ImageTk.PhotoImage(app_add_img)
app_add_agente=Button(frame_adicionar,command=lambda:control('agente'),image=app_add_img, text="AGENTE", width=100,compound=LEFT, anchor=NW, overrelief=RIDGE, relief=RAISED, font=('{Lucida console} 10'),bg=ctx,fg=cbg)
app_add_agente.place(x=10,y=25)

app_add_agente=Button(frame_adicionar,command=lambda:control('divisao'),image=app_add_img, text="DIVISÃO", width=100,compound=LEFT, anchor=NW, overrelief=RIDGE, relief=RAISED, font=('{Lucida console} 10'),bg=ctx,fg=cbg)
app_add_agente.place(x=130,y=25)

app_add_agente=Button(frame_adicionar,command=lambda:control('equipe'),image=app_add_img, text="EQUIPE", width=100,compound=LEFT, anchor=NW, overrelief=RIDGE, relief=RAISED, font=('{Lucida console} 10'),bg=ctx,fg=cbg)
app_add_agente.place(x=250,y=25)

app_add_agente=Button(frame_adicionar,command=lambda:control('missao'),image=app_add_img, text="MISSÃO", width=100,compound=LEFT, anchor=NW, overrelief=RIDGE, relief=RAISED, font=('{Lucida console} 10'),bg=ctx,fg=cbg)
app_add_agente.place(x=370,y=25)

deco_img=Image.open('ordo_realitas_green.png')
deco_img=deco_img.resize((400,200))
deco_img=ImageTk.PhotoImage(deco_img)
app_deco=Label(frame_deco,image=deco_img,bg=cbg)
app_deco.place(x=0,y=0)
deco_text=Label(frame_deco,text='Wellcome Operator Phantom\n\nSystem status: Online\n\nDatabase status:Online\n\nConection: Autorized\n\nLoading data from {sci_data_91.db}...\n\nData Loaded'.upper(),font=('{Lucida Console BOLD} 12'),bg=cbg,fg=ctx)
deco_text.place(x=35,y=250)


janela.mainloop()