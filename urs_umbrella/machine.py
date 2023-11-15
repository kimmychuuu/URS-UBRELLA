import serial
import RPi.GPIO as GPIO
import datetime

from .sim808 import Sim808
from .database_api import DatabaseApi
from inputimeout import inputimeout

class Machine:


    def __init__(self, arduino_port: str, sim808_port: str, api_url: str, api_key: str):
        '''
        Initialize the main machine class

        Parameters:
        arduino_port (str) : Port of Arduino UNO
        sim808_port (str) : Port of GSM SIM808
        api_url (str) : Database API base url
        api_key (str) : API key
        '''
        self.arduino = serial.Serial(arduino_port, 9600, timeout=1)
        self.available_commands = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.inserted_coins = 0

        coin_pin = 10
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(coin_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(coin_pin, GPIO.FALLING, callback=self._increment_inserted_coin, bouncetime=500)

        self.sim808 = Sim808(sim808_port)
        self.database = DatabaseApi(api_url, api_key)



    def send_command(self, command: int):
        '''
        Send command to arduino. 
        Can be used to explicitly invoke Arduino operation without calling specific functions \n

        Parameters:
        command (int) : Command to send
        '''
        if(command in self.available_commands):
            while True:
                self.arduino.write(bytes(str(command)+'\n','utf-8'))
                response = self.get_arduino_response()
                if(response == 'ok'):
                    break
        else:
            raise Exception('Unknown command')



    #################################################
    #                                               #
    #               ARDUINO FUNCTIONS               #
    #                                               #
    #################################################



    def get_arduino_response(self) -> str:
        '''
        Get arduino serial response

        Returns:
        response (str) : Arduino response
        '''
        try:
            response = self.arduino.readline().decode('utf-8').rstrip()
        except UnicodeDecodeError:
            response = self.arduino.readline().decode('utf-8').rstrip()
        return response
    


    def get_distance_from_ultrasonic(self, ultrasonic_number: int) -> float:
        '''
        Get distance from specific ultrasonic number
        '''
        available_ultrasonics_sensor = [1, 2, 3, 4]
        if ultrasonic_number not in available_ultrasonics_sensor:
            raise Exception('Ultrasonic not available')
        
        commands = {
            '1': 0,
            '2': 1,
            '3': 2,
            '4': 3,
        }

        self.send_command(commands[str(ultrasonic_number)])
        while True:
            response = self.get_arduino_response()
            if response:
                break

        return float(response)
    


    def start_motor(self):
        '''
        Explicit function for starting motor in arduino
        '''
        self.send_command(4)

    

    def stop_motor(self):
        '''
        Explicit function for stopping motor in arduino
        '''
        self.send_command(5)


    
    def open_dispensing_servo(self):
        '''
        Explicit function for opening dispensing servo in arduino
        '''
        self.send_command(6)



    def close_dispensing_servo(self):
        '''
        Explicit function for closing dispensing servo in arduino
        '''
        self.send_command(7)
    


    def open_returning_servo(self):
        '''
        Explicit function for opening returning servo in arduino
        '''
        self.send_command(8)



    def close_returning_servo(self):
        '''
        Explicit function for closing returning servo in arduino
        '''
        self.send_command(9)



    #################################################
    #                                               #
    #             COIN SLOT FUNCTIONS               #
    #                                               #
    #################################################



    def _increment_inserted_coin(self, channel):
        '''
        Used as callback for event detection of coin sensor
        '''
        self.inserted_coins += 1



    def reset_inserted_coins(self):
        '''
        Reset inserted_coins to 0.
        Usually called after reset
        '''
        self.inserted_coins = 0

    

    #################################################
    #                                               #
    #              DATABASE FUNCTIONS               #
    #                                               #
    #################################################



    def validate_user(self, user_id: str) -> bool:
        '''
        Validate a user if account exists

        Parameters:
        user_id (str) : User ID

        Returns:
        valid (bool) : Validity
        '''
        return self.database.validate_user(user_id)



    def get_data(self, user_id: str) -> dict:
        '''
        Get user data

        Parameters:
        user_id (str) : User ID

        Returns:
        data (dict) : User data
        '''
        return self.database.get_data(user_id)
    


    def check_availability(self, user_id: str) -> bool:
        '''
        Check if user is available to rent or not

        Parameters:
        user_id (str) : User ID

        Returns:
        availability (bool) : Available or not
        '''
        return self.database.check_availability(user_id)
    


    def get_balance(self, user_id: str) -> float:
        '''
        Get user balance

        Parameters:
        user_id (str) : User ID

        Returns:
        balance (float) : User available credits
        '''
        return self.database.get_balance(user_id)



    def add_balance(self, user_id: str, amount: float):
        '''
        Add amount to user balance

        Parameters:
        user_id (str) : User ID
        amount (float) : Balance to add
        '''
        return self.database.get_balance(user_id, amount)



    def deduct_balance(self, user_id: str, amount: float):
        '''
        Deduct amount to user balance

        Parameters:
        user_id (str) : User ID
        amount (float) : Balance to deduct
        '''
        return self.database.deduct_balance(user_id, amount)
    


    def update_balance(self, user_id: str, balance: float):
        '''
        Deduct amount to user balance

        Parameters:
        user_id (str) : User ID
        balance (float) : Balance to update
        '''
        return self.database.update_balance(user_id, balance)
    


    def reset_balance(self, user_id: str):
        '''
        Deduct amount to user balance

        Parameters:
        user_id (str) : User ID
        '''
        return self.database.reset_balance(user_id)
    


    def rent_umbrella(self, user_id: str, rented_at: datetime.datetime):
        '''
        Save rent transaction

        Parameter:
        user_id (str) : User ID
        rented_at (datetime.datetime) : Datetime rented
        '''
        return self.database.rent_umbrella(user_id, rented_at)
    


    def return_umbrella(self, user_id: str, 
                        returned_at: datetime.datetime, 
                        rent_fee: float, 
                        damage_fee: float):
        '''
        Save return transaction

        Parameter:
        user_id (str) : User ID
        returned_at (datetime.datetime) : Datetime returned
        rent_fee (float) : Base rent fee
        damage_fee (float) : Additional damage fee
        '''
        return self.database.return_umbrella(user_id, returned_at, rent_fee, damage_fee)



    #################################################
    #                                               #
    #               SIM808 FUNCTIONS                #
    #                                               #
    #################################################



    def send_sms(self, number: str, message: str):
        '''
        Send a SMS message

        Parameters:
        number (str) : Number to send message to. Should contain country code
        message
        '''
        return self.sim808.send_sms(number, message)
    


    #################################################
    #                                               #
    #           QRCODE SCANNER FUNCTIONS            #
    #                                               #
    #################################################



    def scan_qrcode(self, wait_time: float = 0):
        '''
        Scan QRCode. Wait time indicates timeout.
        If timeout is <= 0, wait indefinitely

        Parameters:
        wait_time (float) : Timeout

        Returns:
        data (str) : QRCode data
        '''
        qrcode = ''
        if wait_time <= 0:
            qrcode = str(input('QR Scanner: '))
        else:
            try:
                qrcode = inputimeout(prompt='QR Scanner', timeout=wait_time)
            except:
                qrcode = ''
        return qrcode
