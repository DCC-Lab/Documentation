# Access *Calcul Quebec* to run Jupyter Notebooks on *Helios* GPU

This procedure will get you a working Jupyter Notebook logged on CalculQuebec's *Helios* GPU.

 

### Prerequisites

1. Daniel Côté's ComputeCanada Sponsor ID. 

 

### Procedure

1. [**Create a ComputeCanada Account**](https://ccdb.computecanada.ca/account_application)

   You will need the sponsor ID from Daniel Côté. Now wait/ask for approval from Daniel. 

2. **Apply for a CalculQuebec Account** 

   Login to your ComputeCanada Account and go to *Account -> Apply for a consortium account* and apply for CalculQuebec. Make sure to check *Helios* device at least. 

3. **Wait around 30 minutes for approval.**

4. **Log in to Helios server with SSH**

   You need to connect to *Helios* by SSH at least once to get access to a Jupyter Notebook. 

   Follow the procedure [written here](https://wiki.calculquebec.ca/w/Se_connecter_et_transf%C3%A9rer_des_fichiers/en) for windows or mac/linux to connect to the server *helios.calculquebec.ca* on port 22. The website also shows how to transfer data to your server. 

5. [**Open your Jupyter Notebook**](https://jupyter.calculquebec.ca/hub/home)

   Login with your CalculQuebec account. Check *Requires a GPU* to use *Helios*. 

   For further instructions on how to install packages and kernels (python environnements)
   
   [^1]: Make sure you add the desired module (or python version) on the software tab in the jupyter notebook before following the instructions on how to add a new kernel. 
   
   , follow the [CQ Jupyter Wiki](https://wiki.calculquebec.ca/w/JupyterHub). 
