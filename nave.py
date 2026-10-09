from modulos.habitacao import Habitacao
from modulos.combustivel import Combustivel
from modulos.energia import Energia
from modulos.temperatura import Temperatura
from modulos.laboratorio import Laboratorio
from modulos.logistica import Logistica
from modulos.suporte_medico import SuporteMedico


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
            },

            "temperatura": {
                "classe": Temperatura,
                "prioridade": 3,
                "nome": "Temperatura Interna e Externa",
                "objeto": None
            },

            "laboratorio": {
                "classe": Laboratorio,
                "prioridade": 3,
                "nome": "Laboratório",
                "objeto": None
            },

            "logistica": {
                "classe": Logistica,
                "prioridade": 2,
                "nome": "Logística",
                "objeto": None
            },

            "suporte_medico": {
                "classe": SuporteMedico,
                "prioridade": 2,
                "nome": "Suporte Médico",
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