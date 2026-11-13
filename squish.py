import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import linear
from fitting_functions import slope_units
from fitting_functions import print_equation

data = np.loadtxt("MarshmellowExperiment.csv", delimiter=",", dtype=str)

