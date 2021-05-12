import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

import numpy as np
import time

class Cuadrado:
    def __init__(self,lado):#lado
        self.vertices = [[-lado/2,lado/2],
                         [lado/2,lado/2],
                         [lado/2,-lado/2],
                         [-lado/2,-lado/2]]
        
    def traza(self):
        glBegin(GL_LINE_LOOP)
        for v in self.vertices:
            glVertex2fv(v)
        glEnd()        

    def trasladar(self,tx,ty):
        i = 0
        while i < len(self.vertices):
            self.vertices[i][0] += tx
            self.vertices[i][1] += ty
            i += 1
    
    def rotar(self, theta):
        theta = np.radians(theta)
        i = 0
        while i < len(self.vertices):
            x,y = self.vertices[i]
            self.vertices[i][0] = x*np.cos(theta)-y*np.sin(theta)
            self.vertices[i][1] = x*np.sin(theta)+y*np.cos(theta)
            i += 1

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
    
    cuad = Cuadrado(10)
    cuad.rotar(5)
    cuad.trasladar(5,5)

    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)

        glColor(0,0,0)
        glBegin(GL_POINTS)
        for i in range(-250,251):
            glVertex2i(i,0)
            glVertex2i(0,i)
        glEnd()

        cuad.traza()

        time.sleep(0.1)

        cuad.rotar(5)

        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()