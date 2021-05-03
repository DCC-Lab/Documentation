# HOWTO - Python Virtual Environment (venv)

In this tutorial, you will learn:

1. What is a virtual environment (venv)
2. How to use a venv for python
3. How to uninstall anaconda

*be aware of the `\` vs `/`

## 1. What is a virtual environment (venv)

The main purpose of Python virtual environments (venv) is to create an isolated environment for Python projects. This means that *each project* can have its *own* dependencies (module version), regardless of what dependencies every other project has. Also, it assure that everybody working on a project has the *same* *version* than the other persons. Here is an example:

Let's say I have 2 projects on my computer. Project **A** and **B**.

- The 2 project all use different packages, but all use `numpy`.  On your `anaconda`  python interpreter, you have `numpy` installed, but it is version `numpy==2.0.1`. Project **A** is fine with it, but project **B** requires the version `numpy==3.1.1`. What do you do ? You uninstall numpy and you reinstall the correct package while you are working on project **B**. Then, if you want to work on project **A**, you have to revert to the older version... ***painful***. 
- You are not the author of project **B**. The creator of project **B** was using `numpy==3.4.1`. Everything was working fine until you realized `numpy==3.1.1` had a tiny difference with `numpy==3.4.1` which makes the project fail at some point. But all your colleagues all have different version of numpy, so you have to inform all of them to change to 3.4.1. But some might have issues doing so, etc.
- Imagine now that you have 100 packages that are shared on 20 different projects in which 40 people participate. Have fun switching between the versions and telling people to change their versions. It is gonna be a mess.

I made a little diagram to illustrate:



### Without venv

![image-20200511144152846](../assets/HOWTO-PythonVirtualEnvironment(venv)/image-20200511144152846.png)

### With venv

![image-20200511144333739](../assets/HOWTO-PythonVirtualEnvironment(venv)/image-20200511144333739.png)

## 2. How to use a venv for Python

Since I want everyone to follow, I'll explain, in details, each step. The first installation of venv is more complicated, then it becomes really easy.

### First venv install

1. Open a python project. Try to locate a requirements.txt file. If there is one, good, if not, no worries.

2. Verify what python version you have on your system.

   1. **Click** on the terminal in PyCharm ![image-20200511131541332](../assets/HOWTO-PythonVirtualEnvironment(venv)/image-20200511131541332.png)
   2. **Type** `python` in the Terminal window. ![image-20200511131744020](../assets/HOWTO-PythonVirtualEnvironment(venv)/image-20200511131744020.png)
   3. You will see the version of your system interpreter appear![image-20200511131840589](../assets/HOWTO-PythonVirtualEnvironment(venv)/image-20200511131840589.png)
   4. **Type** `exit()`

3. Now we will install the `virtualenv` module for python, to be able to create new `venv`.

   1. **Type** `pip install virtualenv`
   2. If you don't have `pip`, you should seek on to install `pip` first.

4. Now, we will create your first virtual environment for python. The version of python installed will be the same than the one on your computer that you just saw.

   1. **Type** `python -m venv myvenv` 
   2. `-m` means that you want to launch a python module as a script
   3. The first `venv` is the name of the package you want to launch `venv` is the package name of `virtualenv`
   4. `my venv` is the name of your venv, you can call it whatever you want.
   5. Now, in your project tree, you should see a new directory `myvenv` ![image-20200511132850644](../assets/HOWTO-PythonVirtualEnvironment(venv)/image-20200511132850644.png)

5. This new folder is where your packages will be installed. To be able to install packages in this directory, you will need to do the following commands, in order:

   1. Under WINDOWS:
      1. **Type** `myvenv\scripts\activate` Now in the left corner, you should see the name of your venv like such:![image-20200511143308405](../assets/HOWTO-PythonVirtualEnvironment(venv)/image-20200511143308405.png)
   2. Under MacOS:
      1. **Type** `source myvenv/bin/activate` this will activate the venv in one command. 

6. Now, you have to make your new venv as the new project's interpreter, going in File--> Settings--> Project-->Project Interpreter --> ![image-20200511133844041](../assets/HOWTO-PythonVirtualEnvironment(venv)/image-20200511133844041.png)--> Add --> ![image-20200511133923713](../assets/HOWTO-PythonVirtualEnvironment(venv)/image-20200511133923713.png) Then you can hit OK and exit.

7. Now try to run your project! It won't work because we no packages installed. Here is where the magic usually happens. 
   <u>*If you have a requirements.txt*</u>, you simply **Type:**`pip install -r requirements.txt` and it will all install all the packages with the good version that are all written in the requirements.txt. (that's why `-r`) 

   *<u>If you **don't** have a requirements.txt</u>*, you will have to use `pip install` for all the packages, then make yourself the requirements.txt by using the command `pip freeze > requirements.txt`. This will create a file with all the packages name and version that you have installed. You can push this file in the project's repository.

8. That's how you setup a new virtual environment for python!

### Using venv for the second time

It is already much more easy.

1. **Type** the following commands in the pycharm terminal
   1. `python -m venv myvenv`
   2. `myvenv\scripts\activate` or `source myvenv/bin/activate` under MacOS
   6. `pip install -r requirements.txt`
   7. If there is no requirements.txt, install all the packages with `pip install`, then make yourself the .txt with this command `pip freeze > requirements.txt`. `push` this file in the repository, so everyone can thank you. :-) 

### Going out of the venv

Congratulations, you are now stuck in your venv! To get out of it, type the following commands:

1. **Type** : `myvenv\scripts\deactivate` or just `deactivate` under MacOS.