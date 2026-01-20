from main import screen_size

import math
import OpenGL.GL as GL
import OpenGL.GLUT as GLUT

class Circle:
    def __init__(self,centerX,centerY,radius,resolution):

        GL.glBegin(GL.GL_TRIANGLE_FAN)
        GL.glVertex2d(centerX,centerY)

        for i in range(resolution + 1):
            angle = 2.0 * math.pi * (i / resolution)
            x = centerX + math.cos(angle) * radius
            y = centerY + math.sin(angle) * radius

            GL.glVertex2d(x,y)
        
        GL.glEnd()