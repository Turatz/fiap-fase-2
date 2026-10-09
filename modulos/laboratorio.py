from visuais.exibir_card import exibir_card


class Laboratorio:
    def __init__(self):
        
# Informações gerais do módulo
        self.rotulo = "Laboratório"
        self.tipo = "laboratorio"
        self.prioridade = 3
        self.criticidade = 1
        self.integridade = True

    def exibir(self):
        exibir_card(
            self.rotulo.upper(),
            "Informações do módulo",
            [
                "",
                f"Prioridade: {self.prioridade}",
                "",
                f"Criticidade: {self.criticidade}",
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

        self.prioridade = int(
            input(
                f"Prioridade "
                f"[{self.prioridade}]: "
            )
        )

        self.criticidade = int(
            input(
                f"Criticidade "
                f"[{self.criticidade}]: "
            )
        )

    @classmethod
    def cadastrar(cls):
        exibir_card(
            "LABORATÓRIO",
            "Cadastro do módulo",
            [
                "",
                "Cadastro com as informações gerais",
                "definidas para o módulo.",
                "",
            ]
        )

        laboratorio = cls()

        laboratorio.exibir()

        return laboratorio