import math
from entities.carsimulator.RaceUsuari import RaceUsuari
from entities.carsimulator.Car import Car
from entities.carsimulator.CarLogState import CarLogState
import csv
import numpy as np
from typing import List
import pickle


from entities.Inici import Inici
from entities.neuralnetwork.NetworkAmbSensors import NetworkAmbSensors
from entities.carsimulator.LoadSensorsUsuari import LoadSensorsUsuari
from entities.carsimulator.TrainingData import TrainingData
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



class SceneUsuari:
    
    def __init__(self,n,k,m,simulacions,xarxa,option):
        self.__option=option
        self._simulacions = simulacions
        self.__circuit=n
        self._race = RaceUsuari(n,k,m, xarxa)
        self._aspect_ratio = 1
        self._number_simulations = 1
        self._best_time  = None
        self._circuit=n
        self._m=m
        self.entrada_red = None

       
        self._temps = 0




        self.__n=xarxa


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

     
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, self._aspect_ratio, 1, 1501)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # la càmara està sobre el primer cotxe

        c = self._race.get_first_car()
        cotxe_xarxa = self._race._cars[0]

        gluLookAt(c.position.x, c.position.y, 120, c.position.x, c.position.y, 0, 0, 1, 0)

        glEnable(GL_DEPTH_TEST)


        self._race.render()


        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-1*self._aspect_ratio, 1*self._aspect_ratio, -1, 1, -1, 1)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glDisable(GL_DEPTH_TEST)

        # mostram els sensors


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
        text = "Sensors"
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        glRasterPos2f(0.045 * self._aspect_ratio, -0.95)
        text = "S. central".format(self.__circuit)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))


        if self.__circuit in range(1,13):

            glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
            text = "Circuit: {0}".format(self.__circuit)
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
        else:
            glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
            text = "Circuit Test: {0}".format(self.__circuit-12)
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        if self.__option==1:
            glRasterPos2f(-0.95 * self._aspect_ratio, -0.6)
            text = "Iteracions=220   Eta=0.02"
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
        if self.__option == 2:
            glRasterPos2f(-0.95 * self._aspect_ratio, -0.6)
            text = "Iteracions=265   Eta=0.027"
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
        if self.__option == 3:
            glRasterPos2f(-0.95 * self._aspect_ratio, -0.6)
            text = "Iteracions=269   Eta=0.0275"
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
        if self.__option == 4:
            glRasterPos2f(-0.95 * self._aspect_ratio, -0.6)
            text = "Iteracions=600   Eta=0.07"
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))



        glRasterPos2f(-0.95*self._aspect_ratio, -0.9)
        text = "Distància: {0:.2f}".format(cotxe_xarxa.get_total_distance())
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int( ord(ch)))

        glRasterPos2f(-0.95*self._aspect_ratio, -0.85)
        if self._best_time is not None:
            text = "Temps i MillorTemps: {0:.2f},{1:.2f}".format(self._race.total_time, self._best_time)
        else:
            text = "Temps: {0:.2f}".format(self._race.total_time)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int( ord(ch)))

        glRasterPos2f(-0.95*self._aspect_ratio, -0.80)
        text = "Voltes: {0}".format(cotxe_xarxa.laps+1)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int( ord(ch)))

        glRasterPos2f(-0.95*self._aspect_ratio, -0.75)
        text = "Vius: {0}".format(self._race.alives)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int( ord(ch)))

        glRasterPos2f(-0.95*self._aspect_ratio, -0.70)
        text = "Simulacions: {0}".format(self._number_simulations)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int( ord(ch)))

        glRasterPos2f(-0.95*self._aspect_ratio, -0.65)
        text = "Valors: {0:.2f}, {1:.2f}".format(cotxe_xarxa.current_speed, cotxe_xarxa.steer)
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
    def temps(self)-> int:
        return self._temps

    def idle(self):
        global right_pressed, left_pressed, up_pressed,down_pressed
        global last_time
        time = glutGet(GLUT_ELAPSED_TIME)

        if self._number_simulations==1+self._simulacions:
            exit(0)


        elapsed_time = 80 / 1000


        if self._race.alives>0:

                for c in self._race.cars:

                    if  not c.collision:

                        if c.number ==1:
                            c = self._race.cars[1]
                            if right_pressed:
                                c.rotate(-5*(2*math.pi)/360)
                                #car.teclat(1)
                            else:
                                if left_pressed:
                                    c.rotate(5*(2*math.pi)/360)
                                    #car.teclat(0)
                                #else:
                                    #car.teclat(0.5)

                            # VELOCITAT!
                            if up_pressed:
                                    c.current_speed = min(8,c.current_speed+5*0.03)
                                    #car.vel(1)
                            else:
                                if down_pressed:
                                        c.current_speed = max(c.current_speed - 5 * 0.03,2)
                                        #car.vel(0)
                                #else:
                                    #car.vel(0.5)
                        #if c.number==0:
                        #    if c.tempsCar() < len(self._CarLogState.load()[0]):
                        #        c.colocar(self._posicioX[self._temps],self._posicioY[self._temps],self._angle[self._temps],self._vel[self._temps])
                        if c.number == 0 :

                                g=[]
                                for i in c.collision_distances:
                                    g.append([i])
                                c.memoriaSensorCentral().append(g[5][0])
                                if c.tempsCar()<100:
                                    c.SensorCentral().append(g[5][0])
                                    c.SensorCentral().pop(0)
                                    for i in c.SensorCentral():
                                        g.append([i])
                                else:
                                    v=[]
                                    for i in range(10):
                                        v.append(c.memoriaSensorCentral()[c.tempsCar()-i*10])
                                    v.reverse()
                                    for i in v:
                                        g.append([i])
                                self.entrada_red=g
                                g=np.asarray(g)
                                r=self.__n.feedforward(g)

                                steer = r[0]
                                speed = r[1]
                                c.steer = steer[0] - 0.5
                                c.rotate((steer[0] - 0.5) * 10 * (2 * math.pi) / 360)

                                c.current_speed = min(6,max(3,c.current_speed+(speed[0]-0.5)*5*0.03))



                self._race.simulate(elapsed_time)
                self._temps = self._temps +1



                for c in self._race.cars:
                    if not c.collision:
                        c.collision_time = self._race.total_time

                print("Cotxe:  "+ str(self._race.get_first_car().number))
                print("Temps:  "+str(self._race.total_time))
                print("Distància:  "+str(self._race.get_first_car().get_total_distance()))


                if self._race.get_first_car().laps == 2 or (self._race.alives == 0):
                    if (self._race.get_first_car().laps == 2)  and (self._best_time is None or self._race.total_time < self._best_time):
                        self._best_time = self._race.total_time
                    self.reset_race()

            # if last_time == 0 or time >= last_time + 40:
                last_time = time
                glutPostRedisplay()
        else:
            self.reset_race()
            self._temps = 0
            #print(self._race.cars[1].distance)
            #exit()
    def visible(self, vis):
        if vis == GLUT_VISIBLE:
            glutIdleFunc(self.idle)
        else:
            glutIdleFunc(None)

