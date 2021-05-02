def main():
    
    #Caso 3
    #Cuando -1 <= m <= 0

    #Entrada
    xi, yi = 0,0
    xf, yf = 5,-3

    dx = xf - xi
    dy = yf - yi

    print("dx=", dx, " dy=", dy)

    x,y = xi,yi

    while x <= xf:
        print(x,y)
        DPk = 2*dy*x-2*dx*y+2*dy+2*dx*(y-(dy/dx)*x)+dx

        if DPk <= 0 :
            x += 1
            y -= 1
        else:
            x += 1
       
        
            
        
    

if __name__ == "__main__":
    main()