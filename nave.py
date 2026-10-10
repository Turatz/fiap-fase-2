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
                "nome": "Tripulação e suporte à vida",
                "prioridade" : 5 ,
                "objeto": None
            },

            "combustivel": {
                "classe": Combustivel,
                "nome": "Combustível",
                "prioridade" : 5,
                "objeto": None
            },

            "energia": {
                "classe": Energia,
                "nome": "Energia",
                "prioridade" : 4,
                "objeto": None
            },

            "temperatura": {
                "classe": Temperatura,
                "nome": "Temperatura Interna e Externa",
                "prioridade" : 3,
                "objeto": None
            },

            "laboratorio": {
                "classe": Laboratorio,
                "nome": "Laboratório",
                "prioridade" : 2,
                "objeto": None
            },

            "logistica": {
                "classe": Logistica,
                "nome": "Logística",
                "prioridade" : 2 ,
                "objeto": None
            },

            "suporte_medico": {
                "classe": SuporteMedico,
                "nome": "Suporte Médico",
                "prioridade" : 4,
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