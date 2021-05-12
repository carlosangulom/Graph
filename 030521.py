import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

import numpy as np

class Funcion:
    def __init__(self):
        self.vertices = []
        for x in np.linspace(-20,20,200):
            y = x*np.cos(x)
            self.vertices.append([x,y])
    def traza(self):
        glBegin(GL_LINE_STRIP)
        for v in self.vertices:
            glVertex2fv(v)
        glEnd() 

def main():
    if not glfw.init():
        return

    ventana = glfw.create_window(501,501,"POINTS",None,None)
    if not ventana:
        glfw.terminate()
        return

    glfw.make_context_current(ventana)

    glClearColor(1,1,1,0) #RGB
    gluOrtho2D(-20,20,-20,20)#Sugiere ventana de 501x501
    

    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)

        f = Funcion();

        glColor(0,0,0)
        glBegin(GL_POINTS)
        for i in range(-250,251):
            glVertex2i(i,0)
            glVertex2i(0,i)
        glEnd()

        f.traza()

        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()