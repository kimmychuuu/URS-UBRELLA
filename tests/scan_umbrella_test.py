import sys
sys.path.append('../')

import urs_umbrella
import os

from dotenv import load_dotenv

load_dotenv()
arduino_port = os.getenv('arduino_port')
sim808_port = os.getenv('sim808_port')
api_endpoint = os.getenv('api_url')
api_key = os.getenv('api_key')

machine = urs_umbrella.Machine(arduino_port, sim808_port, api_endpoint, api_key, hardware_callbacks='thread')

umbrella_id = machine.scan_qrcode()

machine.confirm_umbrella('1','23URS01')
print(machine.confirm_umbrella('1','23URS01'))