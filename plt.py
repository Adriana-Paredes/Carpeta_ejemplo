import matplotlib.pyplot as plt
import numpy as np

x = np.linspace (-5,5,100)
y= x**3
plt.plot(x,y, "g.-", label="$x^3$", linewidth=5)
plt.title("Grafca")
plt.legend()
plt.grid()
plt.show()

