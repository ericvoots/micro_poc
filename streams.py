import json
import pandas as pd

import toml

'''
used for getting streams to be used in the crawler, then saved into a json file.
'''

class streams(object):
    """_summary_
    used for getting what streams are needed to be used in the crawlers and models
    """
    
    def __init__(self, config_file):
        
        self.config = config_file
       
        
    def get_streams(self):
        
        print(f'test {self.streams}')

    
if __name__ == "__main__":
    
    get_streams = streams()
    streams.config_file = "config.toml"
    
    
    