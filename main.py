import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = sqlite3.conn.cursor()

    def inserir(self,nome,telefone):
        pass

    def editar(self,nome,telefone,id):
        pass

    def excluir(self):
        pass

    def listar(self):
        pass

    def fechar(self):
        self.cursor.close()
        self.conn.close()
