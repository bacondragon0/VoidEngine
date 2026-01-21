import object
import math
import OpenGL.GL as GL
import OpenGL.GLUT as GLUT

G = 50
fBounce = 0.95
unit_scale = 0.1
screen_size = [1000, 750]

class Force:
    def __init__(self):
        self.unit_scale = 1
        self.dist_scale = 1

    def Kinetic(objects):
        for obj in objects:
            obj.position[0] = obj.position[0] + obj.velocity[0]
            obj.position[1] = obj.position[1] + obj.velocity[1]

    def WallBounce(objects):
        for obj in objects:
            if obj.position[0] - obj.radius < 0:
                obj.position[0] = obj.radius
                obj.velocity[0] = abs(obj.velocity[0]) * fBounce
            elif obj.position[0] + obj.radius > screen_size[0]:
                obj.position[0] = screen_size[0] - obj.radius
                obj.velocity[0] = -abs(obj.velocity[0]) * fBounce

        # Y
            if obj.position[1] - obj.radius < 0:
                obj.position[1] = obj.radius
                obj.velocity[1] = abs(obj.velocity[1]) * fBounce
            elif obj.position[1] + obj.radius > screen_size[1]:
                obj.position[1] = screen_size[1] - obj.radius
                obj.velocity[1] = -abs(obj.velocity[1]) * fBounce

    def Collision(objects):
        for i in range(len(objects)):
            a = objects[i]

            for j in range(i+1,len(objects)):
                b = objects[j]

                if math.dist(a.position, b.position) < (a.radius + b.radius):
                    a.velocity[0] *= -1
                    a.velocity[1] *= -1
                    b.velocity[0] *= -1
                    b.velocity[1] *= -1

    def Gravity(objects):
        Glocal = G
        for i in range(len(objects)):
            a = objects[i]

            for j in range(i+1,len(objects)):
                b = objects[j]

                d_x = b.position[0] - a.position[0]
                d_y = b.position[1] - a.position[1]

                r_2 = d_x**2 + d_y**2
                r = math.sqrt(r_2)
                gForce = (Glocal * a.mass * b.mass) / r_2 * unit_scale

                n_x = d_x / r
                n_y = d_y / r

                a_x = (gForce / a.mass) * n_x 
                a_y = (gForce / a.mass) * n_y 
                b_x = -(gForce / b.mass) * n_x 
                b_y = -(gForce / b.mass) * n_y 

                a.ApplyAcceleration(a_x,a_y)
                b.ApplyAcceleration(b_x,b_y)

        
    