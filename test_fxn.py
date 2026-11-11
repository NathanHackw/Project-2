from fitting_functions import linear
from fitting_functions import slope_units
from fitting_functions import print_equation

m = input(print("Please enter Slope: "))
x = input(print("Please input X value: "))
b = input(print("Please input Y intercept: "))
x_units = input(print("Please input X unit: "))
y_units = input(print("Please input Y unit: "))

print("Linear: ", linear(m, x, b))
print("SLope Units: ", slope_units(x_units, y_units))
print_equation(m, b, x_units, y_units)
