import numpy as np
import matplotlib.pyplot as plt

class AffineTransform:
    
    def __init__(self, a, b, c, d, e, f):
        self.a = a; self.b = b; self.c = c;
        self.d = d; self.e = e; self.f = f;
        
    def __call__(self, z):
        x , y = z
        nyx = self.a*x + self.b*y + self.e
        nyy = self.c*x + self.d*y + self.f
        return nyx, nyy
    
def iterating(x):
    r = np.random.random()
    for j, q in enumerate(p):
        if r < q:
            return f[j]
    

if __name__ == "__main__":
    f_1 = AffineTransform(0, 0, 0, 0.16, 0, 0)
    f_2 = AffineTransform(0.85, 0.04, -0.04, 0.85, 0, 1.60)
    f_3 = AffineTransform(0.20, -0.26, 0.23, 0.22, 0, 1.60)
    f_4 = AffineTransform(-0.15, 0.28, 0.26, 0.24, 0, 0.44)
    f = [f_1, f_2, f_3, f_4]
    p_cumulative = [0.01, 0.85, 0.07, 0.07]
    x = ([0,0])
    n = 50000
    y = []
    p = np.cumsum(p_cumulative)
    

    for k in range(n):
        j = iterating(f)
        a = j(x)
        y.append(a)
        x = a
    
    plt.scatter(*zip(*y), s = 0.01, c = "purple")
    plt.axis("equal")
    plt.axis("off")
    marker = "."
    plt.show()
    plt.savefig("barnsley_fern.png")
