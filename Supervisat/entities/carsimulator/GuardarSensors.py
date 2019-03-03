
import csv

class GuardarSensors(object):
    def __init__(self,n,guardar):

        if n==1:
            with open('../Sensors/SensorsCircuit3.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)

        if n==2:
            with open('../Sensors/SensorsCircuit4.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)
        if n==3:
            with open('../Sensors/SensorsCircuit11.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)
        if n==4:
            with open('../Sensors/SensorsCircuit6.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)
        if n==5:
            with open('../Sensors/SensorsCircuit1.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)
        if n==6:
            with open('../Sensors/SensorsCircuit2.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)
        if n==7:
            with open('../Sensors/SensorsCircuit5.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)
        if n==8:
            with open('../Sensors/SensorsCircuit7.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)
        if n==9:
            with open('../Sensors/SensorsCircuit8Cheste.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)
        if n==10:
            with open('../Sensors/SensorsCircuit10.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)

        if n==11:
            with open('../Sensors/SensorsCircuit9Catalunya.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)
        if n==12:
            with open('../Sensors/SensorsCircuit12.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)







