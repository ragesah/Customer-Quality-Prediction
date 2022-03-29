import pandas as pd
import numpy as np

class EDA():
    def __init__(self, data):
#         pass
        self.data = data
#         self.nrow, self.ncol = self.data.shape
        
    def get_size(self, data):
        nrow, ncol = data.shape
        print ("#rows = {}; #columns = {}".format(nrow, ncol))
        return nrow, ncol

    
    def null_stats(self, data):
        cnt = data.isnull().sum()
        per = data.isnull().sum()/ len(data) * 100
        d = pd.concat([pd.DataFrame(cnt, columns = ['count']), pd.DataFrame(per, columns = ['%age'])], axis = 1)
        display(d[d['%age'] > 0])
    
    def column_types(self, data):
        numerical_cols = data.select_dtypes('number').columns
        categorical_cols = data.select_dtypes('object').columns
        return numerical_cols, categorical_cols
    
    def delete_columns(self, data, columns):
        data = data.drop(columns, axis = 1)
        return data
    
    def unique_values(self, data, columns):
#         print('Distinct Values in Categorical Column')
        for col in columns:
            try:
                print('{} -> {}'.format(col,data[col].nunique() ))
            except:
                pass
    def derive_features(self, data, columns):
        for col in columns:
            if col == 'pmonths':
                data['prev_contracted'] = np.where(data[col] == 999, 0, 1)
                data.drop(col, axis = 1, inplace = True)
            elif col == 'pdays':
                data['prev_contracted'] = np.where(data[col] == 999, 0, 1)
                data.drop(col, axis = 1, inplace = True)
        return data
    
    def transform(self, data, columns):
        for col in columns:
            try:
                if col == 'responded':
                    data['responded'] = np.where(data[col] == 'no', 0, 1)
                elif col == 'profession':
                    data[col] = data[col].apply(lambda x: 2 if x in ['technician', 'admin.', 'blue-collar'] else 1)
                elif col == 'marital':
                    data[col] = data[col].apply(lambda x: 3 if x=='single' else 2 if x=='divorced' else 4 if x=='married' else 1)
                elif col == 'default':
                    data[col] = data[col].apply(lambda x: 0 if x=='no' else 1)
                elif col == 'housing':
                    data[col] = data[col].apply(lambda x: 0 if x=='no' else 1)
                elif col == 'loan':
                    data[col] = data[col].apply(lambda x: 0 if x=='no' else 1)
                elif col == 'contact':
                    data[col] = data[col].apply(lambda x: 0 if x== 'telephone' else 1)
                elif col == 'poutcome':
                    data[col] = data[col].apply(lambda x: 2 if x== 'success' else 1 if x== 'failure' else 0)
            except:
                pass
        return data