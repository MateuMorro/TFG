import math
from entities.carsimulator.Race import Race
from entities.carsimulator.Car import Car
from entities.carsimulator.CarLogState import CarLogState
from entities.Inici import Inici
try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
except:
    print ('OpenGL wrapper for python not found')

last_time = 0
right_pressed = False
left_pressed = False
up_pressed = False
down_pressed = False



class Scene:
    # los parametros son, (circuito), (1 si va solo y 0 si el usuario), y el (numero de coches)
    def __init__(self,n,k,m):
        self._race = Race(n,k,m)
        self._aspect_ratio = 1
        self._number_simulations = 1;
        self._best_time  = None

    def reset_race(self):
        self._race.reset()
        self._number_simulations = self._number_simulations + 1

    def init(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)

    def reshape(self, width, height):
        glViewport(0, 0, width, height)
        self._aspect_ratio = width/height

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # visualización 3D
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, self._aspect_ratio, 1, 1501)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # la cámara está sobre el primer coche
        # más adelante se colocará sobe el coche más adelantado
        c = self._race.get_first_car()
        gluLookAt(c.position.x, c.position.y, 120,
                  c.position.x, c.position.y, 0,
                  0, 1, 0)

        glEnable(GL_DEPTH_TEST)

        # renderizamos el circuito
        self._race.render()

        # mostramos el punto que determina la distancia recorrida por el coche
        # for s in self._race.track.segments:
        #     if s.in_segment(c.position):
        #         point = s.advanced(c.position)
        #         if point is not None:
        #             glBegin(GL_LINES)
        #             glColor3f(1, 1, 1)
        #             glVertex3f(point.x-1, point.y-1, 0)
        #             glVertex3f(point.x+1, point.y+1, 0)
        #             glVertex3f(point.x-1, point.y+1, 0)
        #             glVertex3f(point.x+1, point.y-1, 0)
        #             glEnd()

        # visualización 2D
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-1*self._aspect_ratio, 1*self._aspect_ratio, -1, 1, -1, 1)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glDisable(GL_DEPTH_TEST)

        # mostramos las lecturas de profundidad de los "sensores" del coche
        glColor3f(1, 1, 1)
        width_bar = 0.01
        x = -len(c.collision_distances)/2*width_bar
        for dis in c.collision_distances:
            y1 = -0.9
            y2 = y1 + dis/150
            glBegin(GL_QUADS)
            glVertex3f(x, y1, 0)
            glVertex3f(x, y2, 0)
            glVertex3f(x+width_bar*0.95, y2, 0)
            glVertex3f(x+width_bar*0.95, y1, 0)
            glEnd()
            x = x + width_bar

        # mostramos la distancia total recorrida
        glRasterPos2f(-0.95*self._aspect_ratio, -0.9)
        text = "Distància {0:.2f}".format(c.get_total_distance())
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int( ord(ch)))

        glRasterPos2f(-0.95*self._aspect_ratio, -0.85)
        if self._best_time is not None:
            text = "Temps {0:.2f} MillorTemps {1:.2f}".format(self._race.total_time, self._best_time)
        else:
            text = "Temps {0:.2f}".format(self._race.total_time)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int( ord(ch)))

        glRasterPos2f(-0.95*self._aspect_ratio, -0.80)
        text = "Voltes {0}".format(c.laps)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int( ord(ch)))

        glRasterPos2f(-0.95*self._aspect_ratio, -0.75)
        text = "Vius {0}".format(self._race.alives)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int( ord(ch)))

        glRasterPos2f(-0.95*self._aspect_ratio, -0.70)
        text = "Simulacions {0}".format(self._number_simulations)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int( ord(ch)))

        glRasterPos2f(-0.95*self._aspect_ratio, -0.65)
        text = "Valors {0:.2f}, {1:.2f}".format(c.current_speed, c.steer)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int( ord(ch)))

        glutSwapBuffers()

    def special(self, key, x, y):
        global right_pressed, left_pressed, up_pressed, down_pressed
        if key == GLUT_KEY_RIGHT:
            right_pressed = True
        if key == GLUT_KEY_LEFT:
            left_pressed = True
        if key == GLUT_KEY_END:
            sys.exit()
            #self.reset_race()
        if key == GLUT_KEY_UP:
            up_pressed = True
        if key == GLUT_KEY_DOWN:
            down_pressed = True

    def specialUp(self, key, x, y):
        global right_pressed, left_pressed, up_pressed, down_pressed
        if key == GLUT_KEY_RIGHT:
            right_pressed = False
        if key == GLUT_KEY_LEFT:
            left_pressed = False
        if key == GLUT_KEY_UP:
            up_pressed = False
        if key == GLUT_KEY_DOWN:
            down_pressed = False

    def idle(self):
        global right_pressed, left_pressed, up_pressed, down_pressed
        global last_time
        time = glutGet(GLUT_ELAPSED_TIME)



        if last_time == 0 or time >= last_time + 30:
        #if True:
            elapsed_time = (time-last_time)/1000
            elapsed_time = 80/1000

            # conduce la red neuronal
            for car in self._race.cars:
                if not car.collision:
                    # conduce el usuario
                    if car.number == 0:
                        if right_pressed:
                            car = self._race.cars[0]
                            car.rotate(-5*(2*math.pi)/360)
                            car.teclat(1)
                        else:
                            if left_pressed:
                                car = self._race.cars[0]
                                car.rotate(5*(2*math.pi)/360)
                                car.teclat(0)
                            else:
                                car.teclat(0.5)

                        # VELOCITAT!
                        if up_pressed:
                                car.current_speed = min(10,car.current_speed+5*0.03)
                                car.vel(1)
                        else:
                            if down_pressed:
                                    car.current_speed = max(car.current_speed - 5 * 0.03,1)
                                    car.vel(0)
                            else:
                                car.vel(0.5)


                    else:
                        r = car._net.feedforward(car.collision_distances)
                        steer = r[0]
                        speed = r[1]
                        car.steer = steer[0]-0.5
                        car.rotate((steer[0]-0.5) * 10*(2*math.pi)/360)
                        car.current_speed = 7 # 3 + min(3, speed[0] * 3)

            self._race.simulate(elapsed_time)

            ##################
            # chapuza jose maria

            #if len(self._race.cars) > 0:
            #    c = self._race.cars[0]
            #    l = c.log
            #    if (l.time > 5):
            #        l.setCar(c, 3)

            ##################

            if self._race.get_first_car().laps == 2 or (self._race.alives == 0):
                for c in self._race.cars:
                    if c.collision == False:
                        self._race.get_first_car().collision_time = self._race.total_time
                if (self._race.get_first_car().laps == 2)  and (self._best_time is None or self._race.total_time < self._best_time):
                    self._best_time = self._race.total_time
                self.reset_race()

            # if last_time == 0 or time >= last_time + 40:
            last_time = time
            glutPostRedisplay()

    def visible(self, vis):
        if vis == GLUT_VISIBLE:
            glutIdleFunc(self.idle)
        else:
            glutIdleFunc(None)

def main(circuit,usuari,cotxes):
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

    #glutInitWindowSize(800, 800)
    glutInitWindowSize(1000, 900)
    glutInitWindowPosition(50, 50)

    glutCreateWindow(b'Car Machine Learning')


    # Especificar quin circuit volem
    # el primer numero es el circuito
    # el segundo numero es si conduce el usuario (=0) o si no conduce el usuario (=1)
    # el tercer numero es el numero de coches que hay

    #s = Scene(12,0,1)
    s=Scene(circuit,usuari,cotxes)
    s.init()

    glutDisplayFunc(s.display)
    glutReshapeFunc(s.reshape)
    glutVisibilityFunc(s.visible)
    glutSpecialFunc(s.special)
    glutSpecialUpFunc(s.specialUp)

    glutMainLoop()

#[circuit, usuari, cotxes] = Inici().save()
if __name__ == '__main__':
    #main(circuit,usuari,cotxes)
    main(12,0,1)
