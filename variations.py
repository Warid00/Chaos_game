import numpy as np
import matplotlib.pyplot as plt



class Variations: 
    
    def __init__(self, x, y, name):
        self.x = x; self.y = y; self.name = name
        self._func = getattr(Variations, name)
        
    @staticmethod
    def linear(x, y):
        return x, y
    
    @staticmethod
    def handkerchief(x, y):
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(x, y) 
        return r*np.sin(theta + r), np.cos(theta - r)
                  
    @staticmethod
    def swirl(x,y):
        r = np.sqrt(x**2 + y**2)
        return x*np.sin(r**2) - y*np.cos(r**2), x*np.cos(r**2) + y*np.sin(r**2) 
               
    @staticmethod
    def disc(x, y):
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(x, y)
        return theta/np.pi*(np.sin(np.pi*r), np.cos(np.pi*r))

    @staticmethod
    def bubble(x, y):
        r = np.sqrt(x**2 + y**2)
        return 4/(r**2 + 4)*(x, y)

    @staticmethod
    def exponential(x, y):
        return np.exp(x - 1)*(np.cos(np.pi*y), np.sin(np.pi*y))
    
    def transform(self):
        self.x, self.y = self._func(self.x, self.y)
        return self.x, self.y
    
def plot_test_implementation():
    N = 100
    grid_values = np.linspace(-1, 1, N)
    x, y = np.meshgrid(grid_values, grid_values)
    x_values = x.flatten()
    y_values = y.flatten()
    

    transformations = ["linear", "handkerchief", "swirl", "disc"]
    variations = [Variations(x_values, y_values, version) for version in transformations]

    fig, axs = plt.subplots(2, 2, figsize=(9, 9))
    for i, (ax, variation) in enumerate(zip(axs.flatten(), variations)):
   
    
        u, v = variation.transform()
    
        ax.plot(u, -v, markersize=1, marker=".", linestyle="", color="orange")
        # ax.scatter(u, -v, s=0.2, marker=".", color="black")
        ax.set_title(variation.name)
        ax.axis("off")

    #fig.savefig("figures/variations_4b.png")
    plt.show()
    


plot_test_implementation()
