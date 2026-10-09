from visuais.exibir_card import exibir_card

from menus.configurar_modulo import configurar_modulo
from menus.visualizar_modulo import visualizar_modulo
from menus.editar_modulo import editar_modulo
from menus.ordenar import fila_ordenada

def exibir_menu():
    exibir_card(
        "CENTRAL DE CONTROLE",
        "Menu principal",
        [
            "",
            "1. Configurar módulo",
            "2. Visualizar módulo",
            "3. Editar módulo",
            "4. Simular missão",
            "5. Exibir fila de prioridade",
            "0. Encerrar missão",
            ""
        ]
    )


def executar_menu(nave):
    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opção: "))
        match opcao:
            case 1:
                configurar_modulo(nave)
            case 2:
                visualizar_modulo(nave)
            case 3:
                editar_modulo(nave)
            case 4:
                nave.simular_missao()
            case 5:
                fila_ordenada(nave.modulos)
            case 0:
                exibir_card(
                    "MISSÃO FINALIZADA",
                    "Obrigado pela jornada!",
                    []
                )
                break
            case _:
                print("Opção inválida. Tente novamente.")