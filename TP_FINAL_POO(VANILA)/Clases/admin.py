import Clases.Encargado as Enca
import Clases.Profesores as Profe
import os
from Clases.Funciones import *

def validarAdmin(user, passw):
    try:
        with open('user.txt', 'r') as file:
            for line in file:
                u, p = line.strip().split(',')
                if u == user and p == passw:
                    return True
    except FileNotFoundError:
        lp()
        print("Archivo de usuarios no encontrado.")
    return False

def menu_secreto(tencargados,tprofesores):
    while True:
        print(" ╔═════════════════════════════════════════╗")
        print(" ║  Bienvenido Administrador               ║")
        print(" ║    Elija una opción:                    ║")
        print(" ║      1. Crear Encargado                 ║")
        print(" ║      2. Modificar Encargado             ║")
        print(" ║      3. Eliminar Encargado              ║")
        print(" ║      4. Crear Profesor                  ║")
        print(" ║      5. Modificar Profesor              ║")
        print(" ║      6. Eliminar Profesor               ║")
        print(" ║      7. Mostrar Encargados              ║")
        print(" ║      8. Mostrar Profesores              ║")
        print(" ║      9. Guardar y Salir                 ║")
        print(" ╚═════════════════════════════════════════╝")
        op3 = input(" Ingrese un Nro: ")

        if op3 == "1":
            try:
                datos = input("Ingrese Nombre,Dni: ")
                nombre, dni = datos.split(",")

                if dni.isdigit():
                    dni= int(dni)

                    if Enca.crear(nombre, dni, tencargados):
                        lp()
                        print("Se creó correctamente el encargado")
                        print(tencargados)
                        Enca.guardarEncargado("encargados.txt", tencargados)
                    else:
                        lp()
                        print("No se pudo crear el encargado")
                else:
                    lp()
                    print("El DNI ingresado no es un número válido.")
            except ValueError as error:
                lp()
                print(f"Debe colocar ambos datos {error}")


        elif op3 == "2":
            try:
                nombre, dni = input("Ingrese Nombre,Dni: ").split(",")
                if Enca.modificarEncargado(nombre,dni,tencargados):
                    lp()
                    print("Se modifico el encargado")
                    Enca.mostrarEncargados(tencargados)
                    Enca.guardarEncargado("encargados.txt",tencargados)
                else:
                    lp()
                    print("No se pudo modificar el encargado")
            except ValueError:
                lp()
                print("Debe colocar ambos datos")
            except KeyError:
                lp()
                print("El encargado que desa modificar no existe")

        elif op3 == "3":
            try:
                DNI = input("Ingrese el DNI del encargado a eliminar: ")
                Enca.eliminarEncargado(DNI, tencargados)
                lp()
                print("El encargado a sido eliminado")
            except KeyError:
                lp()
                print("El encargado que desa eliminar no existe")
        elif op3 == "4":
            try:
                nombre, materia, curso, division = input("Ingrese Nombre, Materia, Curso, Division del Profesor: ").split(",")
                if Profe.crear(nombre, materia,curso,division, tprofesores):
                    lp()
                    print("Se creo correctamente el encargado")
                    print(tprofesores)
                    Profe.guardarProfesores("profesores.txt", tprofesores)
                else:
                    lp()
                    print("No se pudo crear el profesor")
            except ValueError:
                lp()
                print("Debe colocar ambos datos")

        elif op3 == "5":
            try:
                nombre, materia, curso, division = input("Ingrese Nombre, Materia, Curso, Division del Profesor: ").split(",")
                if Profe.modificarProfesor(nombre, materia,curso,division, tprofesores):
                    lp()
                    print("Se modifico el encargado correctamente")
                    print(tprofesores)
                    Profe.guardarProfesores("profesores.txt", tprofesores)
                else:
                    lp()
                    print("No se pudo crear el profesor")
            except ValueError:
                lp()
                print("Debe colocar ambos datos")
        elif op3 == "6":
            try:
                nombre = input("Ingrese profesor a eliminar: ")
                Profe.eliminarProfesor(nombre,tprofesores)
                lp()
                print("El profesor a sido eliminado")
            except KeyError:
                lp()
                print("El encargado que desa eliminar no existe")

        elif op3 == "7":
            lp()
            for i in tencargados.values():
                print(i)
        elif op3 == "8":
            lp()
            for i in tprofesores.values():
                print(i)

        elif op3 == "9":
            lp()
            break

        else:
            lp()
            print("Opcion invalida, intente nuevamente.")

