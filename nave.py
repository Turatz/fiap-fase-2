from modulos.habitacao import Habitacao
from modulos.combustivel import Combustivel
from modulos.energia import Energia
from modulos.temperatura import Temperatura
from modulos.laboratorio import Laboratorio
from modulos.logistica import Logistica
from modulos.suporte_medico import SuporteMedico
from modulos.modulos import Modulo
from visuais.exibir_card import exibir_card


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
                "prioridade" : -1,
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

    @staticmethod
    def _classificar_condicoes(
        combustivel_suficiente,
        modulo_integro,
        atmosfera_favoravel,
    ):
        condicoes = (
            combustivel_suficiente,
            modulo_integro,
            atmosfera_favoravel,
        )
        if any(not isinstance(condicao, bool) for condicao in condicoes):
            raise ValueError("Condições devem ser booleanas.")

        condicoes_criticas_atendidas = (
            combustivel_suficiente and modulo_integro
        )
        alerta = not condicoes_criticas_atendidas
        em_espera = condicoes_criticas_atendidas and not atmosfera_favoravel

        decisao = (
            "alerta" if alerta
            else "em_espera" if em_espera
            else "autorizado"
        )
        return decisao

    def _avaliar_autorizacao(
        self,
        objeto,
        combustivel_suficiente,
        atmosfera_favoravel,
    ):
        return self._classificar_condicoes(
            combustivel_suficiente,
            objeto is not None and objeto.integridade,
            atmosfera_favoravel,
        )

    def _verificar_modulos(self):
        combustivel = self.modulos["combustivel"]["objeto"]
        temperatura = self.modulos["temperatura"]["objeto"]

        combustivel_por_modulo = (
            Modulo.COMBUSTIVEL_FRENAGEM_KG
            + 2 * Modulo.COMBUSTIVEL_CORRECAO_KG
        )
        combustivel_necessario = len(self.modulos) * combustivel_por_modulo
        combustivel_suficiente = (
            combustivel is not None
            and combustivel.integridade
            and combustivel.combustivel_kg >= combustivel_necessario
        )
        temperatura_interna_ok = (
            temperatura is not None
            and 15 <= temperatura.temperatura_interna <= 35
        )
        temperatura_externa_ok = (
            temperatura is not None
            and 5 <= temperatura.temperatura_externa <= 45
        )
        atmosfera_favoravel = temperatura_interna_ok and temperatura_externa_ok

        linhas = []
        todos_autorizados = True
        for tipo, info in self.modulos.items():
            objeto = info["objeto"]
            resultado = self._avaliar_autorizacao(
                objeto,
                combustivel_suficiente,
                atmosfera_favoravel,
            )
            autorizado = resultado == "autorizado"
            todos_autorizados = todos_autorizados and autorizado
            status_modulo = (
                "não cadastrado" if objeto is None
                else "íntegro" if objeto.integridade
                else "inoperante"
            )
            linhas.append(
                f"{'✅' if autorizado else '❌'} {tipo}: "
                f"{status_modulo}, {resultado}"
            )

        linhas.extend((
            f"Temperatura interna: {'Ok' if temperatura_interna_ok else 'Falha'}",
            f"Temperatura externa: {'Ok' if temperatura_externa_ok else 'Falha'}",
            f"Combustível necessário: {combustivel_necessario:.2f} kg",
            f"Combustível disponível: {combustivel.combustivel_kg:.2f} kg"
            if combustivel is not None
            else "Combustível disponível: não cadastrado",
        ))
        exibir_card(
            "Autorização de pouso",
            "Verificação de cadastro e condições por módulo:",
            linhas,
        )
        input("Pressione Enter para continuar...")
        return todos_autorizados

    def pousar_modulo(self, tipo):
        modulo = self.modulos[tipo]

        if modulo["objeto"] is not None:
            modulo["objeto"].pousar()

    def simular_missao(self):
        if not self._verificar_modulos():
            exibir_card(
                "Missão não iniciada",
                "As verificações iniciais não foram aprovadas.",
                ["Corrija os módulos e tente novamente."],
            )
            input("Pressione Enter para continuar...")
            return False

        combustivel = self.modulos["combustivel"]["objeto"]
        quantidade_por_modulo = (
            Modulo.COMBUSTIVEL_FRENAGEM_KG
            + 2 * Modulo.COMBUSTIVEL_CORRECAO_KG
        )
        fila_pouso = sorted(
            (
                (tipo, info)
                for tipo, info in self.modulos.items()
                if tipo != "combustivel"
            ),
            key=lambda item: item[1]["prioridade"],
            reverse=True,
        )
        fila_pouso.append(("combustivel", self.modulos["combustivel"]))

        resultados = {}
        for tipo, info in fila_pouso.copy():
            objeto = info["objeto"]
            etapa_sucesso = False
            mensagem = ""

            if objeto.pouso_concluido:
                etapa_sucesso = True
                mensagem = "Este módulo já havia pousado."
            elif combustivel.combustivel_kg < quantidade_por_modulo:
                mensagem = "Pouso não realizado: combustível insuficiente."
            else:
                combustivel.consumir(quantidade_por_modulo)
                objeto.abastecer(quantidade_por_modulo)
                etapa_sucesso = objeto.pousar()
                mensagem = (
                    "Pouso realizado com sucesso."
                    if etapa_sucesso
                    else "Falha durante o pouso."
                )

            resultados[tipo] = etapa_sucesso
            fila_pouso.remove((tipo, info))
            proximos = [
                tipo_pendente.capitalize()
                for tipo_pendente, _ in fila_pouso
            ]
            linhas_etapa = [
                mensagem,
                f"Combustível restante: {combustivel.combustivel_kg:.2f} kg",
                "Módulos aguardando:",
                *(proximos or ["Nenhum"]),
            ]

            exibir_card(
                f"Etapa de pouso: {tipo}",
                info["nome"],
                linhas_etapa,
            )

            input("Pressione Enter para continuar...")

        resumo = []
        for tipo, info in self.modulos.items():
            objeto = info["objeto"]
            situacao = (
                "não cadastrado" if objeto is None
                else "operacional" if objeto.integridade
                else "inoperante"
            )
            status_pouso = (
                "pouso realizado" if resultados.get(tipo)
                else "pouso não realizado"
            )
            resumo.append(f"{tipo}: {situacao}; {status_pouso}")
        missao_concluida = all(resultados.values())
        resumo.insert(
            0,
            "Resultado da missão: "
            f"{'sucesso' if missao_concluida else 'falha'}",
        )
        exibir_card("Resumo da missão", "Status final dos módulos:", resumo)
        input("Pressione Enter para continuar...")
        return missao_concluida
