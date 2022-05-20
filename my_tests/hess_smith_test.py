import aerodynamicspy as aero
import matplotlib.pyplot as plt
import numpy as np

x = aero.create_x_array(100)

airfoil = aero.naca(2,4,12,20)

airfoil.plot(details = True)

print("Hello")