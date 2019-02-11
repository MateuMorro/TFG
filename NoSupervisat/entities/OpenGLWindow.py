import math
import pickle
from entities.carsimulator.Race import Race
from entities.carsimulator.Car import Car

from entities.Inici import Inici
from entities.neuralnetwork.Network import Network
from entities.guardar30xarxes import guardar30xarxes
from entities.load30xarxes import load30xarxes
import numpy as np
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

    def __init__(self,n,k,m,g,x,simulacions,ponderacio,de_facil_a_dificil):
        self.__circuit=n
        self.__de_facil_a_dificil=de_facil_a_dificil
        self.__ponderacio=ponderacio
        self._race = Race(n,k,m,g,x,self.__ponderacio)
        self._aspect_ratio = 1
        self._number_simulations = 1
        self._best_time  = None
        self._simulacions=simulacions
        self._temps = 0
        self._memoriaSensorCentral=[[] for i in range(m)]
        #self._SensorCentral = [[20] * 10 for i in range(60)]
        self._tempsCar=[0]*m
        self.entrada_red = None
        self.__m=m
        self.__k=k

    def number_simulations(self):
        return int(self._number_simulations)

    def ponderacio(self):
        return self.__ponderacio
    def reset_race(self,):
        if self._simulacions!=1:
            self._race.reset()
        self._number_simulations = self._number_simulations + 1

    def init(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)

    def reshape(self, width, height):
        glViewport(0, 0, width, height)
        self._aspect_ratio = width/height

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, self._aspect_ratio, 1, 1501)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()


        c = self._race.get_first_car()

        gluLookAt(c.position.x, c.position.y, 120,
                  c.position.x, c.position.y, 0,
                  0, 1, 0)
        glEnable(GL_DEPTH_TEST)

        self._race.render()


# Visualitzar el circuit sense cotxes
######################################################################################################################

        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # glClearColor(1,1,1,1)
        # px = 45
        # py = 50
        # glLoadIdentity()
        # gluLookAt(px, py, 270,
        #           px, py, 0,
        #           0, 1, 0)
        # self._race.track.render2()
        # glutSwapBuffers()
        # return
