import networkx as nx

# Crear el grafo con las aristas correspondientes al pentagrama
G = nx.Graph()
edges = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 0),  # Lados del pentágono exterior
    (0, 5), (1, 6), (2, 7), (3, 8), (4, 9),  # Conexiones entre nodos externos e internos
    (5, 6), (6, 7), (7, 8), (8, 9), (9, 5),  # Lados del pentagrama interno
    (5, 7), (6, 8), (7, 9), (8, 5), (9, 6)   # Conexiones cruzadas en el pentagrama interno
]
G.add_edges_from(edges)

# Encontrar todos los conjuntos independientes maximales
maximal_independent_sets = list(nx.maximal_independent_sets(G))

# Filtrar los que son máximos (de tamaño 3)
maximal_size_3_sets = [s for s in maximal_independent_sets if len(s) == 3]

# Mostrar los conjuntos independientes máximos
for i, s in enumerate(maximal_size_3_sets, 1):
    print(f"Conjunto independiente máximo {i}: {sorted(s)}")

# Mostrar la cantidad de conjuntos independientes máximos
print(f"\nNúmero total de conjuntos independientes máximos: {len(maximal_size_3_sets)}")