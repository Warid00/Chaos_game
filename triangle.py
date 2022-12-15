import matplotlib.pyplot as plt
import numpy as np


#exercise 1a)
#cos 30 = sgrt(3)/2
corner = np.array([(0, 0), (1, 0), (0.5, np.sqrt(3)/2)])
plt.scatter(*zip(*corner))
plt.show()

#exercise 1b)
def triangle(i):
    #making points inside triangle
    w = []
    s = []
    for n in range(i):
        r = np.random.random(3)
        w += [r/np.sum(r)]
        s += [corner[0]*w[n][0]
              + corner[1]*w[n][1]
              + corner[2]*w[n][2]]
    return s

plt.scatter(*zip(*triangle(1000)))
plt.show()

#exercise 1 c, d and e)
def point(i):
    color = []
    xlist = []
    xlist = xlist + triangle(1)
    for n in range(0, i + 3): #removes 5 first
        cj = np.random.randint(3) #random corner
        color = color + [cj]
        xlist = xlist + [(xlist[n] + corner[cj])/2] #formula
    return xlist[4:], color[3:] 

#adding colors from start corners
xlist, color = point(10000)
red = []
blue = []
green = []
for n in range(len(color)):
    if color[n] == 0:
        red.append(xlist[n])
    elif color[n] == 1:
        blue.append(xlist[n])
    elif color[n] == 2:
        green.append(xlist[n])
        
plt.scatter(*zip(*red), s = 0.1, color = "red")
plt.scatter(*zip(*blue), s = 0.1, color = "blue")
plt.scatter(*zip(*green), s = 0.1, color = "green")
plt.axis("equal")
plt.axis("off")
marker = "."
plt.show()


    
