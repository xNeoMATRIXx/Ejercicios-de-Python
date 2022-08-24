dato = str(input("Desea ingresar un nuevo dato?"))
if dato == "si":
    print("Ingrese la siguiente informacion requerida")
    nombre = input("Ingrese Nombre: ")
    apellido = input("Ingrese Apellido: ")
    fecha = input("Ingrese Año de Nacimiento: ")

    print("Estos datos ingresados estaran en la siguiente tabla de informacion")
    lista = [
        {
            'nombre': nombre,
            'apellido': apellido,
            'fecha': fecha
        },
    ]
    print(lista)
    dato = str(input("Desea ingresar algun otro dato?"))
       
else:
    print("Usted eligio la opcion NO, por ende se saldra del sistema")
    

# Hacer un codigo que pregunte al usuario si desea
# ingresar un nuevo dato. Si el usuario escribe la 
# palabra "no" el codigo tiene que culminar. Si el 
# usuario escribe "si" le tiene que preguntar el nombre 
# con un input, el apellido y el año de nacimiento (
# son tres inputs diferentes). Esta informacion tiene 
# almacenarse en una lista de diccionarios. Es
# decir que cada elemento de la lista va a ser un
# diccionario que tiene que contener tres claves(
# 'Nombre', 'Apellido','Año'). Una vez que el usuario
# introduce el año tiene que volver a preguntar si
# desea agregar un nuevo dato. El codigo me tiene 
# que permitir introducir un dato, ningun o 500 y 
# cualquier cantidad intermedia.
# En el caso que el usuario introduzca algo differente
# a un año cuando le preguntes esa informacion el
# codigo tiene que decir "introdujo algo no valido 
# como año, por favor intentelo de nuevo"