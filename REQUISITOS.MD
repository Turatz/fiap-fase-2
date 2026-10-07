# 1. Coletar dados Iniciais

- Durante essa etapa deve se coletar os dados seguindo a estrutura pré definida em modulos.py, cada modulo deve seguir a estrutura abaixo 

```
{
    "rotulo": "str" # Descrição humanizada do nome do Modulo
    "tipo": "str" # Nome Simplificado EX: "habitaco" | "energia" | "laboratorio" | "logistica" | "suporte_medico" 
    "criticidade": int, # Cricidade do Modulo de 1 a 5 (Sendo 5 o meno critico e o 1 o mais critico)
    "integridade": bool # Integridade do Modulo True -> Tudo certo, False -> Algum problema
    "detalhes": { } -> Essa estrutura de dados, representa as informações individuais de cada modulo,
},
```

- Durante a etapa de coleta o usuario deve ser informado de qual modulo ele esta preenchendo, e deve ser feito perguntas especificas para cada tipo, por exmeplo para energia o usuario será perguntado sobre questões da Carga da Bateria, Consumo médio e etc

---

# 2. Ordenação por criticidade

Após ser gerado a lista com os dados de coleta inicial, o programa deve ordenar em uma fila por ordem de criticidade, usando um metódo de Sort

# 3. Verificação de Modulos

Após isso deve ser iniciado uma verificação dos modulos individualmente, cada modulo terá suas regras internas, além disso eles possuem 3 estados

- **pousados**: Modulos do Foguete que foram Pousados com sucesso
- **em espera**: Modulos que estão esperando para serem pousados
- **Em situação de Alerta**:  Modulos que estão com algum impeditivo para serem pousados

# 4. Analise dos resultados

Após todas as verificações deve ser exibido um texto mostrando o resultado do pouso, tal quanto graficos utilizando a biblioteca [MatPlotLib](https://matplotlib.org/2.0.2/users/pyplot_tutorial.html), para ser exibido detalhes do pouso