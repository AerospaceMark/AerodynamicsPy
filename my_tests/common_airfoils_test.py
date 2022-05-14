import aerodynamicspy as aero
import matplotlib.pyplot as plt

x = aero.create_x_array(100)

coords = aero.naca(2,4,12,100)

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(coords.x,coords.z, marker = "o")
ax.set_aspect('equal')
plt.show()