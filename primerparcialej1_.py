#ejercicio1
def buscar_capitan(superheroes: list, indice: int = 0) -> bool:
    if indice >= len(superheroes):
        return False
    if superheroes[indice].lower() == "capitán américa":
        return True
    return buscar_capitan(superheroes, indice + 1)

def listar_superheroes(superheroes: list, indice: int = 0) -> None:
    if indice >= len(superheroes):
        return
    print(superheroes[indice])
    listar_superheroes(superheroes, indice + 1)
superheroes = [
    "Iron Man", "Hulk", "Thor", "black Widow", "hawkeye",
    "Spider-Man", "doctor Strange", "black Panther", "wolverine",
    "Ant-Man", "Capitán América", "scarlet Witch", "vision",
    "falcon", "star-Lord"
]

encontrado = buscar_capitan(superheroes)
print("¿Está Capitán América?", "Sí" if encontrado else "No")

print("Lista de superhéroes:")
listar_superheroes(superheroes)

#ejercicio 2 