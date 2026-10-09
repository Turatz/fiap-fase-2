from visuais.exibir_card import exibir_card


class Temperatura:
    def __init__(
        self,
        temperatura_interna,
        temperatura_externa
    ):
        # Informações gerais do módulo
        self.rotulo = "Temperatura Interna e Externa"
        self.tipo = "temperatura"
        self.prioridade = 3
        self.criticidade = 1
        self.integridade = True

        # Dados informados pelo usuário
        self.temperatura_interna = temperatura_interna
        self.temperatura_externa = temperatura_externa

    def exibir(self):
        exibir_card(
            self.rotulo.upper(),
            "Informações do módulo",
            [
                "",
                f"Temperatura interna: "
                f"{self.temperatura_interna:.2f} °C",
                "",
                f"Temperatura externa: "
                f"{self.temperatura_externa:.2f} °C",
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

        self.temperatura_interna = float(
            input(
                f"Temperatura interna (°C) "
                f"[{self.temperatura_interna}]: "
            )
        )

        self.temperatura_externa = float(
            input(
                f"Temperatura externa (°C) "
                f"[{self.temperatura_externa}]: "
            )
        )

    @classmethod
    def cadastrar(cls):
        exibir_card(
            "TEMPERATURA INTERNA E EXTERNA",
            "Cadastro do módulo",
            [
                "",
                "Informe os dados necessários:",
                "",
            ]
        )

        temperatura_interna = float(
            input("Temperatura interna (°C): ")
        )

        temperatura_externa = float(
            input("Temperatura externa (°C): ")
        )

        temperatura = cls(
            temperatura_interna,
            temperatura_externa
        )

        temperatura.exibir()

        return temperatura