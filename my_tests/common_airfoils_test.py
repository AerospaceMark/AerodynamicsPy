import aerodynamicspy as aero
import matplotlib.pyplot as plt

airfoil = aero.naca(2,4,12,100)

airfoil.plot()

print("Done!")