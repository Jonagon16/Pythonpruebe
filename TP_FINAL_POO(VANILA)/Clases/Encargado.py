import Clases.Alumno as al
from Clases.Funciones import *
class Encargado:
    __id = 0
    def __init__(self,nombre,dni):
        self.__nombre = nombre
        self.__dni = dni
        Encargado.__id += 1
        self.__id = Encargado.__id
        self.__alumnosInscriptos = []

    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self,n):
        n = limpiarDni(n)
        if isinstance(n,int):
            self.__dni = n
        else:
            raise ValueError ("El documento solo puede ser numerico")

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

    def inscribirAlumno(self,fecha=None, alumno=None, materia=None, profesor=None, curso=None, division=None, dic=None):
        a = al.Alumno(fecha, alumno, materia, profesor, curso, division, nota=-1)
        dic[a.id] = a
        self.__alumnosInscriptos.append(a)

    def __str__(self):
        return f"ID: {self.__id}\n Nombre: {self.__nombre}\n Dni: {self.__dni}\n"



def inscribirAlumno(fecha=None, alumno=None, materia=None, profesor=None, curso=None, division=None, dic=None):
    a = al.Alumno(fecha, alumno, materia, profesor, curso, division, nota=-1)
    dic[a.id] = a
def preguntar (funcion):
    respuesta = input("Elije una Opcion y/n: ").lower()
    if respuesta == "y":
        funcion()
    elif respuesta == "n":
        return False
    else:
        print("Elije una opcion valida")
        return preguntar(funcion)
def mostrarEncargados(dic):
    for id, encargado in dic.items():
        print("#" * 20)
        print(encargado)

def crear(nombre, dni, dic):
    retorno = False
    copia_dic = dict(dic)

    for i in copia_dic.values():
        if i.dni == "admin":
            pass
        elif int(i.dni) == int(dni):
            raise AttributeError
        else:
            encargado = Encargado(nombre, dni)
            dic[encargado.nombre] = encargado
            retorno = True
    return retorno


def crearEncargados(archivo):
    fl = {}
    with open (archivo,'r') as arch:
        for i in arch:
            nombre, dni = i.strip().split(',')
            encargado = Encargado(nombre,dni)
            fl[encargado.id] = encargado
    return fl


def guardarEncargado(archivo,dict):
    f=open(archivo,"w")
    for i,j in dict.items():
        f.write(f"{j.nombre},{j.dni}\n")
    f.close()

def modificarEncargado (nombre,dni,dic):
    retorno = False
    copia_dic = dict(dic)
    for i in copia_dic.values():
        if i.dni == "admin":
            pass
        elif int(i.dni) == int(dni):
            encargado = Encargado(nombre, dni)
            dic[encargado.nombre] = encargado
            retorno = True
    return retorno

def validarEncargado (nombre,dni,dic):
    r = False
    for i,j in dic.items():
        if nombre in j.nombre and dni == j.dni:
            r = True
    return r

def eliminarEncargado(dni,dic):
    retorno = False
    for i in dic.values():
        if int(i.dni) == int(dni):
            del dic[i]
            retorno = True
    return retorno

def modificarAlumno(fecha=None, alumno=None, materia=None, profesor=None, curso=None, division=None, dic=None):
    id = nombre_id(alumno,dic)
    print (id)
    print(dic[id])
    if id in dic:
        dic[id].fecha = fecha
        dic[id].materia = materia
        dic[id].profesor = profesor
        dic[id].curso = curso
        dic[id].division = division

