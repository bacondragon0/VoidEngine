from object import Particle
from forces import Force
import math
import OpenGL.GL as GL
import OpenGL.GLUT as GLUT

# Variables
screen_size = [1000, 750]

x1 = Particle(250,250,2,10)
x1.InitConditions([screen_size[0]*1/4,screen_size[1]*3/4],[1,0])

x2 = Particle(250,250,3,1000)
x2.InitConditions([screen_size[0] //2 ,screen_size[1] // 2],[0,0])

x3 = Particle(250,250,2,10)
x3.InitConditions([screen_size[0]*3/4 ,screen_size[1]*1/4],[-1,0])

objects = [x1,x2,x3]

def display():
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GL.glLoadIdentity()
    
    # Draw Primitives
    for obj in objects:
        obj.Draw()

    GL.glFlush()

def update(value):
    Force.Collision(objects)
    Force.Gravity(objects)
    Force.Kinetic(objects)
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
    GLUT.glutInitWindowSize(screen_size[0],screen_size[1])
    GLUT.glutCreateWindow(b"HaydenEngine")
    GL.glClearColor(0.0, 0.0, 0.0, 1.0)
    GLUT.glutDisplayFunc(display)
    GLUT.glutReshapeFunc(reshape)
    GLUT.glutTimerFunc(0, update, 0)
    GLUT.glutMainLoop()

if __name__ == "__main__":
    main()