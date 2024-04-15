from dotenv import load_dotenv
import os

load_dotenv()

actual_phone = os.getenv("USER_PHONE_NUM")
auth_user_phone = os.getenv("AUTH_USER")
screenshots_folder = os.getenv("SCREENS_PATH")
auth_user_psswrd = os.getenv("USER_PSSWRD_NUM")
cookie_path = os.getenv("COOKIE_PATH")
