import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 8, 8)
y = [8,1,6,4,7,6,5,4]
plt.title("geek-docs.com", fontsize=30, fontname="Times New Roman")
plt.plot(x, y,'r')
plt.savefig('pruebaLinea.png')