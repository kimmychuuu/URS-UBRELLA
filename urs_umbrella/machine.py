from .sim808 import Sim808

import serial
import RPi.GPIO as GPIO

class Machine:


    def __init__(self, arduino_port: str, sim808_port: str):
        '''
        Initialize the main machine class

        Parameters:
        arduino_port (str) : Port of Arduino UNO
        sim808_port (str) : Port of GSM SIM808
        '''
        self.arduino = serial.Serial(arduino_port, 9600, timeout=1)
        self.available_commands = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.inserted_coins = 0

        coin_pin = 10
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(coin_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(coin_pin, GPIO.FALLING, callback=self._increment_inserted_coin, bouncetime=500)

        self.sim808 = Sim808(sim808_port)



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
    