import requests
import matplotlib.pyplot as plt

class StockData:
    def __init__(self):
        self.APIKEY = 'IEUGLFJ3HPHL2X7Y'
        self.endpoint = 'https://www.alphavantage.co/query'


    def get_stocks(self, stock_name, basis, n_b, datatype='json',output_s = 'compact'):
        '''
            This function returns an array containing the desired values for the specified amount of basis.

            Params: 
                stock_name = The name or the code of the stock you want to analyze for (e.g TSLA)
                basis = The basis you are looking for (e.g monthly basis, weekly basis, daily basis, hourly basis)
                n_b = Length of the data points you are looking for, i.e. 10 for the latest 10 data points 
                datatype = The type of the data you want to get from the API (Default = json) (json or csv)
                output_s = Specifies the amount of data returns from the API. (Default = compact) (compact or full)
                                                                                                  Compact = Last 100 data points
                                                                                                  Full = Full history
            
            Example Return Value:
                stock_name = TSLA, basis = daily, n_b = 10, datatype = json, output_s = compact
                array = [closing values of TSLA stock of the last 10 days]
        '''

        params = {
            'function': basis,
            'symbol': stock_name,
            'outputsize': output_s,
            'datatype': datatype,
            'apikey': self.APIKEY
        }

        
        response = requests.get(url=self.endpoint, params=params).json()
        
        dates = {resp: response['Time Series (Daily)'][resp] for resp in list(response['Time Series (Daily)'])[:n_b]}
        cv = [dates[date]['4. close'] for date in dates]
        self.visualize(dates)
        return cv

    def visualize(self, dates):
        
        x = [date for date in dates]
        y = [dates[date]['4. close'] for date in x]
        
        plt.plot(x, y, 'o')
        plt.xticks(rotation=45)
        plt.xlabel('Date')
        plt.ylabel('Stock Closing Value')
        plt.show()
                

