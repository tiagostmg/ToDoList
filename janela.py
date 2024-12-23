import tkinter as tk
from tkinter import messagebox
from lista import Lista

# Inicializa a lista
lista = Lista()

# Funções do programa
def adicionar_item():
    texto = entrada_adicionar.get()
    if texto.strip():
        lista.add_lista(texto)
        entrada_adicionar.delete(0, tk.END)
        atualizar_lista()
    else:
        messagebox.showwarning("Aviso", "O texto do item não pode estar vazio.")

def editar_item():
    try:
        id_item = int(entrada_editar_id.get())
        novo_texto = entrada_editar_texto.get()
        if novo_texto.strip():
            lista.edit(id_item, novo_texto)
            entrada_editar_id.delete(0, tk.END)
            entrada_editar_texto.delete(0, tk.END)
            atualizar_lista()
        else:
            messagebox.showwarning("Aviso", "O novo texto do item não pode estar vazio.")
    except ValueError:
        messagebox.showerror("Erro", "ID inválido. Por favor, insira um número.")

def remover_item():
    try:
        id_item = int(entrada_remover.get())
        lista.remove_lista(id_item)
        entrada_remover.delete(0, tk.END)
        atualizar_lista()
    except ValueError:
        messagebox.showerror("Erro", "ID inválido. Por favor, insira um número.")

def trocar_estado():
    try:
        id_item = int(entrada_trocar_estado.get())
        lista.trocar_estado(id_item)
        entrada_trocar_estado.delete(0, tk.END)
        atualizar_lista()
    except ValueError:
        messagebox.showerror("Erro", "ID inválido. Por favor, insira um número.")

def atualizar_lista():
    listbox_tarefas.delete(0, tk.END)
    for item in lista.mostra_lista():
        listbox_tarefas.insert(tk.END, item)

# Criação da janela principal
janela = tk.Tk()
janela.title("To-do List")
janela.geometry("500x500")

# Widgets para exibir a lista
label_titulo = tk.Label(janela, text="To-do List", font=("Arial", 16))
label_titulo.pack(pady=10)

listbox_tarefas = tk.Listbox(janela, width=50, height=15, font=("Arial", 12))
listbox_tarefas.pack(pady=10)

# Widgets para adicionar item
frame_adicionar = tk.Frame(janela)
frame_adicionar.pack(pady=5)

label_adicionar = tk.Label(frame_adicionar, text="Adicionar item:")
label_adicionar.pack(side=tk.LEFT, padx=5)

entrada_adicionar = tk.Entry(frame_adicionar, width=30)
entrada_adicionar.pack(side=tk.LEFT, padx=5)

btn_adicionar = tk.Button(frame_adicionar, text="Adicionar", command=adicionar_item)
btn_adicionar.pack(side=tk.LEFT, padx=5)

# Widgets para editar item
frame_editar = tk.Frame(janela)
frame_editar.pack(pady=5)

label_editar = tk.Label(frame_editar, text="Editar item (ID e novo texto):")
label_editar.pack(side=tk.LEFT, padx=5)

entrada_editar_id = tk.Entry(frame_editar, width=5)
entrada_editar_id.pack(side=tk.LEFT, padx=5)

entrada_editar_texto = tk.Entry(frame_editar, width=20)
entrada_editar_texto.pack(side=tk.LEFT, padx=5)

btn_editar = tk.Button(frame_editar, text="Editar", command=editar_item)
btn_editar.pack(side=tk.LEFT, padx=5)

# Widgets para remover item
frame_remover = tk.Frame(janela)
frame_remover.pack(pady=5)

label_remover = tk.Label(frame_remover, text="Remover item (ID):")
label_remover.pack(side=tk.LEFT, padx=5)

entrada_remover = tk.Entry(frame_remover, width=10)
entrada_remover.pack(side=tk.LEFT, padx=5)

btn_remover = tk.Button(frame_remover, text="Remover", command=remover_item)
btn_remover.pack(side=tk.LEFT, padx=5)

# Widgets para trocar estado
frame_trocar = tk.Frame(janela)
frame_trocar.pack(pady=5)

label_trocar = tk.Label(frame_trocar, text="Trocar estado (ID):")
label_trocar.pack(side=tk.LEFT, padx=5)

entrada_trocar_estado = tk.Entry(frame_trocar, width=10)
entrada_trocar_estado.pack(side=tk.LEFT, padx=5)

btn_trocar = tk.Button(frame_trocar, text="Trocar", command=trocar_estado)
btn_trocar.pack(side=tk.LEFT, padx=5)

# Inicia a interface
atualizar_lista()
janela.mainloop()
