def main():

    #Entrada
    xi, yi = 0,0
    xf, yf = 0,9

    dx = xf - xi
    dy = yf - yi

    if abs(dx) >= abs(dy):
        pasos = abs(dx)
    else:
        pasos = abs(dy)
    
    incX = dx/pasos
    incY = dy/pasos

    print("dx=", dx, " dy=", dy)

    x,y = xi,yi
    i = 0

    while i <= pasos:
        print(round(x),round(y))
        x += incX
        y += incY
        i += 1
    

if __name__ == "__main__":
    main()