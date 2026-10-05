import funcoes
import modulos

while True: #verificar pouso, iniciar pouso, prencher informações
    print("1 - Verificar prioridade")
    print("2 - Verificar função")
    print("3 - Cadastrar modulo")
    print("4 - Atualizar informações do modulo")
    print("9 - Sair")
    opcao = input ("Escolha: ")

    match opcao:
        case "1":
            funcoes.ver_fila(modulos)
        case "2":
            funcoes.verificar_funcao()
        case "3":
            modulos.cadastrar_modulo()
        case "4":
            funcoes.atualizar_modulo()
        case "9":
            print("Saindo...")
            break
