from object import *

import math
import OpenGL.GL as GL
import OpenGL.GLUT as GLUT

# Variables
screen_size = [500, 500]
position = [screen_size[0] // 2, screen_size[1] // 2]
velocity = [15, 0]

def display():
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GL.glLoadIdentity()
    
    # Draw Primitives
    Circle(position[0],position[1],25,64)

    GL.glFlush()

def update(value):
    position[0] = position[0] + velocity[0]
    position[1] = position[1] + velocity[1]

    # Gravity Force
    velocity[1] = velocity[1] -9.81 / 20

    # Border Collision Force
    if (position[0] <= 0) or (position[0] >= screen_size[0]): velocity[0] = velocity[0] * -0.95
    if (position[1] <= 0) or (position[1] >= screen_size[1]): velocity[1] = velocity[1] * -0.95

    # Advance Frame
    GLUT.glutPostRedisplay()
    GLUT.glutTimerFunc(16, update, 0)  # 60 FPS

def reshape(width, height):
    screen_size[0], screen_size[1] = width, height
    GL.glViewport(0, 0, width, height)
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()
    GL.glOrtho(0, width, 0, height, -1, 1)


def main():
    GLUT.glutInit()
    GLUT.glutInitDisplayMode(GLUT.GLUT_SINGLE | GLUT.GLUT_RGB)
    GLUT.glutInitWindowSize(screen_size[0],screen_size[1])
    GLUT.glutCreateWindow(b"HaydenEngine")
    GL.glClearColor(0.0, 0.0, 0.0, 1.0)
    GLUT.glutDisplayFunc(display)
    GLUT.glutReshapeFunc(reshape)
    GLUT.glutTimerFunc(0, update, 0)
    GLUT.glutMainLoop()


if __name__ == "__main__":
    main()