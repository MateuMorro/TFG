import csv

class LoadCircuitUsuari(object):
    def __init__(self,n):
        self.__temps=[]
        self.__coordenadaX=[]
        self.__coordenadaY=[]
        self.__angle=[]
        self.__teclat=[]
        self.__vel=[]
        if n==1:
            with open('../UsuariCircuits/UsuariCircuit3.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__temps.append(i[0])
                    self.__coordenadaX.append(float(i[1]))
                    self.__coordenadaY.append(float(i[2]))
                    self.__angle.append(float(i[3]))
                    self.__teclat.append(float(i[4]))
                    self.__vel.append(float(i[5]))
        if n==2:
            with open('../UsuariCircuits/UsuariCircuit4.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__temps.append(i[0])
                    self.__coordenadaX.append(float(i[1]))
                    self.__coordenadaY.append(float(i[2]))
                    self.__angle.append(float(i[3]))
                    self.__teclat.append(float(i[4]))
                    self.__vel.append(float(i[5]))
        if n==3:
            with open('../UsuariCircuits/UsuariCircuit11.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__temps.append(i[0])
                    self.__coordenadaX.append(float(i[1]))
                    self.__coordenadaY.append(float(i[2]))
                    self.__angle.append(float(i[3]))
                    self.__teclat.append(float(i[4]))
                    self.__vel.append(float(i[5]))
        if n==4:
            with open('../UsuariCircuits/UsuariCircuit6.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__temps.append(i[0])
                    self.__coordenadaX.append(float(i[1]))
                    self.__coordenadaY.append(float(i[2]))
                    self.__angle.append(float(i[3]))
                    self.__teclat.append(float(i[4]))
                    self.__vel.append(float(i[5]))
        if n==5:
            with open('../UsuariCircuits/UsuariCircuit1.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__temps.append(i[0])
                    self.__coordenadaX.append(float(i[1]))
                    self.__coordenadaY.append(float(i[2]))
                    self.__angle.append(float(i[3]))
                    self.__teclat.append(float(i[4]))
                    self.__vel.append(float(i[5]))
        if n==6:
            with open('../UsuariCircuits/UsuariCircuit2.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__temps.append(i[0])
                    self.__coordenadaX.append(float(i[1]))
                    self.__coordenadaY.append(float(i[2]))
                    self.__angle.append(float(i[3]))
                    self.__teclat.append(float(i[4]))
                    self.__vel.append(float(i[5]))
        if n==7:
            with open('../UsuariCircuits/UsuariCircuit5.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__temps.append(i[0])
                    self.__coordenadaX.append(float(i[1]))
                    self.__coordenadaY.append(float(i[2]))
                    self.__angle.append(float(i[3]))
                    self.__teclat.append(float(i[4]))
                    self.__vel.append(float(i[5]))
        if n==8:
            with open('../UsuariCircuits/UsuariCircuit7.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__temps.append(i[0])
                    self.__coordenadaX.append(float(i[1]))
                    self.__coordenadaY.append(float(i[2]))
                    self.__angle.append(float(i[3]))
                    self.__teclat.append(float(i[4]))
                    self.__vel.append(float(i[5]))
        if n==9:
            with open('../UsuariCircuits/UsuariCircuit8Cheste.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__temps.append(i[0])
                    self.__coordenadaX.append(float(i[1]))
                    self.__coordenadaY.append(float(i[2]))
                    self.__angle.append(float(i[3]))
                    self.__teclat.append(float(i[4]))
                    self.__vel.append(float(i[5]))
        if n==10:
            with open('../UsuariCircuits/UsuariCircuit10.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__temps.append(i[0])
                    self.__coordenadaX.append(float(i[1]))
                    self.__coordenadaY.append(float(i[2]))
                    self.__angle.append(float(i[3]))
                    self.__teclat.append(float(i[4]))
                    self.__vel.append(float(i[5]))
        if n==11:
            with open('../UsuariCircuits/UsuariCircuit9Catalunya.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__temps.append(i[0])
                    self.__coordenadaX.append(float(i[1]))
                    self.__coordenadaY.append(float(i[2]))
                    self.__angle.append(float(i[3]))
                    self.__teclat.append(float(i[4]))
                    self.__vel.append(float(i[5]))
        if n==12:
            with open('../UsuariCircuits/UsuariCircuit12.csv') as cs:
                entrada = csv.reader(cs)
                for i in entrada:
                    self.__temps.append(i[0])
                    self.__coordenadaX.append(float(i[1]))
                    self.__coordenadaY.append(float(i[2]))
                    self.__angle.append(float(i[3]))
                    self.__teclat.append(float(i[4]))
                    self.__vel.append(float(i[5]))

    def entrada(self):
        return self.__temps,self.__coordenadaX,self.__coordenadaY,self.__angle,self.__teclat,self.__vel
