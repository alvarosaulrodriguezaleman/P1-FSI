# Fundamentos de los Sistemas Inteligentes - Práctica 1
Breve programa para comparar los métodos de búsqueda de ramificación y acotación y ramificación y acotación con subestimación, además
de la búsqueda en anchura y la búsqueda en profundidad.

La práctica consta de dos partes. En primer lugar, hemos programado el método de ramificación y acotación, que corresponde al método
bab() del fichero search.py, que a su vez usa la clase babg que hemos implementado en el fichero utils.py, y que almacena la lógica 
del algoritmo. El funcionamiento del algoritmo reside en la reordenación de la lista abierta cada vez que insertan elementos según 
el valor path_cost desde el nodo origen.

En segundo lugar, hemos programado el método de búsqueda de ramificación y acotación con subestimación, usando como heurística la 
distancia en línea recta entre cada estado y el estado final, que ya nos es proporcionada en el código base. La implementación de 
dicho algoritmo reside en el método bab_subestimation() del fichero search.py, y en la clase heuristic_babg del fichero utils.py. 
El funcionamiento del algoritmo es similar al del algoritmo de ramificación y acotación, pero en esta ocasión de cara a la 
reordenación de la lista abierta también tenemos en cuenta la heuristica descrita anteriormente.

Para comparar ambos algoritmos implementados y los algoritmos de búsqueda en anchura y búsqueda en profundidad que ya se 
encontraban en el código base, hemos modificado el método graph_search() del fichero search.py para que lleve un contador de los nodos
visitados y expandidos, y que los muestre en pantalla cuando finalize la búsqueda, además de la ruta computada que ya se mostraba
previamente.

Así pues, los resultados obtenidos han sido los siguientes:
````
Ejemplo de búsqueda en anchura entre nodos a y b
Nodos expandidos:  15
Nodos visitados:  16
[<Node B>, <Node F>, <Node S>, <Node A>]
Ejemplo de búsqueda en profundidad entre nodos a y b
Nodos expandidos:  9
Nodos visitados:  10
[<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>]

COMIENZO DE COMPARATIVA ENTRE RAMIFICACIÓN Y ACOTACIÓN Y RAMIFICACIÓN Y ACOTACIÓN CON SUBESTIMACIÓN

A->B Ramificación y acotación
Nodos expandidos:  23
Nodos visitados:  24
[<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]

A->B Ramificación y acotación con subestimación
Nodos expandidos:  5
Nodos visitados:  6
[<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]

B->A Ramificación y acotación
Nodos expandidos:  28
Nodos visitados:  29
[<Node A>, <Node S>, <Node R>, <Node P>, <Node B>]

B->A Ramificación y acotación con subestimación
Nodos expandidos:  4
Nodos visitados:  5
[<Node A>, <Node S>, <Node R>, <Node P>, <Node B>]

A->F Ramificación y acotación
Nodos expandidos:  10
Nodos visitados:  11
[<Node F>, <Node S>, <Node A>]

A->F Ramificación y acotación con subestimación
Nodos expandidos:  2
Nodos visitados:  3
[<Node F>, <Node S>, <Node A>]

A->C Ramificación y acotación
Nodos expandidos:  19
Nodos visitados:  20
[<Node C>, <Node R>, <Node S>, <Node A>]

A->C Ramificación y acotación con subestimación
Nodos expandidos:  6
Nodos visitados:  7
[<Node C>, <Node R>, <Node S>, <Node A>]

A->O Ramificación y acotación
Nodos expandidos:  4
Nodos visitados:  5
[<Node O>, <Node Z>, <Node A>]

A->O Ramificación y acotación con subestimación
Nodos expandidos:  2
Nodos visitados:  3
[<Node O>, <Node Z>, <Node A>]

A->N Ramificación y acotación
Nodos expandidos:  44
Nodos visitados:  45
[<Node N>, <Node I>, <Node V>, <Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node A>]

A->N Ramificación y acotación con subestimación
Nodos expandidos:  38
Nodos visitados:  39
[<Node N>, <Node I>, <Node V>, <Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node A>]

C->S Ramificación y acotación
Nodos expandidos:  5
Nodos visitados:  6
[<Node S>, <Node R>, <Node C>]

C->S Ramificación y acotación con subestimación
Nodos expandidos:  2
Nodos visitados:  3
[<Node S>, <Node R>, <Node C>]

O->P Ramificación y acotación
Nodos expandidos:  13
Nodos visitados:  14
[<Node P>, <Node R>, <Node S>, <Node O>]

O->P Ramificación y acotación con subestimación
Nodos expandidos:  3
Nodos visitados:  4
[<Node P>, <Node R>, <Node S>, <Node O>]

Process finished with exit code 0
````
Como podemos observar, los algoritmos de ramificación y acotación y de ramificación y acotación con subestimación siempre proporcionan 
los mismos resultados (la ruta óptima), pero uno de ellos siempre expande y visita menos nodos que el otro, gracias a la heurística. 
Además, podemos observar que los métodos de búsqueda en anchura y búsqueda en profundidad han fracasado en encontrar la ruta óptima, 
e incluso, pese a ello, han expandido y visitado más nodos que la ramificación y acotación con subestimación. 

**Así pues, podemos concluir que el método de ramificación y acotación con subestimación es el mejor algoritmo de 
los cuatro probados, por su optimalidad y por su eficiencia en hallar los resultados (gracias también al hecho de usar una heurística
útil para el problema en cuestión).**



