import sqlite3




def conexao_banco():
      conexao = sqlite3.connect('contatos.db')
      cursor = conexao.cursor()
      sql = '''
      CREATE TABLE IF NOT EXISTS contatos (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         nome TEXT NOT NULL,
         telefone TEXT NOT NULL,
         email TEXT NOT NULL
      )'''
      cursor.execute(sql)
      conexao.commit()
      return conexao


def adicionar_contato(nome, telefone, email):
   conexao = conexao_banco()
   cursor = conexao.cursor()
   sql =  '''
   INSERT INTO contatos (nome, telefone, email) 
   VALUES (?, ?, ?)'''
   cursor.execute(sql, (nome, telefone, email))
   conexao.commit()
   conexao.close()

def listar_contatos():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM contatos"
    cursor.execute(sql)
    contatos = cursor.fetchall()
    if len(contatos) == 0:
        print("Nenhum contato encontrado.")
    else:
        
            print ("### CONTATOS ###")
            print (f"{'ID':<7} {'Nome':<10} {'Telefone':<17} {'Email':<30}")
            print("-" * 70)
            for contato in contatos:
             print(f"ID: {contato[0]} | Nome: {contato[1]} | Telefone: {contato[2]} | Email: {contato[3]}")

def buscar_contato():
    nome = input("Digite o nome do contato que deseja buscar: ")
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM contatos WHERE nome LIKE ?"
    cursor.execute(sql, ('%' + nome + '%',))
    contatos = cursor.fetchall()
    if len(contatos) == 0:
        print("Nenhum contato encontrado com esse nome.")
    else:
        print ("### CONTATOS ENCONTRADOS ###")
        print (f"{'ID':<7} {'Nome':<10} {'Telefone':<17} {'Email':<30}")
        print("-" * 70)
        for contato in contatos:
            print(f"ID: {contato[0]} | Nome: {contato[1]} | Telefone: {contato[2]} | Email: {contato[3]}")

def atualizar_contato():
    id_contato = input("Digite o ID do contato que deseja atualizar: ")
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM contatos WHERE id = ?"
    cursor.execute(sql, (id_contato,))
    contato = cursor.fetchone()
    if contato is None:
        print("Contato não encontrado.")
    else:
        print(f"Contato encontrado: ID: {contato[0]} | Nome: {contato[1]} | Telefone: {contato[2]} | Email: {contato[3]}")
        nome = input("Digite o novo nome do contato (ou pressione Enter para manter o atual): ")
        telefone = input("Digite o novo telefone do contato (ou pressione Enter para manter o atual): ")
        email = input("Digite o novo email do contato (ou pressione Enter para manter o atual): ")
        if nome == "":
            nome = contato[1]
        if telefone == "":
            telefone = contato[2]
        if email == "":
            email = contato[3]
        sql = "UPDATE contatos SET nome = ?, telefone = ?, email = ? WHERE id = ?"
        cursor.execute(sql, (nome, telefone, email, id_contato))
        conexao.commit()
        print("Contato atualizado com sucesso!")

def excluir_contato():
    id_contato = input("Digite o ID do contato que deseja excluir: ")
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM contatos WHERE id = ?"
    cursor.execute(sql, (id_contato,))
    contato = cursor.fetchone()
    if contato is None:
        print("Contato não encontrado.")
    else:
        print(f"Contato encontrado: ID: {contato[0]} | Nome: {contato[1]} | Telefone: {contato[2]} | Email: {contato[3]}")
        confirmacao = input("Tem certeza que deseja excluir este contato? (s/n): ")
        if confirmacao.lower() == "s":
            sql = "DELETE FROM contatos WHERE id = ?"
            cursor.execute(sql, (id_contato,))
            conexao.commit()
            print("Contato excluído com sucesso!")
        else:
            print("Exclusão cancelada.")



while True:
    print ("### CONTATOS ###")
    print ("1. Adicionar contato")
    print ("2. Listar contatos")
    print ("3. Buscar contato pelo nome")
    print ("4. Atualizar contato")
    print ("5. excluir contato")
    print ("6. Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")
            adicionar_contato(nome, telefone, email)
            print("Contato adicionado com sucesso!")
    elif opcao == "2":
            listar_contatos()
    elif opcao == "3":
            buscar_contato()
    elif opcao == "4":
            atualizar_contato()
    elif opcao == "5":
            excluir_contato()
    elif opcao == "6":
            print("Saindo do programa...")
            break
    else:
            print("Opção inválida. Tente novamente.")

