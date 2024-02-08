tablero=[
  [0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],
  ]

def cargaArchivo():
  archivo=open("tablero.txt","r")
  for i in range(0,9):
    for j in range(0,9):
      tablero[i][j]=int(archivo.readline())

def encuentraVacio(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == 0:
                return (i, j)

    return None

def revisar(tablero, valor, pos):
    for i in range(len(tablero[0])):
        if tablero[pos[0]][i] == valor and pos[1] != i:
            return False
    for i in range(len(tablero)):
        if tablero[i][pos[1]] == valor and pos[0] != i:
            return False
    regionX = pos[1] // 3
    regionY = pos[0] // 3

    for i in range(regionY*3, regionY*3 + 3):
        for j in range(regionX * 3, regionX*3 + 3):
            if tablero[i][j] == valor and (i,j) != pos:
                return False

    return True

def resuelveTablero(tablero):
    Vacio = encuentraVacio(tablero)
    if not Vacio:
        return True
    else:
        fil, col = Vacio
    for i in range(1,10):
        if revisar(tablero, i, (fil, col)):
            tablero[fil][col] = i
            if resuelveTablero(tablero):
              return True
            tablero[fil][col] = 0

    return False

def imprimeTablero(tablero):
  for i in range(0,9):
    print("")
    j=0
    print(tablero[i][j+0]," ",tablero[i][j+1]," ",tablero[i][j+2]," ",tablero[i][j+3]," ",tablero[i][j+4]," ",tablero[i][j+5]," ",tablero[i][j+6]," ",tablero[i][j+7]," ",tablero[i][j+8])

def main():
  cargaArchivo()
  resuelveTablero(tablero)
  print("Solución del Tablero:")
  imprimeTablero(tablero)
  print("\nHasta pronto\n")

main()