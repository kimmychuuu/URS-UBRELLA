#pip install guizero
from guizero import App, Text
from time import sleep
from datetime import datetime

test = 1

#Database Methods
def checkWebConnection():
    if(test):
        status = str(input("(TEST)checkWebConnection: "))
    else:
        status = 0
    print("(checkWebConnection) status: " + status)
    return int(status)

def checkDBConnection():
    if(test):
        status = (input("(TEST)checkDBConnection: "))
    else:
        status = 0
    print("(checkDBConnection) status: " + str(status))
    return int(status)

def checkStudentListFromDB(code):
    print("(checkStudentListFromDB) checking " + code)
    if(test):
        status = str(input("(TEST)checkStudentListFromDB: "))
    else:
        status = 0
    print("(checkStudentListFromDB) " + status)
    return int(status)

def checkUmbrellaListFromDB(code):
    print("(checkUmbrellaListFromDB) checking " + code)
    if(test):
        status = str(input("(TEST)checkUmbrellaListFromDB: "))
    else:
        status = 0
    print("(checkUmbrellaListFromDB) " + status)
    return int(status)
    
def getStudentRentData(code):
    print("(getStudentRentData) Start")
    
    if(test):
        stdStatus = int(input("(TEST)getStudentRentData stdStatus: "))
        stdBal = int(input("(TEST)getStudentRentData stdBal: "))
        startTime = str(input("(TEST)getStudentRentData startTime (DD/MM/YY HH:MM:SS): "))
        if(startTime != ''):
            startTime = datetime.strptime(startTime, "%d/%m/%y %H:%M:%S")
    else:
        stdStatus, stdBal, startTime = 0
        #select stdStatus, stdBal, startTime from StudentDB where sID=code
        
    return code, stdStatus, stdBal, startTime

def insertDBRent(stdID, stdStatus, startTime, scanCode):
    print("(insertDBRent) stdID: " + str(stdID))
    print("(insertDBRent) stdStatus: " + str(stdStatus))
    print("(insertDBRent) startTime: " + str(startTime))
    print("(insertDBRent) scanCode: " + str(scanCode))
    if(test):
        print("(test) insert query executed")
    else:
        #do insert query here
        print("")
        
def insertDBReturn(stdID, stdStatus, endTimeTime, scanCode):
    print("(insertDBReturn) stdID: " + str(stdID))
    print("(insertDBReturn) stdStatus: " + str(stdStatus))
    print("(insertDBReturn) endTimeTime: " + str(endTimeTime))
    print("(insertDBReturn) scanCode: " + str(scanCode))
    if(test):
        print("(test) insert query executed")
    else:
        #do insert query here
        print("")
        
#Hardware Methods

#QR Code Scanner
def scanQR():
    print("(scanQR) start")
    scode = str(input("QR Scanner: "))
    print("(scanQR) Scanned Barcode: " + scode)
    sleep(1)
    return scode

#Coin Acceptor
#pip install rpi.gpio

