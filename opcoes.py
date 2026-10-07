from unittest import case

import funcoes
import banco
from modulos import modulos as lista_modulos

banco.criar_tabela()

while True: #verificar pouso, iniciar pouso, prencher informações
    #falta acrescentar mais opções (turatti)
    print("\nMenu de opções:")
    print("1 - Verificar prioridade")
    print("2 - Cadastrar modulo")
    #print("4 - Atualizar informações do modulo")
    #print("5 - Calcular gasto para pouso")
    #print("6 - Verificar possibilidade de pouso")
    #print("7 - Iniciar pouso")
    #print("8 - Abortar pouso")
    #print("9 - Sair")
    opcao = input ("Escolha: ")

    match opcao:
        case "1":
            funcoes.ver_fila(lista_modulos)
        case "2":
            funcoes.cadastro_modulo()
        case "4":
            #funcoes.atualizar_modulo()
            pass
        case "5":
            pass
            #falta implementar (turatti) 
        case "6":
            pass
            #falta implementar (turatti)
        case "7":
            pass
            #falta implementar (turatti)    
        case "8":
            pass
            #falta implementar (turatti)
        case "9":
            print("Saindo...")
            break
