import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')

load_dotenv(dotenv_path)

AP = os.environ.get("API_KEY")

ARXIV_API_KEY = os.environ.get("ARXIV_API_KEY")
IEEE_API_KEY = os.environ.get("IEEE_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

SKYPE_USERNAME = os.environ.get("SKYPE_USERNAME")
SKYPE_PASSWORD = os.environ.get("SKYPE_PASSWORD")
SKYPE_GROUP_ID = os.environ.get("SKYPE_GROUP_ID")
