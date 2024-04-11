from dotenv import load_dotenv
import os

load_dotenv('.env')
access_token = os.getenv("ACCESS_TOKEN")

load_dotenv('data.env')
user_phone = os.getenv("USER_PHONE_NUM")
auth_user_phone = os.getenv("AUTH_USER")
screenshots_folder = os.path.abspath(os.getenv("SCREENS_PATH"))
