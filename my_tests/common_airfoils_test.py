import aerodynamicspy as aero
import matplotlib.pyplot as plt

x = aero.create_x_array(100)

airfoil = aero.naca(2,4,12,100)

airfoil.plot()

print("Done!")