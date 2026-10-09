
def fila_ordenada(modulos):
    fila = sorted(
        modulos.values(),
        key=lambda modulo: modulo["classe"].prioridade,
        reverse=True
    )

    print("\n--- FILA DE PRIORIDADE ---")

    for modulo in fila:
        prioridade = modulo["classe"].prioridade

        print(
            f"{modulo['nome']} - "
            f"Prioridade: {prioridade}"
        )

    input("\nPressione Enter para voltar ao menu...")