from lista import Lista

lista = Lista()

while True:
    print("To-do List")
    print("----------")
    for item in lista.mostra_lista():
        print(item)
    print("----------")

    print("1 - Adicionar item")
    print("2 - Editar item")
    print("3 - Remover item")
    print("4 - Trocar estado")
    print("0 - Encerrar programa")

    input1 = input("Escolha uma opção: ")

    match input1:
        case "0":
            print("Programa encerrado")
            break
        case "1":
            input_add = input("Insira o texto do novo item: ")
            lista.add_lista(input_add)
        case "2":
            input_id_edit = input("Digite o ID do item a ser editado: ")
            input_texto_edit = input("Insira o novo conteúdo do item: ")

            lista.edit(input_id_edit, input_texto_edit)
        case "3":
            try:
                input_remove = int(input("Digite o ID do item a ser deletado: "))
                lista.remove_lista(input_remove)
            except ValueError:
                print("ID inválido. Por favor, insira um número.")
        case "4":
            try:
                input_troca = int(input("Digite o ID do item a ter seu estado trocado: "))
                lista.trocar_estado(input_troca)
            except ValueError:
                print("ID inválido. Por favor, insira um número.")

        case _:
            print("Opção inválida.")
