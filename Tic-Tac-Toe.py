import time
from MonteCarlo import gameSimulation
from lab6_2 import ejecutar_experimentos
from minimax1 import ejecutar_experimentos_sin_poda

def generar_tabla():
    variantes = [
        ("Minimax", 3, "X"),
        ("Minimax", 3, "O"),
        ("Minimax", 5, "X"),
        ("Minimax", 5, "O"),
        ("Minimax α-β", 3, "X"),
        ("Minimax α-β", 3, "O"),
        ("Minimax α-β", 5, "X"),
        ("Minimax α-β", 5, "O"),
        ("MCTS", 0.1, "X"),
        ("MCTS", 0.1, "O"),
        ("MCTS", 0.2, "X"),
        ("MCTS", 0.2, "O"),
    ]

    print(f"{'Algoritmo':<14} | {'k/t':<5} | {'Empieza':<8} | {'Victorias':<9} | {'Empates':<7} | {'Derrotas':<8} | {'Tiempo (s)':<10}")
    print("-" * 100)

    for algoritmo, param, primero in variantes:
        start = time.time()

        if algoritmo == "Minimax":
            victorias, empates, derrotas = ejecutar_experimentos_sin_poda(primero, N=1000, k=param)
        elif algoritmo in ["MinimaxAB", "Minimax α-β"]:
            victorias, empates, derrotas = ejecutar_experimentos(primero, N=1000, k=param)
        elif algoritmo == "MCTS":
            winX, winO, draws = gameSimulation(primero, N=1000, t=param)
            empates = draws
            if primero == 'X':
                victorias = winX
                derrotas = 1000 - winX - draws
            else:
                victorias = winO
                derrotas = 1000 - winO - draws
        else:
            continue

        end = time.time()
        tiempo = round(end - start, 2)

        print(f"{algoritmo:<14} | {param:<5} | {primero:<8} | {victorias:<9} | {empates:<7} | {derrotas:<8} | {tiempo:<10}")

if __name__ == "__main__":
    generar_tabla()
