screen_size = [500, 500]

import math
import OpenGL.GL as GL
import OpenGL.GLUT as GLUT

class Circle:

    def __init__(self,centerX,centerY,radius,resolution):
        
        self.position = [0, 0]
        self.velocity = [0, 0]

        self.centerX = centerX
        self.centerY = centerY
        self.radius = radius
        self.resolution = resolution
    
    def Draw(self):
        
        GL.glBegin(GL.GL_TRIANGLE_FAN)
        GL.glVertex2d(self.position[0],self.position[1])

        for i in range(self.resolution + 1):
            angle = 2.0 * math.pi * (i / self.resolution)
            x = self.position[0] + math.cos(angle) * self.radius
            y = self.position[1] + math.sin(angle) * self.radius

            GL.glVertex2d(x,y)
        
        GL.glEnd()


    def ApplyForces(self):

        self.position[0] = self.position[0] + self.velocity[0]
        self.position[1] = self.position[1] + self.velocity[1]
        
        # Gravity Force
        self.velocity[1] = self.velocity[1] -9.81 / 20

        restitution = 0.95
        # Border Collision Force

        # X
        if self.position[0] - self.radius < 0:
            self.position[0] = self.radius
            self.velocity[0] = abs(self.velocity[0]) * restitution
        elif self.position[0] + self.radius > screen_size[0]:
            self.position[0] = screen_size[0] - self.radius
            self.velocity[0] = -abs(self.velocity[0]) * restitution

        # Y
        if self.position[1] - self.radius < 0:
            self.position[1] = self.radius
            self.velocity[1] = abs(self.velocity[1]) * restitution
        elif self.position[1] + self.radius > screen_size[1]:
            self.position[1] = screen_size[1] - self.radius
            self.velocity[1] = -abs(self.velocity[1]) * restitution

    def InitConditions(self,init_position,init_velocity):

        self.position = init_position
        self.velocity = init_velocity
