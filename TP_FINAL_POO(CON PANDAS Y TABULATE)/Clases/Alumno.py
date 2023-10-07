from Clases.Funciones import *
class Alumno:
    """
    Esta clase utiliza como identificador un Id para identificar a cada objeto
    """
    __id = 0
    def __init__(self,fecha, nombre, materia, profesor, curso, division,nota):
        self.__fecha = fecha
        self.__nombre = nombre
        self.__materia = materia
        self.__profesor = profesor
        self.__curso = curso
        self.__division = division
        self.__nota = nota
        Alumno.__id += 1
        self.__id = Alumno.__id

    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self,fecha):
        if formato_fecha(fecha):
            self.__fecha = fecha
        else:
            raise ValueError ("La fecha debe ser en forma dd/mm/aaaa")

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def materia(self):
        return self.__materia
    @materia.setter
    def materia(self,materia):
        self.__materia = materia

    @property
    def profesor(self):
        return self.__profesor
    @profesor.setter
    def profesor(self,profesor):
        self.__profesor = profesor

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
    def nota(self):
        return self.__nota
    @nota.setter
    def nota(self,nota):
        self.__nota = nota

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        raise AttributeError ("Este valor es de solo lectura no puede modificarse")

    def __str__(self):
        return f"ID: {self.__id}\nFecha: {self.__fecha}\nNombre: {self.__nombre}\nProfesor: {self.__materia}\nMateria: {self.__profesor}\nCurso: {self.__curso}\nDivisión: {self.__division}\nNota: {self.__nota}"





def crearAlumnos(archivo):
    """
    CREA UN DICCIONARIO DE ALUMNOS A PARTIR DE UN ARCHIVO
    :param archivo: as File
    :return: El diccionario, clave: ID del alumno, valor: objeto alumno
    """
    diccionario_alumnos = {}
    with open(archivo,'r') as arch:
        for i in arch:
            fecha, nombre, profesor, materia, curso, division, nota = i.strip().split(',')
            alumno = Alumno(fecha,nombre,materia,profesor,curso,division,nota)
            diccionario_alumnos[alumno.id] = alumno
    return diccionario_alumnos



def guardarAlumnos(archivo,dict):
    """
    Guarda el diccionario en el archivo
    :param archivo: as File
    :param dict: diccionario de alumnos
    :return: True: al eliminar al alumno // False: al no encontrarlo
    """
    f=open(archivo,"w")
    for i,j in dict.items():
        f.write(f"{j.fecha},{j.nombre},{j.profesor},{j.materia},{j.curso},{j.division},{j.nota}\n")
    f.close()

def validarAlumno(alumno,dic):
    print(dic)
    r = False
    for i in dic.values():
        if alumno in i.nombre:
            r= True
            break
    return r

def validar_alumno_poo(alumno,dic):
    if alumno in dic:
        return True
    else:
        return False

def mostrarAlumnos(dic):
    for id, alumno in dic.items():
        print("#" * 20)
        print(alumno)

def eliminarAlumno(alumno,dic):
    """
    ELIMINA A UN ALUMNO DE UN DICCIONARIO
    :param alumno: Nombre de Alumno
    :param dic: Diccionario de alumnos
    :return: True: al eliminar al alumno // False: al no encontrarlo
    """
    r = False
    for i,j in dic.items():
        if j.nombre == alumno:
            del dic[i]
            r = True
            break
    return r

def filtrar_alumnos(profesor:object,dic:dict):
    """
    SE UTILIZA PARA ENCONTRAR LOS ALUMNOS ANOTADOS PARA RENDIR UNA MATERIA CON UN PROFESOR
    :param profesor: Profesor Loggeado
    :param dic: Diccionario de alumnos
    :return: True : si encuentra alumnos inscriptos en su materia // False :  en caso de no encontrar alumnos
    """
    diccionario_alumnos = {}
    retorno =False
    for i,alumno in dic.items():
        if profesor == alumno.profesor:
            diccionario_alumnos[alumno.id] = alumno
            retorno = True
    return retorno


