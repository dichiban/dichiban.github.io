import matplotlib.pyplot as plt
import numpy as np
import math

plt.style.use('seaborn-v0_8')

# make data
x = np.linspace(0, 1, 100)

y_ideal   = x
y_display = np.power(y_ideal, 2.2)
y_image   = np.power(y_ideal, 1/2.2)

x_comparison = [0.5, 0.5, 0.5]
y_comparison = [x_comparison[0], 
                math.pow(x_comparison[0], 2.2), 
                math.pow(x_comparison[0], 1/2.2)]

# plot
fig, ax = plt.subplots()

# Make lines
ax.plot(x, y_ideal, '-', label="Original")
ax.plot(x, y_display, '-', label="Display Decoding (^2.2)")
ax.plot(x, y_image, '-', label="Image Encoding (^1/2.2)")

# Make points
ax.scatter(x_comparison, y_comparison)
for i, y_val in enumerate(y_comparison):
    ax.text(x_comparison[i]-0.02, y_val+0.03, round(y_val, 3))

ax.set(xlim=(0, 1), xticks=np.arange(0, 1, 0.1),
       ylim=(0, 1), yticks=np.arange(0, 1, 0.1))

ax.legend(loc="upper left")
ax.set_xlabel("Input Color")
ax.set_ylabel("Output Color")
plt.savefig("gamma_corrections_graph.png")