from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


iris = load_iris()     #this loads the measurements data into the variable "iris"

print(iris.data)       # this prints the dataset (containing measures of the flower)
print(iris.target)     # this prints the answer dataset (what type of flower it is,, 0,1 and 2 represents different flower types)

X = iris.data          # storing the data of flower measurments into variable X
y = iris.target        # storing the data of flower type (results) into the Variable Y

X_train, X_test, y_train, y_test = train_test_split(  #]
    X, y, test_size=0.2                               #]----- this splits the data into 2 parts one for testing
)                                                     #]          and the other for training its accuracy

model = DecisionTreeClassifier()        #this uses the decision tree method to classify the data
model.fit(X_train, y_train)             # here is where all the training part of a machine comes to play
predictions = model.predict(X_test)     # this predicts the answers for the 20% of data we split in the beginning 

print(predictions)

print("ACCURACY:",                      #]
    accuracy_score(y_test, predictions) #]----- This is where the predicted answers's result is evaluated 
)                                       #]