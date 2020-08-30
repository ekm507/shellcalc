# a python calculator for shell
# how it works?
# simply getting a command from user and executing so!

# to get input from shell
import sys


# get input from shell as a string.
question = sys.argv[1]


# other arguments
# get settings from shell
# where plot x starts
x_start = -10.0
# where plot x ends
x_end = 10.0
# sampling period
x_step = 0.1
# if plot is to be drawn in a funny way
xkcd = False
# start getting options from shell
other_args = sys.argv[2:]

ROUND = False
FFT = False
INTEGRAL = False
DERIV = False
SHOW_ZERO = False

for i, arg in enumerate(other_args):
    if arg == 'from':
        x_start = float(other_args[i+1])
    elif arg == 'to':
        x_end = float(other_args[i+1])
    elif arg == 'step':
        x_step = float(other_args[i+1])
    elif arg == 'xkcd':
        xkcd = True
    elif arg == 'round':
        ROUND = True
    elif arg == 'fft':
        FFT = True
    elif arg in ['integral', 'int']:
        INTEGRAL = True
    elif arg in ['deriv', 'derivative', 'd']:
        DERIV = True
    elif arg in ['zero',]:
        SHOW_ZERO = True

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
    x = arange(x_start, x_end, x_step)
    # execute provided command. so as an output y should be f(x)
    exec(freeQ)
    # turn xkcd on if demanded
    if xkcd == True:
        plt.xkcd()
    
    if INTEGRAL == True:
        q = []
        k = 0
        for i in y:
            k += i
            q.append(k)
        y = q

    if DERIV == True:
        q = []
        k = y[0]
        for i in y[1:]:
            q.append((k - i) / x_step)
            k = i
        
        q.append(q[-1])
        y = q

    if FFT:
        y = fft.fftshift(abs(fft.fft(y)))
        x = x / x_step / (x_end - x_start) * 2
        print( x_step * (x_end - x_start) / 2)
    # create a plot for generated function array
    plt.plot(x, y)

    if SHOW_ZERO == True:
        zero_dim = zeros(int((x_end - x_start) / x_step))
        plt.plot(x, zero_dim)

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
    if ROUND:
        answer = round(answer)
    print(answer)

