import math

def main():
    r = 10

    x = 0
    y = r

    DPK = 3-2*r

    while x <= y:
        print(x,y)
        print(x,-y)
        print(-x,y)
        print(-x,-y)
        print(y,x)
        print(y,-x)
        print(-y,x)
        print(-y,-x)

        if (DPK >= 0):
            DPK += 4*(x-y)+10
            y -= 1
        else:
            DPK += 4*x+6
        
        x += 1
    
if __name__ == "__main__":
    main()