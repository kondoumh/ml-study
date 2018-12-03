from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pylab as plt

def function_2(x, y):
    return x**2 + y**2


x = np.arange(-3.0, 3.0, 0.1)
y = np.arange(-3.0, 3.0, 0.1)

X, Y = np.meshgrid(x, y)
Z = function_2(X, Y)

fig = plt.figure()
ax = Axes3D(fig)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")

ax.plot_wireframe(X, Y, Z)
plt.show()
