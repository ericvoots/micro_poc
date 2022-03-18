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
        
        self.config = toml.load(config_file)
        self.streams = []
        
        print(f"current setup is {self.config}")
        
    def get_streams(self):
        
        print(f'test {self.streams}')

    
if __name__ == "__main__":
    
    # can probably just make this an argument later with argparse and passed in from jenkins or something
    get_streams = streams(config_file="config.toml")

    
    
    