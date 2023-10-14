#pip install guizero
from guizero import App, Text, ButtonGroup, PushButton
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

#import RPi.GPIO as GPIO
#coinPin = 10
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(coinPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.add_event_detect(coinPin, GPIO.FALLING)

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
    
    coin_title.value = "Please Insert Coin(s)"
    
    while(payment < Fee):
        coin_amount.value = "PHP " + str(payment) + " / " + str(Fee)
        if(test):
            payment += int(input("Coin Acceptor: "))
            print("payment: " + str(payment) + "/" + str(Fee))
        else:
            if(GPIO.event_detected(coinPin)):
                payment += 1
                print("payment: " + str(payment) + "/" + str(Fee))
    
    coin_title.value = ""
    coin_amount.value = "PHP " + str(payment) + " inserted"
    sleep(1)
    return int(payment)

def damage_choices(vis):
    if(vis==1):
        text_dmg_handle.value = "Handle Damage: "
        text_dmg_canopy.value = "Canopy Damage: "
        text_dmg_frame.value = "Frame Damage: "
        text_dmg_runner.value = "Runner Damage: "
        text_dmg_rib.value = "Rib Damage: "
        text_dmg_button.value = "Button Damage: "
        text_dmg_shaft.value = "Shaft Damage: "
        
        choice_dmg_handle.show()
        choice_dmg_canopy.show()
        choice_dmg_frame.show()
        choice_dmg_runner.show()
        choice_dmg_rib.show()
        choice_dmg_button.show()
        choice_dmg_shaft.show()
        
        btn_continue.show()
    else:
        text_dmg_handle.value = ""
        text_dmg_canopy.value = ""
        text_dmg_frame.value = ""
        text_dmg_runner.value = ""
        text_dmg_rib.value = ""
        text_dmg_button.value = ""
        text_dmg_shaft.value = ""
            
        choice_dmg_handle.hide()
        choice_dmg_canopy.hide()
        choice_dmg_frame.hide()
        choice_dmg_runner.hide()
        choice_dmg_rib.hide()
        choice_dmg_button.hide()
        choice_dmg_shaft.hide()
        
        btn_continue.hide()

def checkUmbrellaDamage():
    dmg_handle = 0
    dmg_canopy = 0
    dmg_frame = 0
    dmg_runner = 0
    dmg_rib = 0
    dmg_button = 0
    dmg_shaft = 0
    
    damageFee = 0
    
    damage_choices(1)
    pressed=0
    while(pressed==0):
        pressed=0
        app.update()
        prev_state = int(btn_continue.value)
        sleep(0.1)
        app.update()
        curr_state = int(btn_continue.value)
        if(prev_state==1 and curr_state==0):
            print("pressed")
            pressed=1
        

    
    #if(test):
     #   dmg_handle = int(input("Handle Damage(0-3): "))
     #   dmg_canopy = int(input("Canopy Damage(0-3): "))
     #   dmg_frame = int(input("Frame Damage(0-3): "))
     #   dmg_runner = int(input("Runner Damage(0-3): "))
     #   dmg_rib = int(input("Rib Damage(0-3): "))
     #   dmg_button = int(input("Button Damage(0-3): "))
     #   dmg_shaft = int(input("Shaft Damage(0-3): "))
    
    print("choice_dmg_handle: " + str(choice_dmg_handle.value_text))
    print("choice_dmg_canopy: " + str(choice_dmg_canopy.value_text))
    print("choice_dmg_frame: " + str(choice_dmg_frame.value_text))
    print("choice_dmg_runner: " + str(choice_dmg_runner.value_text))
    print("choice_dmg_rib: " + str(choice_dmg_rib.value_text))
    print("choice_dmg_button: " + str(choice_dmg_button.value_text))
    print("choice_dmg_shaft: " + str(choice_dmg_shaft.value_text))
    
    if(choice_dmg_handle.value_text == "1"):
        damageFee += 1
    elif(choice_dmg_handle.value_text == "2"):
        damageFee += 2
    elif(choice_dmg_handle.value_text == "3"):
        damageFee += 3
    
    if(choice_dmg_canopy.value_text == "1"):
        damageFee += 1
    elif(choice_dmg_canopy.value_text == "2"):
        damageFee += 2
    elif(choice_dmg_canopy.value_text == "3"):
        damageFee += 3
    
    if(choice_dmg_frame.value_text == "1"):
        damageFee += 1
    elif(choice_dmg_frame.value_text == "2"):
        damageFee += 2
    elif(choice_dmg_frame.value_text == "3"):
        damageFee += 3
    
    if(choice_dmg_runner.value_text == "1"):
        damageFee += 1
    elif(choice_dmg_runner.value_text == "2"):
        damageFee += 2
    elif(choice_dmg_runner.value_text == "3"):
        damageFee += 3
    
    if(choice_dmg_rib.value_text == "1"):
        damageFee += 1
    elif(choice_dmg_rib.value_text == "2"):
        damageFee += 2
    elif(choice_dmg_rib.value_text == "3"):
        damageFee += 3
    
    if(choice_dmg_button.value_text == "1"):
        damageFee += 1
    elif(choice_dmg_button.value_text == "2"):
        damageFee += 2
    elif(choice_dmg_button.value_text == "3"):
        damageFee += 3
    
    if(choice_dmg_shaft.value_text == "1"):
        damageFee += 1
    elif(choice_dmg_shaft.value_text == "1"):
        damageFee += 2
    elif(choice_dmg_shaft.value_text == "1"):
        damageFee += 3
        
    return damageFee
    
def checkout(dmg_fee, startTime, endTime):
    #startTime = datetime.strptime(startTime, "%d/%m/%y %H:%M:%S")
    endTime = datetime.strptime(endTime, "%d/%m/%y %H:%M:%S")
    delta = endTime - startTime
    print("(checkout) delta: " + str(delta))
        
    rentHours = delta.total_seconds() // (60*60)
    rentMin = delta.total_seconds() % (60*60)
    rentMin = rentMin // 60

    rent_hours.value = "Rent Duration: " + str(rentHours) + " hrs " + str(rentMin) + " mins"
    rent_endTime.value = "End Time: " + str(endTime)
    
    print("(checkout) startTime: " + str(startTime))
    print("(checkout) endTime: " + str(endTime))
    print("(checkout) rentHours: " + str(rentHours))
    print("(checkout) rentMinutes: " + str(rentMin))
    
    if(rentMin > 10):
        rentHours += 1
        
    rentFee = rentHours * 5
    
    print("(checkout) rentFee: " + str(rentFee))
    print("(checkout) dmg_fee: " + str(dmg_fee))
    
    rent_fee.value = "Rent Fee: PHP " + str(rentFee)
    rent_dmg.value = "Damage Fee: PHP " + str(dmg_fee)
    
    totalFee = rentFee + dmg_fee
    print("(checkout) totalFee: " + str(totalFee))
    
    return totalFee
    
        
        
#ARDUINO COMMANDS
#import serial
#ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

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

app = App(title="Umbrella",height=760, width=800, layout="grid")
title_msg = Text(app, text="", grid=[0,0], align="top", size=30, font="Times New Roman", color="Black")
display_msg = Text(app, text="", grid=[0,1], align="left", size=20, font="Times New Roman")

std_status = Text(app, text="", grid=[0,2], align="left", size=15, font="Times New Roman")
std_bal = Text(app, text="", grid=[0,3], align="left", size=15, font="Times New Roman")
std_startTime = Text(app, text="", grid=[0,4], align="left", size=15, font="Times New Roman")

rent_hours = Text(app, text="", grid=[1,1], align="left", size=15, font="Times New Roman")
rent_fee = Text(app, text="", grid=[1,2], align="left", size=15, font="Times New Roman")
rent_dmg = Text(app, text="", grid=[1,3], align="left", size=15, font="Times New Roman")
rent_endTime = Text(app, text="", grid=[1,4], align="left", size=15, font="Times New Roman")

coin_title = Text(app, text="", grid=[0,5], align="left", size=30, font="Times New Roman")
coin_amount = Text(app, text="", grid=[0,6], align="left", size=15, font="Times New Roman")

umbrella_title = Text(app, text="", grid=[0,7], align="left", size=30, font="Times New Roman")
umbrella_msg = Text(app, text="", grid=[0,8], align="left", size=15, font="Times New Roman")

text_dmg_handle = Text(app, text="", grid=[0,9], align="left", size=15, font="Times New Roman")
text_dmg_canopy = Text(app, text="", grid=[0,10], align="left", size=15, font="Times New Roman")
text_dmg_frame = Text(app, text="", grid=[0,11], align="left", size=15, font="Times New Roman")
text_dmg_runner = Text(app, text="", grid=[0,12], align="left", size=15, font="Times New Roman")
text_dmg_rib = Text(app, text="", grid=[0,13], align="left", size=15, font="Times New Roman")
text_dmg_button = Text(app, text="", grid=[0,14], align="left", size=15, font="Times New Roman")
text_dmg_shaft = Text(app, text="", grid=[0,15], align="left", size=15, font="Times New Roman")

choice_dmg_handle = ButtonGroup(app, grid=[1,9], horizontal=True,options=["0", "1", "2", "3"], selected="0")
choice_dmg_canopy = ButtonGroup(app, grid=[1,10], horizontal=True,options=["0", "1", "2", "3"], selected="0")
choice_dmg_frame = ButtonGroup(app, grid=[1,11], horizontal=True,options=["0", "1", "2", "3"], selected="0")
choice_dmg_runner = ButtonGroup(app, grid=[1,12], horizontal=True,options=["0", "1", "2", "3"], selected="0")
choice_dmg_rib = ButtonGroup(app, grid=[1,13], horizontal=True,options=["0", "1", "2", "3"], selected="0")
choice_dmg_button = ButtonGroup(app, grid=[1,14], horizontal=True,options=["0", "1", "2", "3"], selected="0")
choice_dmg_shaft = ButtonGroup(app, grid=[1,15], horizontal=True,options=["0", "1", "2", "3"], selected="0")

btn_continue = PushButton(app, grid=[1,16], text="Continue")

damage_choices(0)

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
    
    damage_choices(0)
    
    rent_hours.value = ""
    rent_fee.value = ""
    rent_dmg.value = ""
    rent_endTime.value = ""

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
            amountInsert = insertCoin(stdBal, 5)
            print("amountInsert Final: " + str(amountInsert))            
            
            now = datetime.now()
            startTime = now.strftime("%d/%m/%y %H:%M:%S")
            #sendArduinoDispense()
            
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
            umbrella_title.value = "Please Scan Umbrella QR..."
            scanCode = scanQR()
            umbrella_msg.value = "Umbrella ID: " + str(scanCode)
            
            umbrella_title.value = "Verifying QR..."
            while(isUmbrella(scanCode)==0):
                print("\nPlease Scan Umbrella QR..")
                umbrella_title.value = "Please Scan Umbrella QR..."
                scanCode = scanQR() 
                umbrella_msg.value = "Umbrella ID: " + str(scanCode)  
            umbrella_title.value = "Umbrella QR Code Accepted"
            
            dmg_fee = checkUmbrellaDamage()
            print("Return Umbrella")
            #readArduino()
            now = datetime.now()
            endTime = now.strftime("%d/%m/%y %H:%M:%S")
            totalFee = checkout(dmg_fee, startTime, endTime)
            amountInsert = insertCoin(stdBal, totalFee)
            insertDBReturn(stdID, 0, endTime, scanCode)
    else:
        title_msg.value = "Student Verification Failed"
        print("Student Verification Failed")
        
    
    print("\nThank You for Using Umbrella Rent..")
    sleep(3)
    resetGUI()
    title_msg.value = "Transaction Complete"
    app.update()
    sleep(3)
    resetGUI()

app.display()
    
