from visuais.exibir_card import exibir_card
from modulos.modulos import Modulo


class SuporteMedico(Modulo):
    def __init__(
        self,
        leitos,
        kits_emergencia
    ):
        super().__init__("Suporte Médico", "suporte_medico", 2, 3)

        # Dados informados pelo usuário
        self.leitos = leitos
        self.kits_emergencia = kits_emergencia

    def exibir(self):
        exibir_card(
            self.rotulo.upper(),
            "Informações do módulo",
            [
                "",
                f"Quantidade de leitos: {self.leitos}",
                "",
                f"Kits de emergência: {self.kits_emergencia}",
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

        self.leitos = int(
            input(
                f"Quantidade de leitos "
                f"[{self.leitos}]: "
            )
        )

        self.kits_emergencia = int(
            input(
                f"Quantidade de kits de emergência "
                f"[{self.kits_emergencia}]: "
            )
        )

    @classmethod
    def cadastrar(cls):
        exibir_card(
            "SUPORTE MÉDICO",
            "Cadastro do módulo",
            [
                "",
                "Informe os dados necessários:",
                "",
            ]
        )

        leitos = int(
            input("Quantidade de leitos: ")
        )

        kits_emergencia = int(
            input("Quantidade de kits de emergência: ")
        )

        suporte_medico = cls(
            leitos,
            kits_emergencia
        )

        suporte_medico.exibir()

        return suporte_medico
