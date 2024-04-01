from dotenv import load_dotenv
import os

load_dotenv()
access_token = os.getenv("ACCESS_TOKEN")
session_cookie = os.getenv("SESSION_COOKIE")
screenshots_folder = os.path.abspath("C:\\Users\\agafo\\PycharmProjects\\Tele2\\screens")