#####################################################################################################################





        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-1*self._aspect_ratio, 1*self._aspect_ratio, -1, 1, -1, 1)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glDisable(GL_DEPTH_TEST)


        if self.__k==0:
            cotxe_xarxa = self._race._cars[1]
            # mostramos las lecturas de profundidad de los "sensores" del coche
            glColor3f(1, 1, 1)
            width_bar = 0.01
            x = -len(cotxe_xarxa.collision_distances) / 2 * width_bar - 0.2
            for dis in cotxe_xarxa.collision_distances:
                y1 = -0.9
                y2 = y1 + dis / 150
                glBegin(GL_QUADS)
                glVertex3f(x, y1, 0)
                glVertex3f(x, y2, 0)
                glVertex3f(x + width_bar * 0.95, y2, 0)
                glVertex3f(x + width_bar * 0.95, y1, 0)
                glEnd()
                x = x + width_bar

            glColor3f(1, 1, 1)
            width_bar = 0.01
            x = -len(cotxe_xarxa.collision_distances) / 2 * width_bar + 0.2
            if self.entrada_red != None:
                for dis in self.entrada_red[11:20]:
                    y1 = -0.9
                    y2 = y1 + dis[0] / 150
                    glBegin(GL_QUADS)
                    glVertex3f(x, y1, 0)
                    glVertex3f(x, y2, 0)
                    glVertex3f(x + width_bar * 0.95, y2, 0)
                    glVertex3f(x + width_bar * 0.95, y1, 0)
                    glEnd()
                    x = x + width_bar



            glRasterPos2f(-0.15 * self._aspect_ratio, -0.95)
            text = "Sensores"
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            glRasterPos2f(0.045 * self._aspect_ratio, -0.95)
            text = "S. central".format(self.__circuit)
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            if self.__circuit in range(1, 13):

                glRasterPos2f(-0.95 * self._aspect_ratio, -0.5)
                text = "Circuit: {0}".format(self.__circuit)
                for ch in text:
                    glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
            else:
                glRasterPos2f(-0.95 * self._aspect_ratio, -0.5)
                text = "Circuit Test: {0}".format(self.__circuit - 12)
                for ch in text:
                    glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            if self.__ponderacio == 1:
                glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
                text = "Ponderació: d"
                for ch in text:
                    glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
            if self.__ponderacio == 2:
                glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
                text = "Ponderació: d^2"
                for ch in text:
                    glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
            if self.__ponderacio == 3:
                glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
                text = "Ponderació: v"
                for ch in text:
                    glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            if self.__ponderacio == 4:
                glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
                text = "Ponderació: d*v"
                for ch in text:
                    glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
            if self.__ponderacio == 5:
                glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
                text = "Ponderació: d con AG"
                for ch in text:
                    glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            if self.__de_facil_a_dificil == 0:
                glRasterPos2f(-0.95 * self._aspect_ratio, -0.6)
                text = "De fàcil a difícil: Si"
                for ch in text:
                    glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            if self.__de_facil_a_dificil == 1:
                glRasterPos2f(-0.95 * self._aspect_ratio, -0.6)
                text = "De fàcil a difícil: No"
                for ch in text:
                    glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            glRasterPos2f(-0.95 * self._aspect_ratio, -0.9)
            text = "Distància: {0:.2f}".format(cotxe_xarxa.get_total_distance())
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            glRasterPos2f(-0.95 * self._aspect_ratio, -0.85)
            if self._best_time is not None:
                text = "Temps i MillorTemps: {0:.2f},{1:.2f}".format(self._race.total_time, self._best_time)
            else:
                text = "Temps: {0:.2f}".format(self._race.total_time)
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            glRasterPos2f(-0.95 * self._aspect_ratio, -0.80)
            text = "Voltes: {0}".format(cotxe_xarxa.laps + 1)
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            glRasterPos2f(-0.95 * self._aspect_ratio, -0.75)
            text = "Vius: {0}".format(self._race.alives)
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            glRasterPos2f(-0.95 * self._aspect_ratio, -0.70)
            text = "Simulacions: {0}".format(self._number_simulations)
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            glRasterPos2f(-0.95 * self._aspect_ratio, -0.65)
            text = "Valors {0:.2f}, {1:.2f}".format(cotxe_xarxa.current_speed, cotxe_xarxa.steer)
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
                # glRasterPos2f(-0.95*self._aspect_ratio, -0.65)
                # text = "Velocitat i direcció: {0:.2f}".format(c.current_speed)
                # for ch in text:
                #   glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int( ord(ch)))
        else:

            glColor3f(1, 1, 1)
            width_bar = 0.01
            x = -len(c.collision_distances) / 2 * width_bar - 0.2
            for dis in c.collision_distances:
                y1 = -0.9
                y2 = y1 + dis / 150
                glBegin(GL_QUADS)
                glVertex3f(x, y1, 0)
                glVertex3f(x, y2, 0)
                glVertex3f(x + width_bar * 0.95, y2, 0)
                glVertex3f(x + width_bar * 0.95, y1, 0)
                glEnd()
                x = x + width_bar

            glColor3f(1, 1, 1)
            width_bar = 0.01
            x = -len(c.collision_distances) / 2 * width_bar + 0.2
            if self.entrada_red != None:
                for dis in self.entrada_red[11:20]:
                    y1 = -0.9
                    y2 = y1 + dis[0] / 150
                    glBegin(GL_QUADS)
                    glVertex3f(x, y1, 0)
                    glVertex3f(x, y2, 0)
                    glVertex3f(x + width_bar * 0.95, y2, 0)
                    glVertex3f(x + width_bar * 0.95, y1, 0)
                    glEnd()
                    x = x + width_bar



            glRasterPos2f(-0.15 * self._aspect_ratio, -0.95)
            text = "Sensores"
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            glRasterPos2f(0.045 * self._aspect_ratio, -0.95)
            text = "S. central".format(self.__circuit)
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            if self.__circuit in range(1, 13):

                glRasterPos2f(-0.95 * self._aspect_ratio, -0.5)
                text = "Circuit: {0}".format(self.__circuit)
                for ch in text:
                    glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
            else:
                glRasterPos2f(-0.95 * self._aspect_ratio, -0.5)
                text = "Circuit Test: {0}".format(self.__circuit - 12)
                for ch in text:
                    glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            if self.__ponderacio == 1:
                glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
                text = "Ponderació: d"
                for ch in text:
                    glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
            if self.__ponderacio == 2:
                glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
                text = "Ponderació: d^2"
                for ch in text:
                    glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
            if self.__ponderacio == 3:
                glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
                text = "Ponderació: v"
                for ch in text:
                    glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            if self.__ponderacio == 4:
                glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
                text = "Ponderació: d*v"
                for ch in text:
                    glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
            if self.__ponderacio == 5:
                glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
                text = "Ponderació: d con AG"
                for ch in text:
                    glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            if self.__de_facil_a_dificil == 0:
                glRasterPos2f(-0.95 * self._aspect_ratio, -0.6)
                text = "De fàcil a difícil: Si"
                for ch in text:
                    glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            if self.__de_facil_a_dificil == 1:
                glRasterPos2f(-0.95 * self._aspect_ratio, -0.6)
                text = "De fàcil a difícil: No"
                for ch in text:
                    glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            glRasterPos2f(-0.95 * self._aspect_ratio, -0.9)
            text = "Distància: {0:.2f}".format(c.get_total_distance())
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            glRasterPos2f(-0.95 * self._aspect_ratio, -0.85)
            if self._best_time is not None:
                text = "Temps i MillorTemps: {0:.2f},{1:.2f}".format(self._race.total_time, self._best_time)
            else:
                text = "Temps: {0:.2f}".format(self._race.total_time)
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            glRasterPos2f(-0.95 * self._aspect_ratio, -0.80)
            text = "Voltes: {0}".format(c.laps + 1)
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            glRasterPos2f(-0.95 * self._aspect_ratio, -0.75)
            text = "Vius: {0}".format(self._race.alives)
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            glRasterPos2f(-0.95 * self._aspect_ratio, -0.70)
            text = "Simulacions: {0}".format(self._number_simulations)
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

            glRasterPos2f(-0.95 * self._aspect_ratio, -0.65)
            text = "Valors {0:.2f}, {1:.2f}".format(c.current_speed, c.steer)
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
                # glRasterPos2f(-0.95*self._aspect_ratio, -0.65)
                # text = "Velocitat i direcció: {0:.2f}".format(c.current_speed)
                # for ch in text:
                #   glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int( ord(ch)))


        glutSwapBuffers()



    def special(self, key, x, y):
        global right_pressed, left_pressed,up_pressed,down_pressed
        if key == GLUT_KEY_RIGHT:
            right_pressed = True
        if key == GLUT_KEY_LEFT:
            left_pressed = True
        if key == GLUT_KEY_END:
            #sys.exit()
            self.reset_race()
        if key == GLUT_KEY_UP:
            up_pressed = True
        if key == GLUT_KEY_DOWN:
            down_pressed = True


    def specialUp(self, key, x, y):
        global right_pressed, left_pressed,up_pressed,down_pressed
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

        if self._number_simulations == 1+self._simulacions:
            xarxes=[]
            for i in range(self.__m):
                xarxes.append(self._race.cars[i].net)
            #guardar30xarxes(xarxes,self.__ponderacio,self.__de_facil_a_dificil)

            exit(0)


        if last_time == 0 or time >= last_time + 30:
        #if True:
            #elapsed_time = (time-last_time)/1000
            elapsed_time = 80/1000

            # condueix la xarxa neuronal
            for car in self._race.cars:
                if not car.collision:
                    # condueix l'usuari
                    if car.number == 0:
                        if right_pressed:
                            car = self._race.cars[0]
                            car.rotate(-5*(2*math.pi)/360)
                            car.teclat(1)
                            #car.steer=1
                        else:
                            if left_pressed:
                                car = self._race.cars[0]
                                car.rotate(5*(2*math.pi)/360)
                                car.teclat(0)
                             #   car.steer = -1
                            else:
                                car.teclat(0.5)
                              #  car.steer=0
                        if up_pressed:
                                    car.current_speed = min(8, car.current_speed + 5 * 0.03)
                                    car.vel(1)
                        else:
                                    if down_pressed:
                                        car.current_speed = max(car.current_speed - 5 * 0.03, 2)
                                        car.vel(0)
                                    else:
                                        car.vel(0.5)




                    else:
                        g = []
                        for i in car.collision_distances:
                            g.append([i])

                        car.memoriaSensorCentral().append(g[5][0])
                        if car.carTemps() < 100:
                            car.SensorCentral().append(g[5][0])
                            car.SensorCentral().pop(0)
                            for i in car.SensorCentral():
                                g.append([i])
                        else:
                            v = []
                            for i in range(10):

                                v.append(car.memoriaSensorCentral()[car.carTemps() - i * 10])
                            v.reverse()
                            for i in v:
                                g.append([i])
                        self.entrada_red = g
                        #r = car._net.feedforward(car.collision_distances)
                        g = np.asarray(g)
                        r = car._net.feedforward(g)
                        steer = r[0]
                        speed = r[1]
                        car.steer = steer[0]-0.5
                        car.rotate((steer[0]-0.5) * 10*(2*math.pi)/360)

                        car.current_speed = 3 + min(3, speed[0] * 3)

                        self._tempsCar[car.number-1]=self._tempsCar[car.number-1]+1


            self._temps = self._temps + 1
            self._race.simulate(elapsed_time)





            for c in self._race.cars:
                if not c.collision:
                    c.collision_time = self._race.total_time


            print(self._race.get_first_car().number)
            print(self._race.total_time)
            print(self._race.get_first_car().get_total_distance())







            if self._race.get_first_car().laps == 2 or (self._race.alives == 0):
                print(self._race.total_time)
                print(self._race.get_first_car().get_total_distance())
                for c in self._race.cars:
                    if not c.collision:
                        c.collision_time = self._race.total_time
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