if(test==0):
    import RPi.GPIO as GPIO
    coinPin = 10
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(coinPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(coinPin, GPIO.FALLING)


#Utilities
def isStudent(code):
    if(checkStudentListFromDB(code)):
        print("(isStudent) Student Scanned Valid")
        return 1
    else:
        print("(isStudent) Not in List")
        return 0

def isUmbrella(code):
    if(checkUmbrellaListFromDB(code)):
        print("(isUmbrella) Umbrella Scanned Valid")
        return 1
    else:
        print("(isUmbrella) Not in List")
        return 0

def insertCoin(stdBal, Fee):
    amountInsert = 0
    print("(insertCoin) stdBal: " + str(stdBal))
    payment = amountInsert+int(stdBal)
    while(payment < Fee):
        if(test):
            payment += int(input("Coin Acceptor: "))
            print("payment: " + str(payment) + "/" + str(Fee))
        else:
            if(GPIO.event_detected(coinPin)):
                payment += 1
                print("payment: " + str(payment) + "/" + str(Fee))
        coin_amount.value = "PHP " + str(payment)
    return int(payment)
        
def checkUmbrellaDamage():
    dmg_handle = 0
    dmg_canopy = 0
    dmg_frame = 0
    dmg_runner = 0
    dmg_rib = 0
    dmg_button = 0
    dmg_shaft = 0
    
    damageFee = 0
    
    if(test):
        dmg_handle = int(input("Handle Damage(0-3): "))
        dmg_canopy = int(input("Canopy Damage(0-3): "))
        dmg_frame = int(input("Frame Damage(0-3): "))
        dmg_runner = int(input("Runner Damage(0-3): "))
        dmg_rib = int(input("Rib Damage(0-3): "))
        dmg_button = int(input("Button Damage(0-3): "))
        dmg_shaft = int(input("Shaft Damage(0-3): "))
    
    if(dmg_handle == 1):
        damageFee += 10
    elif(dmg_handle == 2):
        damageFee += 20
    elif(dmg_handle == 3):
        damageFee += 30
    
    if(dmg_canopy == 1):
        damageFee += 10
    elif(dmg_canopy == 2):
        damageFee += 20
    elif(dmg_canopy == 3):
        damageFee += 30
    
    if(dmg_frame == 1):
        damageFee += 10
    elif(dmg_frame == 2):
        damageFee += 20
    elif(dmg_frame == 3):
        damageFee += 30
    
    if(dmg_runner == 1):
        damageFee += 10
    elif(dmg_runner == 2):
        damageFee += 20
    elif(dmg_runner == 3):
        damageFee += 30
    
    if(dmg_rib == 1):
        damageFee += 10
    elif(dmg_rib == 2):
        damageFee += 20
    elif(dmg_rib == 3):
        damageFee += 30
    
    if(dmg_button == 1):
        damageFee += 10
    elif(dmg_button == 2):
        damageFee += 20
    elif(dmg_button == 3):
        damageFee += 30
    
    if(dmg_shaft == 1):
        damageFee += 10
    elif(dmg_shaft == 2):
        damageFee += 20
    elif(dmg_shaft == 3):
        damageFee += 30
        
    return damageFee
    
def checkout(dmg_fee, startTime, endTime):
    #startTime = datetime.strptime(startTime, "%d/%m/%y %H:%M:%S")
    endTime = datetime.strptime(endTime, "%d/%m/%y %H:%M:%S")
    delta = endTime - startTime
    print("(checkout) delta: " + str(delta))
        
    rentHours = delta.total_seconds() // (60*60)
    rentMin = delta.total_seconds() % (60*60)
    if(rentMin > 10):
        rentHours += 1
    
    print("(checkout) startTime: " + str(startTime))
    print("(checkout) endTime: " + str(endTime))
    print("(checkout) rentHours: " + str(rentHours))
    
    rentFee = rentHours * 5
    print("(checkout) rentFee: " + str(rentFee))
    print("(checkout) dmg_fee: " + str(dmg_fee))
    
    totalFee = rentFee + dmg_fee
    print("(checkout) totalFee: " + str(totalFee))
    
    return totalFee
    
        
        
#ARDUINO COMMANDS
import serial
ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)

def sendArduinoDispense():
    print("sending arduino dispense command")
    toSend = "d"
    toSend = toSend.encode()
    ser.write(toSend)
    sleep(1)
    
def readArduino():
    print("readArduino Ultrasonic sensor")
    print("sending arduino dispense command")
    toSend = "r"
    toSend = toSend.encode()
    ser.write(toSend)
    
    #Arduino reply for Ultrasonic
    
    sleep(1)


#main Methods
def initialize():
    while(checkDBConnection()==0):
        print("(initialize): Trying to Connect to DB..")
        sleep(3)


initialize()

app = App(title="Umbrella",height=800, width=600, layout="grid")
title_msg = Text(app, text="", grid=[0,0], align="top", size=40, font="Times New Roman", color="Black")
display_msg = Text(app, text="", grid=[0,1], align="left", size=20, font="Times New Roman")

