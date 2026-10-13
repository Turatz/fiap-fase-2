Requisitos do sistema — MGPEB

Projeto de gerenciamento de módulos de uma nave e simulação de pousos em Marte.

Funcionalidades
•Cadastrar os módulos de habitação, combustível, energia, temperatura, laboratório, logística e suporte médico.
•Visualizar os dados e a situação de cada módulo.
•Editar módulos ainda não pousados, preservando os dados anteriores quando a edição for inválida.
•Registrar prioridade, combustível do veículo de pouso, massa, instante de chegada e integridade dos sensores.
•Calcular disponibilidade e autonomia de combustível, energia, água e oxigênio.
•Ordenar a fila operacional de pouso.
•Verificar as condições individuais e a disponibilidade global de combustível. Módulos em espera por chegada, atmosfera ou área não impedem o processamento dos demais autorizados.
•Solicitar os consumos de frenagem e correção ao operador.
•Simular o pouso sequencial, descontar combustível e apresentar os resultados das etapas e da missão.
•Manter listas de módulos pousados, em espera e em alerta, além do histórico de estados.
•Buscar módulos por tipo, menor percentual de combustível ou maior prioridade.
•Consultar o topo da pilha sem removê-lo; a retirada é opcional e não desfaz um pouso.
•Carregar um exemplo hipotético apenas quando a nave estiver vazia.
•Encerrar o programa pelo menu principal.

Requisitos técnicos
•Utilizar Python 3.10 ou superior, devido ao uso de match/case.
•Executar pelo terminal, com entrada por teclado e saída textual.
•Não exigir bibliotecas externas.
•Organizar a lógica com classes, funções, listas e dicionários.
•Tratar entradas numéricas inválidas e validar os limites dos dados cadastrados.
•Manter os dados em memória durante a execução, sem banco de dados ou gravação em arquivo.

Regras de funcionamento
•Prioridade e criticidade devem estar entre 1 e 5. O módulo de combustível utiliza prioridade -1 e pousa por último.
•A fila operacional considera maior prioridade, menor criticidade, menor percentual de combustível e chegada mais cedo, nessa ordem. Neste projeto, 1 indica maior criticidade e 5 menor criticidade. Empates completos preservam a ordem de cadastro. Combustível permanece por último.
•A energia deve apresentar carga mínima de 20% e integridade operacional.
•Cada veículo de pouso deve apresentar combustível mínimo de 50%. Esse percentual é diferente do estoque global de combustível em quilogramas.
•A temperatura interna permitida é de 15 a 35 °C, e a externa de 5 a 45 °C, incluindo os limites.
•O pouso exige módulo e sensores íntegros, chegada já ocorrida, atmosfera favorável e área livre.
•A reserva por módulo corresponde a uma frenagem mais duas correções, com valores positivos informados pelo operador. A detecção de obstáculos permite no máximo duas correções.
•O estoque global deve cobrir o consumo de todos os módulos pendentes antes de iniciar a missão.
•Falhas nas condições críticas geram alerta. Restrições de atmosfera, área ou chegada geram espera quando as condições críticas estão atendidas.
•Quantidades físicas não podem ser negativas. Temperaturas podem ser negativas no cadastro, mas devem respeitar as faixas de autorização para o pouso.
•Capacidades devem ser positivas. Combustível, carga da bateria, tripulação e alimentos não podem exceder suas respectivas capacidades.
•A missão termina com sucesso quando os sete módulos estão cadastrados e com pouso concluído.

Dependências
•Python 3.10 ou superior.
•Terminal para executar o programa.
•Nenhum pacote externo: não é necessário executar pip install.

Limitações
•Interface exclusivamente pelo terminal.
•Dados e histórico não são preservados após encerrar o programa.
•Simulação acadêmica com dados hipotéticos, sem validação científica de uma missão real.