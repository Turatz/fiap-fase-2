from opcoes import menu
from modulos.habitacao import Habitacao

modulos_inicial = [
    {
        "rotulo": "Combustível",
        "tipo": "combustivel",
        "prioridade": 5,
        "criticidade": 5,
        "integridade": True,
        "detalhes": {
            "combustivel_kg": 70,
            "capacidade_tanque_kg": 100,
            "consumo_pouso_kg": 50,
            "consumo_decolagem_kg": 0,
        }
    },
]

def main():
    while True: #verificar pouso, iniciar pouso, prencher informações
        opcao = menu()
        
        match opcao:
            case "1":
                habitacao = Habitacao.cadastrar()
                habitacao.exibir()
                

main()