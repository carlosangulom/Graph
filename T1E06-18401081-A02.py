def main():
    
    #Caso 4
    #Cuando m <= -1

    #Entrada
    xi, yi = 0,0
    xf, yf = 2,-9

    dx = xf - xi
    dy = yf - yi

    print("dx=", dx, " dy=", dy)

    x,y = xi,yi

    while y <= yf:
        print(x,y)
        DPk = 2*dy*x-2*dx*y-2*dx+2*dx*(y-(dy/dx)*x)+dy

        if DPk >= 0 :
            y += 1
        else:
            x -= 1
            y += 1

if __name__ == "__main__":
    main()