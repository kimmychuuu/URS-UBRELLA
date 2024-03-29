import serial
import RPi.GPIO as GPIO
import time
import tkinter.simpledialog as simpledialog
import threading

from .sim808 import Sim808
from .database_api import DatabaseApi
from .utils import machineutils
from inputimeout import inputimeout
from datetime import datetime, timedelta

class Machine:


    def __init__(self, 
                 arduino_port: str, 
                 sim808_port: str, 
                 api_url: str, 
                 api_key: str, 
                 hardware_callbacks: str = 'gpio'):
        '''
        Initialize the main machine class

        Parameters:
        arduino_port (str) : Port of Arduino UNO
        sim808_port (str) : Port of GSM SIM808
        api_url (str) : Database API base url
        api_key (str) : API key
        '''
        self.arduino = serial.Serial(arduino_port, 9600, timeout=1)
        self.available_commands = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10]
        self.inserted_coins = 0

        coin_pin = 7
        self.accepting_coin = False
        self.sleep_after_command = 1
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(coin_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        if hardware_callbacks == 'gpio':
            GPIO.add_event_detect(coin_pin, GPIO.BOTH, callback=self._increment_inserted_coin, bouncetime=500)
        elif hardware_callbacks == 'thread':
            GPIO.add_event_detect(coin_pin, GPIO.RISING)
            threading.Thread(target=self._watch_coin_event, args=(coin_pin,)).start()
        else:
            raise Exception('Invalid hardware callback priority value')

        self.sim808 = Sim808(sim808_port)
        self.database = DatabaseApi(api_url, api_key)

        self.user = None



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
                    time.sleep(self.sleep_after_command)
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

        distance = 1000
        self.send_command(commands[str(ultrasonic_number)])
        while True:
            response = self.get_arduino_response()
            if response:
                try:
                    distance = float(response)
                    break
                except:
                    pass    

        return distance
    


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



    def tone(self):
        '''
        Explicit function for buzzer in arduino
        '''
        self.send_command(10)



    #################################################
    #                                               #
    #             COIN SLOT FUNCTIONS               #
    #                                               #
    #################################################


    def _increment_inserted_coin(self, channel):
        '''
        Used as callback for event detection of coin sensor
        (For GPIO)
        '''
        if self.accepting_coin:
            self.inserted_coins += 1



    def _watch_coin_event(self, coin_pin):
        '''
        Used as callback for event detection of coin sensor
        (For thread)
        '''
        while True:
            if self.accepting_coin and GPIO.event_detected(coin_pin):
                self.inserted_coins += 1

    
    def reset_inserted_coins(self):
        '''
        Reset inserted_coins to 0.
        Usually called after reset
        '''
        self.inserted_coins = 0



    def accept_coin(self, enable: bool):
        '''
        Toggle machine coin acceptor.
        If off, inserted coins are not counted

        Parameters:
        enable (bool) : Accept coins or not
        '''
        self.accepting_coin = enable

    

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
    


    def check_availability(self, user_id: str = None, umbrella_uuid: str = None) -> bool:
        '''
        Check if user is available to rent or not

        Parameters:
        user_id (str) : User ID
        umbrella_uuid (str) : Umbrella UUID

        Returns:
        availability (bool) : Available or not
        '''
        return self.database.check_availability(user_id=user_id, umbrella_uuid=umbrella_uuid)
    


    def get_latest_transaction(self, user_id: str = None, umbrella_uuid: str = None) -> dict:
        '''
        Get users latest transaction

        Parameters:
        user_id (str) : User ID

        Returns:
        transaction (dict) : Transaction Details
        '''
        return self.database.get_latest_transaction(user_id=user_id, umbrella_uuid=umbrella_uuid)



    def compute_rent_fee(self,
                         start: datetime, 
                         end: datetime, 
                         rate: float = 5,
                         deposit_amount: float = 5,
                         excluded_start: str  = '',
                         excluded_end: str = ''):
        '''
        Compute rent fee from start to end based on rate.
        End should be later than start

        Parameters:
        start (datetime.datetime) : Start datetime
        end (datetime.datetime) : End datetime
        rate (float) : Rate per hour
        excluded_start (str) : Excluded start time (24h-format)
        excluded_end (str) : Excluded end time (24h-format)

        Return:
        rent (float) : Base rent
        '''
        if start > end:
            raise Exception('Invalid datetime ranges')
        
        excluded_start_time = None
        excluded_end_time = None
        if excluded_start or excluded_end:
            if not excluded_start or not excluded_end:
                raise Exception('Excluded range is required')
            
            excluded_start_time = datetime.strptime(excluded_start, '%H:%M').time()
            excluded_end_time = datetime.strptime(excluded_end, '%H:%M').time()
                
        duration = end - start
        if excluded_start_time and excluded_end_time:
            current_datetime = start
            duration = timedelta()

            while current_datetime < end:
                current_end_time = min(current_datetime + timedelta(hours=1), end)
                current_duration = current_end_time - current_datetime
                current_time = current_datetime.strftime('%H:%M')
                if not machineutils.time_falls_between(current_time, excluded_start, excluded_end):
                    duration += current_duration
                current_datetime += timedelta(hours=1)

        hours_rented, remaining_minutes = divmod(duration.total_seconds(), 3600) 
        remaining_minutes //= 60
        rent = hours_rented * rate
        if remaining_minutes >= 15:
            rent += rate
        # Has deposit
        rent -= deposit_amount
        return rent.__floor__()
    


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
        return self.database.add_balance(user_id, amount)



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
    


    def rent_umbrella(self, user_id: str, umbrella_uuid: str, rented_at: datetime):
        '''
        Save rent transaction

        Parameter:
        user_id (str) : User ID
        umbrella_uuid (str) : Umbrella UUID
        rented_at (datetime.datetime) : Datetime rented
        '''
        return self.database.rent_umbrella(user_id, umbrella_uuid, rented_at)
    


    def return_umbrella(self, user_id: str, 
                        returned_at: datetime, 
                        rent_fee: float, 
                        damage_fee: float,
                        damage_rating: str):
        '''
        Save return transaction

        Parameter:
        user_id (str) : User ID
        returned_at (datetime.datetime) : Datetime returned
        rent_fee (float) : Base rent fee
        damage_fee (float) : Additional damage fee
        damage_rating (str) : Damage rating / level
        '''
        return self.database.return_umbrella(user_id, returned_at, rent_fee, damage_fee, damage_rating)



    def confirm_umbrella(self, user_id: str, umbrella_uuid: str):
        '''
        Check if umbrella matched to pending transaction

        Parameter:
        user_id (str) : User ID
        umbrella_uuid (str) : Umbrella UUID
        '''
        return self.database.confirm_umbrella(user_id, umbrella_uuid)


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
    #                OTHER FUNCTIONS                #
    #                                               #
    #################################################


    def scan_qrcode(self, gui: bool = False, wait_time: float = 0):
        '''
        Scan QRCode. Wait time indicates timeout.
        If timeout is <= 0, wait indefinitely

        Parameters:
        gui (bool) : GUI mode (default to False)
        wait_time (float) : Timeout

        Returns:
        data (str) : QRCode data
        '''
        qrcode = ''
        if wait_time <= 0:
            if gui:
                qrcode = simpledialog.askstring('QR Scanner', 'Scan QR Code')
            else:
                qrcode = str(input('QR Scanner: '))
        else:
            try:
                qrcode = inputimeout(prompt='QR Scanner', timeout=wait_time)
            except:
                qrcode = ''
        return qrcode



    def set_current_user(self, user_id):
        '''
        Set current user to user ID
        '''
        self.user = user_id



    def logout(self):
        '''
        Set user to None
        '''
        self.user = None
