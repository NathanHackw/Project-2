import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import linear
from fitting_functions import slope_units
from fitting_functions import print_equation

data = np.loadtxt("MarshmellowExperiment.csv", skiprows=1, delimiter=",", dtype=str)

for i in range(len(data)):
    data[i, 0] = data[i,0].rstrip('g')
    data[i, 1] = data[i,1].rstrip('cm')

x = data[0:, 0].astype(np.float32)
y = data[0:, 1].astype(np.float32)

print("y = ", y)
print("x = ", x)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]
#EXERCISE 1
x_units = "g"
y_units = "cm"
print_equation(slope, intercept, x_units, y_units)
#The equation of the line is: y =  -0.0035136610041552885 cm/g x +  5.009835989748822 cm
#Im not sure if this is right
#EXERCISE 2
fig = plt.figure()
plt.scatter(x, y, label='Marshmellow Experiment')
plt.plot(x, linear(x, slope, intercept),label='Linear Fit')
plt.legend(loc='best')
plt.xlabel("Weight (g)")
plt.ylabel("Height (cm)")
plt.show()
fig.savefig('Marshmellow_DataPlot.png')
