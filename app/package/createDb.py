import sqlite3

def createDb():
    databaseFile = "app/database/alunos.db"
    conn = sqlite3.connect(databaseFile)
    
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE  IF NOT EXISTS alunos (
            id_numpasta TEXT NOT NULL,
            nome TEXT NOT NULL,
            idade INTEGER,
            cpf VARCHAR(11) NOT NULL PRIMARY KEY,
            turma TEXT NOT NULL,
            ano NUMERIC(4),
            situacao TEXT,
            pedencias TEXT,
            fone TEXT,
            cidade TEXT,
            responsavel TEXT NOT NULL
            );
        """)
    conn.close()

    return ('Tabela criada com sucesso')
