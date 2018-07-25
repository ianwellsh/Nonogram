#Sergio Alvarez Pedreros 18.035.923-0
#Ian Wells Hernandez 18.783.804-5
import numpy as np
    
def createNonogram(n,m):#n y m son las dimensiones de la matriz
    nonogram=np.zeros((n,m))
    return nonogram

def rules(nonogram,rowHints,columnHints,n,m):  
    i=-1#flag
    print("Si la pista es 0 rellena con 1")
    for listP in rowHints:
        #Si dentro de las pistas encuentra un 0, rellena con 1
        i=i+1
        for elem in listP:            
            if(elem == 0):
                for y in range(m):
                    nonogram[i,y] = 1
    print ("Filas")
    printNonogram(nonogram)
    i=-1 #flagreset
    for listP in columnHints:
        #Si dentro de las pistas encuentra un 0, rellena con 1
        i=i+1
        for elem in listP:            
            if(elem == 0):
                for x in range(n):
                    nonogram[x,i] = 1
    print ("Columnas")
    printNonogram(nonogram)
    i=-1 #flagreset
    print("Si la pista es igual a M ó N, rellena con 2")
    for listP in rowHints:
        #Si dentro de las pistas encuentra un n, rellena toda la fila con 2
        i=i+1
        for elem in listP:            
            if(elem == m):
                for y in range(m):
                    nonogram[i,y] = 2
    print ("Filas")
    printNonogram(nonogram)
                    
    i=-1 #flag reset    
    for listP in columnHints:
        #Si dentro de las pistas encuentra un m, rellena toda la fila con 2
        i=i+1
        for elem in listP:            
            if(elem == n):
                for x in range(n):
                    nonogram[x,i] = 2
    print("Columnas")    
    printNonogram(nonogram)                    
    i=-1 #flag reset    
    for listP in rowHints:
        #Si hay solo una pista, y esta es mayor a n/2 o m/2, pinta
        i=i+1
        for elem in listP:
            if(elem > m/2):
                for y in range(elem - (m-elem)):
                    nonogram[i,m-elem + y] = 2
    
    i=-1 #flag reset 
    print("Si la pista es mayor a n/2 ó m/2, se pintan las celdas que van si ó si")
    print("Filas")
    printNonogram(nonogram)          
    i=-1 #flag reset    
    for listP in columnHints:
        #Si hay solo una pista, y esta es mayor a n/2 o m/2, pinta
        i=i+1
        for elem in listP:
            if(elem > n/2):
                for x in range(elem - (m-elem)):
                    nonogram[m-elem + x,i] = 2
                    
    print("Columnas")
    printNonogram(nonogram)          
    #falta función que revise las pistas múltiples, y lea las pintadas 
    #en caso que se puedan completar
    print("Si la pista ya se cumple, el resto se rellena con 1")
    i=-1 #flag reset
    for listP in rowHints:
        cont= 0
        i=i+1
        for elem in listP:
            for y in range(n):
                if(nonogram[i,y]==2):
                    cont=cont+1
            if(elem-cont == 0):
                nonogram[i,y+1:]=1
                            
                
    print("Fila")
    printNonogram(nonogram)
    i=-1 #flag reset
    for listP in rowHints:
        cont= 0
        i=i+1
        for elem in listP:
            for x in range(m):
                if(nonogram[x,i]==2):
                    cont=cont+1
                if(elem-cont == 0):
                    nonogram[x+1:,i]=1
                
    print("Columna")
    printNonogram(nonogram)
    #falta función que revise las pistas contrarias, en busca de 1's, lo que 
    #indica que se deben pintar puntos ·
    i=-1#flag
    print("Si la pista es 1 y hay solo un 0, se rellena")
    for listP in rowHints:
        #Si dentro de las pistas encuentra un 0, rellena con 1
        i=i+1
        cont=0
        for elem in listP:            
            if(elem == 1):
                for y in range(m):
                    if(nonogram[i,y] == 0):
                        cont=cont+1
                        aux = y
                if(elem-cont == 0):
                    nonogram[i,aux] = 2
                    
                    
    print ("Filas")
    printNonogram(nonogram)
    i=-1 #flagreset
    for listP in columnHints:
        #Si dentro de las pistas encuentra un 0, rellena con 1
        i=i+1
        cont=0
        for elem in listP:            
            if(elem == 1):
                for x in range(n):
                    if(nonogram[x,i] == 0):
                        cont=cont+1
                        aux = x
                if(elem-cont == 0):
                    nonogram[aux,i] = 2
                    
    print ("Columnas")
    printNonogram(nonogram)
    
    return nonogram


def printNonogram(nonogram):
    print(nonogram,"\n")
    return

path = '/users/personal/documents/github/nonogram/nonogram.txt'
#path = '/home/killgor/git/Nonogram/nonogram.txt'

file = open(path,'r')
    
n = file.readline()
m = file.readline()
n = int(n)
m = int(m)

nonogram = createNonogram(n,m)
rowHints = []
columnHints = []

for i in range(n):
    hints = file.readline() #se lee una linea del archivo con pistas 
    elementList = []
    for element in hints.split():
        elementList.append(int(element)) #se transforman los elementos en numero
    rowHints.append(elementList)
    
for i in range(m):
    hints = file.readline() #se lee una linea del archivo con pistas 
    elementList = [] 
    for element in hints.split():
        elementList.append(int(element)) #se transforman los elementos en numero
    columnHints.append(elementList)

nonogram = rules(nonogram,rowHints,columnHints,n,m)