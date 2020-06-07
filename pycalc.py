# a python calculator for shell
# how it works?
# simply getting a command from user and executing so!

# to get input from shell
import sys

# get input from shell as a string. if multiple inputs are provided, join them.
question = ''.join(sys.argv[1:])

# remove all whitespaces from input.
# this is done to check if this is in form of 'y=f(x)' or not
freeQ = question.replace(' ', '').replace(' ', '')

# check if there is nothing!
if len(freeQ) < 1:
    # TODO: replace with an inline calculating funcion
    sys.exit(1)

# so if user is trying to plot a function:
if freeQ[:2] == 'y=':
    # import numpy for vector calculations
    from numpy import *
    # import pyplot for plotting
    from matplotlib import pyplot as plt
    # generate x dimention of the function.
    # TODO: make it more smart or let user provide it
    x = arange(-10, 10, 0.1)
    # execute provided command. so as an output y should be f(x)
    exec(freeQ)
    # create a plot for generated function array
    plt.plot(y)
    # show generated plot
    plt.show()

# but if user is trying to get answer of a single line mathematical expression
else:
    # import math functions
    # math lib is used because it is small and loads faster
    from math import *
    # add a variable name to beginning of the command so equation can be printed
    command = 'answer=' + question
    # execute command. now output of the math equation should be stored in `answer` variable
    exec(command)
    # print the answer
    print(answer)

