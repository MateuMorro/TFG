from typing import List
from entities.carsimulator.GuardarCircuit import GuardarCircuit
from entities.carsimulator.GuardarSensors import GuardarSensors
import csv
from entities.carsimulator.LoadCircuitUsuari import LoadCircuitUsuari

class CarLogState(object):

    def __init__(self,n):

        self.__guardar=[]
        self.__t = 0
        self.__n=n

        #####

        self.__temps = []
        self.__coordenadaX = []
        self.__coordenadaY = []
        self.__angle = []
        self.__teclat = []
        self.__vel=[]

        self.__guardarSensors=[]

    @property
    def time(self) -> float:
        return self.__t

    def add(self,posicioX,posicioY,angle,tecla,velocitat):
        self.__guardar.append([self.__t, posicioX,posicioY,angle,tecla,velocitat])
        self.__t = self.__t + 1

    def guardar(self) -> List[List[float]]:
        return self.__guardar

    def save(self):
            GuardarCircuit(self.__n,self.__guardar)



# revisar jose
    def setCar(self,car,i):
        dato = self.__guardar[i]
        car.position.x = dato[1]
        #jo
        car.position.y = dato[2]
        car.rotate(dato[3])
        car.__teclat = dato[4]
        car.__vel=dato[5]

# nou ######################

    def setSimulation(self,v):
        self.__guardarSensors.append(v)

    def guardarSensors(self) -> List[List[float]]:
        return self.__guardarSensors
    def saveSensors(self)->List[List[float]]:
        GuardarSensors(self.__n, self.__guardarSensors)

############################




##############################

# ESTO TIENE QUE SER UNA CLASE carregar circuit usuari
    def load(self) ->List[List[float]]:

        #with open('..\\UsuariCircuits\\UsuariCircuit12.csv') as cs:
        #    entrada = csv.reader(cs)
        #entrada=LoadCircuitUsuari(self.__n).entrada()
        #for i in entrada:
        #        self.__temps.append(i[0])
        #        self.__coordenadaX.append(float(i[1]))
        #        self.__coordenadaY.append(float(i[2]))
        #        self.__angle.append(float(i[3]))
        #        self.__teclat.append(float(i[4]))
        self.__temps, self.__coordenadaX, self.__coordenadaY, self.__angle, self.__teclat ,self.__vel=LoadCircuitUsuari(self.__n).entrada()
        return self.__temps,self.__coordenadaX,self.__coordenadaY,self.__angle,self.__teclat,self.__vel

