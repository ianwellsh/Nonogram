#Sergio Alvarez Pedreros 18.035.923-0
#Ian Wells Hernández 18.783.804-5
import numpy as np
    
def createNonogram(n,m):#n y m son las dimensiones de la matriz
    nonogram=np.zeros((n,m))
    return nonogram

def rules(nonogram,rowHints,columnHints,n,m):
    #pistas=Pistas.split()
    x=0
    y=0
    for listP in rowHints:
        #Si dentro de las pistas encuentra un 0, rellena toda la fila con 1
        if(listP==0):
            for y in range(m):
                nonogram[x,y]=1
        if(listP==m):
            for y in range(m):
                nonogram[x,y]=2

        x=x+1
        
    for listP in columnHints:
        if(listP==0):
            for x in range(n):
                nonogram[x,y]=1
        if(listP==n):
            for x in range(m):
                nonogram[x,y]=2
        y=y+1
    print(nonogram)
    return nonogram

def printNonogram(nonogram):
    print(nonogram)
    return

path = '/users/personal/documents/github/nonogram/nonogram.txt'

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
print(rowHints)
print(columnHints)
nonogram = rules(nonogram,rowHints,columnHints,n,m)
#printNonogram(nonogram)