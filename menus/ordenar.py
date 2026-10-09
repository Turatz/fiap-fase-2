def fila_ordenada(modulos):
    fila = sorted(
        modulos.values(),
        key=lambda modulo: modulo["prioridade"],
        reverse=True
    )

    print("\n--- FILA DE PRIORIDADE ---")

    for modulo in fila:
        print(
            f"{modulo['nome']} - "
            f"Prioridade: {modulo['prioridade']}"
        )

    input("\nPressione Enter para voltar ao menu...")