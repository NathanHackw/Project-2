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
