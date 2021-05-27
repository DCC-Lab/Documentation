# HOWTO - DCCLAB SERVER CONNECTIONS
### GENERAL INFORMATIONS

- **What is DCCSERVER?**: It is a physical device. A SynologyXS3618 which is a computer with 12 drive bay and 4 ethernet connections. It allows for 200TB of storage, where the group data is stored and actually runs ww.dcclab.ca, the group's website. 
- **What is Cafeine2?**: It is a physical device. A MacMini Server which is a MacMini inside a server case. It controls 2 storage bays of 140TB, where a lot of the group's data is stored.
- **What is Cafeine3?**: It is a linux virtual machine. It is running on *dccserver* and allows for doing anything we would like. It has its own IP adress, so we can SSH on it, without compromising *dccserver*, on which we shouldn't SSH.
- **What is 172.16.1.107 / 108 / 109?**: These are the local IP adresses of our machines
- **What is "Goliath"**: It is the name of the volume that we should use to store the data. There are many "virtual drive" like this one. "webdrive" and "vmweb" are other virtual drives used for the webserver on the computer.
- **Can I access "dccserver" ?**: Yes, from internal networks (ulaval + crulrg)
  - ssh dcclab@cafeine2.crulrg.ulaval.ca
    ssh dcclab@dccserver.local
- **Can I access "cafeine3" ?**: Yes, from internal networks (ulaval + crulrg)
  - ssh dcclab@cafeine2.crulrg.ulaval.ca
    ssh dcclab@172.16.1.109
- **Can I access "cafeine2" ?**: Yes,  from remote (the internet) and from internal networks (ulaval + crulrg)
  - ssh dcclab@cafeine2.crulrg.ulaval.ca
- **Can I access "lmaris" computer?**: Yes, from home
  - ssh [dcclab@cafeine2.crulrg.ulaval.ca](mailto:dcclab@cafeine2.ulaval.ca) -L5901:Mac-Imaris.local:5900’
- **Internet Public IP for Ulaval Network**: 132.203.x.x
- **I want to manage dccserver:** Administrator link to manage *dccserver*: https://admin.dccserver.crulrg.ulaval.ca/
- **Why can't I connect to  dccserver and cafeine3 from home?**: People from CRULRG didn't allow SSH remote connection from the internet on DCCSERVER nor on CAFEINE3. SSH on those machines is possible from the ULAVAL Network or from CRULRG network. It will be possible soon.





# Data Storage Connection
### For MacOS Users
1. Go in *finder*
2. Go to the *Network/Reseau* tab on the left
3. In the list of devices you should see *dccserver*, click on it
4. Upper-right corner click on *Connect*.
5. There you go. For more details, see Apple's tutorial.
	https://support.apple.com/fr-fr/guide/mac-help/mchlp1140/mac
6. Now *dccserver* should always appear in your finder.

### For Windows Users
1. Go in your folders
2. Go to *This PC*
3. Upper-left click *Computer*
4. Click on *Map a network drive*
5. Connection steps:
	1. Select a Drive Letter (Any)
	2. Enter this in the folder entry :\\172.16.1.108\Goliath
	3. Select *Connect using different credentials* and use:
		**username:** dcclab  		**mdp**: You know it
6. Now the drive will always appear in your drives.





# SSH Connection

## Network Diagram

![dcc_network](.\HOWTO-GitHub.assets\dcc_network.png)

## IP Address catalog

|IP ULVAL| IP CRULRG |DNS ULAVAL|DNS CRULRG|
|--|--|--|--|
| 132.203.179.107 | 172.16.1.107 | cafeine2 | cafeine2 |
| 132.203.179.108 | 172.16.1.108 | dccserver | dccserver |
| 132.203.179.109 | 172.16.1.109 | cafeine3 | NOT SET |


## SHH Connection guide
| YOUR LOCATION | SERVER NAME   | USERNAME | PASSWORD | COMMAND                                                      |
| ------------- | ------------- | -------- | -------- | ------------------------------------------------------------ |
|               | **CAFEINE2**  |          |          |                                                              |
| **INTERNET**  | cafeine2      | dcclab   | x        | ssh dcclab@cafeine2.crulrg.ulaval.ca                         |
| **ULAVAL**    | cafeine2      | dcclab   | x        | ssh dcclab@cafeine2.crulrg.ulaval.ca                         |
| **CRULRG**    | cafeine2      | dcclab   | x        | ssh dcclab@cafeine2.local                                    |
|               | **CAFEINE3**  |          |          |                                                              |
| **INTERNET**  | Not Permited  | dcclab   | x        | Connect from *Cafeine2* then use command from CRULRG network |
| **ULAVAL**    | cafeine3      | dcclab   | x        | ssh dcclab@cafeine3.crulrg.ulaval.ca                         |
| **CRULRG**    | 172.16.1.109  | dcclab   | x        | ssh dcclab@172.16.1.109                                      |
|               | **DCCSERVER** |          |          |                                                              |
| **INTERNET**  | Not Permited  | dccadmin | x        | Connect from *Cafeine2* then use command from CRULRG network |
| **ULAVAL**    | dccserver     | dccadmin | x        | ssh dccadmin@dccserver.crulrg.ulaval.ca                      |
| **CRULRG**    | dccserver     | dccadmin | x        | ssh dccadmin@dccserver.local                                 |

- You Can interchange the DNS(name) with the IP when trying to make a connection through SSH.
- If you are an administrator, you use **dccadmin** on the other machines, if you know the password. This will grant you all permissions.

