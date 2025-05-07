import random
import copy

def posibles_movimientos(tablero):
    return [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == ' ']

def make_move(tablero, move, jugador):
    nuevo = copy.deepcopy(tablero)
    nuevo[move[0]][move[1]] = jugador
    return nuevo

def evaluar_ganador(tablero):
    lineas = []

    for i in range(3):
        lineas.append(tablero[i])
        lineas.append([tablero[0][i], tablero[1][i], tablero[2][i]])
    lineas.append([tablero[0][0], tablero[1][1], tablero[2][2]])
    lineas.append([tablero[0][2], tablero[1][1], tablero[2][0]])

    for linea in lineas:
        if linea[0] != ' ' and linea[0] == linea[1] == linea[2]:
            return linea[0]
    return None

def evaluar_heuristica(tablero, jugador):
    oponente = 'O' if jugador == 'X' else 'X'
    score = 0
    lineas = []

    for i in range(3):
        lineas.append(tablero[i])
        lineas.append([tablero[0][i], tablero[1][i], tablero[2][i]])
    lineas.append([tablero[0][0], tablero[1][1], tablero[2][2]])
    lineas.append([tablero[0][2], tablero[1][1], tablero[2][0]])

    for linea in lineas:
        if linea.count(jugador) == 3:
            return 10
        if linea.count(oponente) == 3:
            return -10
        if linea.count(jugador) == 2 and linea.count(' ') == 1:
            score += 5
        if linea.count(oponente) == 2 and linea.count(' ') == 1:
            score -= 5

    if tablero[1][1] == jugador:
        score += 3
    for i, j in [(0,0), (0,2), (2,0), (2,2)]:
        if tablero[i][j] == jugador:
            score += 2
    for i, j in [(0,1), (1,0), (1,2), (2,1)]:
        if tablero[i][j] == jugador:
            score += 1

    return score

def minimax(tablero, profundidad, es_max, alpha, beta, jugador, contador):
    contador[0] += 1
    oponente = 'O' if jugador == 'X' else 'X'
    ganador = evaluar_ganador(tablero)
    
    if ganador == jugador:
        return 10
    elif ganador == oponente:
        return -10
    elif not posibles_movimientos(tablero) or profundidad == 0:
        return evaluar_heuristica(tablero, jugador)

    if es_max:
        max_eval = -float('inf')
        for move in posibles_movimientos(tablero):
            nuevo = make_move(tablero, move, jugador)
            eval = minimax(nuevo, profundidad - 1, False, alpha, beta, jugador, contador)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in posibles_movimientos(tablero):
            nuevo = make_move(tablero, move, oponente)
            eval = minimax(nuevo, profundidad - 1, True, alpha, beta, jugador, contador)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def obtener_mejor_movimiento(tablero, jugador, profundidad):
    mejor_valor = -float('inf')
    mejor_mov = None
    contador = [0]

    for move in posibles_movimientos(tablero):
        nuevo_tablero = make_move(tablero, move, jugador)
        valor = minimax(nuevo_tablero, profundidad - 1, False, -float('inf'), float('inf'), jugador, contador)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_mov = move

    return mejor_mov, contador[0]

def jugar_aleatorio(tablero, jugador):
    movimientos = posibles_movimientos(tablero)
    if movimientos:
        move = random.choice(movimientos)
        return make_move(tablero, move, jugador)
    return tablero

def simular_juego(k, quien_empieza):
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    turno = quien_empieza
    jugador = 'X'
    oponente = 'O'
    nodos = 0

    while evaluar_ganador(tablero) is None and posibles_movimientos(tablero):
        if turno == jugador:
            move, nodos_turno = obtener_mejor_movimiento(tablero, jugador, k)
            if move:
                tablero = make_move(tablero, move, jugador)
                nodos += nodos_turno
        else:
            tablero = jugar_aleatorio(tablero, oponente)
        turno = oponente if turno == jugador else jugador

    resultado = evaluar_ganador(tablero)
    if resultado == jugador:
        return 1, nodos
    elif resultado == oponente:
        return -1, nodos
    else:
        return 0, nodos

def ejecutar_experimentos(N=1000, k=3):
    victorias = empates = derrotas = nodos_total = 0

    for _ in range(N):
        primero = random.choice(['X', 'O'])
        print("Empieza el jugador, ",primero)
        resultado, nodos = simular_juego(k, primero)
        nodos_total += nodos
        if resultado == 1:
            victorias += 1
        elif resultado == -1:
            derrotas += 1
        else:
            empates += 1

    print(f"Simulaciones: {N}")
    print(f"✅ Victorias de X: {victorias}")
    print(f"🤝 Empates: {empates}")
    print(f"❌ Derrotas: {derrotas}")
    print(f"📊 Promedio de nodos explorados: {nodos_total / N:.2f}")


ejecutar_experimentos(N=1000, k=3)