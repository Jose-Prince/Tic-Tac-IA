from MonteCarlo import gameSimulation
from lab6_2 import ejecutar_experimentos
from minimax1 import ejecutar_experimentos_sin_poda

if __name__ == "__main__":
    statsMinimax = ejecutar_experimentos_sin_poda()
    statsMinimaxAB = ejecutar_experimentos()
    statsMCTS = gameSimulation()
