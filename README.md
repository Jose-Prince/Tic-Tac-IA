Inciso 1 y 2 heuristica

+10 si el jugador ha ganado (ha completado una línea).

-10 si el oponente ha ganado.

+5 por cada "doble" del jugador (dos marcas en una línea con un espacio vacío).

-5 por cada "doble" del oponente.

+3 por tener una marca en el centro.

+2 por tener una marca en una esquina.

+1 por tener una marca en un borde.

# Comparación algoritmos:

| Algoritmo      | k/t   | Empieza | Victorias | Empates | Derrotas | Tiempo (s) |
|----------------|-------|---------|-----------|---------|----------|-------------|
| Minimax        | 3     | X       | 980       | 0       | 20       | 12.98       |
| Minimax        | 3     | O       | 884       | 1       | 115      | 5.75        |
| Minimax        | 5     | X       | 947       | 0       | 53       | 214.23      |
| Minimax        | 5     | O       | 843       | 36      | 121      | 87.44       |
| Minimax α-β    | 3     | X       | 970       | 0       | 30       | 5.69        |
| Minimax α-β    | 3     | O       | 884       | 1       | 115      | 3.87        |
| Minimax α-β    | 5     | X       | 949       | 0       | 51       | 55.38       |
| Minimax α-β    | 5     | O       | 863       | 18      | 119      | 26.96       |
| MCTS           | 0.1   | X       | 406       | 342     | 252      | 370.29      |
| MCTS           | 0.1   | O       | 319       | 224     | 457      | 444.62      |
| MCTS           | 0.2   | X       | 409       | 343     | 248      | 746.19      |
| MCTS           | 0.2   | O       | 304       | 217     | 479      | 873.68      |

Viendo los datos de la tabla, se puede sacar varias conclusiones. La primera de ellas es que el MCTS (Monte Carlo Tree Search) presenta el mayor tiempo de ejecución y el peor ratio de victorias tanto si empieza el juego con "X" o con "O". Otra dato interesante que obtenemos al analizar el algoritmo minimax (tanto con como sin α-β prunning) se ve que al aumentar la profundidad con la que se ve en el arbol aumenta la cantidad de empates. Viendo los diferentes algoritmos se nota que el mejor de estos 3 es el minimax con α-β prunning debido a que presenta una gran probabilidad de ganar tanto si empieza o si no empieza a jugar la IA, además el tiempo de ejecución mejora circunstancial en el tiempo de ejecución al hacerle esta mejora al minimax.
