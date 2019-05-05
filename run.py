# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
ba = search.GPSProblem('B', 'A', search.romania)
af = search.GPSProblem('A', 'F', search.romania)
ac = search.GPSProblem('A', 'C', search.romania)
ao = search.GPSProblem('A', 'O', search.romania)
an = search.GPSProblem('A', 'N', search.romania)
cs = search.GPSProblem('C', 'S', search.romania)
op = search.GPSProblem('O', 'P', search.romania)


print("Ejemplo de búsqueda en anchura entre nodos a y b")
print(search.breadth_first_graph_search(ab).path())
print("Ejemplo de búsqueda en profundidad entre nodos a y b")
print(search.depth_first_graph_search(ab).path())

print("\nCOMIENZO DE COMPARATIVA ENTRE RAMIFICACIÓN Y ACOTACIÓN Y RAMIFICACIÓN Y ACOTACIÓN CON SUBESTIMACIÓN")
print("\nA->B Ramificación y acotación")
print(search.bab(ab).path())
print("\nA->B Ramificación y acotación con subestimación")
print(search.bab_subestimation(ab).path())

print("\nB->A Ramificación y acotación")
print(search.bab(ba).path())
print("\nB->A Ramificación y acotación con subestimación")
print(search.bab_subestimation(ba).path())

print("\nA->F Ramificación y acotación")
print(search.bab(af).path())
print("\nA->F Ramificación y acotación con subestimación")
print(search.bab_subestimation(af).path())

print("\nA->C Ramificación y acotación")
print(search.bab(ac).path())
print("\nA->C Ramificación y acotación con subestimación")
print(search.bab_subestimation(ac).path())

print("\nA->O Ramificación y acotación")
print(search.bab(ao).path())
print("\nA->O Ramificación y acotación con subestimación")
print(search.bab_subestimation(ao).path())

print("\nA->N Ramificación y acotación")
print(search.bab(an).path())
print("\nA->N Ramificación y acotación con subestimación")
print(search.bab_subestimation(an).path())

print("\nC->S Ramificación y acotación")
print(search.bab(cs).path())
print("\nC->S Ramificación y acotación con subestimación")
print(search.bab_subestimation(cs).path())

print("\nO->P Ramificación y acotación")
print(search.bab(op).path())
print("\nO->P Ramificación y acotación con subestimación")
print(search.bab_subestimation(op).path())