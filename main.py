from object import Particle

import math
import OpenGL.GL as GL
import OpenGL.GLUT as GLUT

# Variables
screen_size = [1000, 750]
G = 50

x1 = Particle(250,250,2,10)
x1.InitConditions([screen_size[0]*1/4,screen_size[1]*3/4],[3,0])

x2 = Particle(250,250,2,10)
x2.InitConditions([screen_size[0] //2 ,screen_size[1] // 2],[0,3])

x3 = Particle(250,250,2,10)
x3.InitConditions([screen_size[0]*3/4,screen_size[1]*1/4],[-3,0])

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

    collisions()
    gravity()

    for obj in objects:
        obj.ApplyDefaultForces()

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

        for j in range(i+1,len(objects)):
            b = objects[j]

            if math.dist(a.position, b.position) < (a.radius + b.radius):
                a.velocity[0] *= -1
                a.velocity[1] *= -1
                b.velocity[0] *= -1
                b.velocity[1] *= -1

def gravity():
    for i in range(len(objects)):
        a = objects[i]

        for j in range(i+1,len(objects)):
            b = objects[j]

            d_x = b.position[0] - a.position[0]
            d_y = b.position[1] - a.position[1]

            r_2 = d_x**2 + d_y**2
            r = math.sqrt(r_2)
            gForce = (G * a.mass * b.mass) / r_2

            n_x = d_x / r
            n_y = d_y / r

            a_x = (gForce / a.mass) * n_x
            a_y = (gForce / a.mass) * n_y
            b_x = -(gForce / b.mass) * n_x
            b_y = -(gForce / b.mass) * n_y

            a.ApplyAcceleration(a_x,a_y)
            b.ApplyAcceleration(b_x,b_y)

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