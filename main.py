        
from models import user
from utils import csvhandler

def main():
    user_info_data = user.get_user_info()
    csvhandler.write_to_csv(user_info_data, 'twitter_user_info.csv', 'w')
        
if __name__ == "__main__":
    main()