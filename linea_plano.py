def funcionX(x, xi, yi, xf, yf): 
    return round((x-xi)*(yf-yi)/(xf-xi)+yi)

def funcionY(y, xi, yi, xf, yf): 
    return round((y-yi)*(xf-xi)/(yf-yi)+xi)

def main():

    #Entrada
    xi, yi = 1,1
    xf, yf = 9,9

    dx = xf - xi
    dy = yf - yi

    print("dx=", dx, " dy=", dy)
    
    if dx >= dy:
        x = xi
        while x <= xf:
            print (x, funcionX(x, xi, yi, xf, yf))
            x += 1
    else:
        y = yi
        while y <= yf:
            print (funcionY(y, xi, yi, xf, yf), y)
            y += 1

if __name__ == "__main__":
    main()