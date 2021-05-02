def main():

    #Entrada
    xi, yi = 0,0
    xf, yf = 5,9

    dx = xf - xi
    dy = yf - yi

    print("dx=", dx, " dy=", dy)

    x,y = xi,yi

    while x <= xf:
        print(x,y)
        DPk = 2*x*dy+2*dy-2*y*dx+2*yi*dx-2*xi*dy-dx

        if DPk >= 0 :
            y += 1
            
        x += 1
    

if __name__ == "__main__":
    main()