import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.power(np.e, (-x/10)) * np.sin(np.pi * x)

def g(x):
    return x * np.power(np.e, (-x/3))

# t = np.arange(0.0, 10.0, 0.01)
t = np.linspace(0, 10, 100)

plt.plot(t, f(t), 'g',label = 'f(x)')
plt.plot(t, g(t), 'r',label = "g(x)")
plt.legend()

plt.ylabel("Trục y")
plt.xlabel("Trục x")

plt.savefig("plot.png")
# plt.savefig("plot.jpg")
# Can import Pillow
plt.show()
