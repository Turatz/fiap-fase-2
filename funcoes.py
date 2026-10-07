from modulos import modulos as lista_modulos
import modulos
import banco

def ver_fila(modulos):
    modulos_db = banco.listar_modulos_db()

    lista_completa = list(modulos)

    for modulo in modulos_db: #deixar os dois padronizados, vi um chines fazendo assim (turatti)
        lista_completa.append({ #usado para ter a lista completa
            "rotulo": modulo[0],
            "tipo": modulo[1],
            "prioridade": modulo[2],
            "criticidade": modulo[3],
            "integridade": modulo[4],
            "detalhes": modulo[5]
        })

    fila = sorted(
        lista_completa,
        key=lambda modulo: modulo["prioridade"],
        reverse=True
    )

    for modulo in fila:
        print(
            f"Rótulo: {modulo['rotulo']} - "
            f"Prioridade: {modulo['prioridade']}"
        )

def listar_modulos(): #mostra todos os modulos na lista de modulos (turatti)
                      #testei e funcionou (turatti)
    numero = 1
    for modulo in lista_modulos:
        print(f"{numero} - Rotulo: {modulo['rotulo']} - Tipo: {modulo['tipo']}")
        numero = numero + 1

    for modulo in banco.listar_modulos_db():
        print(f"{numero} - Rotulo: {modulo[0]} - Tipo: {modulo[1]}")
        numero = numero + 1

def cadastro_modulo():
    rotulo = input("Digite o rótulo do módulo: ")

    for modulo in lista_modulos:
        if modulo["rotulo"].lower() == rotulo.lower():
            print("Módulo já cadastrado.")
            return

    modulos_db = banco.listar_modulos_db()

    for modulo in modulos_db:
        if modulo[0].lower() == rotulo.lower():
            print("Módulo já cadastrado.")
            return

    tipo = input("Digite o tipo do módulo: ")
    prioridade = int(input("Digite a prioridade do módulo (1 a 5): "))
    criticidade = int(input("Digite a criticidade do módulo (1 a 5): "))
    detalhes = input("Digite os detalhes do módulo: ")

    # acredito que deu certo, mas não testei ainda (turatti)
    banco.cadastrar_modulo(
        rotulo,
        tipo,
        prioridade,
        criticidade,
        True,
        detalhes
    )

    print(f"Módulo '{rotulo}' cadastrado com sucesso.")

def escolher_modulo(): ##testei e funcionou (turatti)
    numero = 1 
    for modulos in modulos:
        print(f"{numero} - {modulos['rotulo']}")
        numero = numero + 1
        texto = input("Digite o nome do módulo que deseja escolher: ").lower()
        if not texto.isdigit():
            print("Digite um número válido.")
            return None
    escolha = int(texto)
    if escolha < 1 or escolha > len(modulos):
        print("Numero fora da lista.")
        return None
    return modulos[escolha - 1]
    
def atualizar_modulo(): ##testado e funcionando (turatti)
    modulo = escolher_modulo()
    if modulo is None:
        return
    print("\nModulo:", modulo["rotulo"]) ##falta acrescentar mais informações do modulo (turatti)
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


 #def cadastrar_modulos():  #coloquei em hastag para não dar erro (turatti)
    # clona o modulos
    # percorre todos os modulos (FOR)
        # Verifica o tipo do modulo
        # Informa o usuario o modulo que ele esta preenchendo
            # Faz perguntas referentes a cada tipo de modulo (separar em um match case para ficar organizado)
            
            # EXEMPLO: 
            # match tipo_modulo:
            #     case "habitacao" verificar_habitacao()
            #     case _: 
    