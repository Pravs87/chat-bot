# chat-bot
Recognizes the intents and entities of a chat dialogue

**Part A**

**_Training a model to detect entities and intention of a user_** 

**`Libraries used:`**

NLTK - for NLP techniques like pre-processing, tokenizing etc.

Tensorflow - for building the chatbot model

Numpy - storing data

spaCy - Entity Recognition

**`Dataset`**

The training data is a file which contains various intents which has the following metadata: tagname for the intent, list of patterns that fall under this intent, list of responses that could be randomly given as a response

**`Training`**

1. We create a bag of word representation for each document (here each pattern). We store the class label (here intent tag name) along with the training data.
2. We use a 2 layer neural network to train on the data where the learning happens through gradient descent optimizer
3. After few hundreds of iterations and some error thresholding we have our model

**`Testing`**

1. Given a new pattern, we get the bow representation for that pattern and give to the model which will classify it into one of the intents
2. Once we have intents, we can find various entities in the intents using a Named Entity Recognition analyzer.

**`Note`**

We have used a 2-layer neural network which will classify patterns into various classes. If we were to have a contextual based bot, as is the trend these days, this approach definitely wont work. We need to move towards a seq2seq learning using LSTM network. 

**`Running the code`**

_Pre-requisites_ :
You should install all the required libraries - tensorflow, tflearn, spaCy, numpy, nltk. NLTK might also require you to download data for english (like stemmer, tokenizer etc.).

_Run_

The main file in the project is the modelBuild.py which has a driver function in main. This will take in a pattern / sentence as an argument for running. Make sure you enclose the sentence in double quotes (").

Input: "test sentence related to the intents"

Output: a. classified intent for the test sentence ; b. entities present in the sentence 

**I have also kept few screen shots of the results that I got while running**
**Part B**

**_Facebook integration with dialogflow (api.ai)_**

I have trained the dialogflow (previously api.ai) bot with the same set of data given in intents.json
You can access the bot here: https://www.facebook.com/mspbot/

You can start chatting with the bot by clicking of message button.

Important:
Even though the page is public the bot is not public. So anyone who wants to access the bot has to have permissions either as a developer / tester. 
If you want to try that, please let me know your facebook username so that I can add it to the list of developer or tester.

The reason why bot can't be public is that - facebook can only make it public after we raise a request to them stating we have a bot. Then FB guys are going to test this bot before releasing public. Thats quite a tedious process for a test bot. So it is private for now.

**Summary**

After working on both dialogflow and creating own model my observations are the following:
1. Advantage of building our own model gives control to us than using any library

1. dialogflow is very user-friendly and easy to get started with basic chatbot like intent and entity detection
2. dialogflow has many system generated entities which is tough for any new model to handle. Since the knowledge the library gained is on humongous data.
3. dialogflow also has nice integrations with many social apps like FB, Twitter, Slack etc. which is very cool to use.

Next steps is to explore a more context based modelling.