import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from regression import LinearRegression
from mpl_toolkits import mplot3d

ax = plt.axes(projection='3d')
X, y = datasets.make_regression(n_samples=100, n_features=2, noise=20, random_state=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)


regression = LinearRegression(X_train, y_train)
regression.fit(0.01, 1000)
predicted_labels = regression.predict(X)

# plt.scatter(X_test, y_test, color='red', s=10)
# plt.scatter(X_train, y_train, color='green', s=10)
# plt.plot(X, predicted_labels, color='black')
# plt.show()

ax.scatter(X[:, 0], X[:, 1], y, marker='o', color='red')


x1 = np.linspace(-6, 6, 30)
x2 = np.linspace(-6, 6, 30)

X1, X2 = np.meshgrid(x1, x2)
Y = regression.graph([X1, X2])

ax.plot_wireframe(X1, X2, Y)
ax.set_xlabel('1st Feature')
ax.set_ylabel('2nd Feature')
ax.set_zlabel('Label')
plt.show()

plt.plot(range(1, len(regression.costs) + 1), regression.costs)
plt.xlabel('Number of Iterations')
plt.ylabel('MSE Error Value')
plt.title('Graph of Convergence of the Cost Function')
plt.show()
