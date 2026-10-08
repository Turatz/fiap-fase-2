from visuais.exibir_card import exibir_card


class Combustivel:
    def __init__(
        self,
        capacidade_tanque_kg,
        combustivel_kg,
        consumo_kg_segundo
    ):
        # Informações gerais do módulo
        self.rotulo = "Combustível"
        self.tipo = "combustivel"
        self.prioridade = 5
        self.criticidade = 5
        self.integridade = True

        # Dados informados pelo usuário
        self.capacidade_tanque_kg = capacidade_tanque_kg
        self.combustivel_kg = combustivel_kg
        self.consumo_kg_segundo = consumo_kg_segundo

        # Valores calculados
        self.percentual_combustivel = 0
        self.autonomia_segundos = 0
        self.autonomia_minutos = 0

        self.atualizar_calculos()

    def atualizar_calculos(self):
        self.percentual_combustivel = (
            self.combustivel_kg /
            self.capacidade_tanque_kg
        ) * 100

        self.autonomia_segundos = (
            self.combustivel_kg /
            self.consumo_kg_segundo
        )

        self.autonomia_minutos = (
            self.autonomia_segundos / 60
        )

    def consumir(self, quantidade_kg):
        self.combustivel_kg -= quantidade_kg

        if self.combustivel_kg <= 0:
            self.integridade = False
            self.combustivel_kg = 0

        self.atualizar_calculos()

    def exibir(self):
        exibir_card(
            self.rotulo.upper(),
            "Informações do módulo",
            [
                "",
                f"Combustível: "
                f"{self.combustivel_kg:.2f}/"
                f"{self.capacidade_tanque_kg:.2f} kg",
                "",
                f"Quantidade disponível: "
                f"{self.percentual_combustivel:.1f}%",
                "",
                f"Consumo: "
                f"{self.consumo_kg_segundo:.2f} kg/s",
                "",
                f"Autonomia: "
                f"{self.autonomia_segundos:.2f} segundos",
                f"           "
                f"{self.autonomia_minutos:.2f} minutos",
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

        self.capacidade_tanque_kg = float(
            input(
                f"Capacidade do tanque (kg) "
                f"[{self.capacidade_tanque_kg}]: "
            )
        )

        self.combustivel_kg = float(
            input(
                f"Combustível disponível (kg) "
                f"[{self.combustivel_kg}]: "
            )
        )

        self.consumo_kg_segundo = float(
            input(
                f"Consumo (kg/s) "
                f"[{self.consumo_kg_segundo}]: "
            )
        )

        self.atualizar_calculos()
    
    @classmethod
    def cadastrar(cls):
        exibir_card(
            "COMBUSTÍVEL",
            "Cadastro do módulo",
            [
                "",
                "Informe os dados necessários:",
                "",
            ]
        )

        capacidade_tanque_kg = float(
            input("Capacidade do tanque (kg): ")
        )

        combustivel_kg = float(
            input("Combustível disponível (kg): ")
        )

        consumo_kg_segundo = float(
            input("Consumo de combustível (kg/s): ")
        )

        combustivel = cls(
            capacidade_tanque_kg,
            combustivel_kg,
            consumo_kg_segundo
        )

        combustivel.exibir()

        return combustivel