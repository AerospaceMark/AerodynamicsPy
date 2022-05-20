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

        # Calculate the length of each panel
        self.Lengths = np.sqrt((x[0:-1] - x[1:])**2 + (z[0:-1] - z[1:])**2)

        # Calculate the sines and cosines for the panels
        angles = pd.DataFrame
        angles.cos_theta_i = (x[1:] - x[0:-1]) / self.Lengths
        angles.sin_theta_i = (z[1:] - z[0:-1]) / self.Lengths
        self.Angles = angles

        # Calculate the unit normals and tangents
        self.Unit_Normals = np.transpose([-self.Angles.sin_theta_i, self.Angles.cos_theta_i])
        self.Unit_Tangents = np.transpose([self.Angles.cos_theta_i, self.Angles.sin_theta_i])

    def plot(self, details = False):

        fig, ax = plt.subplots()
        ax.plot(self.Coords[:,0],self.Coords[:,1],
                marker = "o",
                label = "Airfoil")

        if details:

            # Plot the center points
            ax.plot(self.Centers[:,0],self.Centers[:,1],
                    label = "Center Points",
                    color = "red",
                    marker = "o",
                    linestyle = "")

            # Plot the unit normals and tangents
            size_factor = 0.05
            centers_x = np.transpose([self.Centers[:,0], self.Centers[:,0]])
            centers_z = np.transpose([self.Centers[:,1], self.Centers[:,1]])
            normals_x = np.transpose([np.zeros(len(self.Unit_Normals)), self.Unit_Normals[:,0]]) * size_factor + centers_x
            normals_z = np.transpose([np.zeros(len(self.Unit_Normals)), self.Unit_Normals[:,1]]) * size_factor + centers_z

            tangents_x = np.transpose([np.zeros(len(self.Unit_Tangents)), self.Unit_Tangents[:,0]]) * size_factor + centers_x
            tangents_z = np.transpose([np.zeros(len(self.Unit_Tangents)), self.Unit_Tangents[:,1]]) * size_factor + centers_z

            for i in range(len(normals_x)):
                ax.plot(normals_x[i,:],normals_z[i,:], color = "green")
                ax.plot(tangents_x[i,:],tangents_z[i,:], color = "purple")
            

        ax.set_aspect('equal')
        ax.set_title(self.Name)
        ax.set_xlabel("X (m)")
        ax.set_ylabel("Z (m)")
        ax.set_ylim(- max(self.Coords[:,0])/2, max(self.Coords[:,0])/2)
        ax.grid()
        ax.legend()
        plt.show()

