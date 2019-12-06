# name this: teachingMatplotlib.py
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 100)   # An array of 100 numbers between 0 and 2
yLinear = x       # y = x
yQuadratic = x**2 # y = x*x
yCubic = x**3     # y = x*x*x

fig = plt.figure()  # an empty figure with no axes
plt.plot(x, yLinear, label='linear') # Create first curve, with a label
plt.plot(x, yQuadratic, label='quadratic')
plt.plot(x, yCubic, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend() # Show legend
plt.savefig("MyFigure.tiff",dpi=600) # Save the figure as high res tiff
plt.savefig("MyFigure.pdf") # Save as a PDF, which is always high res
plt.show()