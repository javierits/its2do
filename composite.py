#Importo el módulo abstract base class asi puedo hacer la clase de componente, una clase base abstracta

from abc import ABC, abstractmethod

#Hago de Component una clase derivada de ABC para convertirla en una clase base abstracta
#y defino Size como un método abstracto usando el decorador @abstract
#Las clases de Archivo y Carpeta serán clases derivadas de Component, que debe
#proporcionar una implementación de este método de Size.


class Component(ABC):
    
    @abstractmethod
    def size(self):
        pass
#Los archivos son una clase derivada de Component, así que deben implementar Size.
#Los objetos de archivo serán los objetos 'hoja' en la implementación del patrón.

class File(Component):
    
#Los objetos File deben recibir un nombre y tamaño cuando se instancian
    def __init__(self, name, size):
        self.__name = name
        self.__size = size
        
#Como un File es un objeto 'hoja', su operación de Size, devuelve su tamaño
    def size(self):
        return self.__size
    
#Los objetos de Folder, también son una clase derivada de Component, y también deben
#proporcionar una implementación de Size. Los objetos de Folder son los objetos 'compuestos'
#por lo tanto pueden tener hijos que son otros componentes(Files o Folders y subFolders de una Folder)

class Folder(Component):
    
#Cuando creamos una instancia de un objeto Folder, le asignamos un nombre y una
#lista de componentes, los componentes son los 'hijos' de Folder
   
    def __init__(self, name, components):
        self.__name = name
        self.__components = components 
        
        
#EL objeto Folder para devolver su Size, tiene que sumar y devolver el Size de 
#todos sus hijos(estos pueden ser objetos de File y/o objetos de Folder)

    def size(self):
        total= 0                                #Inicializo el total en 0
        for component in self.__components:
            total += component.size()
        return total
    
    
#Implementación de un método add que agrega un nuevo componente(hijo), a la lista de componentes
    def add(self, component):
        self.__components.append(component)
        
#Creo 3 objetos de File para representar un curriculum, una carta de presentación y una carta de referencia

resume = File("resume.doc", 1024)
coverLetter = File("cover.doc", 2048)
reference = File("reference.pdf", 4096)

#Creo un objeto Folder 'Documento' que contiene estas 3 Files como hijos

documents = Folder("Documents", [resume, coverLetter,reference])

#Creo 2 objetos File para representar una lista de tareas pendientes y screenshot

todo = File("todo.txt", 256)
screenshot = File("screenshot.png", 25000)

#Creo una Folder 'Desktop' que contiene estas 2 Files como hijos
desktop = Folder("Desktop", [todo,screenshot])

#Creo un objeto Folder "User" que contiene a Desktop y Documents Folders como hijos

user = Folder("User",[desktop, documents])


#Por ahora nuestra estructura se vería así

#                todo.txt
#               /
#        Desktop
#       /       \
#      /         screenshot.png
#  User            
#      \            resume.doc
#       \          /
#        Documents - cover.doc
#                  \
#                   reference.pdf

#Implemento el método Size, ya sea el objeto un File o Folder

print(resume.size())
print(documents.size())
print(desktop.size())
print(user.size())

#Creo una lista de Components que incluye Files y Folders

components = [todo, user, screenshot]

#Uso el método Size con todos los objetos en esta lista, ya sean Files o Folders,
#ya que todos admiten la operación size
for component in components:
    print(component.size())