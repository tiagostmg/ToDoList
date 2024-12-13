class Item:
    def __init__(self, id: int, conteudo: str, estado: bool):
        self.id = id
        self.conteudo = conteudo
        self.estado = estado

    def __str__(self):
        estado_str = "[X]" if self.estado else "[ ]"

        return f"{estado_str} {self.conteudo}"

    def get_id(self):
        return "id: ", self.id