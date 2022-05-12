# How to connect to CAFEINE3/GOLATH/LABDATA

## General Knowledge

`cafeine3` is the main server of DCCLab where the data and website are. `Goliath` is the name of the very, very large disk (100TB) on the server. Inside `Goliath`, there's a folder where we keep **everything** : `/labdata`. More **important** info on labdata available [here](HOWTO-labdata.md).

- The simplest option: You should be able to connect via Windows/macOS/Linux easily with the standard tools (Connect to, Network Neighbouhood, etc...). Look for Cafeine3 and then Goliath.  Identify as 'dcclab' with the standard password. More details below.

- To connect to the actual server `cafeine3` with a shell (i.e. a command-line window or a terminal), you must use `ssh` (meaning Secure Shell). Use this command: `ssh dcclab@cafeine3.crulrg.ulaval.ca`.  Obviously you must have `ssh` installed (standard with macOS, Windows, you're on your own).

- To connect to access the data that is on the disk, there are two ways (Here's the first method) :

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

![cafeine3_1](https://raw.githubusercontent.com/DCC-Lab/Documentation/master/HOWTO/HOWTO-GitHub.assets/cafeine3_1.png)

![cafeine3_2](https://raw.githubusercontent.com/DCC-Lab/Documentation/master/HOWTO/HOWTO-GitHub.assets/cafeine3_2.png)

![cafeine3_3](https://raw.githubusercontent.com/DCC-Lab/Documentation/master/HOWTO/HOWTO-GitHub.assets/cafeine3_3.png)

![cafeine3_4](https://raw.githubusercontent.com/DCC-Lab/Documentation/master/HOWTO/HOWTO-GitHub.assets/cafeine3_4.png)

### FOR WINDOWS 10

You can connect to the SMB service (SIMBA File System) **FOR Windows**

1. Go to "My Computer / Ce PC"
2. In the upper tab menu, click on "Computer/Ordinateur"
3. Click on "Map a network drive / Connecter un lecteur réseau"
4. Choose a drive letter and enter the server's address: `\\cafeine3.crulrg.ulaval.ca\Public Directory\Goliath`
5. Enter dcclab credentials (might have to create a new login account).
6. You should now have access to Goliath as a drive on your computer.

### For Commodore-64

Please talk to Daniel.
