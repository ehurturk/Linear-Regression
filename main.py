import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from regression import LinearRegression
from grapher import Grapher


# Get the Data

# 2+ Dimensional Data:
# X, y = sklearn.datasets.make_regression(n_samples=100, n_features=2, noise=20, random_state=1)

# 1 Dimensional Data
dataset = pd.read_csv('Salary_Data.csv')

X = np.array(dataset['YearsExperience'])  # if it is 1D, make a mx1 matrix, else mxn matrix (MUST BE RESHAPED TO 1 IF IT IS A VECTOR)

# If X is 1 Dimensional, then reshape it to (-1,1) fit the needs of calculations in dot product
try:
    print(X.shape[1])
except IndexError:
    X = X.reshape(-1, 1)

y = np.array(dataset['Salary'])
# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# Inits
grapher = Grapher()
regression = LinearRegression(X_train, y_train)


# Fit the parameters
regression.fit(0.01, 1000)


# Graph 3D Points of the Data
#grapher.graph3Dscat(X[:, 0], X[:, 1], y) # grapher.graph3dscat(first_feature_vector, second_feature_vector, label_vector)


# Graph 3D Regression Equation
# x1 = np.linspace(-6, 6, 30)
# x2 = np.linspace(-6, 6, 30)
# X1, X2 = np.meshgrid(x1, x2)
# Y = regression.graph([X1, X2])
# grapher.graph3Deq(X1, X2, Y)

grapher.graph2Dscat(X_test, y_test, X_train, y_train)

x = np.linspace(np.min(X), np.max(X), 30).reshape(-1,1)
predicted_labels = regression.predict(x)
grapher.graph2Deq(x, predicted_labels, 'Years of Experience vs. Salary', 'Years of Experience', 'Salary')

# Graph Cost Function
grapher.graph2Deq(range(1, len(regression.costs) + 1), regression.costs, 'Graph of Convergence of the Cost Function', 'Number of Iterations', 'MSE Error Value')








