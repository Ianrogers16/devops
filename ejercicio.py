nombre = input("Ingresa nombre: ")
while not nombre.replace(" ", "").isalpha():
    print("¡Error! No se permiten números en el nombre.")
    nombre = input("Por favor, ingresa un nombre válido: ")


musica = input("Ingresa música: ")
while not musica.replace(" ", "").isalpha():
    print("¡Error! No se permiten números en el nombre.")
    musica = input("Por favor, ingresa un tipo de musica válido: ")
pelicula = input("Ingresa película: ")
un_hobbie = input("Ingresa tus hobbies: ")


un_hobbie=[nombre,musica,pelicula,un_hobbie]

print("\nHola", un_hobbie[0]) # El nombre es el primer elemento (índice 0)
print("Tus gustos son:", un_hobbie[1], ",", un_hobbie[2], "y", un_hobbie[3])
