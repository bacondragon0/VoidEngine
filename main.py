from object import Circle

import math
import OpenGL.GL as GL
import OpenGL.GLUT as GLUT

# Variables
screen_size = [500, 500]

x2 = Circle(250,250,25,64)
x2.InitConditions([300,250],[12,20])

x3 = Circle(250,250,25,64)
x3.InitConditions([150,250],[12,20])

objects = [x2,x3]

def display():
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GL.glLoadIdentity()
    
    # Draw Primitives
    x2.Draw()
    x3.Draw()

    GL.glFlush()

def update(value):

    collisions()

    x2.ApplyForces()
    x3.ApplyForces()

    # Advance Frame
    GLUT.glutPostRedisplay()
    GLUT.glutTimerFunc(16, update, 0)  # 60 FPS

def reshape(width, height):
    screen_size[0], screen_size[1] = width, height
    GL.glViewport(0, 0, width, height)
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()
    GL.glOrtho(0, width, 0, height, -1, 1)

def collisions():
    for i in range(len(objects)):
        a = objects[i]

        for j in range(i,len(objects)):
            b = objects[j]

            if math.dist(a.position, b.position) < (a.radius + b.radius):
                a.velocity[0] *= -1
                a.velocity[1] *= -1
                b.velocity[0] *= -1
                b.velocity[1] *= -1

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