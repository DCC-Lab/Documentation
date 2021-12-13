# How to connect to CAFEINE3/GOLATH/LABDATA

## Some General Knowledge

`cafeine3` is DCCLAB's Virtual Machine running on `dccserver`, the main DCCLAB server where the data and website are. We go through `cafeine3` because it is more secure. This way, if someone messes with `cafeine3`, no problem, we can revert and the data won't be lost. `Goliath` is the name of the 100TB volume on the server. Inside `Goliath`, there's the `/labdata`

- To connect to `cafeine3` console, you can go via `ssh` , use this command: `ssh dcclab@cafeine3.crulrg.ulaval.ca`

- To connect to access the data, there are two ways (Here's the first method) :

    1. You can use the `scp` command. For this, you have to know the path of the file you want to get, or the path where of where you want to put your file.

        - **FROM** *your* computer, COPY a file **TO** `cafeine3`: :  `scp /pathToYourComputerFile dcclab@cafeine3.crulrg.ulaval.ca:/pathWhereItGoes`

        - **FROM** *your* computer, GET a file **FROM** `cafeine3`: :  `scp dcclab@cafeine3.crulrg.ulaval.ca:/pathWhereItIs /pathOnYourComputerWhereItGoes `

## TLDR: What you Really want to know

### FOR MAC OS

You can connect to the AFP service (Apple File System) **FOR MAC**

1. Go to Network in your Finder.
2. Select Cafeine3
3. Click on `Connect As ...`
4. Enter the DCCLAB credentials
5. You should now have a `read/write` access to `Goliath/labdata`

![cafeine3_1](\HOWTO-GitHub.assets\cafeine3_1.png)

![cafeine3_2](\HOWTO-GitHub.assets\cafeine3_2.png)![cafeine3_3](\HOWTO-GitHub.assets\cafeine3_3.png)

![cafeine3_4](\HOWTO-GitHub.assets\cafeine3_4.png)



### FOR WINDOWS 10

You can connect to the SMB service (SIMBA File System) **FOR Windows**

1. Go to "My Computer / Ce PC"
2. In the upper tab menu, click on "Computer/Ordinateur"
3. Click on "Map a network drive / Connecter un lecteur réseau"
4. Choose a drive letter and enter the server's address: `:\\cafeine3.crulrg.ulaval.ca`
5. Enter dcclab credentials
6. You should now have access to Goliath as a drive on your computer.