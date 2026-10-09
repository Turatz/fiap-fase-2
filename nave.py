from modulos.habitacao import Habitacao
from modulos.combustivel import Combustivel
from modulos.energia import Energia

class Nave:
    def __init__(self):
        self.modulos = {
            "habitacao": {
                "classe": Habitacao,
                "prioridade": 4,
                "nome": "Tripulação e suporte à vida",
                "objeto": None
            },

            "combustivel": {
                "classe": Combustivel,
                "prioridade": 5,
                "nome": "Combustível",
                "objeto": None
            },

            "energia": {
                "classe": Energia,
                "prioridade": 4,
                "nome": "Energia",
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