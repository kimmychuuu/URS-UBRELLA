import sys
sys.path.append('../')

from urs_umbrella import DatabaseApi
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()
api_endpoint = os.getenv('api_url')
api_key = os.getenv('api_key')

database = DatabaseApi(base_url=api_endpoint, api_key=api_key)

database.rent_umbrella('20B0427', '23URS01', datetime.now())
