import celery
import json

from streams import streams
from features import features

'''
this is where everything from streams, getting data, creating features and models will be called

'''




if __name__ == "__main__":
    
    #TODO add schedule here for updating the streams based on config file
    # step 1 kind of every day or week or so make sure streams are updated
    streamsdl = streams(config_file="config.toml")
    
    streamsdl.get_streams()

        # get the streams
    stream_json = open("streams.json")
    stream_dict = json.load(stream_json)
    
    print(stream_dict)
    
    #TODO remove this, just a temp loop so I dont use all the streams
    stream_list = ["c2_rebalanced_95.json", "c5_cardano.json"]

# if not updating streams step 2, get data and features
    for s in stream_list:
        print(f"getting data and analyzing for stream:  {s}")
        features_class = features(config_file="config.toml",
                                  stream=s)
    
        features_class.get_data()


# step 3 feature selection if updating the model, default update schedule is once a week



# step 4 model retrain if updating the model as well



