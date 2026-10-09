from visuais.exibir_card import exibir_card

class Habitacao:
    def __init__(
        self,
        capacidade_pessoas,
        pessoas_atuais,
        oxigenio_kg,
        agua_litros
    ):
        # Informações gerais do módulo
        self.rotulo = "Tripulação e suporte à vida"
        self.tipo = "habitacao"
        self.prioridade = 4
        self.criticidade = 5
        self.integridade = True

        # Dados informados pelo usuário
        self.capacidade_pessoas = capacidade_pessoas
        self.pessoas_atuais = pessoas_atuais
        self.oxigenio_kg = oxigenio_kg
        self.agua_litros = agua_litros

        # Valores calculados
        self.consumo_oxigenio_kg_dia = 0
        self.consumo_agua_litros_dia = 0
        self.autonomia_oxigenio_dias = 0
        self.autonomia_agua_dias = 0
        self.autonomia_dias = 0

        self.atualizar_calculos()

    def atualizar_calculos(self):
        """Atualiza os valores derivados do módulo."""

        self.consumo_oxigenio_kg_dia = (
            self.pessoas_atuais * 0.84
        )

        self.consumo_agua_litros_dia = (
            self.pessoas_atuais * 3.0
        )

        self.autonomia_oxigenio_dias = (
            self.oxigenio_kg /
            self.consumo_oxigenio_kg_dia
        )

        self.autonomia_agua_dias = (
            self.agua_litros /
            self.consumo_agua_litros_dia
        )

        self.autonomia_dias = min(
            self.autonomia_oxigenio_dias,
            self.autonomia_agua_dias
        )

    def exibir(self):
        exibir_card(
            self.rotulo.upper(),
            "Informações do módulo",
            [
                "",
                f"Tripulação: "
                f"{self.pessoas_atuais}/"
                f"{self.capacidade_pessoas} pessoas",
                "",
                f"Oxigênio: {self.oxigenio_kg} kg",
                f"Consumo de oxigênio: {self.consumo_oxigenio_kg_dia:.2f} kg/dia",
                "",
                f"Água: {self.agua_litros} L",
                f"Consumo de água: {self.consumo_agua_litros_dia:.2f} L/dia",
                "",
                f"Autonomia: {self.autonomia_dias:.2f} dias",
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

        self.capacidade_pessoas = int(
            input(
                f"Capacidade máxima "
                f"[{self.capacidade_pessoas}]: "
            )
        )

        self.pessoas_atuais = int(
            input(
                f"Quantidade de pessoas "
                f"[{self.pessoas_atuais}]: "
            )
        )

        self.oxigenio_kg = float(
            input(
                f"Oxigênio disponível (kg) "
                f"[{self.oxigenio_kg}]: "
            )
        )

        self.agua_litros = float(
            input(
                f"Água disponível (litros) "
                f"[{self.agua_litros}]: "
            )
        )

        self.atualizar_calculos()

    @classmethod
    def cadastrar(cls):
        exibir_card(
            "TRIPULAÇÃO E SUPORTE À VIDA",
            "Cadastro do módulo",
            [
                "",
                "Informe os dados necessários:",
                "",
            ]
        )

        capacidade_pessoas = int(
            input("Capacidade máxima de pessoas: ")
        )

        pessoas_atuais = int(
            input("Quantidade de pessoas: ")
        )

        oxigenio_kg = float(
            input("Oxigênio disponível (kg): ")
        )

        agua_litros = float(
            input("Água disponível (litros): ")
        )

        habitacao = cls(
            capacidade_pessoas,
            pessoas_atuais,
            oxigenio_kg,
            agua_litros
        )

        habitacao.exibir()

        return habitacao