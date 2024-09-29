# Importación de "heapq", es una estructura de cola de prioridad que siempre devuelve el elemento con menor valor de prioridad
import heapq

# Función heurística, esta función calcula la distancia estimada desde la posición actual hasta la posición objetivo
def heuristica(pos_actual, pos_objetivo):
    return abs(pos_actual - pos_objetivo)

def busqueda_heuristica_a_estrella(pos_actual, pos_objetivo, delta_h):
    # Cola de prioridad que almacena las posiciones a explorar. La cola prioriza los elementos con menor costo f(n)
    cola = []
    # Agregamos la posición inicial a la cola con un coste inicial de 0
    heapq.heappush(cola, (0, pos_actual))
    
    while cola:
        # Extraemos la posición con el menor valor de f(n) de la cola de prioridad
        _, pos_actual = heapq.heappop(cola)
        
        # Comprobamos si la posición actual está lo suficientemente cerca de la posición objetivo
        if abs(pos_actual - pos_objetivo) <= delta_h:
            return pos_actual
        
        # Generamos las posiciones vecinas a partir de la posición actual
        for siguiente_pos in [pos_actual + delta_h, pos_actual - delta_h]:

            # Calculamos el costo heurístico (h(n)) desde la posición siguiente hacia el objetivo
            costo = heuristica(siguiente_pos, pos_objetivo)
            heapq.heappush(cola, (costo, siguiente_pos))
    
    return None

# Parametros, como ejemplo
pos_inicial = 0  # Posición inicial
pos_objetivo = 10  # Posición objetivo
delta_h = 0.1  # Paso 

resultado = busqueda_heuristica_a_estrella(pos_inicial, pos_objetivo, delta_h)
print(f"Posición encontrada: {resultado}")
