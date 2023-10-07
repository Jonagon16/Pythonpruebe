import Clases.Alumno as al
class Profesor:
    __id = 0
    def __init__(self,nombre,materia,curso,division):
        self.__nombre = nombre
        self.__materia = materia
        Profesor.__id += 1
        self.__id = Profesor.__id
        self.__curso = curso
        self.__division = division
        self.__alumnosInscriptos = []

    @property
    def curso(self):
        return self.__curso
    @curso.setter
    def curso(self,curso):
        self.__curso = curso

    @property
    def division(self):
        return self.__division
    @division.setter
    def division(self,division):
        self.__division = division

    @property
    def materia(self):
        return self.__materia
    @materia.setter
    def materia(self,materia):
        self.__materia = materia

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def alumnosInscriptos(self):
        return self.__alumnosInscriptos
    @alumnosInscriptos.setter
    def alumnosInscriptos(self,alumno):
        self.__alumnosInscriptos.append(alumno)

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        raise AttributeError ("Este valor es de solo lectura no puede modificarse")

    def poner_nota(self,alumno:object,nota:int):
        if alumno.nombre in self.__alumnosInscriptos:
            alumno.nota(nota)
            return True
        else:
            return False

    def __str__(self):
        return f"ID: {self.__id}\n Nombre: {self.__nombre}\n Materia: {self.__materia}\n Curso: {self.__curso}\n Division: {self.__division}\n"

def crear (nombre,materia,curso,division,dic):
    nombre_id = al.nombre_id(nombre,dic)
    if not nombre_id in dic:
        p = Profesor(nombre,materia,curso,division)
        dic[p.id] = p
        return True


def mostrarProfesores(dic):
    for id, profesor in dic.items():
        print("#" * 20)
        print(profesor)

def validarProfesor (nombre,materia,curso,division,dic):
    r = False
    for i,j in dic.items():
        if nombre == j.nombre and materia == j.materia and division == j.division and curso == j.curso:
            r = True
    return r

def mostrarNotas(dic):
    for alumno, datos in dic.items():
        print("#" * 20)
        print(f"Alumno: {datos.nombre}")
        print(f"Materia: {datos.materia}")
        print(f"Nota: {datos.nota}")


def eliminarNota(alumno,dic):
    alumno_id = al.nombre_id(alumno, dic)
    dic[alumno_id].nota = "-1"

def modificarNota(alumno,materia,nota,dic):
    alumno_id = al.nombre_id(alumno,dic)
    dic[alumno_id].nota = nota

def crearProfesores(archivo):
    fl = {}
    with open (archivo,'r') as arch:
        for i in arch:
            nombre, materia, curso, division= i.strip().split(',')
            p = Profesor(nombre,materia,curso,division)
            fl[p.id]=p
    return fl

def guardarProfesores(archivo,dict):
    f=open(archivo,"w")
    for i,j in dict.items():
        f.write(f"{j.nombre},{j.materia},{j.curso},{j.division}\n")
    f.close()

def validarNota(nota):
    try:
        note = int(nota)
        if 0 <= note <= 10:
            return nota
        else:
            return '-1'
    except ValueError:
        return '-1'



def eliminarProfesor(nombre,dic):
    retorno = False
    for i in dic.values():
        if i.nombre == nombre:
            del dic[i]
            retorno = True
        else:
            return KeyError
    return retorno

def modificarProfesor (nombre,materia,curso,division,dic):
    retorno = False
    for i in dic.values():
        if i.nombre == nombre:
            dic[i.nombre] = nombre
            dic[i.materia] = materia
            dic[i.curso] = curso
            dic[i.division] = division
            retorno = True
        else:
            return KeyError
    return retorno