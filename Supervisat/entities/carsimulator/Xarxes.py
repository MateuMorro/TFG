from entities.carsimulator.TrainingData import TrainingData
from entities.neuralnetwork.NetworkAmbSensors import NetworkAmbSensors
class Xarxes(object):

    def __init__(self,epochs,eta):
        self.__training_data = TrainingData().training()
        self.__mini_batch_size = len(self.__training_data)
        self.__xarxa = NetworkAmbSensors([11, 25, 2])
        self.__eta=eta
        self.__epochs=epochs
        self.__mini_batch_size=len(self.__training_data)

        self.__sizes = self.__xarxa.sizes
        self.__biases = self.__xarxa.biases
        self.__weights = self.__xarxa.weights

    def entrenament(self):
        self.__xarxa.SGD(self.__training_data, self.__epochs, self.__mini_batch_size, self.__eta)


    def sizes(self):
        return self.__sizes
    def biases(self):
        return self.__biases
    def weights(self):
        return self.__weights


xarxa=Xarxes(10,0.2)
xarxa.entrenament()