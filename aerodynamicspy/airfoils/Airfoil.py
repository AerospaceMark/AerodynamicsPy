import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Airfoil:

    def __init__(self, Name, x, z):

        # Give the airfoil a name
        self.Name = Name

        # Get the airfoil coordinates
        self.Coords = np.transpose([x, z])

        # Calculate the center points
        self.Centers = np.transpose([(x[0:-1] + x[1:]) / 2, (z[0:-1] + z[1:]) / 2])

        print(self.Coords)


    def plot(self, details = False):

        fig, ax = plt.subplots()
        ax.plot(self.Coords[:,0],self.Coords[:,1],
                marker = "o",
                label = "Airfoil")

        if details:
            ax.plot(self.Centers[:,0],self.Centers[:,1],
                    label = "Center Points",
                    color = "red",
                    marker = "o",
                    linestyle = "")

        ax.set_aspect('equal')
        ax.set_title(self.Name)
        ax.set_xlabel("X (m)")
        ax.set_ylabel("Z (m)")
        ax.set_ylim(- max(self.Coords[:,0])/2, max(self.Coords[:,0])/2)
        ax.grid()
        ax.legend()
        plt.show()

