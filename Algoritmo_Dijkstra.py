# ================================================================= #
# ==================== DEFINICION DE VARIABLES ==================== #
# ================================================================= #

# Definición de las conexiones entre nodos de un grafo
nodos = [("A", "B", 3), ("A", "C", 1), ("A", "D", 10), ("C", "A", 1), ("C", "D", 2), ("C", "B", 7),("D", "A", 10), ("D", "C", 2),
         ("D", "E", 7), ("D", "B", 5), ("B", "A", 1), ("B", "C", 7), ("B", "D", 5), ("B", "E", 1), ("E", "B", 1), ("E", "D", 7)]

# Definición de las conexiones entre nodos de un grafo distinto al anterior
nodos2 = [("A", "B", 16), ("A", "C", 10), ("A", "D", 5), ("B", "A", 16), ("B","C", 2), ("B", "G", 6),
          ("B", "F", 4), ("C", "A", 10), ("C", "B", 2), ("C", "D", 4), ("C", "F", 12), ("C", "E", 10),
          ("D", "A", 5), ("D", "C", 4), ("D", "E", 15), ("G", "B", 6), ("G", "F", 8), ("G", "Z", 7),
          ("F", "B", 4), ("F", "G", 8), ("F", "Z", 16), ("F", "C", 12),("F", "E", 3), ("E", "D", 15),
          ("E", "C", 10), ("E", "F", 3), ("E", "Z", 5)]

# Lista vacía para probrar las funciónes de creación y gestión de nodos
lista_nodos = []

# ================================================================= #
# ==================== DEFINICION DE FUNCIONES ==================== #
# ================================================================= #

# Función para añadir nodos con/ sin pesos y dirigidos o no
def add_node(node1, node2, nodes_list, weight=0, driven=False):
    node1 = node1.upper()
    node2 = node2.upper()
    
    if driven == False:
        nodes_list.append((node1, node2, weight))
        nodes_list.append((node2, node1, weight))
    
    else:
        nodes_list.append((node1, node2, weight))

# Función para añadir nodos en ambos sentidos o no
def erase_nodes(node1, node2, nodes_list, both=True):
    
    if both == True: # Si se quieren eliminar ambos sentidos
        
        for nodes in nodes_list[:]:
        
            if nodes[0] == node1 or nodes[0] == node2:
                nodes_list.remove(nodes)

    else: # Si solo se quieren borrar las conexiones en un sentido
        for nodes in nodes_list:
            if nodes[0] == node1:
                nodes_list.remove(nodes)

# Función que retorna los nodos adyacentes a un nodo dado
def find_adjacent_nodes(node, lista):
    adjacent_nodes = []
    
    for nodes in lista:
        if nodes[0] == node:
            adjacent_nodes.append(nodes[1])
    
    return adjacent_nodes

# Función que te retorna el peso que hay entre la conexión de dos nodos
def get_edges_weight(node1, node2, nodes_list):

    for nodes in nodes_list:
        if nodes[0] == node1 and nodes[1] == node2:
            return nodes[2]
        
    # Si la conexión no existe, lanzar una excepción
    raise ValueError(f"No se encontró una conexión entre los nodos {node1} y {node2}.")

# Función que te retorna todos los nodos del grafo
def get_all_nodes(lista):
    all_nodes = []
    
    for edges in lista:
        if edges[0] not in all_nodes:
            all_nodes.append(edges[0])
        if edges[1] not in all_nodes:
            all_nodes.append(edges[1])
    return all_nodes

# ================================================================= #
# ==================== DEFINICION DE ALGORITMOS =================== #
# ================================================================= #

