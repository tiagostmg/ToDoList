from item import Item
from sqlConnection import *

class Lista:
    def __init__(self):
        self.lista = []
        self.carregar_lista()

    # Carregar itens existentes do banco de dados
    def carregar_lista(self):
        query = "SELECT id, conteudo, estado FROM lista"
        resultados = select_query(query)  # Função que executa o SELECT no banco
        if resultados:
            for id, conteudo, estado in resultados:
                item = Item(id, conteudo, estado)
                self.lista.append(item)

    def mostra_lista(self):
        if self.lista.__len__() != 0:
            i = 1
            for l in self.lista:
                if l.estado:
                    print(f"{i} [X] - {l.conteudo}")
                elif not l.estado:
                    print(f"{i} [ ] - {l.conteudo}")
                i+=1
        else:
            print("")

    def trocar_estado(self, index_troca):
        if 0 < index_troca <= len(self.lista):
            item = self.lista[index_troca - 1]

            item.estado = not item.estado

            query = "UPDATE lista SET estado = %s WHERE id = %s"
            params = (item.estado, item.id)
            update_query(query, params)

        else:
            print("Índice inválido. Nenhum item foi alterado.")

    def add_lista(self, conteudo):
        novo_item = Item(None, conteudo, False)
        self.lista.append(novo_item)

        # Inserir no banco de dados
        query = "INSERT INTO lista (conteudo, estado) VALUES (%s, %s)"
        params = (conteudo, False)
        insert_query(query, params)

    # Remover item da lista e do banco de dados
    def remove_lista(self, index_remove):
        if 0 < index_remove <= len(self.lista):
            item_id = self.lista[index_remove - 1].id

            # Remover o item da lista
            self.lista.pop(index_remove - 1)

            # Remover do banco de dados
            query = "DELETE FROM lista WHERE id = %s"
            params = (item_id,)
            delete_query(query, params)

        else:
            print("Índice inválido. Nenhum item foi removido.")
