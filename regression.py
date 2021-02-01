import numpy as np


class LinearRegression:
    def __init__(self, x, y, w):
        self.X = x
        self.Y = y
        self.W = w

    def fit(self, a, n):
        '''
        Parameters:
        --------------
        X: {array} A 2D m x n matrix. The first column of this must be 1 for all rows, as the feature x0 w
    would equal 1, for the bias convention. This matrix is a example x feature matrix, which rows represent each training example and columns represent each feature.
        Y: {array} A m x 1 vector. This vector represents the true labels for each training example.
        W: {array} Th e weight matrix which must be 1 x X.shape[1].
        a: {float} The learning rate which is responsible for controlling the gradient descent algorithm.
        n: {int} The number of iterations

        Returns:
        --------------
        W: {array} An array containing weights of the each input feature.

        Formula:
        --------------
        Iterative Way:
            for n iterations:
                wJ = wJ - a * 1/len(X.shape[0]) * sum((predicted value - true value * xij))

        Matrixed Way:
            for n iterations:
                W = W - (a * 1/len(X.shape[0]) * )
        '''
        n_samples = len(self.Y)
        costs = np.zeros((n, 1))

        for i in range(n):
            self.W = self.W - (a / n_samples) * self.X.transpose() @ (self.X @ self.W - self.Y)
            costs[i] = self.mse()

        return costs, self.W

    def mse(self):
        n_samples = self.X.shape[0]
        h = self.X @ self.W
        return (1 / (2 * n_samples)) * np.sum((h - self.Y) ** 2)


