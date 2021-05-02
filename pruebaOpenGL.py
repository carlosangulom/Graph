import glfw
from OpenGL.GL import *

def main():
    if not glfw.init():
        return

    ventana = glfw.create_window(400, 400, "Prueba GLF&OpenGL", None, None)
    if not ventana:
        glfw.terminate()
        return

    glfw.make_context_current(ventana)

    glClearColor(0,0,0,0)

    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        glfw.swap_buffers(ventana)
    
    glfw.terminate()

if __name__ == "__main__":
    main()
