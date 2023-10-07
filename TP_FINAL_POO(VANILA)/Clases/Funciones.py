import os
def lp():
    os.system('cls' if os.name == 'nt' else 'clear')
#funciones lambda
color_verde = lambda text: "\033[32m" + text + "\033[0m"
color_rojo = lambda text: "\033[31m" + text + "\033[0m"
color_amarillo = lambda text: "\033[33m" + text + "\033[0m"

#funcion recursiva
def limpiarDni(dni):
    """
    Funcion Recursiva para validar Dni
    :param dni: DNI ingresado por el Usuario
    :return: True: Si el DNI es invalido // False: limpiarDni()
    """
    dni = dni.replace(".","")
    if len(dni) == 8:
        return dni
    elif dni == "exit":
        raise ValueError
    else:
        print("Ingrese un Dni valido, con mas de 7 numeros y menos de 8 numeros")
        return limpiarDni(input())

def formato_fecha(fecha):
    """
    Funcion Recursiva
    :param fecha: Fecha a validar
    :return: False: formato_fecha // True: fecha
    """
    try:
        dia,mes,anio = fecha.split("/")
        if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and int(anio) >= 0:
            return fecha
        else:
            print("La fecha ingresada no es válida.")
            return formato_fecha(input(" "))
    except ValueError:
        print("Ingrese una fecha con un formato valido dd/mm/aa")
        return formato_fecha(input(" "))

def preguntar(funcion):
    """
    Funcion recursiva para preguntar
    :param funcion: Funcion a agregar en caso afirmativo
    :return: y : funcion() // n : pass
    """
    respuesta = input(color_amarillo(" ¿Quieres intentarlo de nuevo y/n? ")).lower()
    if respuesta == "y":
        funcion()
    elif respuesta == "n":
        pass
    else:
        print("Elije una letra valida")
        return preguntar(funcion)

def preguntar_arg(funcion,*args):
    """
    Funcion recursiva para preguntar
    :param funcion: Funcion a agregar en caso afirmativo
    :return: y : funcion() // n : pass
    """
    respuesta = input(color_amarillo(" ¿Quieres intentarlo de nuevo y/n? ")).lower()
    if respuesta == "y":
        funcion(*args)
    elif respuesta == "n":
        pass
    else:
        print("Elije una letra valida")
        return preguntar(funcion)

def guardar(alum,talumnos):
    alum.guardarAlumnos("alumnos.txt", talumnos)

def nombre_id(nombre,dic:dict):
    """
    TRANSFORMA EL NOMBRE EN UN ID
    :param nombre: Nombre de un alumno
    :param dic: Diccionario donde se encuentran los alumnos
    :return: En caso de encontrar el id devuelve el mismo, y None en caso False
    """
    ids = None
    for id,alumno in dic.items():
        if alumno.nombre == nombre:
            ids = id
    return ids

def menu_eliminar_alumno(alum,talumnos):
    try:
        print(talumnos)
        alumno, materia = input(
            "Ingrese el alumno que desea eliminar: alumno,materia ").split(",")
        if not alum.validarAlumno(alumno, talumnos):
            raise ValueError
        else:
            if alum.eliminarAlumno(alumno, talumnos):
                lp()
                guardar(alum,talumnos)
                print(color_verde(f"Se elimino el alumno {alumno} correctamente."))
            else:
                lp()
                print(color_rojo(f"No se pudo eliminar al alumno correctamente"))
    except ValueError:
        lp()
        print(color_rojo("El Alumno ingresado no se encuentra inscripto."))
        preguntar_arg(menu_eliminar_alumno,alum,talumnos)


