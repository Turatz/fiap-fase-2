class Modulo:
    """Estrutura comum a todos os módulos da nave."""

    def __init__(self, rotulo, tipo, prioridade, criticidade, integridade=True):
        self.rotulo = rotulo
        self.tipo = tipo
        self.prioridade = prioridade
        self.criticidade = criticidade
        self.integridade = integridade
