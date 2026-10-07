modulos = [
    {
        "rotulo": "Tripulação e suporte à vida",
        "tipo": "habitacao",
        "prioridade": 4,
        "criticidade": 4,
        "integridade": True,
        "detalhes": {
            "capacidade_pessoas": 8,
            "oxigenio": 100,
        }
    },

    {
        "rotulo": "Combustivel",
        "tipo": "combustivel",
        "prioridade": 5,
        "criticidade": 5,
        "combustivel": 70,
        "integridade": True,
        "detalhes": {
            "carga": 70,
            "capacidade_kwh": 100,
        }
    },

    {
        "rotulo": "Energia",
        "tipo": "energia",
        "prioridade": 5,
        "criticidade": 5,
        "combustivel": 70,
        "energia": 80,
        "integridade": True,
        "detalhes": {
            "capacidade_kwh": 100
        }
    },

    {
        "rotulo": "Temperatura Interna e Externa",
        "tipo": "temperatura",
        "prioridade": 3,
        "criticidade": 1,
        "temperatura_interna": 25,
        "temperatura_externa": 20,
        "integridade": True,
        "detalhes": {
            "descricao": "Controle de temperatura interna e externa do modulo"
        }
    },

    {
        "rotulo": "Laboratório",
        "tipo": "laboratorio",
        "prioridade": 3,
        "criticidade": 1,
        "integridade": True,
        "detalhes": {}
    },

    {
        "rotulo": "Logística",
        "tipo": "logistica",
        "prioridade": 2,
        "criticidade": 2,
        "integridade": True,
        "detalhes": {
            "capacidade_carga_kg": 500,
            "alimentos_kg": 100,
        }
    },

    {
        "rotulo": "Suporte Médico",
        "tipo": "suporte_medico",
        "prioridade": 2,
        "criticidade": 3,
        "integridade": True,
        "detalhes": {
            "leitos": 4,
            "kits_emergencia": 10,
        }
    }
]
