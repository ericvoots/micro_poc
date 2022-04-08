import json
import microprediction
import pandas as pd

import toml

from celery import Task
from microprediction import MicroReader

'''
used for getting streams to be used in the crawler, then saved into a json file.
'''

class streams(Task):
    """_summary_
    used for getting what streams are needed to be used in the crawlers and models
    """
    # don't need to save results
    ignore_result = True
    
    def __init__(self, config_file):
        
        self.config = config_file
        self.streams = {}
        self.mr = MicroReader()
        
    def get_streams(self):
        """_summary_
        this is the function used to update the streams and save them off to a json file
        """
        all_streams = self.mr.get_stream_names()
        
        for stream in self.config['stream_prefixes']:
            #self.streams.append([i for i in all_streams if i.startswith(stream)])
            
            self.streams[stream] = [i for i in all_streams if i.startswith(stream)]
            
         # save stream names into current folder with json, just change the folder to save to using config if needed
        
        with open("streams.json", "w") as outfile:
            json.dump(self.streams, outfile)
    
    def run(self):
        """_summary_
        this will run get streams or any new functions added
        """
        self.get_streams()