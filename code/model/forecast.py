#!pip install fbprophet
import fbprophet
import datetime
import itertools
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from util.package import *

   
RANDOM_SEED = 42

class Forecast():
    def __init__(self, Xtrain,  model_type = 'P'):
        self.Xtrain = Xtrain
        self.forecast_point = 4
        self.forecast = 0
        self.mt = model_type
        if self.mt == 'P':
            self.model = fbprophet.Prophet(yearly_seasonality=False, weekly_seasonality=True,daily_seasonality=True,growth = 'flat').fit(self.Xtrain)
        elif self.mt == 'E':
            self.model = ExponentialSmoothing(self.Xtrain,trend='add',seasonal='add',seasonal_periods=96).fit()
        elif self.mt == 'A':
            self.model = sm.tsa.statespace.SARIMAX(self.Xtrain,  order=(1,1,1), seasonal_order=(1,1,1,4), simple_differencing = False).fit() # (P,D,Q,M) ## seasonality (P,D,Q,M) are chosen based on 1 degree of differentiation

    
    def forecasting(self):
        def get_forecast_range():
            future = (pd.DataFrame(columns=['NULL'],
                            index=pd.date_range('1970-04-13 19:00:00', '1970-04-13 19:45:00',freq='15T'))
                                    .between_time('07:00','21:00')
                                    .index.strftime('%Y-%m-%d %H:%M:%S')
                                    .tolist() )
            future = pd.DataFrame(future)
            future.columns = ['ds']
            future['ds']= pd.to_datetime(future['ds'])
            return future
        
        if self.mt == 'P':
            self.forecast = self.model.predict(get_forecast_range())
            self.forecast.yhat = self.forecast.yhat.astype('int')
            self.forecast = self.forecast[['ds','yhat']]
        elif self.mt == 'E': 
            self.forecast = self.model.forecast(self.forecast_point).rename('TES Forecast')
            self.forecast = pd.DataFrame(self.forecast.astype('int'))
        elif self.mt == 'A':
            self.forecast = self.model.predict(start = 9788, end= 9792, dynamic= True)
            self.forecast = pd.DataFrame(self.forecast.astype('int'))

        return self.forecast

    
    def evaluate(self):
        pass