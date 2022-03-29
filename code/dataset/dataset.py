import pandas as pd

class Dataset():
    def __init__(self, path, isTimeSeries=False):
        self.path = path
        self.isTimeSeries = isTimeSeries
        self.data = None
        
    def read_trainset(self):
        if not self.isTimeSeries:
            data = pd.read_csv(self.path+'/training.csv')
        else:
            data = pd.read_json(self.path+'/failuretime.json')
        return data
    
    def read_testset(self):
        if not self.isTimeSeries:
            data = pd.read_csv(self.path+'/testingCandidate.csv')
        else:
            raise 'Invalid dataset demand'
        return data
    

