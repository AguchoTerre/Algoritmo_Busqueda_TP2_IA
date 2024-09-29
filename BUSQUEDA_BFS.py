# Importación de "deque", es una estructura de datos de cola doble, que permite agregar y quitar elementos de ambos extremos
from collections import deque 

def busqueda_exhaustiva_bfs(pos_inicial, pos_objetivo, delta_h, limite_izquierdo, limite_derecho, max_cola_size):
    # Inicializamos la cola con la posición inicial y un conjunto de posiciones visitadas
    cola = deque([pos_inicial])
    visitados = set([pos_inicial])
    
    while cola:
        # Controlamos el tamaño de la cola para evitar consumir demasiada memoria
        if len(cola) > max_cola_size:
            print("Tamaño máximo de la cola alcanzado. Deteniendo la búsqueda.")
            return None
        
        # Extraemos la posición actual de la cola
        pos_actual = cola.popleft()
        
        # Comprobamos si hemos alcanzado la posición objetivo
        if abs(pos_actual - pos_objetivo) <= delta_h:
            return pos_actual
        
        # Calculamos las nuevas posiciones a explorar
        nueva_pos_derecha = pos_actual + delta_h
        nueva_pos_izquierda = pos_actual - delta_h
        
        # Exploramos la posición derecha si está dentro del límite y no ha sido visitada
        if nueva_pos_derecha <= limite_derecho and nueva_pos_derecha not in visitados:
            cola.append(nueva_pos_derecha)
            visitados.add(nueva_pos_derecha)
        
        # Exploramos la posición izquierda
        if nueva_pos_izquierda >= limite_izquierdo and nueva_pos_izquierda not in visitados:
            cola.append(nueva_pos_izquierda)
            visitados.add(nueva_pos_izquierda)
    
    return None 

# Parametros, como ejemplo
pos_inicial = 0  # Posición inicial "B"
pos_objetivo = 11  # Posición objetivo "A"
delta_h = 0.1  # Paso
limite_izquierdo = -100  # Límite de búsqueda a la izquierda
limite_derecho = 100  # Límite derecho
max_cola_size = 10000  # Límite de tamaño de la cola para evitar desbordamientos de memoria

resultado = busqueda_exhaustiva_bfs(pos_inicial, pos_objetivo, delta_h, limite_izquierdo, limite_derecho, max_cola_size)
print(f"Posición encontrada: {resultado}")

