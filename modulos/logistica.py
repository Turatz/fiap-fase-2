from visuais.exibir_card import exibir_card
from modulos.modulos import Modulo


class Logistica(Modulo):
    def __init__(
        self,
        capacidade_carga_kg,
        alimentos_kg
    ):
        super().__init__("Logística", "logistica", 2, 2)

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
