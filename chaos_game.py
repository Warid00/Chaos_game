import numpy as np
import matplotlib.pyplot as plt

class ChaosGame:
    
    def __init__(self, n, r = 0.5):
        #2 arguments and raises error if something is off
        if type(n) != int and type(r) != float:
            raise ValueError("n have to be int and r must be a float")
        if n >= 3:
            self.n = n
        else:
            raise ValueError("n can't be lower than 3")
        if 0 < r < 1:
            self.r = r
        else:
            raise ValueError("r needs to be between 0 and 1")
            
        #going back and updated constructor 
        self.corners = self._generate_ngon()
            
    def _generate_ngon(self):
        #making corners of figure
        i = np.linspace(0, 2*np.pi, self.n)
        corners = [(np.sin(theta), np.cos(theta)) for theta in i]
        return corners
    
    def plot_ngon(self):
        #plots
        plt.scatter(*zip(*self.corners))
        plt.axis("equal")
        plt.axis("off")
        plt.show()
        
    def _starting_point(self):
        ylist = []
        xlist = []
        r = np.random.random(self.n)
        for k in range(self.n):
            ylist = ylist + [r[k]/sum(r)]
            xlist = xlist + [ylist[k]*np.array(self.corners[k])]
        return sum(xlist)
    
    def iterate(self, steps, discard = 5):
        xlist = []
        xlist = xlist + [self._starting_point()]
        for i in range(steps):
            r = np.random.randint(self.n)
            cj = np.array(self.corners)[r]
            xlist = xlist + [self.r*xlist[i] + (1 - self.r) * cj]
        self.xlist= xlist
        
    def plot(self, color = False, cmap = "jet"):
        if color != False:
            color = self.gradient_color
            plt.axis("equal")
            plt.axis("off")
        else:
            cmap = "black"
        plt.scatter(*zip(*self.xlist), marker = ".", s = 0.01, c  = cmap)
        plt.axis("equal")
        plt.axis("off")
        
    def show(self):
        self.plot(color = False, cmap = "jet")
        plt.show()
        
    @property
    def gradient_color(self):
        C = [self.xlist[0]]
        for i in range(0, len(self.xlist)):
            C.append((C[-1] + self.xlist[i])/2)
        return C
    
    def savepng(outfile, color = False, cmap = "jet"):
        if ".png" in outfile:
            a = outfile
        elif "." not in outfile:
            a = outfile + ".png"
        else:
            raise ValueError("forgot .png or nothing")
        plt.show()
        plt.savefig(a, dpi = 300, transparent = True)
        
if __name__ == "__main__":
    n_3 = ChaosGame(3)
    n_4 = ChaosGame(4)
    n_5 = ChaosGame(5)
    n_6 = ChaosGame(6)
    n_7 = ChaosGame(7)
    n_8 = ChaosGame(8)
    
    n_3.plot_ngon()
    n_4.plot_ngon()
    n_5.plot_ngon()
    n_6.plot_ngon()
    n_7.plot_ngon()
    n_8.plot_ngon()
    
    #plotting 1000 random points within pentagon
    p_5 = []
    for k in range(5000):
        p_5.append(n_5._starting_point())
    plt.scatter(*zip(*p_5))
    plt.axis("equal")
    plt.axis("off")
    plt.show()
        
    #2e
    e = ChaosGame(3, float(1/2))
    e.iterate(5000)
    e.show()
    
    #2i
    i1 = ChaosGame(3, 1/2)
    i1.iterate(5000)
    i1.savepng("chaos{1}")
    
    i2 = ChaosGame(4, 1/3)
    i2.iterate(5000)
    i2.savepng("chaos{2}")
    
    i3 = ChaosGame(5, 1/3)
    i3.iterate(5000)
    i3.savepng("chaos{3}")
    
    i4 = ChaosGame(5, 3/8)
    i4.iterate(5000)
    i4.savepng("chaos{4}")
    
    i5 = ChaosGame(6, 1/3)
    i5.iterate(5000)
    i5.savepng("chaos{5}")
    
