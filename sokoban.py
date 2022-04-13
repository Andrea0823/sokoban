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
	[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
	[3,1,1,1,1,1,1,1,4,1,1,1,1,1,1,4,1,3],
	[3,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,3],
	[3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
  [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3], 
  [3,1,1,4,1,1,1,1,1,1,1,1,0,1,1,1,1,3],
  [3,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,3],
  [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3],
  [3,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,1,3],  
	[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
      ]#Define el mapa de juego
  mapa = np.array(mapa)
  result = np.where(mapa == 0)
  muneco_fila=result[0]
  muneco_columna=result[1]
  def __init__(self):
    pass
  def imprimirMapa(self): #Metodo para imprimir el mapa
    for j in range(10):#Recorre cada caracterer del juego
      for i in range(18):
        if self.mapa[j][i] == 0:
          print("🐶", end = "")
        elif self.mapa[j][i] == 1:
          print("  ", end = "")
        elif self.mapa[j][i] == 2:
          print("🎁", end = "")
        elif self.mapa[j][i] == 3:
          print("🌳", end = "")

        else:
          print(self.mapa[j][i], end=" ")
      print()
    print() #Imprime una linea vacia
  def moverDerecha(self):
    #5.-Personaje, espacio 
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

#Mover Izquierda      
  def moverIzquierda(self):
    if self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==1:
      self.mapa[self.muneco_fila,self.muneco_columna-1]=0
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.muneco_columna-=1
    #18.- Personaje, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==4:
      self.mapa[self.muneco_fila,self.muneco_columna-1]=5
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.muneco_columna-=1
    #19.-Personaje, caja, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==2 and self.mapa[self.muneco_fila,self.muneco_columna-2]==1 :
      self.mapa[self.muneco_fila,self.muneco_columna-1]=0
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila,self.muneco_columna-2]=2
      self.muneco_columna-=1
     #20.-Personaje, caja, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==2 and self.mapa[self.muneco_fila,self.muneco_columna-2]==4 :
      self.mapa[self.muneco_fila,self.muneco_columna-1]=0
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila,self.muneco_columna-2]=6
      self.muneco_columna-=1    
      #    #21.-Personaje, caja_meta, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==6 and self.mapa[self.muneco_fila,self.muneco_columna-2]==1 :
      self.mapa[self.muneco_fila,self.muneco_columna-1]=5
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila,self.muneco_columna-2]=2
      self.muneco_columna-=1
    #22.-Personaje, caja_meta, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==6 and self.mapa[self.muneco_fila,self.muneco_columna-2]==4 :
      self.mapa[self.muneco_fila,self.muneco_columna-1]=5
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila,self.muneco_columna-2]=6
      self.muneco_columna-=1
    #23.-Personaje_meta, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==1:
      self.mapa[self.muneco_fila,self.muneco_columna-1]=0
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.muneco_columna-=1 
    #24.-Personaje_meta,espacio
        #24.-Personaje_meta, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==4:
      self.mapa[self.muneco_fila,self.muneco_columna-1]=5
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.muneco_columna-=1
    #25.-Personaje_meta, caja, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==2 and self.mapa[self.muneco_fila,self.muneco_columna-2]==1 :
      self.mapa[self.muneco_fila,self.muneco_columna-1]=0
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila,self.muneco_columna-2]=2
      self.muneco_columna-=1
    #26.-Personaje_meta, caja, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]==5 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==2 and self.mapa[self.muneco_fila,self.muneco_columna-2]==4 :
      self.mapa[self.muneco_fila,self.muneco_columna-1]=0
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila,self.muneco_columna-2]=6
      self.muneco_columna-=1
    #27.-Personaje_meta, caja_meta, espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==6 and self.mapa[self.muneco_fila,self.muneco_columna-2]==1 :
      self.mapa[self.muneco_fila,self.muneco_columna-1]=5
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila,self.muneco_columna-2]=2
      self.muneco_columna-=1
    #28.-Personaje_meta, caja_meta, meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila,self.muneco_columna-1]==6 and self.mapa[self.muneco_fila,self.muneco_columna-2]==4 :
      self.mapa[self.muneco_fila,self.muneco_columna-1]=5
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila,self.muneco_columna-2]=6
      self.muneco_columna-=1

    # Mover Arriba
  def moverArriba(self): 
     #29.- Espacio / Personaje 
    if self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila-1,self.muneco_columna]=0
      self.muneco_fila-=1
    #30.- Meta / Personaje 
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila-1,self.muneco_columna]=5
      self.muneco_fila-=1
        #31.- Espacio / Caja / Personaje
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==2 and  self.mapa[self.muneco_fila-2,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila-1,self.muneco_columna]=0
      self.mapa[self.muneco_fila-2,self.muneco_columna]=2
      self.muneco_fila-=1
    #32.- Meta / Caja / Personaje
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==2 and  self.mapa[self.muneco_fila-2,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila-1,self.muneco_columna]=0
      self.mapa[self.muneco_fila-2,self.muneco_columna]=6
      self.muneco_fila-=1
        #33.- Espacio / Caja_meta / Personaje
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==6 and  self.mapa[self.muneco_fila-2,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila-1,self.muneco_columna]=5
      self.mapa[self.muneco_fila-2,self.muneco_columna]=2
      self.muneco_fila-=1
    #34.- Meta / Caja_meta / Personaje
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==6 and  self.mapa[self.muneco_fila-2,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila-1,self.muneco_columna]=5
      self.mapa[self.muneco_fila-2,self.muneco_columna]=6
      self.muneco_fila-=1
    #35.- Espacio / Personaje_meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila-1,self.muneco_columna]=0
      self.muneco_fila-=1
   #36.- Meta / Personaje_meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila-1,self.muneco_columna]=5
      self.muneco_fila-=1
    #37.- Espacio / Caja / Personaje_meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==2 and  self.mapa[self.muneco_fila-2,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila-1,self.muneco_columna]=0
      self.mapa[self.muneco_fila-2,self.muneco_columna]=2
      self.muneco_fila-=1
    #38.- Meta / Caja / Personaje_meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==2 and  self.mapa[self.muneco_fila-2,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila-1,self.muneco_columna]=0
      self.mapa[self.muneco_fila-2,self.muneco_columna]=6
      self.muneco_fila-=1     
    #39.- Espacio / Caja_meta / Personaje_meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==6 and  self.mapa[self.muneco_fila-2,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila-1,self.muneco_columna]=5
      self.mapa[self.muneco_fila-2,self.muneco_columna]=2
      self.muneco_fila-=1         
    #40.- Meta / Caja_meta / Personaje_meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila-1,self.muneco_columna]==6 and  self.mapa[self.muneco_fila-2,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila-1,self.muneco_columna]=5
      self.mapa[self.muneco_fila-2,self.muneco_columna]=6
      self.muneco_fila-=1
    # Metodo moverAbajo
  def moverAbajo(self): 
    #41.- Espacio / Personaje 
    if self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila+1,self.muneco_columna]=0
      self.muneco_fila+=1 
    #42.- Personaje / Meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila+1,self.muneco_columna]=5
      self.muneco_fila+=1  
   #43.- Personaje / Caja / Espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==2 and  self.mapa[self.muneco_fila+2,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila+1,self.muneco_columna]=0
      self.mapa[self.muneco_fila+2,self.muneco_columna]=2
      self.muneco_fila+=1       
   #44.- Personaje / Caja / Meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==2 and  self.mapa[self.muneco_fila+2,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila+1,self.muneco_columna]=0
      self.mapa[self.muneco_fila+2,self.muneco_columna]=6
      self.muneco_fila+=1 
   #45.- Personaje / Caja_meta / Espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==6 and  self.mapa[self.muneco_fila+2,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila+1,self.muneco_columna]=5
      self.mapa[self.muneco_fila+2,self.muneco_columna]=2
      self.muneco_fila+=1 
   #46.- Personaje / Caja_meta / Meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 0 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==6 and  self.mapa[self.muneco_fila+2,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=1
      self.mapa[self.muneco_fila+1,self.muneco_columna]=5
      self.mapa[self.muneco_fila+2,self.muneco_columna]=6
      self.muneco_fila+=1       
    #47.- Personaje_meta / Espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila+1,self.muneco_columna]=0
      self.muneco_fila+=1         
    #48.- Personaje_meta / Meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila+1,self.muneco_columna]=5
      self.muneco_fila+=1  
   #49.- Personaje_meta / Caja / Espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==2 and  self.mapa[self.muneco_fila+2,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila+1,self.muneco_columna]=0
      self.mapa[self.muneco_fila+2,self.muneco_columna]=2
      self.muneco_fila+=1            
    #50.- Personaje_meta / Caja / Meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==2 and  self.mapa[self.muneco_fila+2,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila+1,self.muneco_columna]=0
      self.mapa[self.muneco_fila+2,self.muneco_columna]=6
      self.muneco_fila+=1        
     #51.- Personaje_meta / Caja_meta / Espacio
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==6 and  self.mapa[self.muneco_fila+2,self.muneco_columna]==1:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila+1,self.muneco_columna]=5
      self.mapa[self.muneco_fila+2,self.muneco_columna]=2
      self.muneco_fila+=1         
    #52.- Personaje_meta / Caja_meta / Meta
    elif self.mapa[self.muneco_fila,self.muneco_columna]== 5 and  self.mapa[self.muneco_fila+1,self.muneco_columna]==6 and  self.mapa[self.muneco_fila+2,self.muneco_columna]==4:
      self.mapa[self.muneco_fila,self.muneco_columna]=4
      self.mapa[self.muneco_fila+1,self.muneco_columna]=5
      self.mapa[self.muneco_fila+2,self.muneco_columna]=6
      self.muneco_fila+=1
juego = Sokoban()#Crea un objeto para jugar
juego.imprimirMapa()#Imprime el mapa

while True:#Bucle para jugar N veces
    intrucciones = "d-Derecha\na-Izquierda\nr-Arriba\nl-Abajo\nq-Salir" #Instrucciones
    print(intrucciones)
    movimientos = input("mover a: ")#Lee el movimiento
    if movimientos == 'd': #si es d - mover a la derecha
        juego.moverDerecha() #mueve el muñeco  a la derecha
        juego.imprimirMapa() #imprime el mapa
    elif movimientos == 'a': #si es a - mover a la izquierda
        juego.moverIzquierda() #mueve el muñeco  a la izquierda
        juego.imprimirMapa() #imprime el mapa
    elif movimientos == 'r': #si es r - mover a arriba
        juego.moverArriba()#mueve el muñeco  a arriba
        juego.imprimirMapa()#imprime el mapa
    elif movimientos == 'l': #si es l - mover a abajo
        juego.moverAbajo()#mueve el muñeco  a abajo
        juego.imprimirMapa()#imprime el mapa
    elif movimientos == "q":#si es q-salir
        print("Saliste del juego")#Imprmir mensaje
        break #Rompe el ciclo whilee