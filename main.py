import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from regression import LinearRegression
from data import Data

data_handler = Data()

x_data, X, Y, W = data_handler.get_data(load_boston)
lr_handler = LinearRegression(X, Y, W)


JH, params = lr_handler.fit(0.01, 1500)
print(f'Params: {params}')
# plt.plot(range(len(JH)), JH, 'r')

# plt.title("Convergence Graph of Cost Function")
# plt.xlabel("Number of Iterations")
# plt.ylabel("Cost")
# plt.show()


ydata = data_handler.predict(X, W)
plt.plot(x_data, Y, 'o')
plt.title("House Ages vs. Housing Prices (My Model)")
plt.xlabel("House Age")
plt.ylabel("House Price")
plt.plot(x_data, ydata)
plt.show()

