from dotenv import load_dotenv
import os

load_dotenv()

actual_phone = os.getenv("USER_PHONE_NUM")
auth_user_phone = os.getenv("AUTH_USER")
screenshots_folder = os.getenv("SCREENS_PATH")
cookie_path = os.getenv("COOKIE_PATH")
