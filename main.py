import math
import config
import OpenGL.GL as GL
import OpenGL.GLUT as GLUT

from forces import Force
from object import Particle

# Variables
screen_size = config.screen_size
dt = config.delta_time

x1 = Particle(250, 250, 8, 10, 64, {'R':255.0,'G':0.0,'B':0.0,'A':100.0})
x1.InitConditions([screen_size[0] // 2, screen_size[1] * 3 / 4], [30, 0])

x2 = Particle(250, 250, 10, 1000 * 2, 64, {'R':0.0,'G':0.0,'B':255.0,'A':100.0})
x2.InitConditions([screen_size[0] // 2, screen_size[1] // 2], [0, 0])



objects = [x1, x2]


def display():
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GL.glLoadIdentity()

    # Draw Primitives
    for obj in objects:
        obj.Draw()

    GL.glFlush()


def update(value):

    Force.Collision(objects, dt)
    Force.Gravity(objects, dt)
    Force.Kinetic(objects, dt)
    Force.WallBounce(objects)

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
    GLUT.glutInitWindowSize(screen_size[0], screen_size[1])
    GLUT.glutCreateWindow(b"HaydenEngine")
    GL.glClearColor(0.0, 0.0, 0.0, 1.0)
    GLUT.glutDisplayFunc(display)
    GLUT.glutReshapeFunc(reshape)
    GLUT.glutTimerFunc(0, update, 0)
    GLUT.glutMainLoop()


if __name__ == "__main__":
    main()
