from dotenv import load_dotenv
import os

load_dotenv()
access_token = os.getenv("ACCESS_TOKEN")
user_phone = os.getenv("USER_PHONE_NUM")
screenshots_folder = os.path.abspath("C:\\Users\\agafo\\PycharmProjects\\Tele2\\screens")
token_folder = os.getenv("ENVIRONMENT_FOLDER")
