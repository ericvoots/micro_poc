import microprediction
from datetime import datetime, timedelta
from microprediction import MicroReader

import json
import toml
import pandas as pd

'''
this will be for creating features and selecting them based off some thresholds set beforehand that can be altered in the toml file
i.e. so you don't end up creating 100 features and then using them all
'''
# any point in making a parent child class structure later? will come back to that thought, maybe given they all use the same config file
class features(object):
    """_summary_
    this will do some basic feature engineering
    Args:
        object (object): _description_ features class
    """
    
    def __init__(self, config_file, stream):
        """_summary_
        init of the features class
        Args:
            config_file (string): _description_ location of the toml file with all the settings
            stream (string): _description_ which stream is currently being used
        """
        self.stream = stream
        self.config = toml.load(config_file)
       
        # maximum number of values to download
        self.max_count = 900        
        self.mr = MicroReader()
    
    
    def check_max_datetime(self, datetime):
        """_summary_
        checks to be sure that the max date available in the time series is within the last 30 minutes UTC
        later add a discord web hook
        Args:
            datetime (string/datetime): _description_
        """
        
    def ma_feature_calc(self):
        """
        creates some moving average based features based on lags and pct diff from current
        """    
        
        
    def get_data(self):
        """_summary_
        this function will download the most recent 900 values if there is no data 
        if there is data will get the most recent 20 then append to the data
        once data is downloaded will append
        can just add a max to the config file if you want to limit the total number 
        """
        
        print('getting lagged values for stream {self.stream}')
        
                   
        # add a step to check if data exists
        
        
        lagged_values, lagged_seconds = self.mr.get_lagged_values_and_times(name=self.stream,
                                                                            count=self.max_count)
        
        values = list(reversed(lagged_values))
        dt = [ datetime.fromtimestamp(s) for s in reversed(lagged_seconds)] 
        self.df = pd.DataFrame(columns=['date', 'y'])
        self.df['date'] = dt
        self.df['y'] = values
        
        # append to previously downloaded data
        print(self.df.tail(20))
            
            # look into processing times and max data set size per stream, for now limit to 5000
       
    