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

class Cuadro:
    def __init__(self,lado):
        mitad = round(lado/2)
        self.r1 = Recta(-mitad, mitad, mitad, mitad)
        self.r2 = Recta(-mitad, -mitad, mitad, -mitad)
        self.r3 = Recta(-mitad, -mitad, -mitad, mitad)
        self.r4 = Recta(mitad, -mitad, mitad, mitad)
    def traza(self):
        self.r1.traza()
        self.r2.traza()
        self.r3.traza()
        self.r4.traza()

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

class CuadroInscritro:
    def __init__(self, diametro):
        r = round(diametro/2)
        l = round(2*r/math.sqrt(2))
        self.cir = Circunferencia(r)
        self.cua = Cuadro(l)
    def traza(self):
        self.cir.traza()
        self.cua.traza() 

class CuadroCircunscrito:
    def __init__(self, lado):
        r = round(lado/2)
        self.cua = Cuadro(lado)
        self.cir = Circunferencia(r)
    def traza(self):
        self.cua.traza()
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
    
    recta = Recta(50, 50, 200, 200)
    cuadro = Cuadro(20)
    circ = Circunferencia(80)
    cuadIn = CuadroInscritro(180)
    cuadCir = CuadroCircunscrito(180)

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

        #cuadro.traza()
        #circ.traza()
        #cuadIn.traza()
        cuadCir.traza()

        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()

