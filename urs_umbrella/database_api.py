import requests

from .response_codes import ResponseCodes
from datetime import datetime

class DatabaseApi:
    

    def __init__(self, base_url: str, api_key: str):
        '''
        Initialize an object to call database API \n
        All methods raises an exception on error

        Parameters:
        base_url (str) : Base API endpoint
        api_key (str) : API Key
        '''
        self.base_url = base_url
        self.api_key = api_key

    

    def _validate_result(self, result: dict):
        '''
        Validate result from json response
        '''
        if 'success' not in result.keys():
            raise Exception(ResponseCodes.UNKNOWN_ERROR)
        if not result['success']:
            error_code = result.get('error_code')
            raise Exception(ResponseCodes.get_message(error_code))



    def validate_user(self, user_id: str) -> bool:
        '''
        Validate a user if account exists

        Parameters:
        user_id (str) : User ID

        Returns:
        valid (bool) : Validity
        '''
        response = requests.post(f'{self.base_url}/validateUser', {
            'apiKey': self.api_key,
            'idNumber': user_id,
        })

        result = response.json()
        try:
            self._validate_result(result)
            return True
        except:
            return False
        


    def get_data(self, user_id: str) -> dict:
        '''
        Get user data

        Parameters:
        user_id (str) : User ID

        Returns:
        data (dict) : User data
        '''
        response = requests.post(f'{self.base_url}/getData', {
            'apiKey': self.api_key,
            'idNumber': user_id,
        })
        result = response.json()
        self._validate_result(result)
        return result['data']
    


    def check_availability(self, user_id: str = None, umbrella_uuid: str = None) -> bool:
        '''
        Check if user is available to rent or not

        Parameters:
        user_id (str) : User ID
        umbrella_uuid (str) : Umbrella UUID

        Returns:
        availability (bool) : Available or not
        '''
        initial_params = {
            'idNumber': user_id,
            'umbrellaUUID': umbrella_uuid
        }
        params = {key: value for key, value in initial_params.items() if value is not None}
        response = requests.post(f'{self.base_url}/checkAvailability', {
            'apiKey': self.api_key,
            **params
        })
        result = response.json()
        self._validate_result(result)
        return result['available']
    


    def get_latest_transaction(self, user_id: str = None, umbrella_uuid: str = None) -> dict:
        '''
        Get users latest transaction

        Parameters:
        user_id (str) : User ID

        Returns:
        transaction (dict) : Transaction Details
        '''
        initial_params = {
            'idNumber': user_id,
            'umbrellaUUID': umbrella_uuid
        }
        params = {key: value for key, value in initial_params.items() if value is not None}
        response = requests.post(f'{self.base_url}/getLatestTransaction', {
            'apiKey': self.api_key,
            **params
        })
        result = response.json()
        try:
            self._validate_result(result)
            return result['transaction']
        except:
            return None
    


    def get_balance(self, user_id: str) -> float:
        '''
        Get user balance

        Parameters:
        user_id (str) : User ID

        Returns:
        balance (float) : User available credits
        '''
        response = requests.post(f'{self.base_url}/getBalance', {
            'apiKey': self.api_key,
            'idNumber': user_id,
        })
        result = response.json()
        self._validate_result(result)
        return result['balance']
    


    def add_balance(self, user_id: str, amount: float):
        '''
        Add amount to user balance

        Parameters:
        user_id (str) : User ID
        amount (float) : Balance to add
        '''
        response = requests.patch(f'{self.base_url}/addBalance', {
            'apiKey': self.api_key,
            'idNumber': user_id,
            'amount': amount
        })
        result = response.json()
        self._validate_result(result)



    def deduct_balance(self, user_id: str, amount: float):
        '''
        Deduct amount to user balance

        Parameters:
        user_id (str) : User ID
        amount (float) : Balance to deduct
        '''
        response = requests.patch(f'{self.base_url}/deductBalance', {
            'apiKey': self.api_key,
            'idNumber': user_id,
            'amount': amount
        })
        result = response.json()
        self._validate_result(result)



    def update_balance(self, user_id: str, balance: float):
        '''
        Deduct amount to user balance

        Parameters:
        user_id (str) : User ID
        balance (float) : Balance to update
        '''
        response = requests.patch(f'{self.base_url}/updateBalance', {
            'apiKey': self.api_key,
            'idNumber': user_id,
            'balance': balance
        })
        result = response.json()
        self._validate_result(result)



    def reset_balance(self, user_id: str):
        '''
        Deduct amount to user balance

        Parameters:
        user_id (str) : User ID
        '''
        response = requests.patch(f'{self.base_url}/resetBalance', {
            'apiKey': self.api_key,
            'idNumber': user_id
        })
        result = response.json()
        self._validate_result(result)


    
    def rent_umbrella(self, user_id: str, umbrella_uuid: str, rented_at: datetime):
        '''
        Save rent transaction

        Parameter:
        user_id (str) : User ID
        umbrella_uuid (str) : Umbrella UUID
        rented_at (datetime.datetime) : Datetime rented
        '''
        response = requests.post(f'{self.base_url}/rentUmbrella', {
            'apiKey': self.api_key,
            'idNumber': user_id,
            'rentedAt': rented_at,
            'umbrellaUUID': umbrella_uuid,
        })
        result = response.json()
        self._validate_result(result)



    def return_umbrella(self, user_id: str, returned_at: datetime, rent_fee: float, 
                        damage_fee: float, damage_rating: str):
        '''
        Save return transaction

        Parameter:
        user_id (str) : User ID
        returned_at (datetime.datetime) : Datetime returned
        rent_fee (float) : Base rent fee
        damage_fee (float) : Additional damage fee
        damage_rating (str) : Damage rating / level
        '''
        response = requests.post(f'{self.base_url}/returnUmbrella', {
            'apiKey': self.api_key,
            'idNumber': user_id,
            'returnedAt': returned_at,
            'rentFee': rent_fee,
            'damageFee': damage_fee,
            'damageRating': damage_rating,
        })
        result = response.json()
        self._validate_result(result)



    def confirm_umbrella(self, user_id: str, umbrella_uuid: str):
        '''
        Check if umbrella matched to pending transaction

        Parameter:
        user_id (str) : User ID
        umbrella_uuid (str) : Umbrella UUID
        '''
        response = requests.post(f'{self.base_url}/confirmUmbrella', {
            'apiKey': self.api_key,
            'idNumber': user_id,
            'umbrellaUUID': umbrella_uuid,
        })
        result = response.json()
        try:
            self._validate_result(result)
            return result.get('confirmation')
        except:
            return False
