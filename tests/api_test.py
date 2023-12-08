import sys
sys.path.append('../')

import urs_umbrella
import os
import unittest
import time

from dotenv import load_dotenv
from datetime import datetime

class ApiTest(unittest.TestCase):
    
    def setUp(self) -> None:
        super().setUp()


    
    def test_1_validate_user(self):
        load_dotenv()
        api_endpoint = os.getenv('api_url')
        api_key = os.getenv('api_key')
        database = urs_umbrella.database_api.DatabaseApi(api_endpoint, api_key)
        validity = database.validate_user('TEST0001')
        self.assertEqual(validity, True)



    def test_2_get_data(self):
        load_dotenv()
        api_endpoint = os.getenv('api_url')
        api_key = os.getenv('api_key')
        database = urs_umbrella.database_api.DatabaseApi(api_endpoint, api_key)
        data = database.get_data('TEST0001')
        expected_output = {
            'id': 1, 
            'first_name': 'Test', 
            'middle_name': '', 
            'last_name': 'User', 
            'extension_name': None, 
            'id_number': 'TEST0001', 
            'address': None, 
            'campus': 'Boac (Main)', 
            'department': 'BS Computer Engineering', 
            'year_lvl': '4', 
            'balance': '0.00', 
            'email': 'testusers@gmail.com', 
            'email_verified_at': None, 
            'created_at': '2023-11-14T02:36:42.000000Z', 
            'updated_at': '2023-11-14T02:36:41.000000Z', 
            'deleted_at': None
        }
        for key in data.keys():
            self.assertEqual(data[key], expected_output[key])



    def test_3_check_availability(self):
        load_dotenv()
        api_endpoint = os.getenv('api_url')
        api_key = os.getenv('api_key')
        database = urs_umbrella.database_api.DatabaseApi(api_endpoint, api_key)
        try:
            database.check_availability('TEST0001')
        except Exception:
            self.fail()



    def test_4_transaction_process(self):
        load_dotenv()
        api_endpoint = os.getenv('api_url')
        api_key = os.getenv('api_key')
        database = urs_umbrella.database_api.DatabaseApi(api_endpoint, api_key)
        available = database.check_availability('TEST0001')
        if not available:
            database.return_umbrella('TEST0001', datetime.now(), 5, 0)
        available = database.check_availability('TEST0001')
        self.assertEqual(available, True)
        time.sleep(5)
        try:
            database.rent_umbrella('TEST0001', datetime.now())
        except:
            self.fail()
        time.sleep(5)
        available = database.check_availability('TEST0001')
        self.assertEqual(available, False)
        try:
            database.return_umbrella('TEST0001', datetime.now(), 5, 0)
        except:
            self.fail()
        time.sleep(5)
        available = database.check_availability('TEST0001')
        self.assertEqual(available, True)



    def test_validate_user_not_found(self):
        load_dotenv()
        api_endpoint = os.getenv('api_url')
        api_key = os.getenv('api_key')
        database = urs_umbrella.database_api.DatabaseApi(api_endpoint, api_key)
        with self.assertRaises(Exception) as context:
            database.check_availability('TEST0002')

        exception = context.exception
        self.assertEqual(str(exception), 'USER_NOT_FOUND')


if __name__ == '__main__':
    unittest.main()