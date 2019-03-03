import csv

class LoadSensorsUsuari(object):
    def __init__(self,n):
        self.__sensors=[]
        if n==1:
            with open('../Sensors/SensorsCircuit3.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__sensors.append([[float(i[k])] for k in range(0, 11)])
        if n==2:
            with open('../Sensors/SensorsCircuit4.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__sensors.append([[float(i[k])] for k in range(0, 11)])
        if n==3:
            with open('../Sensors/SensorsCircuit11.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__sensors.append([[float(i[k])] for k in range(0, 11)])

        if n==4:
            with open('../Sensors/SensorsCircuit6.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__sensors.append([[float(i[k])] for k in range(0, 11)])

        if n==5:
            with open('../Sensors/SensorsCircuit1.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__sensors.append([[float(i[k])] for k in range(0, 11)])

        if n==6:
            with open('../Sensors/SensorsCircuit2.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__sensors.append([[float(i[k])] for k in range(0, 11)])

        if n==7:
            with open('../Sensors/SensorsCircuit5.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__sensors.append([[float(i[k])] for k in range(0, 11)])

        if n==8:
            with open('../Sensors/SensorsCircuit7.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__sensors.append([[float(i[k])] for k in range(0, 11)])

        if n==9:
            with open('../Sensors/SensorsCircuit8Cheste.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__sensors.append([[float(i[k])] for k in range(0, 11)])

        if n==10:
            with open('../Sensors/SensorsCircuit10.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__sensors.append([[float(i[k])] for k in range(0, 11)])

        if n==11:
            with open('../Sensors/SensorsCircuit9Catalunya.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__sensors.append([[float(i[k])] for k in range(0, 11)])

        if n==12:
            with open('../Sensors/SensorsCircuit12.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__sensors.append([[float(i[k])] for k in range(0, 11)])


    def sensors(self):
        return self.__sensors