# Función del algoritmo de Dijkstra que toma como parámetros el nodo inicial, el de destino y la lista que contiene definido el grafo con sus pesos en caso de haberlos y conexiones
def dijkstra_algorithm(start_node, end_node, lista_nodos):
    
    # Verifica si el nodo inicial y el nodo de destino están en la lista de nodos
    if start_node not in get_all_nodes(lista_nodos) or end_node not in get_all_nodes(lista_nodos):
        raise ValueError("El nodo de inicio o el nodo de destino no están en el grafo.")
    
    # Verifica si la lista de nodos está vacía
    if len(get_all_nodes(lista_nodos)) == 0:
        raise ValueError("La lista de nodos está vacía.")
    
    # Creación de la tabla donde se aplicarán los pasos del algoritmo de Dijkstra
    dijkstra_table = {}
    
    # Función que representa gráficamente la tabla de Dijkstra que utilizaremos para mostrar los pasos seguidos por el algoritmo
    def draw_dijkstra_table(dijkstra_table):
        
        print(f"{'|Nodos':<5} {'|Pesos':<15} {'|Vértices':<15} |Visitado|")
        print(f"{'|':-<6}-{'|':-<15}-{'|':-<15}-{'|':-<9}|")
        
        
        for index, node in enumerate(dijkstra_table):
            
            if index == len(dijkstra_table)-1:
                print(f"|{node:<5} |{' '.join(map(str, dijkstra_table[node]['Weights'])):<14} |{' '.join(map(str, dijkstra_table[node]['Edges'])):<14} |{dijkstra_table[node]['Visited']:^8}|")
                print(f"{'|':-<48}|")
                print("\n")
                
            else:   
                print(f"|{node:<5} |{' '.join(map(str, dijkstra_table[node]['Weights'])):<14} |{' '.join(map(str, dijkstra_table[node]['Edges'])):<14} |{dijkstra_table[node]['Visited']:^8}|")
                print(f"{'|':-<6}-{'|':-<15}-{'|':-<15}-{'|':-<9}|")
    
    # Crea la situación inicial de la tabla
    # Obtiene todos los nodos y los añade con su información a la tabla de Dijkstra
    for node in get_all_nodes(lista_nodos):
        
        if node == start_node: # Si el nodo es el inicial le asigna un peso 0
            dijkstra_table[node] = {"Weights": [0], "Edges": [], "Visited": "SI"}
        
        else: # Si el nodo no es el inicial les asigna peso X, simulando el infinito
            dijkstra_table[node] = {"Weights": ["X"], "Edges": [], "Visited": "NO"}
    
    draw_dijkstra_table(dijkstra_table) # Muestra la tabla inicial de Dijkstra por pantalla

    parent_node = start_node # Asignamos el nodo de inicio como el nodo pariente inicial
    not_visited_nodes = [] # Lista que contiene los nodos no visitados
    
    # Cargamos los nodos no visitados a la vista de nodos no visitados
    for node in dijkstra_table: 
        
        if dijkstra_table[node]["Visited"] == "NO": # Si no ha sido visitado
            not_visited_nodes.append(node) # Añade el nombre del nodo a la lista de nodos no visitados
    
    # Bucle que aplica la lógica del algoritmo de Dijkstra a la tabla con los datos que hemos creado
    while len(not_visited_nodes) > 0: # Bucle que se itera continuamente hasta que todos los nodos hayan sido visitados
        
        nodes_weight = [] # Peso de los las conexiones entre nodos
        nodos_candidatos = [] # Nodos candidatos para ser el siguiente parent_node
        
        # Carga a la lista de nodos_candidatos los nodos de la tabla que no hayan sido visitados y que tengan algún peso distinto de infinito
        for node in dijkstra_table:
            
            if dijkstra_table[node]["Visited"] == "NO" and dijkstra_table[node]["Weights"][-1] != "X":
                
                nodos_candidatos.append(node)
                nodes_weight.append(dijkstra_table[node]["Weights"][-1])
        
        # Busca los nodos adyacentes al nodo padre (parent_node) y actualiza sus pesos hasta ese nodo pasando por el nodo padre en caso de ser menor al camino de destino anterior a dicho nodo
        for node in find_adjacent_nodes(parent_node, lista_nodos):
            
            if dijkstra_table[node]["Visited"] == "NO": # Si el nodo no ha sido visitado
                
                if dijkstra_table[node]["Weights"][-1] == "X": # Si el último peso del nodo es infinito
                    
                    nodes_weight.append(get_edges_weight(parent_node, node, lista_nodos) + dijkstra_table[parent_node]["Weights"][-1]) # Añade el peso del camino total hasta el nodo pasando por el nodo padre a la lista nodes_weight
                    
                    dijkstra_table[node]["Weights"].append(get_edges_weight(parent_node, node, lista_nodos) + dijkstra_table[parent_node]["Weights"][-1]) # Añade el peso del camino total hasta el nodo pasando por el nodo padre a la tabla de Dijkstra
                    
                    dijkstra_table[node]["Edges"].append(parent_node) # Añade el nodo padre a columna de vértices de ese nodo en la tabla de Dijkstra
                    
                    nodos_candidatos.append(node) # Añade el nodo a la lista de nodos_candidatos
                    
                
                elif (dijkstra_table[parent_node]["Weights"][-1] + get_edges_weight(parent_node, node, lista_nodos)) < dijkstra_table[node]["Weights"][-1]: # Si el nodo tiene como último peso uno distinto de infinito
                    
                    nodes_weight.append(get_edges_weight(parent_node, node, lista_nodos) + dijkstra_table[parent_node]["Weights"][-1]) # Añade el peso del camino total hasta el nodo pasando por el nodo padre a la lista nodes_weight
                    
                    dijkstra_table[node]["Weights"].append(get_edges_weight(parent_node, node, lista_nodos) + dijkstra_table[parent_node]["Weights"][-1]) # Añade el peso del camino total hasta el nodo pasando por el nodo padre a la tabla de Dijkstra
                    
                    dijkstra_table[node]["Edges"].append(parent_node) # Añade el nodo padre a columna de vértices de ese nodo en la tabla de Dijkstra
                    
                    nodos_candidatos.append(node) # Añade el nodo a la lista de nodos_candidatos
                    
                else:
                    pass
                
            else:
                pass
            
        if len(nodes_weight) == 1: # Si la longitud de la lista de nodes_weight, que será siempre la misma que nodos_candidatos, es de uno
            dijkstra_table[nodos_candidatos[0]]["Visited"] = "SI" # Cambia el nodo como visitado en la tabla de Dijkstra
            parent_node = nodos_candidatos[0] # Establece el único nodo que hay como parent_node
            
            not_visited_nodes.remove(parent_node) # Elimina el nodo de la lista de nodos no visitados, rompiendo con el bucle while
            
        else:
            
            dijkstra_table[nodos_candidatos[nodes_weight.index(min(nodes_weight))]]["Visited"] = "SI" # Cambia el nodo con peso más pequeño de entre los nodos candidatos como visitado
            parent_node = nodos_candidatos[nodes_weight.index(min(nodes_weight))] # Añade el nodo con peso más pequeño de entre los nodos candidatos como parent_node para la siguiente iteración del bucle while
            
            not_visited_nodes.remove(nodos_candidatos[nodes_weight.index(min(nodes_weight))]) # Elimina el nodo de la lista de nodos visitados
        
        draw_dijkstra_table(dijkstra_table) # Muestra la tabla de Dijkstra por pantalla
        
    path = [(end_node,)] # Estable una lista de tuplas que va a contener el camino seguido

    # Va añadiendo el último elemento de la lista de vértices de cada nodo y va iterándose por dicho elemento
    while path[-1][0]!= start_node:
        path.append((dijkstra_table[path[-1][0]]["Edges"][-1],))

    path_lista = [] # Estable una lista con el nombre de los nodos calculados por el algoritmo de Dijkstra
    
    for node in path:
        
        path_lista.append(node[0])

    path_lista.reverse() # Le da la vuelta a la lista para que esté ordenada desde el nodo inicial hasta el nodo destino


    return f"El camino más corto pesa {dijkstra_table[end_node]['Weights'][-1]} y tiene la siguiente ruta: {path_lista}" # Retorna el peso total del camino más corto junto al orden visitado hasta el nodo destino
            

# ================================================================= #
# ==================== IMPRESION EN PANTALLA ====================== #
# ================================================================= #

# print(dijkstra_algorithm("A", "E", nodos))


print(dijkstra_algorithm("A", "Z", nodos2))