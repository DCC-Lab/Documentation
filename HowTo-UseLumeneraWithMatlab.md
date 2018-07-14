# How to use Lumenera camera with Matlab

1. Extract files from the zip file 'MATLAB Image Acquisition v 2.0.1' into a directory of your choice, such as 'C:\Lumenera MatLab Plugin'. You can also download the [zip file](https://www.lumenera.com/matlab-image-acquisition.html). Make sure to choose version 2.0.1.

2. Run 'install.bat' by either:  
    * double-clicking it in a Windows Explorer window. A command window will open. Enter option ‘2’ (for Matlab 2010 and later versions and with windows 32 bits). The command window will close pretty quickly. Nevertheless try to get if this message is displayed:  
    ```
    The message
    ```
    * or by opening a Command Promp window and typing the following:  
    ```
    C:
    cd "\Lumenera Matlab Plugin"
    install <option>
    ```
    where <option> is 2 (for Matlab 2010 and later versions and with windows 32 bits).  
New files should be created in the directory 'C:\Lumenera MatLab Plugin'.
  
3. Now open Matlab 2017a. Use the following commands:
```
imaqregister('C:\Lumenera MatLab Plugin\lumeneraimaq.dll');
imaqreset
```
This should not create any errors. However, it is normal if at Matlab toolbar->Apps->Image Toolbox, it is showed no plug-ins are detected. Close Matlab.

4. Run 'install.bat' like at step 2 expept by choosing option 3 (Matlab 2010 and later versions for WIndows 64 bits).

5. Repeat step 3. Now if you go to Matlab toolbar->Apps->Image Toolbox, the plug-in 'lumeneraimaq' should be detected.

6. In MatLab, add the directories 'C:\Lumenera MatLab Plugin\' and 'C:\Lumenera MatLab Plugin\Samples\' to Matlab's search path (under the File->Set Path->Add Folder... menu option).
