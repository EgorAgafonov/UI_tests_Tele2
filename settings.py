from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv('email')
password = os.getenv('pass')
invalid_email = os.getenv('invalid_email')
invalid_password = os.getenv('invalid_pass')

screenshots_folder = os.path.abspath("C:\\Users\\agafo\\PycharmProjects")
