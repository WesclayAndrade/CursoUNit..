import sqlite3 

conexao = sqlite3.connect('banco.db') #coectando o banco a variável
cursor = conexao.cursor() #objeto mensageiro cursor

#criando os dados no banco/ triplo aspas duplas permiti criar sem identação
cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titular TEXT NOT NULL,
    saldo FLOAT NOT NULL,
    cpf TEXT NOT NULL UNIQUE)""")

#cursor.execute("""INSERT INTO contas_bancarias
#    (titular, saldo, cpf) VALUES 
#    ('Josefa', 700, '888.110.000.-88')""")

cursor.execute("""SELECT titular, saldo FROM contas_bancarias""")
conta = cursor.fetchall() # pega tudo que executar no select e armazena em nova variável criada
#cursor.execute("DELETE FROM contas_bancarias WHERE SALDO < 500")
cursor.execute("UPDATE contas_bancarias SET saldo = 1000 WHERE ID = 2")


for conta in conta:
    titular, saldo = conta
    print(f"""
       
        Titular: {titular}
        Saldo: {saldo} 
        """)




conexao.commit()



