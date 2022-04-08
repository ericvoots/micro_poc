from celery import Celery
from celery.schedules import crontab
import json

from redis import Redis
from rq import Queue
from streams import streams
from features import features

import toml

'''
this is where everything from streams, getting data, creating features and models will be called

'''



# get config file, or later use a command line argument to change filename if you want
config = toml.load("config.toml")

# create celery app to monitor and schedule
app = Celery(name='main',
             broker="pyamqp://guest@python.microprediction.stonks.voots.org")

app.conf.enable_utc = True

stream_cron = crontab(**config["stream_schedule"])

# step 1 kind of every day or week or so make sure streams are updated
# weekly flag will update the streams to use every saturday a few times

app.conf.beat_schedule = {
                            "stream_task": {
                                "task":  streams(config_file=config),
                                "schedule": stream_cron
                            }
    
    
}
      
    
    #streamsdl = streams(config_file=config)    
    #streamsdl.get_streams()

    # get the streams
    #stream_json = open("streams.json")
    #stream_dict = json.load(stream_json)
    
    # create redis queue
    #q = Queue(connection=Redis())
    
    #TODO remove this, just a temp loop so I dont use all the streams
    #stream_list = ["c2_rebalanced_95.json", "c5_cardano.json", "fathom_00.json"]

    # add stream to queue to be processed
    
"""
#step 2, if not updating streams get data and features
for s in stream_list:
    print(f"getting data and analyzing for stream:  {s}")
    features_class = features(config_file=config,
                                stream=s)

    features_class.get_data()
"""

    # step 3 feature selection if updating the model, default update schedule is once a week



    # step 4 model retrain if updating the model as well



