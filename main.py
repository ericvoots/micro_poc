import celery

from streams import streams

'''
this is where everything from streams, getting data, creating features and models will be called

'''




if __name__ == "__main__":
           
    # step 1 kind of every day or week or so make sure streams are updated
    streamsdl = streams(config_file="config.toml")
    
    streamsdl.get_streams()



# if not updating streams step 2, get data and features



# step 3 feature selection if updating the model, default update schedule is once a week



# step 4 model retrain if updating the model as well



