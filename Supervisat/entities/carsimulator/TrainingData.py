from entities.carsimulator.CarLogState import CarLogState
from entities.carsimulator.LoadSensorsUsuari import LoadSensorsUsuari
import numpy as np

from scipy.stats import norm


def nova_tecla(tecla):
    tecla = np.asarray(tecla)
    nova = []
    for i in range(9):
        nova.append(0.5)
    w = np.arange(0, 2, 0.2)
    w = norm.pdf(w)
    w = w / sum(w)
    w = w[::-1]
    for i in range(1, len(tecla) - 10):
        nova.append(np.dot(tecla[i:i + 10], w))
    n=[]
    for i in range(len(nova)):
        n.append(nova[i])
    n.append(0.5)
    n.append(0.5)
    return n

class TrainingData(object):


    def __init__(self,n):

        sensors1 = LoadSensorsUsuari(1).sensors()
        tecla1 = CarLogState(1).load()[4]
        vel1 = CarLogState(1).load()[5]


        sensors2 = LoadSensorsUsuari(2).sensors()
        tecla2 = CarLogState(2).load()[4]
        vel2 = CarLogState(2).load()[5]

        sensors3 = LoadSensorsUsuari(3).sensors()
        tecla3 = CarLogState(3).load()[4]
        vel3 = CarLogState(3).load()[5]

        sensors4 = LoadSensorsUsuari(4).sensors()
        tecla4 = CarLogState(4).load()[4]
        vel4 = CarLogState(4).load()[5]

        sensors5 = LoadSensorsUsuari(5).sensors()
        tecla5 = CarLogState(5).load()[4]
        vel5 = CarLogState(5).load()[5]

        sensors6 = LoadSensorsUsuari(6).sensors()
        tecla6 = CarLogState(6).load()[4]
        vel6 = CarLogState(6).load()[5]

        sensors7 = LoadSensorsUsuari(7).sensors()
        tecla7 = CarLogState(7).load()[4]
        vel7 = CarLogState(7).load()[5]

        sensors8 = LoadSensorsUsuari(8).sensors()
        tecla8 = CarLogState(8).load()[4]
        vel8 = CarLogState(8).load()[5]

        sensors9 = LoadSensorsUsuari(9).sensors()
        tecla9 = CarLogState(9).load()[4]
        vel9 = CarLogState(9).load()[5]


        sensors10 = LoadSensorsUsuari(10).sensors()
        tecla10 = CarLogState(10).load()[4]
        vel10 = CarLogState(10).load()[5]

        sensors11 = LoadSensorsUsuari(11).sensors()
        tecla11 = CarLogState(11).load()[4]
        vel11 = CarLogState(11).load()[5]

        sensors12 = LoadSensorsUsuari(12).sensors()
        tecla12 = CarLogState(12).load()[4]
        vel12 = CarLogState(12).load()[5]

        self.__training_data = []


        for i in range(len(tecla1)):
            values = sensors1[i]
            if i > 100:
                for j in range(10):
                    values.append([vel1[i - (10 - j) * 10]])
            else:
                if 10 < i < 100:
                    for j in range(10):
                        values.append([vel1[i - (10 - j)]])
                else:
                    for j in range(10):
                        values.append([0.5])
            values = np.asarray(values)
            resultado = np.asarray([[tecla1[i]], [vel1[i]]])
            self.__training_data.append([values, resultado])

        for i in range(len(tecla2)):
            values = sensors2[i]
            if i > 100:
                for j in range(10):
                    values.append([vel2[i - (10 - j) * 10]])
            else:
                if 10 < i < 100:
                    for j in range(10):
                        values.append([vel2[i - (10 - j)]])
                else:
                    for j in range(10):
                        values.append([0.5])
            values = np.asarray(values)
            resultado = np.asarray([[tecla2[i]], [vel2[i]]])
            self.__training_data.append([values, resultado])

        for i in range(len(tecla3)):
            values = sensors3[i]
            if i>100:
                for j in range(10):
                    values.append([vel3[i-(10-j)*10]])
            else:
                if 10<i<100:
                    for j in range(10):
                        values.append([vel3[i - (10 - j)]])
                else:
                    for j in range(10):
                        values.append([0.5])
            values = np.asarray(values)
            resultado = np.asarray([[tecla3[i]], [vel3[i]]])
            self.__training_data.append([values, resultado])


        for i in range(len(tecla4)):
            values = sensors4[i]
            if i > 100:
                for j in range(10):
                    values.append([vel4[i - (10 - j) * 10]])
            else:
                if 10 < i < 100:
                    for j in range(10):
                        values.append([vel4[i - (10 - j)]])
                else:
                    for j in range(10):
                        values.append([0.5])
            values = np.asarray(values)
            resultado = np.asarray([[tecla4[i]], [vel4[i]]])
            self.__training_data.append([values, resultado])

        for i in range(len(tecla5)):
            values = sensors5[i]
            if i > 100:
                for j in range(10):
                    values.append([vel5[i - (10 - j) * 10]])
            else:
                if 10 < i < 100:
                    for j in range(10):
                        values.append([vel5[i - (10 - j)]])
                else:
                    for j in range(10):
                        values.append([0.5])
            values = np.asarray(values)
            resultado = np.asarray([[tecla5[i]], [vel5[i]]])
            self.__training_data.append([values, resultado])

        for i in range(len(tecla6)):
            values = sensors6[i]
            if i > 100:
                for j in range(10):
                    values.append([vel6[i - (10 - j) * 10]])
            else:
                if 10 < i < 100:
                    for j in range(10):
                        values.append([vel6[i - (10 - j)]])
                else:
                    for j in range(10):
                        values.append([0.5])
            values = np.asarray(values)
            resultado = np.asarray([[tecla6[i]], [vel6[i]]])
            self.__training_data.append([values, resultado])

        for i in range(len(tecla7)):
            values = sensors7[i]
            if i > 100:
                for j in range(10):
                    values.append([vel7[i - (10 - j) * 10]])
            else:
                if 10 < i < 100:
                    for j in range(10):
                        values.append([vel7[i - (10 - j)]])
                else:
                    for j in range(10):
                        values.append([0.5])
            values = np.asarray(values)
            resultado = np.asarray([[tecla7[i]], [vel7[i]]])
            self.__training_data.append([values, resultado])

        for i in range(len(tecla8)):
            values = sensors8[i]
            if i > 100:
                for j in range(10):
                    values.append([vel8[i - (10 - j) * 10]])
            else:
                if 10 < i < 100:
                    for j in range(10):
                        values.append([vel8[i - (10 - j)]])
                else:
                    for j in range(10):
                        values.append([0.5])
            values = np.asarray(values)
            resultado = np.asarray([[tecla8[i]], [vel8[i]]])
            self.__training_data.append([values, resultado])

        for i in range(len(tecla9)):
            values = sensors9[i]
            if i > 100:
                for j in range(10):
                    values.append([vel9[i - (10 - j) * 10]])
            else:
                if 10 < i < 100:
                    for j in range(10):
                        values.append([vel9[i - (10 - j)]])
                else:
                    for j in range(10):
                        values.append([0.5])
            values = np.asarray(values)
            resultado = np.asarray([[tecla9[i]], [vel9[i]]])
            self.__training_data.append([values, resultado])

        for i in range(len(tecla10)):
            values = sensors10[i]
            if i > 100:
                for j in range(10):
                    values.append([vel10[i - (10 - j) * 10]])
            else:
                if 10 < i < 100:
                    for j in range(10):
                        values.append([vel10[i - (10 - j)]])
                else:
                    for j in range(10):
                        values.append([0.5])
            values = np.asarray(values)
            resultado = np.asarray([[tecla10[i]], [vel10[i]]])
            self.__training_data.append([values, resultado])

        for i in range(len(tecla11)):
            values = sensors11[i]
            if i > 100:
                for j in range(10):
                    values.append([vel11[i - (10 - j) * 10]])
            else:
                if 10 < i < 100:
                    for j in range(10):
                        values.append([vel11[i - (10 - j)]])
                else:
                    for j in range(10):
                        values.append([0.5])
            values = np.asarray(values)
            resultado = np.asarray([[tecla11[i]], [vel11[i]]])
            self.__training_data.append([values, resultado])

        for i in range(len(tecla12)):
            values = sensors12[i]
            if i > 100:
                for j in range(10):
                    values.append([vel12[i - (10 - j) * 10]])
            else:
                if 10 < i < 100:
                    for j in range(10):
                        values.append([vel12[i - (10 - j)]])
                else:
                    for j in range(10):
                        values.append([0.5])
            values = np.asarray(values)
            resultado = np.asarray([[tecla12[i]], [vel12[i]]])
            self.__training_data.append([values, resultado])



    def training(self):
        return self.__training_data