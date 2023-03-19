import json

datos = {}

with open('basededatos.json', 'r') as file:
            datos.update(json.load(file))

def registro(datos):
    user = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    
    if user not in datos.keys():
        datos.update({user:password})
        guardar_datos(datos)
        return 'Registro exitoso'
    else:
        return "Usted ya esta registrado"

def guardar_datos(datos):
    # Intenta abrir el archivo JSON existente, si no existe crea uno nuevo
    try:
        with open("basededatos.json", "r") as file:
            data_existente = json.load(file)
    except FileNotFoundError:
        data_existente = {}

    # Actualiza el diccionario existente con los nuevos datos
    data_existente.update(datos)

    # Guarda el diccionario actualizado en el archivo JSON
    with open("basededatos.json", "w") as file:
        json.dump(data_existente, file, indent=4)


def leer_data(datos):
    with open('basededatos.json','r') as file:
        datos = json.load(file)
    
    for key,value in datos.items():
        print(f'\nUsuario: {key}\nContraseña: {value}\n')
    return ''

def iniciar_sesion(datos):
    user = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    
    if user in datos.keys():
        if password != datos[user]:
            return "Contraseña incorrecta"
        else:
            return "Inicio de sesion exitoso"
    else: 
        return "No se encontro el usario, si no esta registrado hagalo y si lo esta verifique su nombre de usuario"

while True:
    print("\nMenú de inicio de sesión")
    print("1. Registro de usuario")
    print("2. Iniciar sesión")
    print("3. Leer data")
    print("4. Salir")

    opcion = input("Ingrese su opción (1-4): ")
    
    if opcion == "1":
        print(registro(datos))
    elif opcion == "2":
        print(iniciar_sesion(datos))
    elif opcion == "3":
        print(leer_data(datos))
    elif opcion == "4":
        print("¡Hasta pronto!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")