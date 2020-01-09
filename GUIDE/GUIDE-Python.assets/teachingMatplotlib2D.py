import matplotlib.pyplot as plt
import numpy as np
import PIL

image = PIL.Image.open("MyFigure.tiff")
image.show()

imageAsArray = np.array(image)
plt.imshow(imageAsArray)
plt.show()