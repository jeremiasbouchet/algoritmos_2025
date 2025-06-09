from super_heroes_data import superheroes
from list_ import List
from queue_ import Queue


lista_personajes = List(superheroes)


lista_personajes.add_criterion("name", lambda p: p["name"])
lista_personajes.add_criterion("real_name", lambda p: p["real_name"] or "")
lista_personajes.add_criterion("first_appearance", lambda p: p["first_appearance"])


lista_personajes.sort_by_criterion("name")
print("1. Personajes ordenados por nombre:")
for p in lista_personajes:
    print(p["name"])


pos_thing = lista_personajes.search("The Thing", "name")
pos_rocket = lista_personajes.search("Rocket Raccoon", "name")
print(f"2. The Thing está en la posición: {pos_thing}")
print(f"   Rocket Raccoon está en la posición: {pos_rocket}")


villanos = List([p for p in lista_personajes if p["is_villain"]])
print("3. Villanos:")
for v in villanos:
    print(v["name"])


cola_villanos = Queue()
for v in villanos:
    cola_villanos.arrive(v)

print("4. Villanos que aparecieron antes de 1980:")
for i in range(cola_villanos.size()):
    villano = cola_villanos.move_to_end()
    if villano["first_appearance"] < 1980:
        print(villano["name"])


print("5. Superhéroes que comienzan con Bl, G, My o W:")
for p in lista_personajes:
    if p["name"].startswith(("Bl", "G", "My", "W")):
        print(p["name"])


lista_personajes.sort_by_criterion("real_name")
print("6. Personajes ordenados por nombre real (ascendente):")
for p in lista_personajes:
    print(f"{p['real_name']} → {p['name']}")


lista_personajes.sort_by_criterion("first_appearance")
print("7. Personajes ordenados por aparición:")
for p in lista_personajes:
    print(f"{p['name']} ({p['first_appearance']})")


for p in lista_personajes:
    if p["name"] == "Ant Man":
        p["real_name"] = "Scott Lang"
        print(f"8. Nuevo nombre real de Ant Man: {p['real_name']}")
        break

print("9. Personajes con 'time-traveling' o 'suit' en la biografía:")
for p in lista_personajes:
    bio = p["short_bio"].lower()
    if "time-traveling" in bio or "suit" in bio:
        print(p["name"])

print("10. Información de personajes eliminados:")

for nombre in ["Electro", "Baron Zemo"]:
    eliminado = lista_personajes.delete_value(nombre, "name")
    if eliminado:
        print(f"\n{eliminado['name']}:")
        for clave, valor in eliminado.items():
            print(f"  {clave}: {valor}")
    else:
        print(f"\n{nombre} no se encontraba en la lista.")