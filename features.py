import microprediction
from datetime import datetime, timedelta
from microprediction import MicroReader

import json
import toml
import pandas as pd

import os.path

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
        self.config = config_file
       
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
        """_summary_
        creates some moving average based features based on x number of lags and pct diff from current
        where x is set by max_ma_lags in the config file
        """    
        
    def diff_feature_calc(self):
        """_summary_
        creates pct diff from latest up to x number of lags,w here x is set by max_diff_lags in the config file
        """
        
    def get_data(self):
        """_summary_
        this function will download the most recent 900 values if there is no data
        going beyond 900 tends to result in longer dl times so can append over time 
        if there is data will get the most recent 20 then append to the data
        once data is downloaded will append
        can just add a max to the config file if you want to limit the total number
        
        after checking for processed data or not this will then calculate a few features then predict
        if a model has been trained 
        """
        
        print(f'getting lagged values for stream {self.stream}')        

        # add a step to check if data exists
        if os.path.exists(self.config["processed_data_location"] + self.stream.rstrip("json") + "csv"):
            
            print(f"processed data exists for {self.stream}")
            # set to max ma lags to be double sure enough values are there for ma calcs later when appending
            # can just drop any duplicate values before processing
            self.max_count = self.config["max_ma_lags"]
        else:
            print(f"processed data does not exist for {self.stream}")
        
        lagged_values, lagged_seconds = self.mr.get_lagged_values_and_times(name=self.stream,
                                                                            count=self.max_count)
        
        values = list(reversed(lagged_values))
        dt = [ datetime.fromtimestamp(s) for s in reversed(lagged_seconds)] 
        self.df = pd.DataFrame(columns=['date', 'y'])
        self.df['date'] = dt
        self.df['y'] = values
        
        print(self.df.tail(20))
        
        # append to previously downloaded data

        # look into processing times and max data set size per stream, for now limit to 5000
       
    