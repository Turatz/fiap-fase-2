
def fila_ordenada(modulos):
    fila = sorted(
        modulos.values(),
        key=lambda info: info["prioridade"],
        reverse=True
    )

    print("\n--- FILA DE PRIORIDADE ---")

    for info in fila:
        print(
            f"- {info['nome']}: "
            f"Prioridade - {info['prioridade']}"
        )

    input("\nPressione Enter para voltar ao menu...")
