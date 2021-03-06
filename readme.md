O presente projeto foi desenvolvido como atividade para a disciplina de Sistemas Operacionais (turma 2021.1) do curso de Engenharia de Computação da Universidade Tecnológica Federal do Paraná, campus Toledo.

========================================================

Você foi contratado para automatizar (simular) um treino de Fórmula 1. 
Os  requisitos estabelecidos pela direção do treino são as seguintes:

========================================================

R1) Há 7 escuderias e cada uma delas possui 2 carros.

R2) No máximo 5 carros das 7 escuderias podem entrar na pista simultaneamente para realizar cada ciclo de voltas de treino.

R3) Não é permitido que dois carros da mesma escuderia treinem na pista simultaneamente.

R4) Considere que um carro treina na pista por um número aleatório de voltas variando entre 4 e 12 (chamado de ciclo de voltas), que pode ser gerado quando o carro entra na pista. Cada carro pode entrar na pista e sair dela por até 2 vezes. Assim, cada carro pode realizar 2 ciclos de voltas (com cada ciclo variando entre 4 e 12 voltas).

R5) O momento e a ordem de entrada na pista deve ser aleatório. Caso haja disponibilidade para entrar, um carro deve aguardar um tempo aleatório entre 100ms e 500ms para realizar a entrada. O carro só é considerado como sendo parte do treino após transcorrido este tempo (evento de entrar na pista). O evento de saída da pista é considerado como imediato (0 ms para sair)

R6) Cada volta de cada carro que entrar na pista deverá ser modelado por um tempo aleatório (simbólico), medido em milissegundos (ms), que pode variar entre 1000ms e 1400ms. Para o mesmo carro, suas voltas dentro de um ciclo poderão variar +/- 10% do tempo gerado para a primeira volta (volta de entrada)

Exemplo: Carro entra na pista e seu primeiro tempo de volta aleatório é gerado como 1100ms, para um também número aleatório de voltas de 5.

Suas próximas voltas poderão ter um tempo aleatório de menos 10% ou mais 10%.

Mínimo: 1100ms – (110ms) = 990ms => só que o mínimo é 1000ms => 1000ms.

Máximo: 1100ms + (110ms) = 1210ms.

As 5 (cinco) voltas neste exemplo deverão ser de tempos aleatórios entre 1000ms e 1210ms, sendo que a primeira será de 1100ms.

R7) O tempo total máximo de treino deverá ser de 60 segundos (ou 60.000ms). Ao final deste tempo, todos os carros devem deixar imediatamente a pista, mesmo que não tenham completado o total de voltas.

R8) Faça uma solução multithread para simular o processo de treino de acordo com as regras citadas. O paralelismo de execução deve aparecer no fato de que os carros devem ser representados por threads.

R9) A solução deverá fazer o uso de semáforos, monitores, ou mecanismo de controle de concorrência similar, para controlar a quantidade máxima de carros na pista, bem como controlar a quantidade de carros por equipe que estão em treino.

R10) Para verificar sua solução exiba na tela informações sobre os carros em treinamento de forma organizada, com no mínimo os seguintes dados, na seguinte ordem:

Quando um carro entrar, mostrar:

·       ID do Carro e ID da escuderia (ex: E1C1, E2C2, E5C2 etc...)

·       Sinalizar que é uma entrada na pista.

·       Momento exato de entrada em milissegundos (ms), após passado o tempo de espera.

·       Número de ciclo de voltas do carro (Ciclo 1 ou 2. Pode ser abreviado: CC1 ou CC2)

·       Número da volta inicial

·       Número de voltas faltantes esperadas.

·       Número total de carros na pista naquele momento (incluindo o carro que entrou).

 

Quando um carro completar uma volta, mostrar:

·       ID do Carro e ID da escuderia.

·       Sinalizar que é uma volta sendo completada.

·       Momento exato que completou a volta em milissegundos (ms).

·       Número de ciclo de voltas do carro

·       Número da volta completada

·       Número de voltas faltantes esperadas.

·       Número total de carros na pista naquele momento.

 

Quando um carro sair, mostrar:

·       ID do Carro e ID da escuderia.

·       Sinalizar que é uma saída da pista.

·       Momento exato de saída em milissegundos (ms).

·       Número de ciclo de voltas do carro

·       Número da volta final completada.

·       Número de voltas faltantes esperadas.

·       Número total de carros na pista naquele momento (descontar o carro que saiu).

========================================================

OBS: Sugere-se implementar um recurso para  “ligar/desligar” a geração do arquivo de log em arquivo de texto ao realizar a demonstração em sala, pois isso interfere nos tempos e resultados (fica pesado e lento).

========================================================
