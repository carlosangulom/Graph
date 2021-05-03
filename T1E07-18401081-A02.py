import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

class Recta:
    def __init__(self,xi,yi,xf,yf):
        self.xi = xi
        self.yi = yi
        self.xf = xf
        self.yf = yf
    
    def traza(self):
        dx = self.xf-self.xi
        dy = self.yf-self.yi

        if abs(dx) >= abs(dy):
            pasos = abs(dx)
        else:
            pasos = abs(dy)

        incX = dx/pasos
        incY = dy/pasos
        
        x,y = self.xi,self.yi
        i = 0
        glBegin(GL_POINTS)
        while i <= pasos:
            glVertex2i(round(x),round(y))
            x += incX
            y += incY
            i +=1
        glEnd()


class Circunferencia:
    def __init__(self,radio):
        self.r = radio

    def traza(self):
        glBegin(GL_POINTS)
        x = 0
        y = self.r
        DPk = 3-2*self.r
        while x <= y:
            glVertex2i(x,y)
            glVertex2i(x,-y)
            glVertex2i(-x,y)
            glVertex2i(-x,-y)
            glVertex2i(y,x)
            glVertex2i(y,-x)
            glVertex2i(-y,x)
            glVertex2i(-y,-x)
            if DPk >= 0:
                DPk += 4*(x-y)+10
                y -= 1
            else:
                DPk += 4*x+6
            x += 1
        glEnd()

class TrianguloEquilatero :
    def __init__(self,d):
        r = round(d/2)
        l = round(math.sqrt(3)* r)
        ap = round((math.sqrt(3)/6)*l)
        la = round(l/2)

        self.r1 = Recta(0,r,la,-ap)
        self.r2 = Recta(-la,-ap,la,-ap)
        self.r3 = Recta(-la,-ap,0,r)

    def traza(self):
        self.r1.traza()
        self.r2.traza()
        self.r3.traza()

class TrianguloEquilateroInscrito:
    def __init__(self,d):
        r = round(d/2)
        self.tri = TrianguloEquilatero(d)
        self.cir = Circunferencia(r)
    def traza(self):
        self.tri.traza()
        self.cir.traza()

def main():
    if not glfw.init():
        return

    ventana = glfw.create_window(501,501,"POINTS",None,None)
    if not ventana:
        glfw.terminate()
        return

    glfw.make_context_current(ventana)

    glClearColor(1,1,1,0) #RGB
    gluOrtho2D(-250,250,-250,250)#Sugiere ventana de 501x501
    
    triangulo = TrianguloEquilateroInscrito(200)

    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)

        #ejes 
        glColor(0,0,0)
        glBegin(GL_POINTS)
        for i in range(-250,251):
            glVertex2i(i,0)
            glVertex2i(0,i)
        glEnd()

        triangulo.traza()

        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()

