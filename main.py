import numpy
import scipy.special
import matplotlib.pyplot


class NeuralNetwork:

    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes,
        self.onodes = outputnodes

        self.lr = learningrate

        self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))

        print("Weight-Input-Hidden (wih):")
        print(self.wih)
        print("Weight-Hidden-Output (who):")
        print(self.who)

    def train(self):
        print('training')

    def query(self):
        print("I ask...")


input_nodes = 3
hidden_nodes = 3
output_nodes = 3

learning_rate = 0.3

n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

n.train()

outputs = n.query()


print("performance = great")