def main():
    
    #Caso 2
    #Cuando m >= 1

    #Entrada
    xi, yi = 0,0
    xf, yf = 5,9

    dx = xf - xi
    dy = yf - yi

    print("dx=", dx, " dy=", dy)

    x,y = xi,yi

    while x <= xf:
        print(x,y)
        DPk = 2*y*dx+2*dx-2*x*dy+2*xi*dy-2*yi*dx-dy

        if DPk >= 0 :
            x += 1
            
        y += 1
    

if __name__ == "__main__":
    main()