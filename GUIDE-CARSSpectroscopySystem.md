[TOC]



## Workings of CARS

### Laser and microscope

#### Fibers

<u>Yellow fiber</u> : connected to laser from HalifaxBiophot

- Monomode to better focus light (higher resolution)
- Has the pump (792.5 nm) and the stokes (1021-1044 nm) laser going through it simultaneously
- Cable from yellow fiber to laser : VERY valuable

<u>Orange fiber</u> : connected to Photon counter

- Multimode to accept more light

<u>Probe</u> :

- Both fibers stripped and cleaved, "naked" fiber for ±10cm
- both put through in syringe needle of 400 um outer diameter
- end of syringe needle superglued to prevent fibers from slipping out, ends of fibers aren't glued (I think)
- Heat shrink around part of needle and rest of stripped fiber to make it more robust, and tape around the shrink and unstripped fiber
- Held by magnetic clamp

**2 fiber probe: **![](fig/2fiberprobe.jpg)

Camera + objective was used to check if the probe was clean (left picture)

<u>To test if fibers are dirty</u> : 

- Check with camera (dirty surface directly)
- shine light on other end (connector), light should come out uniformly

<u>Clean probe tip</u> : 

- Take diamond sanding paper and sand grey-purple white
- Clean with acetone and optical cloth
- spray with compressed air

#### Optical setup

- No open optics, all fiber based!
- clamp holds the probe that goes into the sample

### General operation of the CARS

- We send a pump and stokes laser through the yellow emission fiber. Their pulses have to be in phase at the sample so we have to adjust the delays since both lasers don't travel at the same speed
- CARS excitation of sample emits light that goes through orange fiber and goes to a photon counter
- Software allows to sweep different stokes wavelength to analyze the molecular constitution of the sample



## Using the CARS spectro

### Hardware

- CLOSE ALL THE LIGHTS! Photon counter is very sensitive.
  - Also put blanket over the setup and a separate one on the photon counter itself
- Behind the spectro, connect the red wire the the +5V input, use scissors to push it down. 

### Software

#### Matlab app

![](fig/matlab.png)

**To make sure everything works : **

- add all folders and subfolders from Github\CARS\niDAQAquisition to path
- also add Github\CARS\CARSFiberDataAnalysis
- run "niDAQGUI" in the console, GUI shown above opens
- change name in data log directory from Damon to dcclab as shown

**Parameters :**

- analog input : always 1?
- settings for photon counter (might not be optimal but they work):
  - acquisition duration : 4
  - acquisition rate : 16
  - counter interval : 0.001
- settings for PMT :
  - keep default
- sweep settings : make sure they match the ones on GUI

#### GUI Program

![](fig/GUI.png)

- <u>Right column</u> : shouldn't have to change anything
  
  - If Vbias arent between 2 and 5V : problem! (close laser)
- <u>Middle column</u> : sweep should always be bidirectional
  
  - sweep details : usual settings are from 1021 to 1044 with 0.2nm step
  - time between steps : 1000 us
  - nb steps: should be 116
- <u>Left column</u> : Main settings to change
  - Good power settings for DMSO + white tape underneath :
    - Programmable laser : 10%
    - MOPA : 15%
  - Good power for other substances with less signal (ethanol, acetone, etc) with white tape background : 
    - Programmable : 20%
    - MOPA : 40%
  - Can change manually the wavelength of the stokes with prog wavelength
  - Harmonic should stay at 2? Maybe 4 (unsure)
  - <u>Delays :</u>
    - Change global offset when changing length of fiber of probe
      
      - cutting 1m = ± -30ps of global offset
      
    - Delay underneath is loaded with excel file with all delays (shortcut on lab desktop)
    
    - delay step to manually change delay
    
    - **Optimal global delay with current fiber lengths and setup : -5 ps**
    
      ![](../golbalDelay/Figure_1.png)
    
      Delay seem to be slightly different depending on the peak we watch, but noise could be an important factor in the measured value. The 2909 peak had a lot more data so noise should be a less important factor, so we use its value of -5ps as optimal global delay

### Saving data

#### Normal acquisition over time 

- **CLOSE ALL THE LIGHTS AND COVER PHOTON COUNTER**
- plug the photon counter's red cable inside de +5V behind the system
- Open GUI and DAQGUI
- On DAQGUI, select the photon counter as device
- click start DAQ, you should see graph of the noise generated (should stay belay 15 counts)
- On GUI, change the settings of the laser and click START
- you should see the photon count jump slightly (20-30)

#### CARS sweep

- **CLOSE ALL THE LIGHTS AND COVER PHOTON COUNTER**
- plug the photon counter's red cable inside de +5V behind the system
- Open GUI and DAQGUI
- On DAQGUI, select the photon counter as device
- click start DAQ, you should see graph of the noise generated
- on GUI, change the settings in the sweep mode (middle column) and click "start sweep"
- In DAQGUI, tick "counter sweep plot" under stop daq and click "Start DAQ", you should see a cars spectrum of the sample.
- To save, check sweep log and perform sweep plot, then "Log Data" in desired folder. You need to stop the DAQ if it is running to save the data.

#### Typical errors



## Data analysis

### Matlab

After you have a saved dataset of a CARS spectrum, run the following commands 

``` data = dlmReadFile;``` and select data file

``` [wavenumbers,EpiSignal]=geniaRawDataAnalysisCounter(data,1021,1044,0.2);``` 

- change the values if different ones were used

- this function has been updated and now puts a .csv file with the data at the desired directory. With this data you can now plot it with python.

```plot(wavenumbers,EpiSignal)```

Should give a savable plot of the data.

![](plot.jpg)



