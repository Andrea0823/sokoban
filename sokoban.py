print("hola")
import numpy as np
class Sokoban:
#Reprsentacion de comandos del juego------------
  #0 = muñeco 
  #1 = espacio
  #2 = caja
  #3 = paredes
  #4 = metas
  #5 = muñeco_meta
  #6 = caja_meta
  #mapa = [3,1,1,1,0,1,1,1,3]#Define el mapa de juego

  mapa = [
	[3,3,3,3,3,3,3,3,3,3,3,3],
	[3,1,1,1,1,1,1,1,1,1,1,3],
	[3,1,1,1,0,1,1,1,1,1,1,3],
	[3,1,1,1,1,1,1,1,1,1,1,3],
    [3,1,1,1,1,1,1,1,1,1,1,3], 
    [3,1,1,1,1,1,1,1,1,1,1,3],  
	[3,3,3,3,3,3,3,3,3,3,3,3]
      ]#Define el mapa de juego
  mapa = np.array(mapa)
  result = np.where(mapa == 0)
  muneco_fila=result[0]
  muneco_columna=result[1]
  def __init__(self):
    pass
  def imprimirMapa(self): #Metodo para imprimir el mapa
      for j in range(7):#Recorre cada caracterer del juego
        for i in range(12):
          if self.mapa[j][i] == 1:#Si encuentra un numero 1 -  espacio
            #for a in range(len(self.mapa[0])):
            print("_", end = "")#Cambiar un 1 por un ""
          elif self.mapa[j][i] == 3: #3-pared
            #for a in range(len(self.mapa)):
            print("#", end = "")#Cambia un 3 por un simbolo
            
          else:
            print(self.mapa[j][i], end="")
        print()
      print() #Imprime una linea vacia
      #mover
def moverDerecha(self):
    #5.- Personaje, espacio 
    if self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==1:
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila,self.muneco_columna+1]=0
        self.muneco_columna+=1
        #6.-Personaje, meta    
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==4:
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila,self.muneco_columna+1]=5
        self.muneco_columna+=1
    #7.-Personaje, caja, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==2 and self.mapa[self.muneco_fila,self.muneco_columna+2]==1 :
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila,self.muneco_columna+1]=0
        self.mapa[self.muneco_fila,self.muneco_columna+2]=2
        self.muneco_columna+=1
    #8.-Personaje, caja, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==2 and self.mapa[self.muneco_fila,self.muneco_columna+2]==4 :
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila,self.muneco_columna+1]=0
        self.mapa[self.muneco_fila,self.muneco_columna+2]=6
        self.muneco_columna+=1
    #9.-Personaje, caja_meta, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==6 and self.mapa[self.muneco_fila,self.muneco_columna+2]==1 :
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila,self.muneco_columna+1]=5
        self.mapa[self.muneco_fila,self.muneco_columna+2]=2
        self.muneco_columna+=1
    #10.-Personaje, caja_meta, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==6 and self.mapa[self.muneco_fila,self.muneco_columna+2]==4 :
        self.mapa[self.muneco_fila,self.muneco_columna]=1
        self.mapa[self.muneco_fila,self.muneco_columna+1]=5
        self.mapa[self.muneco_fila,self.muneco_columna+2]=6
        self.muneco_columna+=1
    #11.-Personaje_meta, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==1:
        self.mapa[self.muneco_fila,self.muneco_columna]=4
        self.mapa[self.muneco_fila,self.muneco_columna+1]=0
        self.muneco_columna+=1
    #12.-Personaje_meta, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==4:
        self.mapa[self.muneco_fila,self.muneco_columna]=4
        self.mapa[self.muneco_fila,self.muneco_columna+1]=5
        self.muneco_columna+=1
    #13.-Personaje_meta, caja, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==2 and self.mapa[self.muneco_fila,self.muneco_columna+2]==1 :
        self.mapa[self.muneco_fila,self.muneco_columna]=4
        self.mapa[self.muneco_fila,self.muneco_columna+1]=0
        self.mapa[self.muneco_fila,self.muneco_columna+2]=2
        self.muneco_columna+=1
    #14.-Personaje_meta, caja, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==2 and self.mapa[self.muneco_fila,self.muneco_columna+2]==4 :
        self.mapa[self.muneco_fila,self.muneco_columna]=4
        self.mapa[self.muneco_fila,self.muneco_columna+1]=0
        self.mapa[self.muneco_fila,self.muneco_columna+2]=6
        self.muneco_columna+=1
    #15.-Personaje_meta, caja_meta, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==6 and self.mapa[self.muneco_fila,self.muneco_columna+2]==1 :
        self.mapa[self.muneco_fila,self.muneco_columna]=4
        self.mapa[self.muneco_fila,self.muneco_columna+1]=5
        self.mapa[self.muneco_fila,self.muneco_columna+2]=2
        self.muneco_columna+=1
      #16.-Personaje_meta, caja_meta, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna+1]==6 and self.mapa[self.muneco_fila,self.muneco_columna+2]==4 :
        self.mapa[self.muneco_fila,self.muneco_columna]=4
        self.mapa[self.muneco_fila,self.muneco_columna+1]=5
        self.mapa[self.muneco_fila,self.muneco_columna+2]=6
        self.muneco_columna+=1
        
                  
juego = Sokoban()#Crea un objeto para jugar
juego.imprimirMapa()#Imprime el mapa

while True:#Bucle para jugar N veces
  intrucciones = "d-Derecha\na-Izquierda\nr-Arriba\nl-Abajo\nq-Salir" #Instrucciones
  print(intrucciones)
  movimientos = input("mover a: ")#Lee el movimiento
  if movimientos == 'd': #si es d - mover a la derecha
    juego.moverDerecha()#mueve el muñeco  a la derecha
    juego.imprimirMapa()#imprime el mapa
  elif movimientos == 'a': #si es a - mover a la izquierda
    juego.moverIzquierda()#mueve el muñeco  a la izquierda
    juego.imprimirMapa()#imprime el mapa
  elif movimientos == 'r': #si es r - mover a arriba
    juego.moverArriba()#mueve el muñeco  a arriba
    juego.imprimirMapa()#imprime el mapa
  elif movimientos == 'l': #si es l - mover a abajo
    juego.moverAbajo()#mueve el muñeco  a abajo
    juego.imprimirMapa()#imprime el mapa
  elif movimientos == "q":#si es q-salir
    print("Saliste del juego")#Imprmir mensaje
    break #Rompe el ciclo whilee