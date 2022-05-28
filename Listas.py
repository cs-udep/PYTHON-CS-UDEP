#Creación de listas de una línea
from ast import List


Lista = []

#Agregamos elementos a la lista
Lista.append('📕')
Lista.append('📚')
Lista.append('⚽')

#Agregamos elementos a la lista de manera iterativa:
for i in range(5):
    Lista.append(i)

#Agregamos tuplas
Lista.append((5,6))
Lista.append(("Alvaro","Felipe"))

#Agregamos cadenas de texto
Lista.append("Python 🐍")
Lista.append("JAVA 🧾")

#Longitud de una lista
print("Longitud de la Lista => "+str(len(Lista)))
#Accedemos a la información de la lista
print("Elemento 1 => "+str(Lista[0]))
print("Elemento 6 => "+str(Lista[5]))

#Imprimimos Lista
print(Lista)

#Creación de Matrices
Matrix = []

Matrix.append(["⚽",'📚','📕'])
Matrix.append(['😉','😥','😎'])

#Imprimimos una matriz
print(Matrix)