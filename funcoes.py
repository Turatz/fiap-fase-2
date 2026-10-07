from modulos import modulos as lista_modulos
import modulos


def ver_fila(modulos):  # funcionando (turatti)

    fila = sorted(
        modulos,
        key=lambda modulo: modulo["prioridade"],
        reverse=True
    )

    for modulo in fila:
        print(
            f"Rótulo: {modulo['rotulo']} - "
            f"prioridade: {modulo['prioridade']}"
        )


def listar_modulos():  # mostra todos os módulos

    numero = 1

    for modulo in lista_modulos:
        print(
            f"{numero} - "
            f"Rótulo: {modulo['rotulo']} - "
            f"Tipo: {modulo['tipo']}"
        )

        numero = numero + 1


def cadastro_modulo():

    rotulo = input("Digite o rótulo do módulo: ")

    for modulo in lista_modulos:
        if modulo["rotulo"].lower() == rotulo.lower():
            print("Módulo já cadastrado.")
            return

    tipo = input("Digite o tipo do módulo: ")
    prioridade = int(input("Digite a prioridade do módulo (1 a 5): "))
    criticidade = int(input("Digite a criticidade do módulo (1 a 5): "))
    detalhes = input("Digite os detalhes do módulo: ")

    modulo = {
        "rotulo": rotulo,
        "tipo": tipo,
        "prioridade": prioridade,
        "criticidade": criticidade,
        "integridade": True,
        "detalhes": detalhes
    }

    lista_modulos.append(modulo)

    print(f"Módulo '{rotulo}' cadastrado com sucesso.")


def escolher_modulo():  # testado e funcionando (turatti)

    numero = 1

    for modulo in lista_modulos:
        print(f"{numero} - {modulo['rotulo']}")
        numero = numero + 1

    texto = input("Digite o número do módulo que deseja escolher: ")

    if not texto.isdigit():
        print("Digite um número válido.")
        return None

    escolha = int(texto)

    if escolha < 1 or escolha > len(lista_modulos):
        print("Número fora da lista.")
        return None

    return lista_modulos[escolha - 1]


def atualizar_modulo():  # testado e funcionando (turatti)

    modulo = escolher_modulo()

    if modulo is None:
        return

    print("\nMódulo:", modulo["rotulo"])

    print("1 - Atualizar detalhes")
    print("2 - Atualizar criticidade")
    print("3 - Atualizar combustível")
    print("4 - Atualizar energia")
    print("5 - Atualizar temperatura interna e externa")

    opcao = input("Escolha uma opção: ")

    match opcao:

        case "1":
            detalhes = input("Digite os novos detalhes do módulo: ")
            modulo["detalhes"] = detalhes
            print("Detalhes atualizados com sucesso.")

        case "2":
            criticidade = float(
                input("Digite a nova criticidade do módulo: ")
            )
            modulo["criticidade"] = criticidade
            print("Criticidade atualizada com sucesso.")

        case "3":
            combustivel = float(
                input("Digite o novo nível de combustível do módulo: ")
            )
            modulo["combustivel"] = combustivel
            print("Combustível atualizado com sucesso.")

        case "4":
            energia = float(
                input("Digite o novo nível de energia do módulo: ")
            )
            modulo["energia"] = energia
            print("Energia atualizada com sucesso.")

        case "5":
            temperatura_interna = float(
                input("Digite a nova temperatura interna do módulo: ")
            )

            temperatura_externa = float(
                input("Digite a nova temperatura externa do módulo: ")
            )

            modulo["temperatura_interna"] = temperatura_interna
            modulo["temperatura_externa"] = temperatura_externa

            print("Temperatura interna e externa atualizadas com sucesso.")