std_status = Text(app, text="", grid=[0,3], align="left", size=15, font="Times New Roman")
std_bal = Text(app, text="", grid=[0,4], align="left", size=15, font="Times New Roman")
std_startTime = Text(app, text="", grid=[0,5], align="left", size=15, font="Times New Roman")

coin_title = Text(app, text="", grid=[0,7], align="left", size=40, font="Times New Roman")
coin_amount = Text(app, text="", grid=[0,8], align="left", size=15, font="Times New Roman")

umbrella_title = Text(app, text="", grid=[0,9], align="left", size=40, font="Times New Roman")
umbrella_msg = Text(app, text="", grid=[0,10], align="left", size=15, font="Times New Roman")

def resetGUI():
    title_msg.value = ""
    display_msg.value = ""
    std_status.value = ""
    std_bal.value = ""
    std_startTime.value = ""
    coin_title.value = ""
    coin_amount.value = ""
    umbrella_title.value = ""
    umbrella_msg.value = ""

while(True):
    title_msg.value = "Please Scan Student ID..."
    print("\nPlease Scan Student ID..")
    scanCode = scanQR()
    title_msg.value = "Verifying ID..."
    display_msg.value = "Student ID: " + str(scanCode)
    
    if(isStudent(scanCode)):
        title_msg.value = "Student ID Verified"
        stdID, stdStatus, stdBal,startTime = getStudentRentData(scanCode)
        print("Rent Status: " + str(stdStatus))
        print("Rent Balance: " + str(stdBal))
        print("Rent Start Time: " + str(startTime))
        
        std_status.value = "Rent Status: " + str(stdStatus)
        std_bal.value = "Rent Balance: " + str(stdBal)
        std_startTime.value = "Rent Start Time: " + str(startTime)
        
        #No Umbrella Rent
        if(stdStatus==0):
            coin_title.value = "Please Insert Coin(s)"
            amountInsert = insertCoin(stdBal, 5)
            print("amountInsert Final: " + str(amountInsert))
            coin_title.value = ""
            coin_amount.value = "PHP " + str(amountInsert) + " inserted"
            
            
            now = datetime.now()
            startTime = now.strftime("%d/%m/%y %H:%M:%S")
            sendArduinoDispense()
            
            std_startTime.value = "Rent Start Time: " + str(startTime)
            
            print("\nPlease Scan Umbrella QR..")
            umbrella_title.value = "Please Scan Umbrella QR..."
            scanCode = scanQR()
            umbrella_msg.value = "Umbrella ID: " + str(scanCode)
            
            umbrella_title.value = "Verifying QR..."
            while(isUmbrella(scanCode)==0):
                umbrella_title.value = "Please Scan Umbrella QR.."
                print("\nPlease Scan Umbrella QR..")
                scanCode = scanQR()  
                umbrella_msg.value = "Umbrella ID: " + str(scanCode)
            
            umbrella_title.value = "Umbrella QR Code Accepted"
            insertDBRent(stdID, 1, startTime, scanCode)

                
            sleep(1)
        
        #Existing Umbrella Rent
        elif(stdStatus==1):
            print("\nPlease Scan Umbrella QR..")
            scanCode = scanQR()

            while(isUmbrella(scanCode)==0):
                print("\nPlease Scan Umbrella QR..")
                scanCode = scanQR()   
        
            dmg_fee = checkUmbrellaDamage()
            print("Return Umbrella")
            readArduino()
            now = datetime.now()
            endTime = now.strftime("%d/%m/%y %H:%M:%S")
            totalFee = checkout(dmg_fee, startTime, endTime)
            amountInsert = insertCoin(stdBal, totalFee)
            insertDBReturn(stdID, 0, endTime, scanCode)
    else:
        title_msg.value = "Student Verification Failed"
        print("Student Verification Failed")
        
    
    print("\nThank You for Using Umbrella Rent..")
    resetGUI()
    title_msg.value = "Transaction Complete"
    sleep(3)
    resetGUI()

app.display()
    
