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
    
    def __init__(self, config_file):
        """_summary_
        init of the features class
        Args:
            config_file (string): _description_ location of the toml file with all the settings
        """
        
        self.config = toml.load(config_file)
        # to limit the number of lags for feature creation
        self.max_lag = self.config["max_lags"]
        
        # get the streams
        stream = open("streams.json")
        self.streams = json.load(stream)
        
        self.mr = MicroReader()
        
        
    def get_data(self):
        """_summary_
        this function will download the most recent 900 values if there is no data 
        if there is data will get the most recent 20 then append to the data
        once data is downloaded will append
        can just add a max to the config file if you want to limit the total number 
        """
        
        print('getting data')
        
        # hard coding which two streams to only use for now
        print(f"config file {self.config} ")
        
        #TODO remove this
        stream_list = ["c2_rebalanced_95.json", "c2_rebalanced_55_mean.json"]
        
        for stream in stream_list:
        
            lagged_values, lagged_seconds = self.mr.get_lagged_values_and_times(stream)
            values = list(reversed(lagged_values))
            dt = [ datetime.fromtimestamp(s) for s in reversed(lagged_seconds)] 
            df = pd.DataFrame(columns=['date', 'y'])
            df['date'] = dt
            df['y'] = values
            
            print(f"\n\n\ntest {df.tail(20)}")
            

if __name__ == "__main__":
    
    features_class = features(config_file="config.toml")
    
    features_class.get_data()
        
    