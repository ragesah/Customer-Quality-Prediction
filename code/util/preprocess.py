from sklearn.preprocessing import StandardScaler as Scaler
from sklearn.model_selection import train_test_split
from util.package import *

FEATURES = ['custAge', 'profession', 'marital', 'default', 'housing', 'loan',
       'contact', 'campaign', 'pdays', 'previous', 'poutcome', 'emp.var.rate',
       'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed',
       'pastEmail', 'prev_contracted']
TARGET = 'responded'


def split_dataset(X,y,test_size=0.3,random_seed=42,scaler=False):
    if scaler:
        X_train, X_val, y_train, y_val = train_test_split(X, y , test_size=test_size, stratify=y, random_state=random_seed)
        print('Train Size: {}'.format(X_train.shape))
        print('Validation Size: {}'.format(X_val.shape))
        scaler = Scaler().fit(X_train,y_train)
        X_train = scaler.transform(X_train)
        X_val = scaler.transform(X_val)
        
        return X_train, X_val, y_train, y_val,scaler
    else:
        X_train, X_val, y_train, y_val = train_test_split(X, y , test_size=test_size, stratify=y, random_state=random_seed)
        print('Train Size: {}'.format(X_train.shape))
        print('Validation Size: {}'.format(X_val.shape))
        
        return X_train, X_val, y_train, y_val
    
def unfold_metrics(mx):
    print('Precision = {}%; Recall = {}%'.format(mx[0]*100,mx[1]*100))
    
def save_plot(path, name,format_='pdf'):
    plt.savefig(path+'/'+name+'.'+format_, format=format_, dpi = 300)