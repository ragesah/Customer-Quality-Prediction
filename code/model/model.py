from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix as CM
from sklearn.model_selection import cross_val_score
# import numpy as np
from util.package import *

   
RANDOM_SEED = 42


class Model():
    def __init__(self, Xtrain, ytrain, Xval, yval, model_type = 'R'):
        if model_type == 'R':
            self.model = RandomForestClassifier(random_state=RANDOM_SEED)
        else:
            self.model = LogisticRegression(random_state=RANDOM_SEED)
        
        self.Xtrain = Xtrain
        self.ytrain = ytrain
        self.Xtest = Xval
        self.ytest = yval
        self.ypred = None
    
    def train(self):
        self.model.fit(self.Xtrain, self.ytrain)       
    
    def predict(self, Xtest):
        self.ypred =  self.model.predict(Xtest)
        return self.ypred
    
    def evaluate(self):
        cm = CM(self.ytest, self.ypred)
        tn, fp, fn, tp = CM(self.ytest, self.ypred).ravel()
        precision, recall = tp/(tp+fp), tp/(tp+fn)
        return round(precision,4), round(recall,4), cm
    
    def cross_val_score(self):
        score = cross_val_score(self.model, self.Xtrain, self.ytrain, scoring='recall', cv=5)
        return np.mean(score)
