import os
os.system("cls")

#Declarando listas
listaNIF = []
listaNombre = []
listaEdad = []

def mensajeNIF():   #Funcion para mandar mensaje de nif invalido
    print("NIF Inválido, NIF debe consistir de 8 números, guión y 3 letras.")

def tieneNumeros(palabra = ""): #Funcion para checkear si un string tiene números
    for letra in palabra:
        if letra.isdigit():     #Si una de las letras que revisa es un numero manda true
            return True
    else:
        return False



def grabarNIF():
    while True:                         #Validando el nif
        nif = input("Ingrese NIF: ")
        if len(nif) != 12:              #Revisando si lo ingresado tiene el largo correcto
            mensajeNIF()                #en caso contrario le manda mensaje de error
        elif nif[8] != "-":             #verificando que tenga guion
            mensajeNIF()
        elif not (nif[:8]).isdigit():   #revisando que los primeros 8 digitos sean numeros con not y .isdigit()
            mensajeNIF()
        elif tieneNumeros(nif[9:12]):   #revisando si los ultimos 3 tiene un numero
            mensajeNIF()
            print("los ultimos 3 deben ser solo letras")
        else:
            listaNIF.append(nif)        #agregando el nif a la lista
            print("NIF Ingresado")
            break
    while True:
        nom = input("Ingrese el nombre: ")
        if len(nom) > 2:
            listaNombre.append(nom)
            break
        else:
            print("El nombre ingresado debe tener mas de 2 caracteres")


