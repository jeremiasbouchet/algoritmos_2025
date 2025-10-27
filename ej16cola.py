"""16. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
siguiente situación:
a. cargue tres documentos de empleados (cada documento se representa solamente con
un nombre).
b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
c. cargue dos documentos del staff de TI.
d. cargue un documento del gerente.
e. imprima los dos primeros documentos de la cola.
f. cargue dos documentos de empleados y uno de gerente.
g. imprima todos los documentos de la cola de impresión."""

from heap import HeapMax

Crear la cola de impresión (usando HeapMax para que el mayor tenga más prioridad),
cola_impresion = HeapMax()

a) Cargar tres documentos de empleados (prioridad 1),
cola_impresion.arrive("Documento_E1", 1)
cola_impresion.arrive("Documento_E2", 1)
cola_impresion.arrive("Documento_E3", 1)

b) Imprimir el primer documento de la cola,
print("b) Primer documento impreso:", cola_impresion.attention()[1])

c) Cargar dos documentos del staff de TI (prioridad 2),
cola_impresion.arrive("Documento_TI1", 2)
cola_impresion.arrive("Documento_TI2", 2)

d) Cargar un documento del gerente (prioridad 3),
cola_impresion.arrive("Documento_G1", 3)

e) Imprimir los dos primeros documentos de la cola,
print("e) Primer documento impreso:", cola_impresion.attention()[1])
print("e) Segundo documento impreso:", cola_impresion.attention()[1])

f) Cargar dos documentos de empleados (prioridad 1) y uno de gerente (prioridad 3),
cola_impresion.arrive("Documento_E4", 1)
cola_impresion.arrive("Documento_E5", 1)
cola_impresion.arrive("Documento_G2", 3)

g) Imprimir todos los documentos restantes en la cola,
print("\ng) Impresión final de todos los documentos pendientes:")
while cola_impresion.size() > 0:
    print("-", cola_impresion.attention()[1])
