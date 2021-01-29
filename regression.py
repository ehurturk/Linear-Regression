import random

class LinearRegression(Regression):
    def __init__(self, inputs):
        self,inputs = inputs
        super().__init__(inputs)
    def cost(self, true_labels):
        '''
            Formula: cost(weights) = 1/n * SUM((true label - predict(xi))**2)
        '''
        cost = 0
        for i in range(0, len(self.inputs)):
            cost += (true_labels[i] - self.predict(self.inputs[i])) ** 2
        return cost/len(self.inputs)

    def gradient_descent(self, epochs):
        return NotImplementedError

class Regression:
    def __init__(self, inputs):
        self.weights = [random.uniform(0, 5) for _ in inputs]
    def predict(self, input_):
        '''
            Returns the dot product of inputs and paramerers
            p(xj) = w0x0 + w1x1 + w2x2 + ... + wNxN in which xj = a training ex.
                                                             xji = i'th feature of the j'th training example
        '''
        prediction = 0
        for i in range(0, len(self.weights)):
            prediction += self.weights[i] * input_
        return prediction
