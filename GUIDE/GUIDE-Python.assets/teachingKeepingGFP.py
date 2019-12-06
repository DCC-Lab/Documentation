import matplotlib.pyplot as plt
import numpy as np
import PIL

image = PIL.Image.open("test2.png")

imageAsArray = np.array(image)
print("My image has a shape of:", imageAsArray.shape)

(height, width, colours) = imageAsArray.shape

gfpChannel = np.zeros(shape=(height, width))

for i in range(width):
    for j in range(height):
        gfpChannel[j][i] = imageAsArray[j][i][1]

print("My new array is: ", gfpChannel.shape)
print("Its first element is: ", gfpChannel[0][0])

gfpImage = PIL.Image.fromarray(gfpChannel.astype('uint8'))
gfpImage.save("GFPImage.jpg", "JPEG")

