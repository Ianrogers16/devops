#realizar una solicitud de tus calificaciones del semtres 

nombre = input("ingresa tu nombre de alumno: ")
materia = input("ingresa la materia (poo, ingles, desarrollo full stack): ")

if materia == "poo":
    calificacion = float(input("ingresa tu calificación en POO: "))
    print(f"Tu calificación en POO es: {calificacion}")
    if calificacion >= 60:
        print("aprobaste la materia ", materia)
    else:
        print("no aprobaste la materia ", materia)
elif materia == "ingles":
    calificacion = float(input("ingresa tu calificación en Inglés: "))
    print(f"Tu calificación en Inglés es: {calificacion}")
    if calificacion >= 60:
        print("aprobaste la materia ", materia)
    else:
        print("no aprobaste la materia ", materia)
elif materia == "desarrollo full stack":
    calificacion = float(input("ingresa tu calificación en Desarrollo Full Stack: "))
    print(f"Tu calificación en Desarrollo Full Stack es: {calificacion}")
    if calificacion > 100:
        print("La calificación no puede exceder 100")
    if calificacion >= 60:
        print("aprobaste la materia ", materia)
    else:
        print("no aprobaste la materia ", materia)
        print("tu calificaciónes son: ", nombre)


##traductor  3 idiomas 
print("Bienvenido al traductor de idiomas")
idioma = input("Ingresa el idioma al que deseas traducir (español, inglés, aleman").lower()
if id

