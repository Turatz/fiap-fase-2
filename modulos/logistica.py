from visuais.exibir_card import exibir_card


class Logistica:
    def __init__(
        self,
        capacidade_carga_kg,
        alimentos_kg
    ):
        # Informações gerais do módulo
        self.rotulo = "Logística"
        self.tipo = "logistica"
        self.prioridade = 2
        self.criticidade = 2
        self.integridade = True

        # Dados informados pelo usuário
        self.capacidade_carga_kg = capacidade_carga_kg
        self.alimentos_kg = alimentos_kg

    def exibir(self):
        exibir_card(
            self.rotulo.upper(),
            "Informações do módulo",
            [
                "",
                f"Capacidade de carga: "
                f"{self.capacidade_carga_kg:.2f} kg",
                "",
                f"Alimentos disponíveis: "
                f"{self.alimentos_kg:.2f} kg",
                "",
                (
                    "Status: Operacional"
                    if self.integridade
                    else "Status: Inoperante"
                )
            ]
        )

    def editar(self):
        exibir_card(
            self.rotulo.upper(),
            "Edição do módulo",
            [
                "",
                "Informe os novos dados:",
                "",
            ]
        )

        self.capacidade_carga_kg = float(
            input(
                f"Capacidade de carga (kg) "
                f"[{self.capacidade_carga_kg}]: "
            )
        )

        self.alimentos_kg = float(
            input(
                f"Alimentos disponíveis (kg) "
                f"[{self.alimentos_kg}]: "
            )
        )

    @classmethod
    def cadastrar(cls):
        exibir_card(
            "LOGÍSTICA",
            "Cadastro do módulo",
            [
                "",
                "Informe os dados necessários:",
                "",
            ]
        )

        capacidade_carga_kg = float(
            input("Capacidade de carga (kg): ")
        )

        alimentos_kg = float(
            input("Alimentos disponíveis (kg): ")
        )

        logistica = cls(
            capacidade_carga_kg,
            alimentos_kg
        )

        logistica.exibir()

        return logistica