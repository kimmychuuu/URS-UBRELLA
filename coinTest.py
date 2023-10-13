#pip install rpi.gpio
import RPi.GPIO as GPIO
from time import sleep

coinPin = 10
GPIO.setmode(GPIO.BOARD)
GPIO.setup(coinPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def insertCoin():
    amountInsert = 0
    while(amountInsert < 5):
        if(GPIO.event_detected(coinPin)):
            amountInsert += 1
            print("amountInsert: " + str(amountInsert))
    return int(amountInsert)
            
 
GPIO.add_event_detect(coinPin, GPIO.FALLING)

while(True):
    print("Please Insert Coin")
    amountInsert = insertCoin()
    print("amountInsert Final: " + str(amountInsert))
    sleep(1)