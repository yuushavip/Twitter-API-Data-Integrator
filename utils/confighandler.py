import configparser
import tweepy

def get_api_config():
    config = configparser.ConfigParser()
    file_name = 'twitter_api.ini'
    file_path = f"config/{file_name}"
        
    config.read(file_path)
    
    return config

def get_auth_config():
    config = get_api_config()
    auth_config = config['AUTH']
    
    return auth_config

def get_tweepy_api():
    auth_config = get_auth_config()
    consumer_key = auth_config['consumer_key']
    consumer_secret = auth_config['consumer_secret']
    access_token = auth_config['access_token']
    access_token_secret = auth_config['access_token_secret']
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    tweepy_api = tweepy.API(auth)
    
    return tweepy_api

def get_screen_name():
    auth_config = get_auth_config()
    screen_name = auth_config['screen_name']
    
    return screen_name