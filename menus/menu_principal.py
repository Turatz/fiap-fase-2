from visuais.exibir_card import exibir_card

from menus.configurar_modulo import configurar_modulo
from menus.visualizar_modulo import visualizar_modulo
from menus.editar_modulo import editar_modulo


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
            "",
            "0. Encerrar missão",
            ""
        ]
    )


def executar_menu(nave):
    while True:
        exibir_menu()

        try:
            opcao = int(input("\nSelecione uma opção: "))
        except ValueError:
            continue

        if opcao == 1:
            configurar_modulo(nave)

        elif opcao == 2:
            visualizar_modulo(nave)

        elif opcao == 3:
            editar_modulo(nave)

        elif opcao == 4:
            nave.simular_missao()

        elif opcao == 0:
            exibir_card(
                "MISSÃO FINALIZADA",
                "Obrigado pela jornada!",
                []
            )
            break