def menu_inscribir_alumno(alum,talumnos,c_encargado,Enca):
    print(talumnos)
    try:
        fecha = input("ingrese Fecha: ")
        fecha = formato_fecha(fecha)
        alumno = input("ingrese Nombre: ")
        materia = input("ingrese Materia: ")
        profesor = input("ingrese Profesor: ")
        curso = input("ingrese Curso: ")
        division = input("ingrese Division: ")
        if alum.validarAlumno(alumno, talumnos):
            raise SyntaxError
        else:
            Enca.inscribirAlumno(fecha, alumno, materia, profesor, curso, division, talumnos)
            lp()
            guardar(alum,talumnos)
            print(color_verde(f"Se inscribio al alumno {alumno} en la materia {materia} correctamente."))
    except SyntaxError:
        lp()
        print(color_rojo("El Alumno ingresado ya se encuentra anotado en esa materia"))
        preguntar_arg(menu_inscribir_alumno,alum,talumnos,c_encargado)
    except ValueError:
        lp()
        print(color_rojo("Debe colocar todos los datos solicitados"))
        preguntar_arg(menu_inscribir_alumno,alum,talumnos,c_encargado)


def menu_modificar_alumno(alum,talumnos,c_encargado,Enca):
    try:
        fecha = input("ingrese Fecha: ")
        fecha = formato_fecha(fecha)
        alumno = input("ingrese Nombre: ")
        materia = input("ingrese Materia: ")
        profesor = input("ingrese Profesor: ")
        curso = input("ingrese Curso: ")
        division = input("ingrese Division: ")
        if not alum.validarAlumno(alumno, talumnos):
            raise AttributeError
        else:
            Enca.modificarAlumno(fecha, alumno, materia, profesor, curso, division, talumnos)
            lp()
            guardar(alum, talumnos)
            print(color_verde(f"Se modifico el alumno {alumno} correctamente."))
    except ValueError:
        lp()
        print(color_rojo("Debe ingresar todos los datos solicitados."))
        preguntar_arg(menu_modificar_alumno,alum,talumnos,c_encargado)
    except AttributeError:
        print(color_rojo("El Alumno ingresado no se encuentra inscripto."))
        preguntar_arg(menu_modificar_alumno, alum, talumnos, c_encargado)


def menu_eliminar_nota(alum,talumnos,Profe):
    try:
        alumno, materia = input("ingrese: Alumno,materia ").split(",")
        if not alum.validarAlumno(alumno, talumnos):
            raise ValueError
        else:
            Profe.eliminarNota(alumno, talumnos)
            lp()
            guardar(alum,talumnos)
            print(color_verde(f"Se elimino la nota del alumno {alumno} correctamente"))
    except ValueError:
        lp()
        print(color_rojo("El Alumno ingresado no existe o no esta anotado para la materia nombrada"))
        preguntar_arg(menu_eliminar_nota,alum,talumnos,Profe)

def menu_modificar_nota(alum,talumnos,Profe):
    try:
        alumno, materia, nota = input("ingrese: Alumno,materia,nota ").split(",")
        if not alum.validarAlumno(alumno, talumnos):
            raise ValueError
        else:
            Profe.modificarNota(alumno, materia, Profe.validarNota(nota), talumnos)
            lp()
            guardar(alum,talumnos)
            print(color_verde(f"Se modifico la nota del alumno {alumno} correctamente"))
    except ValueError:
        lp()
        print(color_rojo("El Alumno ingresado no existe o no esta anotado para la materia nombrada"))
        preguntar_arg(menu_modificar_nota,alum,talumnos,Profe)

def menu_cargar_nota(alum,talumnos,Profe):
    try:
        alumno, materia, nota = input("ingrese: Alumno,materia,nota ").split(",")
        if not alum.validarAlumno(alumno, talumnos):
            raise ValueError
        else:
            Profe.modificarNota(alumno, materia, Profe.validarNota(nota), talumnos)
            lp()
            guardar(alum,talumnos)
            print(color_verde(f"Se asigno la nota {nota} al alumno {alumno} correctamente"))
    except ValueError:
        lp()
        print(color_rojo("El Alumno ingresado no existe o no esta anotado para la materia nombrada"))
        preguntar_arg(menu_cargar_nota,alum,talumnos,Profe)
    except KeyError:
        lp()
        print(color_rojo("El Alumno ingresado no existe o no esta anotado para la materia nombrada"))
        preguntar_arg(menu_cargar_nota,alum,talumnos,Profe)


