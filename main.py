from lista import Lista

lista = Lista()

while True:
    print("To-do List")
    print("----------")
    lista.mostra_lista()
    print("----------")

    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Trocar estado")
    print("0 - Encerrar programa")

    input1 = input("Escolha uma opção: ")

    match input1:
        case "0":
            print("Programa encerrado")
            break
        case "1":
            inputAdd = input("Insira o texto do novo item: ")
            lista.add_lista(inputAdd)
        case "2":
            try:
                inputRemove = int(input("Digite o ID do item a ser deletado: "))
                lista.remove_lista(inputRemove)
            except ValueError:
                print("ID inválido. Por favor, insira um número.")
        case "3":
            input_troca = int(input("Digite o ID do item a ter seu estado trocado: "))
            lista.trocar_estado(input_troca)

        case _:
            print("Opção inválida.")
