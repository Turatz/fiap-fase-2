from modulos.habitacao import Habitacao
from modulos.combustivel import Combustivel


class Nave:
    def __init__(self):
        self.modulos = {
            "habitacao": {
                "classe": Habitacao,
                "nome": "Tripulação e suporte à vida",
                "objeto": None
            },

            "combustivel": {
                "classe": Combustivel,
                "nome": "Combustível",
                "objeto": None
            }
        }

    def configurar_modulo(self, tipo):
        modulo = self.modulos[tipo]

        modulo["objeto"] = modulo["classe"].cadastrar()

    def exibir_modulo(self, tipo):
        modulo = self.modulos[tipo]

        if modulo["objeto"] is not None:
            modulo["objeto"].exibir()
            
    def editar_modulo(self, tipo):
        modulo = self.modulos[tipo]

        if modulo["objeto"] is not None:
            modulo["objeto"].editar()


    def simular_missao(self):
        pass