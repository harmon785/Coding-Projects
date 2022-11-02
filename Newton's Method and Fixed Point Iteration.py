# State three stopping criteria for the root finding algorithms along with their pros and cons.
# Implement these stopping criteria in your code while computing the 4th root of 47 using Newton's method.

# Choose two stopping criterion for Newton's Method
max_iterations = 21
error_tolerance = 10**(-4)

# define a function to represent the iterative formula of Newton's Method
def iterative_formula(xn):
    fx = (xn ** 4) - 47
    fprimex = 4 * (xn ** 3)
    return xn - (fx/fprimex)

# define function to implement Newton's method up to the given number of iterations
def newtons_method(x0):
    iteration_list = [] # use list to store results of each iteration 
    iteration_number = 1 # starting iteration
    while iteration_number < max_iterations: # while loop to calculate the result of each iteration updated each time
        current_iteration = iterative_formula(x0)
        x0 = current_iteration
        iteration_list.append(current_iteration)
        iteration_number += 1
    print(iteration_list, "\n")

newtons_method(2.6) # Choose an initial guess to be used, in this case, 2.6

print ("The pros of these three stopping criterion are that it prevents the method from iterating forever, being able to")
print("accomodate a smaller margin of error, and the cons of these stopping criterion are that there can be many")
print("duplicate values after each iteration as a result of said higher accomodation for error.")


# How many roots does the function f(x) = sin10x - x have? Using the intermediate value theorem, provide some of the starting
# guesses for each of these roots that can be fed into an iterative root solver to compute these roots. No need to do any
# iterations.
import math
import matplotlib.pyplot as plt

x_axis = [-1.0, -0.5, 0.0, 0.5, 1.0] # Choose some x values that are close to where all the roots are
y_axis = [] # Use empty list to store f(x) for each x value 

# define a function to represent the given function
def function(x):
    fx = math.sin(10 * x) - x
    return fx

# define a function to plot the given function
def plot_function(x):
    
    for i in range(len(x_axis)):
        y_axis.append(function(x_axis[i]))
    plt.plot(x_axis, y_axis, label = "sin(10x) - x" )
    print(y_axis, "\n")

plot_function(x_axis)
plt.legend()

print("Using intermediate value theorem, let [a,b] = [-1, 1] as all the roots of this function are contained within this")
print("interval. Therefore, as for starting guesses, either -1 or 1 can be used in an iterative method to determine the")
print("the amount of roots that are contained within this interval, which in this case would be 7 as that is how many")
print("times the function intersects the x-axis.")


# For the equation f(x) = x - e^-x = 0, find two formulations for the fixed point iteration, say
# g1(x) and g2(x). On the interval [0,1], plot f(x), g1(x), g2(x) and y = x.
# What is the connection between them?

import numpy as np
import matplotlib.pyplot as plt

# Create three separate sets of x values that will be appended to each of their respective y value lists
first_x_axis = [0.0, 0.25, 0.5, 0.75, 1.0]
first_y_axis = []

second_x_axis = [0.0, 0.25, 0.5, 0.75, 1.0]
second_y_axis = []

third_x_axis = [0.01, 0.25, 0.5, 0.75, 1.0]
third_y_axis = []

fourth_x_axis = [0.0, 0.25, 0.5, 0.75, 1.0]
fourth_y_axis = []

# Define four different functions to represent each of the given functions
def f(x):
    return x - math.exp(-x)

def g1(x):
    return math.exp(-x)

def g2(x):
    return np.log(x) * -1

def y(x):
    return x

# Define four different functions that will be used to plot each function
def plot_f(x):
    for i in range(len(first_x_axis)):
        first_y_axis.append(g1(first_x_axis[i]))
    plt.plot(first_x_axis, first_y_axis, label = "f(x) = x - e^-x" )
    print("f(x) = x - e^-x:",first_y_axis, "\n")

def plot_g1(x):
    for i in range(len(second_x_axis)):
        second_y_axis.append(g1(second_x_axis[i]))
    plt.plot(second_x_axis, second_y_axis, label = "g1(x) = e^-x" )
    print("g1(x) = e^-x:",second_y_axis, "\n")

def plot_g2(x):
    for i in range(len(third_x_axis)):
        third_y_axis.append(g2(third_x_axis[i]))
    plt.plot(third_x_axis, third_y_axis, label = "g2(x) = -ln(x)" )
    print("g2(x) = -ln(x):", third_y_axis, "\n")

def plot_y(x):
    for i in range(len(fourth_x_axis)):
        fourth_y_axis.append(f(fourth_x_axis[i]))
    plt.plot(fourth_x_axis, fourth_y_axis, label = "y = x")
    print("y = x:", fourth_y_axis, "\n")

plot_f(first_x_axis)
plot_g1(second_x_axis)
plot_g2(third_x_axis)
plot_y(fourth_x_axis)

plt.legend()

print("The connection between all four of these functions is that they are all approximations of one another as x")
print("converges to 1.")

