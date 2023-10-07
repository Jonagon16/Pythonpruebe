import Clases.Profesores as Profe
import Clases.Encargado as Enca
import Clases.Alumno as alum
import Clases.admin
from Clases.Funciones import *
#diccionarios para desempaquetar archivos y cookies
c_profesor = ""
c_alumno = ""
c_encargado = ""
temp_cookie = ""
tprofesores = {}
tencargados = {}
talumnos = {}
try:
    tencargados = Enca.crearEncargados("Data/encargados.txt")
except FileNotFoundError:
    print("Archivo de encargados no encontrado.")
try:
    tprofesores = Profe.crearProfesores("Data/profesores.txt")
except FileNotFoundError:
    print("Archivo de profesores no encontrado.")
try:
    talumnos = alum.crearAlumnos("Data/alumnos.txt")
except FileNotFoundError:
    print("Archivo de alumnos no encontrado.")


#variables para salir de bucles
x = False
z = False
v = False
#menu inicial
while not x:
    print(" ╔═════════════════════════════════════════╗")
    print(" ║  Bienvenido al menu de inscripciones    ║")
    print(" ║    Elija su opción:                     ║")
    print(" ║      1. Profesor                        ║")
    print(" ║      2. Encargado                       ║")
    print(" ║      3. Salir                           ║")
    print(" ╚═════════════════════════════════════════╝")
    op = input(" Ingrese un Nro: ")
#verifico si se eligio la opcion 1 y hago la vadilacion de datos
    if op == "1":
        try:
            nombre, materia, curso, division = input("Ingrese: Nombre,Materia,curso,division ").split(",")
            if not Profe.validarProfesor(nombre,materia,curso,division,tprofesores):
                raise SyntaxError
            else:
                z = False
                c_prof =nombre_id(nombre,tprofesores)
                c_profesor = tprofesores[c_prof]
                lp()
                #ingreso al menu profesor
                while not z:
                    print(" ╔═════════════════════════════════════════╗")
                    print(f" ║  Bienvenido Profesor                    ║")
                    print(" ║    Elija una opción:                    ║")
                    print(" ║      1. Cargar Notas                    ║")
                    print(" ║      2. Mostrar Notas                   ║")
                    print(" ║      3. Modificar Notas                 ║")
                    print(" ║      4. Eliminar Notas                  ║")
                    print(" ║      5. Volver al Menú Anterior         ║")
                    print(" ╚═════════════════════════════════════════╝")
                    op1 = input(" Ingrese un Nro: ")
                    #verifica si existe el alumno y si existe lo modifica
                    if op1 == "1":
                        menu_cargar_nota(alum,talumnos,Profe)

                    elif op1 == "2":
                        lp()
                        mostrar_notas_dataframe(talumnos)

                    #modifica notas
                    elif op1 == "3":
                        menu_modificar_nota(alum,talumnos,Profe)

                    #elimina una nota de un alumno en una materia
                    elif op1 == "4":
                        menu_eliminar_nota(alum,talumnos,Profe)

                    elif op1 == "5":
                        alum.guardarAlumnos("alumnos.txt", talumnos)
                        lp()
                        c_prof = ""
                        c_profesor = ""
                        z = True

                    else:
                        lp()
                        print(color_rojo("Ingrese una opcion correcta."))
        except SyntaxError:
            lp()
            print(color_rojo("Datos incorrectos, por favor intente nuevamente"))
            continue
        except ValueError:
            lp()
            print(color_rojo("Debe cargar todos los datos solicitados"))
            continue

#valida los datos del encargado
    elif op == "2":
        try:
            nombre, dni = input("Ingrese:Nombre,DNI ").split(",")
            if Enca.validarEncargado(nombre,dni,tencargados) == 0:
                raise ValueError
            else:
                v = False
                lp()
                c_enc = nombre_id(nombre,tencargados)
                c_encargado = tencargados[c_enc]
                #ingreso al menu encargado
                while not v:
                    print(" ╔═════════════════════════════════════════╗")
                    print(" ║  Bienvenido Encargado                   ║")
                    print(" ║    Elija una opción:                    ║")
                    print(" ║      1. Inscribir Alumno                ║")
                    print(" ║      2. Mostrar Alumnos                 ║")
                    print(" ║      3. Modificar Alumno                ║")
                    print(" ║      4. Eliminar Alumno                 ║")
                    print(" ║      5. Volver al Menú Anterior         ║")
                    print(" ╚═════════════════════════════════════════╝")
                    op2 = input(" Ingrese un Nro: ")
                    #verifica si existe el alumno o si no lo agrega
                    if op2 == "1":
                        menu_inscribir_alumno(alum,talumnos,c_encargado,Enca)

                    elif op2 == "2":
                        lp()
                        mostrar_alumnos_dataframe(talumnos)

                    #modifica el alumno
                    elif op2 == "3":
                        menu_modificar_alumno(alum,talumnos,c_encargado,Enca)

                    elif op2 == "4":
                        menu_eliminar_alumno(alum,talumnos)
                    elif op2 == "5":
                        alum.guardarAlumnos("alumnos.txt",talumnos)
                        lp()
                        v = True
                    else:
                        lp()
                        print(color_rojo("Ingrese una opcion correcta."))
        except ValueError:
            lp()
            print(color_rojo("Datos Incorrectos, por favor intente nuevamente"))
            continue

    elif op == "3":
        alum.guardarAlumnos("alumnos.txt", talumnos)
        lp()
        x = True

    #elif op == "admin":
    #    dni = ""
    #    nombre = ""
    #    alum.guardarAlumnos("alumnos.txt", talumnos)
    #    lp()
    #    try:
    #        user, passw = input("Ingrese usuario,contraseña: ").split(",")
    #        if admin.validarAdmin(user, passw):
    #            dni = ""
    #            nombre = ""
    #            admin.menu_secreto(tencargados, tprofesores)
    #        else:
    #            print(color_rojo("Datos incorrectos, acceso denegado"))
    #    except ValueError:
    #        print(color_rojo("Debe colocar los usuario y contraseña separados por una ','"))

    else:
        lp()
        print(color_rojo("Ingrese una opcion correcta."))