def main(circuit,usuari,cotxes,simulacions,xarxa,option):



    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

    #glutInitWindowSize(800, 800)
    glutInitWindowSize(1000, 900)
    glutInitWindowPosition(50, 50)

    glutCreateWindow(b'Car Machine Learning')



    s=SceneUsuari(circuit,usuari,cotxes,simulacions,xarxa,option)

    s.init()
    glutDisplayFunc(s.display)
    glutReshapeFunc(s.reshape)
    glutVisibilityFunc(s.visible)
    glutSpecialFunc(s.special)
    glutSpecialUpFunc(s.specialUp)
    glutMainLoop()






### ENTRENAMENT ########
# xarxa = NetworkAmbSensors([21, 25, 2])
# # # 0 si entrenam amb el teclat normal, 1 si entrenam amb la conversio a la gausiana
# training_data=TrainingData(0).training()
# #print(training_data)
# epochs = 600
# mini_batch_size = len(training_data)
# eta = 0.05
# xarxa.SGD(training_data, epochs, mini_batch_size, eta,test_data=None)
# pickle.dumps(xarxa)
# f = open('..\\Xarxes\\prova600-005.csv', 'wb')
# pickle.dump(xarxa,f)
# f.close()











def eleccio_de_la_xarxa(opcio):
    if opcio==1:
        return pickle.load(open('..\\Xarxes\\prova220-002.csv', 'rb'))
    if opcio==2:
        return pickle.load(open('..\\Xarxes\\prova265-0027.csv', 'rb'))
    if opcio==3:
        return pickle.load(open('..\\Xarxes\\prova269-00275.csv', 'rb'))
    if opcio==4:
        return pickle.load(open('..\\Xarxes\\prova600-007.csv', 'rb'))

def eleccio_cotxes(u):
    if u==0:
        return 2
    if u==1:
        return 1



finestra=Inici()
finestra.start()
circuit=finestra.circuit()
u=finestra.usuari()
cotxes=eleccio_cotxes(u)
option=finestra.option()
xarxa=eleccio_de_la_xarxa(option)
simulacions=finestra.simulaciones()
usuari=finestra.usuari()






#xarxa = pickle.load(open('..\\Xarxes\\prova265-0027.csv', 'rb'))
#circuit=15
#cotxes=1
#simulacions=1
#option=1

if __name__ == '__main__':
          main(circuit,0,cotxes,simulacions,xarxa,option)


