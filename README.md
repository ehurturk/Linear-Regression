# Linear-Regression

## Introduction

This is a simple **univariate** / **multivariate** linear regression project for my Mathematics project. 

This project is written in Python 3.7 and with packages NumPy, Matplotlib, Pandas, and Sklearn

I used NumPy to:
- Perform the calculations in a vectorized way to be more efficient
- It is also an extended version of the current Math library of Python

I used Matplotlib to:
- Plot the graphs in both 2D and 3D

I used Sklearn to:
- Split the data into 2 parts: Training and Testing sets
- To access the datasets of the library

I used Pandas to:
- Getting the data from a .csv file
- Easy to use with NumPy

Math included in this project:
- Statistics (MSE, Gradient Descent, Regression)
- A bit of Calculus (Gradient Descent)
- Linear Algebra (Making the algorithm in a vectorized way - Using Matrices and Vectors in calculations)

## Installations

To use this code, firsr of all you need to install python3. You can download python3 from [their official website] (https://www.python.org/downloads/)

To install the libraries the code depends on, you need to type:
- `pip3 install matplotlib` - To install Matplotlib (for pip users)
- `pip3 install numpy` - To install NumPy (for pip users)
- `pip3 install sklearn` - To install Sklearn (also for pip users)

- `conda install matplotlib` - To install Matplotlib (for conda users)
- `conda install numpy` - To install NumPy (for conda users)
- `conda install sklearn` - To install Sklearn (also for conda users)

## Usage

This code comes with an example .csv file to test the code yourself. If you want to use another data, you can simply type the location of the file into the `pd.read_csv(YOUR_URL)` part. 

Classes:
- Grapher (in grapher.py)
- LinearRegression (in regression.py)

### Grapher
This class is used to plot the data in both 2D and 3D with Matplotlib. 
There are 4 methods in this class:
- graph2Deq(): Graphs a 2D equation into a cartesian plane
- graph2Dscat(): Scatters the data points into a cartesian plane
- graph3Deq(): Graphs a 3D equation into a 3D space
- graph3Dscat(): Scatters 3D points into a 3D space

### LinearRegression
This class is used for fitting the data into an equation and predicting further data.
There are 3 methods in this class:
- fit(): Used to fit an equation according to given X, Y data
- graph(): Used to return a 3D array containing the predicted points based on the weights that was fitted. Use for plotting a 3D equation.
- predict(): Used to return a **FLOAT**, based on a input value, x. Inout value x can be a range, or numpy linspace. Use for plotting a 2D equation.

Also, you can have an idea of the code from the comments I wrote. 
If you find any bug or want to add any feature to this project, please email me: emirhurturk444@gmail.com

Thanks for being interested in,
