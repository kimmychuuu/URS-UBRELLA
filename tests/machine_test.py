import urs_umbrella
import os
import unittest
import time

from dotenv import load_dotenv
from datetime import datetime

class MachineTest(unittest.TestCase):
    

    def setUp(self) -> None:
        return super().setUp()
    


    def test_1(self):
        load_dotenv()
        arduino_port = os.getenv('arduino_port')
        sim808_port = os.getenv('sim808_port')
        api_endpoint = os.getenv('api_url')
        api_key = os.getenv('api_key')
        machine = urs_umbrella.Machine(arduino_port, sim808_port, api_endpoint, api_key)
    

if __name__ == '__main__':
    unittest.main()