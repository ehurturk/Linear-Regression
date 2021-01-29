import numpy as np
import matplotlib.pyplot as plt


class LinearReg:
    def __init__(self, X, Y, seed=1):
        self.X = X
        self.Y = Y
        self.seed = seed

    def fit(self, a, iters):
        col = np.ones(self.X.shape[0])
        self.X = np.c_[col, self.X]
        rgen = np.random.RandomState(self.seed)
        self.W = rgen.normal(loc=0.0, scale=0.01, size=self.X.shape[1])
        # needs a convergencew point:
        for _ in range(iters):
            for xi, yi in zip(self.X, self.Y):
                temp = (a / self.X.shape[0]) * ((self.get(xi) - yi) * xi)
            self.W -= temp
        return self.W

    def get(self, xi):
        return np.dot(xi, self.W)


class Graph:

    def visualize(self, *datas):
        for coordinate_pair in datas:
            self.x = coordinate_pair[0]
            self.y = coordinate_pair[1]
            if coordinate_pair[2]:
                plt.plot(self.x, self.y, 'o')
            else:
                plt.plot(self.x, self.y)
        plt.xlabel('X Inputs')
        plt.ylabel('Stock Closing Value')
        plt.show()


def predict(xdata, params):
    y = []
    for i in range(0, len(xdata)):
        y.append(np.dot(xdata[i], params[1:])+params[0])
    return y


# X = np.array([[10, 20, 30], [40, 50, 60],[70,80,90]])
# Y = np.array([[25], [52], [77]])
X = np.array([[0], [1], [2], [4], [5]])
Y = np.array([[2], [3], [6], [9], [14]])

lr = LinearReg(np.asarray(X, order='F'), np.asarray(Y, order='F'))

params = lr.fit(0.01, 100)
print(f'Weights: {params}')


ydata = predict(X, params)
graph = Graph()
graph.visualize((X, Y, True), (X, ydata, False))