# circuit, usuari, cotxes, si se guarda o no, xarxes,simulacions
def main(circuit,usuari,cotxes,g,x,simulacions,ponderacio,de_):

    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

    #glutInitWindowSize(800, 800)
    glutInitWindowSize(1000, 900)
    glutInitWindowPosition(50, 50)

    glutCreateWindow(b'Car Machine Learning')




    s=Scene(circuit,usuari,cotxes,g,x,simulacions,ponderacio,de_facil_a_dificil)

    s.init()

    glutDisplayFunc(s.display)
    glutReshapeFunc(s.reshape)
    glutVisibilityFunc(s.visible)
    glutSpecialFunc(s.special)
    glutSpecialUpFunc(s.specialUp)


    glutMainLoop()


def eleccio_del_cotxe(ponderacion, de_facil_a_dificil):
    if ponderacion == 1 and de_facil_a_dificil == 0:
        return int(27)
    if ponderacion == 2 and de_facil_a_dificil == 0:
        return int(30)
    if ponderacion == 3 and de_facil_a_dificil == 0:
        return int(12)
    if ponderacion == 4 and de_facil_a_dificil == 0:
        return int(15)
    if ponderacion == 5 and de_facil_a_dificil == 0:
        return int(7)
    if ponderacion == 1 and de_facil_a_dificil == 1:
        return int(14)
    if ponderacion == 2 and de_facil_a_dificil == 1:
        return int(16)
    if ponderacion == 3 and de_facil_a_dificil == 1:
        return int(19)
    if ponderacion == 4 and de_facil_a_dificil == 1:
        return int(19)
    if ponderacion == 5 and de_facil_a_dificil == 1:
        return int(28)







finestra=Inici()
finestra.start()
circuit=finestra.circuit()
ponderacio=finestra.ponderacion()
de_facil_a_dificil=finestra.de_facil_a_dificil()
cotxes=finestra.cotxes()
simulacions=1
usuari=finestra.usuari()



if usuari==1:
    if cotxes!=1:
        x=load30xarxes(ponderacio,de_facil_a_dificil).xarxa()
    else:
        x=[load30xarxes(ponderacio,de_facil_a_dificil).xarxa_cotxe_n(eleccio_del_cotxe(ponderacio,de_facil_a_dificil)-1)]
else:
    cotxes=2
    x=[]
    x.append(load30xarxes(ponderacio,de_facil_a_dificil).xarxa_cotxe_n(eleccio_del_cotxe(ponderacio,de_facil_a_dificil)-1))
    x.append(load30xarxes(ponderacio, de_facil_a_dificil).xarxa_cotxe_n(eleccio_del_cotxe(ponderacio, de_facil_a_dificil)-1))










if __name__ == '__main__':

        g=0 # si és 1 se guarda en UsuariCircuit el cotxe inicial

        main(circuit,usuari,cotxes,g,x,simulacions,ponderacio,de_facil_a_dificil)

