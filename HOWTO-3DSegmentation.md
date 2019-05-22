# 3D Object Segmentation and Analysis with Fiji

We will here look into manually extracting basic spatial informations about structures of interest inside a 3D image. 

## Prerequisites

1. [Fiji](https://imagej.net/Fiji/Downloads)
2. A 3D image (usually a stack of .tif images)

 

## Test data and context

The data we will be looking at for the tutorial is a 3D image of a mouse brain from *Dr. Edward Ruthazer*. Here is a preview of the volume:

![3D Test Image Preview](https://github.com/DCC-Lab/Documentation/blob/master/Sources/HOWTO-3DSegmentation/data3DPreview.png)

> " The blue channel is dapi to label nuclei, the green channel is a 3A10 antibody that labels retinal axons, the **red channel** is MBP immunostaining. **It is the MPB we would like to fully parameterize** for analysis across treatments. It represents the onset of early optic tract myelination. " - *Dr. Edward Ruthazer*.

 

## The Method

1. **Load stack**

   Drag and drop your stack folder or stack file inside Fiji and load it as a stack. 

2. **Set pixel dimensions**

   With *Image -> Properties* (skipped for demo since we don't have the info)

3. **Isolate channel of interest** (if applicable) 

   With *Image -> Color -> Split channels*. Then discard blue and green channels in our case.

5. **Filter out noise**

   With *Process -> Noise -> Remove outliers* (r≈4, thr.≈1)

![](https://github.com/DCC-Lab/Documentation/blob/master/Sources/HOWTO-3DSegmentation/prep.PNG)

6. **Crop** (if desired)

   It helps to reduce the amount of data for the next step.

   Drag a rectangle then use *Image -> Crop*.

7. **Segment**

   i. With *Analyze -> 3D Object Counter* (thr.≈20, min≈1000, max≈55 000 000)

   ii. Keep the object map and use *Image -> Adjust -> Brightness -> Apply*. 3D Objects are now visible and colored.

![](https://github.com/DCC-Lab/Documentation/blob/master/Sources/HOWTO-3DSegmentation/segment.PNG)

8. **Save** statistics and object map if desired

![](https://github.com/DCC-Lab/Documentation/blob/master/Sources/HOWTO-3DSegmentation/results.PNG)

9. **3D View**

   At any point you can ask for a 3D view of your stack (original or segmented) with *Plugins -> 3D Viewer*.

