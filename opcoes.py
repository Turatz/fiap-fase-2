import sys

def menu():
    while True:
        print("\nMenu de opções:")
        print("1 - Cadastrar Informações Iniciais")
        print("9 - Sair")
        
        opcao = input ("Escolha: ")

        if opcao == "9":
            print("Até Mais :D")
            sys.exit()
        
        return opcao