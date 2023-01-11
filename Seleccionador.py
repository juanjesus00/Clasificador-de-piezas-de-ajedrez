from asyncio.windows_events import NULL
import os
import errno
import shutil
import random

"""clasificador accede a la carpeta donde se guardan las imagenes, para luego generar una lista con todos los nombres
de imagenes"""  
def clasificador (direccion, lista):
    for i in lista:
        imagenes = []
        temp = direccion + i
        contenido = os.listdir(temp)
        for fichero in contenido:
            if os.path.isfile(os.path.join(temp, fichero)) and fichero.endswith('.jpg'):
                imagenes.append(fichero[:-4])
        seleccionador(imagenes, i)
        
"""seleccionador genera una lista con las imagenes aleatorias segun el porcentaje"""     
def seleccionador(imagenes, nombre):
    tamaño = (len(imagenes) * porcentaje)/100
    reducida = [nombre]
    for i in range(int(tamaño)):
        reducida.append(imagenes[random.randint(0, len(imagenes)-1)])
    Rellenar(direccion3, reducida)

def DataSetCreator(direccion2):
    for i in lista2:
        temp = direccion2 + '/DataSet-Chess/' + i
        direccion3 = direccion2 + '/DataSet-Chess/'
        for j in lista:
            temp2 = temp +'/' + j
            os.makedirs(temp2, exist_ok = True)
    return direccion3    

def Rellenar (direccion3, relleno):
    for i in range(1, len(relleno)):
        if(relleno[0] == "Bishop"):
            if(porcentaje == 70):
                shutil.copy(direccion + 'Bishop/' + relleno[i] + '.jpg', direccion3 + 'Entrenamiento/Bishop')
            elif(porcentaje == 40):
                shutil.copy(direccion + 'Bishop/' + relleno[i] + '.jpg', direccion3 + 'Validacion/Bishop')
            elif(porcentaje == 10):
                shutil.copy(direccion + 'Bishop/' + relleno[i] + '.jpg', direccion3 + 'Test/Bishop')
        if(relleno[0] == "King"):
            if(porcentaje == 70):
                shutil.copy(direccion + 'King/' + relleno[i] + '.jpg', direccion3 + 'Entrenamiento/King')
            elif(porcentaje == 40):
                shutil.copy(direccion + 'King/' + relleno[i] + '.jpg', direccion3 + 'Validacion/King')
            elif(porcentaje == 10):
                shutil.copy(direccion + 'King/' + relleno[i] + '.jpg', direccion3 + 'Test/King')
        if(relleno[0] == "knight"):
            if(porcentaje == 70):
                shutil.copy(direccion + 'knight/' + relleno[i] + '.jpg', direccion3 + 'Entrenamiento/knight')
            elif(porcentaje == 40):
                shutil.copy(direccion + 'knight/' + relleno[i] + '.jpg', direccion3 + 'Validacion/knight')
            elif(porcentaje == 10):
                shutil.copy(direccion + 'knight/' + relleno[i] + '.jpg', direccion3 + 'Test/knight')
        if(relleno[0] == "Pawn"):
            if(porcentaje == 70):
                shutil.copy(direccion + 'Pawn/' + relleno[i] + '.jpg', direccion3 + 'Entrenamiento/Pawn')
            elif(porcentaje == 40):
                shutil.copy(direccion + 'Pawn/' + relleno[i] + '.jpg', direccion3 + 'Validacion/Pawn')
            elif(porcentaje == 10):
                shutil.copy(direccion + 'Pawn/' + relleno[i] + '.jpg', direccion3 + 'Test/Pawn')
        if(relleno[0] == "Queen"):
            if(porcentaje == 70):
                shutil.copy(direccion + 'Queen/' + relleno[i] + '.jpg', direccion3 + 'Entrenamiento/Queen')
            elif(porcentaje == 40):
                shutil.copy(direccion + 'Queen/' + relleno[i] + '.jpg', direccion3 + 'Validacion/Queen')
            elif(porcentaje == 10):
                shutil.copy(direccion + 'Queen/' + relleno[i] + '.jpg', direccion3 + 'Test/Queen')
        if(relleno[0] == "Rook"):
            if(porcentaje == 70):
                shutil.copy(direccion + 'Rook/' + relleno[i] + '.jpg', direccion3 + 'Entrenamiento/Rook')
            elif(porcentaje == 40):
                shutil.copy(direccion + 'Rook/' + relleno[i] + '.jpg', direccion3 + 'Validacion/Rook')
            elif(porcentaje == 10):
                shutil.copy(direccion + 'Rook/' + relleno[i] + '.jpg', direccion3 + 'Test/Rook')

#variables globales
direccion = 'D:/TERCERO/PRIMER SEMESTRE/FSI/PRACTICAS/P2/CHESS-DATASET/ENTRENAMIENTO/'
direccion2 = 'D:/TERCERO/PRIMER SEMESTRE/FSI/PRACTICAS/P2'
lista = ["Bishop", "King", "knight", "Pawn", "Queen", "Rook"]
lista2 = ["Entrenamiento", "Test", "Validacion"]

direccion3 = DataSetCreator(direccion2)

PorcentajeLista = [70, 40, 10]   
for i in PorcentajeLista:
    porcentaje = i 
    clasificador(direccion, lista)
    
    
    