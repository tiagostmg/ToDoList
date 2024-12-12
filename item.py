class Item:
    def __init__(self, id: int, conteudo: str, estado: bool):
        self.id = id
        self.conteudo = conteudo
        self.estado = estado

    def __str__(self):
        estado_str = "Ativo" if self.estado else "Inativo"
        return f"Item(ID: {self.id}, Conteúdo: '{self.conteudo}', Estado: {estado_str})"
