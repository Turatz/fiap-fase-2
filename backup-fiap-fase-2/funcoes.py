import modulos

def verificar_modulo():
    modulos
    nome_digitado = input("Digite o nome do módulo que deseja verificar: ")
    for modulo in modulos:
        if modulo == nome_digitado:
            for modulo in modulos:
                if modulo["rotulo"].lower() == nome_digitado.lower():
                    print(f"O módulo '{nome_digitado}' está presente.")
                    return
                else: 
                    print(f"O módulo '{nome_digitado}' não está presente.")
                    return

def escolher_modulo():
    numero = 1 
    for modulo in modulos:
        print(f"{numero} - {modulo['rotulo']}")
        numero = numero + 1
    texto = input("Digite o nome do módulo que deseja escolher: ")
    if not texto.isdigit():
        print("Digite um número válido.")
        return None
    escolha = int(texto)
    if escolha < 1 or escolha > len(modulos):
        print("Numero fora da lista.")
        return None
    return modulos[escolha - 1]
    
def atualizar_modulo():
    modulo = escolher_modulo()
    if modulo is None:
        return
    print("\nModulo:", modulo["rotulo"])
    print("1 - Atualizar detalhes")
    print("2 - Atualizar criticidade")
    print("3 - Atualizar combustivel")
    print("4 - Atualizar energia")
    print("5 - Atualizar temperatura interna e externa")
    opcao = input("Escolha uma opção: ")
    match opcao:
        case "1":
            detalhes = input("Digite os novos detalhes do módulo: ")
            modulo["detalhes"] = detalhes
            print("Detalhes atualizados com sucesso.")
        case "2":
            criticidade = float(input("Digite a nova criticidade do módulo: "))
            modulo["criticidade"] = criticidade
            print("Criticidade atualizada com sucesso.")
        case "3":
            combustivel = float(input("Digite o novo nível de combustível do módulo: "))
            modulo["combustivel"] = combustivel
            print("Combustível atualizado com sucesso.")
        case "4":
            energia = float(input("Digite o novo nível de energia do módulo: "))
            modulo["energia"] = energia
            print("Energia atualizada com sucesso.")
        case "5":
            temperatura_interna = float(input("Digite a nova temperatura interna do módulo: "))
            temperatura_externa = float(input("Digite a nova temperatura externa do módulo: "))
            modulo["temperatura_interna"] = temperatura_interna
            modulo["temperatura_externa"] = temperatura_externa
            print("Temperatura interna e externa atualizadas com sucesso.")

def cadastro_modulo():
    rotulo = input("Digite o rotulo do módulo: ")
    tipo = input("Digite o tipo do módulo: ")
    detalhes = input("Digite os detalhes do módulo: ")
    modulo = {"rotulo": rotulo,"tipo": tipo,"detalhes": detalhes, "integridade": True,}
    modulos.append(modulo)
    print(f"Módulo '{rotulo}' cadastrado com sucesso.")

def ver_fila(modulos):
    fila = sorted(modulos, key=lambda modulo: modulo["prioridade"], reverse=True)

    for modulo in fila:
        print(f"Rotulo: {modulo['rotulo']}, - prioridade: {modulo['prioridade']},")
        
def cadastrar_modulos():
    # clona o modulos
    # percorre todos os modulos (FOR)
        # Verifica o tipo do modulo
        # Informa o usuario o modulo que ele esta preenchendo
            # Faz perguntas referentes a cada tipo de modulo (separar em um match case para ficar organizado)
            
            # EXEMPLO: 
            # match tipo_modulo:
            #     case "habitacao" verificar_habitacao()
            #     case _: 
    