from utils import confighandler
import datetime

def get_user_info():
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    screen_name = confighandler.get_screen_name()
    tweepy_api = confighandler.get_tweepy_api()
    user_api = tweepy_api.get_user(screen_name=screen_name)
    data = [current_date, user_api.screen_name, user_api.followers_count, user_api.friends_count, user_api.statuses_count]
    
    return data