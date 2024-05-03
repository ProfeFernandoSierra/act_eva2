#crear un menu
#validar todos los datos del alumno
#tengo que validar que el usuario que ingresa en la opc 2 sea admin
#en el resumen tengo que condicionar el nem para que imprima informacion
#importamos time para "congelar la app cuando sea necesario y os para limpiar consola cuando tmbn sea necesario"
import time, os
os.system("cls")
#creamos variables para el usuario admin
user = "admin"
password = "admin"

#creamos cabecera y cuerpo del menu
while True:
    os.system("cls")
    print("\tSistema de Gestión de Alumnos")
    print("1. Registrar Alumno")
    print("2. Consultar Datos de Alumno")
    print("3. Salir")
    try:
        #solicitar al usuario que escoja una opcion
        opcion = int(input("ingrese opcion\n"))
        #debemos condicionar lo que viene en la opcion pára que el usuario pueda acceder al cuerpo de la opcion seleccionada
        if opcion == 1:
            os.system("cls")
            print("REGISTRO ALUMNO")
            #solicitar nombre y validar que no venga vacio
            nombre = input("ingrese nombre\n")
            while nombre == "":
                nombre = input("ingrese nombre\n")
            #solicitar direccion y validar que no venga vacia
            direccion = input("ingrese direccion\n")
            while direccion == "":
                direccion = input("ingrese direccion\n")
            #solicitar correo y validar que contenga al menos un '@'
            correo = input("ingrese correo\n")
            while '@' not in correo:
                correo = input("ingrese correo, debe contener un @\n")
            #solicitar el rut y validar que este entre los rango solicitados
            rut = int(input("ingrese rut (5000000 hasta 39999999)\n"))
            while rut < 5000000 or rut > 39999999:
                rut = int(input("ingrese rut (5000000 hasta 39999999)\n"))
            edad = int(input("ingrese edad\n"))
            while edad < 17 or edad > 90:
                edad = int(input("ingrese edad\n"))
            #solicitar NEM, no hay validacion ya que la actividad no lo sugiere
            nem = float(input("ingrese NEM\n"))
        elif opcion == 2:
            os.system("cls")
            print("CONSULTA DATOS ALUMNO")
            #solicitar usuario y contraseña
            usuario = input("ingrese usuario\n")
            clave = input("ingrese clave\n")
            #comparar si es que el usuario efectivamente es un admin
            if (usuario == user and clave == password):
                print("\tBienvenido admin")
                #consultar por rut a buscar y si coincide con lo que existe, imprimir la informacion restante
                rut_alumno = int(input("ingrese rut de alumno a consultar\n"))
                if rut_alumno == rut:
                    print(f"NOMBRE: {nombre}")
                    print(f"DIRECCION: {direccion}")
                    print(f"EDAD: {edad}")
                    print(f"CORREO: {correo}")
                    print(f"RUT: {rut}")
                    print(f"NEM: {nem}")
                    if nem < 5.2 :
                        print("alumno no cumple con requisitos")
                    else:
                        print("alumno cumple con requisitos")
                
                else:
                    print("el rut ingresado no existe en los registros")
                #crear manualmente un 'esperar tecla' o un time.sleep pero manual
                x = input("presione enter para continuar")
            else:
                print("credenciales no son validas como admin")
        elif opcion == 3:
            #opcion salir solo debo crear un break
            os.system("cls")
            print("SALIR")
            print("Ha salido del sistema…")
            x = input("presione enter para confirmar salir")
            break
        else:
            print("opcion no existe")
    except:
        print("tipo de dato ingresado no es valido")