
import numpy as np
import matplotlib.pyplot as plt
import random


def calculate(e, t, iterations):

    s = 0

    if(e == True):
        for e in range(iterations):
            if(random.random() < t):
                s += 1
        return s




    for d in range(iterations):

        if((random.random() < e)  and (random.random() < t)):
            s += 1

    return s

iterations = 1000

a1, a2 = 0.17, 0.05
b1, b2 = 0.03, 0.25
c1, c2 = True, 0.06


a, b, c = {}, {}, {}

box_1 = 0
box_2 = 0
box_3 = 0


for i in range(500):

    
    print(i)

    box_1 = calculate(a1, a2, iterations)
    box_2 = calculate(b1, b2, iterations)
    box_3 = calculate(c1, c2, iterations)

    if (box_1 == 0):
        box_1 = 1

    if (box_2 == 0):
        box_2 = 1

    if (box_3 == 0):
        box_3 = 1

    #a.append(iterations*0.99/box_1)
    a[i] = (iterations*0.99/box_1)
    b[i] = (iterations*1.2/box_2)
    c[i] = (iterations*0.7/box_3)


    iterations += 500




x = list(a.keys())
y = list(a.values())
mean = np.mean(y)
plt.axhline(y=mean, color='red', linestyle='--', linewidth=3, label='Avg')
plt.plot(x, y)
plt.legend(['Mean: ${}'.format(round(mean, 2))])
plt.show()

x = list(b.keys())
y = list(b.values())
mean = np.mean(y)
plt.axhline(y=mean, color='red', linestyle='--', linewidth=3, label='Avg')
plt.plot(x, y)
plt.legend(['Mean: ${}'.format(round(mean, 2))])
plt.show()

x = list(c.keys())
y = list(c.values())
mean = np.mean(y)
plt.axhline(y=mean, color='red', linestyle='--', linewidth=3, label='Avg')
plt.plot(x, y)
plt.legend(['Mean: ${}'.format(round(mean, 2))])
plt.show()

