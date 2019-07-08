# Machine Learning

The goal of this document is to give an introduction to the general concepts and theory around Machine Learning and its applications. 

 

----

### Table Of Content

1. [Introduction](#introduction)
   1. [Understanding the nomenclature](#nomenclature)
   2. [Branches of Machine Learning](#branches)
2. [Machine learning algorithms](#algorithms)
   1. [Neural Networks](#NN)
   2. [Deep Learning](#DL)

-----

 

## 1. Introduction <a name="introduction"></a>

### Understanding the nomenclature <a name="nomenclature"></a>

<img src="assets/machineLearning/categories.png" width="400px" />

**Artificial intelligence** is used to describe machines that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving" [1]. This general domain contains image processing, cognitive science, machine learning, neural networks and much more. **Machine learning** on its end is a more specific subject of AI that nowadays encapsulates almost all AI research topics. Its core idea is that the computer does not just use a pre-written algorithm, but learns how to solve the problem itself. 

> *Machine Learning is a field of study that gives computers the ability to learn without being explicitly programmed.* - **Arthur Samuel** (1959)

Machine learning started flourishing with the arrival of the big data, the increase in computation power (GPU) and the development of new machine learning algorithms. 

##### Traditional programming VS Machine Learning
<img src="assets/machineLearning/traditional.png" width="600px" />

In traditional programming you hard code the behavior of the program. In machine learning, you leave a lot of that to the machine to learn from the data iteratively. ML is used in the case when traditional programming strategy falls behind and it is not enough to fully implement a certain task. This is usually the case when the amount of inputs is too high, as with forecasts, image processing, speech recognition, etc.

### Branches of Machine Learning <a name="branches"></a>

<img src="assets/machineLearning/MLtypes.png" width="800px" />

**Reinforcement learning** is about optimizing a decision making policy with experiences and rewards. It focuses on finding a balance between exploration of territory and exploitation of current knowledge. 

*[Example](https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html): the agent has to decide between two actions - moving the cart left or right - so that the pole attached to it stays upright*

<img src="assets/machineLearning/RLcartpole.gif" width="400px"/>

**Supervised learning** tries to learn a function that maps an input to an output based on a learning process over training examples. In supervised learning, each example is a *pair* consisting of an input object and a desired output value (labels). This topic divides into classification (hottest subject in machine learning) and regression (forecasts, predictions). 

<img src="assets/machineLearning/class_regress.png" width="600px"/>

**Unsupervised learning** helps to find unknown patterns in an input dataset without pre-existing labels to regroup inputs into clusters, reduce the number of dimensions or simplify a vast input into a few principle components. The main methods used in unsupervised learning are principal component and cluster analysis. 

<img src="assets/machineLearning/clustering.png" width="600px"/>

In image classification, supervised learning will extract features from the input and learn to correctly link these features to the input label. Unsupervised learning with extract features from the inputs and only try to regroup them into *different* clusters.

<img src="assets/machineLearning/unsupervised.png" width="600px"/>

 

----



## 2. Machine learning algorithms <a name="algorithms"></a>

After all the subjects we presented, we will focus our attention on supervised learning for classification, which is clearly the subject of interest for data analysis in science. To address the problem of classification, we will discuss two popular machine learning algorithms suited for the task : the "simple" neural networks (perceptron) and the deep learning approach (focussed on CNN). 

*An interesting and exhausting list of all the popular machine learning algorithms is also available [here](https://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/).*

### Neural Networks <a name="NN"></a>

### Deep Learning <a name="DL"></a>

 

 

-----

----------

###### Scratch

-----

----

- Neural networks: perceptron, feature extraction, loss function, activation, back propagation
- Discuss the different DL architectures specfific for different kinds of task (**CNN** for images (UNet for semantic), LSTM, )

A good way to better understand supervised learning is to jump into the inner workings of its model: in this case, a "simple" fully-connected neural network. 


#### The basis for supervised learning

1. Data collection
2. Data preparation
3. **Model choice and training**
4. Model evaluation
5. Optimisation

<img src="assets/machineLearning/supervised.png" width="600px"/>


#### Application examples

alphaGo, self driving cars, image and speech recognition, forecast






#### References

[1] [Russell, Stuart J.](https://en.wikipedia.org/wiki/Stuart_J._Russell); [Norvig, Peter](https://en.wikipedia.org/wiki/Peter_Norvig) (2009). *Artificial Intelligence: A Modern Approach* (3rd ed.).





###### todo

https://en.wikipedia.org/wiki/Supervised_learning#Algorithm_choice , see dimensionality reduction.

