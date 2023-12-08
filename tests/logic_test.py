import sys
sys.path.append('../')

from urs_umbrella import Machine
from datetime import datetime

machine = Machine(arduino_port='', sim808_port='', api_url='', api_key='')

id_number = machine.scan_qrcode()

# id_number = STUDENT ID

valid = machine.validate_user(id_number)

if not valid:
    print('User not valid')
    exit()

rent_available = machine.check_availability(id_number)

if not rent_available:
    # Handle for returning
    umbrella_uuid = machine.scan_qrcode()
    returned_at = datetime.now()
    rent_date = machine.get_latest_transaction()['rented_at']
    rent_date = datetime.strptime(rent_date, '%Y-%m-%d %H:%M:%S')
    rent_fee = machine.compute_rent_fee(rent_date, returned_at)

    # Handle damage rating
    damage_rating = 'None'
    damage_fee = 0

    total_payment = rent_fee + damage_fee
    while machine.inserted_coins < total_payment:
        pass
    else:
        extra = machine.inserted_coins - total_payment
        machine.add_balance(id_number, extra)
        machine.reset_inserted_coins()

    print('Please return umbrella')
    while machine.get_distance_from_ultrasonic(1) > 30:
        pass
    machine.open_returning_servo()
    machine.start_motor()
    while machine.get_distance_from_ultrasonic(2) > 30:
        pass
    machine.close_returning_servo()
    machine.stop_motor()
    machine.return_umbrella(id_number, returned_at, rent_fee, damage_fee, damage_rating)
    

else:
    # Handle renting
    print('Enter 5 pesos')
    while machine.inserted_coins < 5:
        pass
    else:
        extra = machine.inserted_coins - 5
        machine.add_balance(id_number, extra)
        machine.reset_inserted_coins()
        
    machine.start_motor()
    
    while machine.get_distance_from_ultrasonic(3) > 30:
        pass

    machine.open_dispensing_servo()

    while machine.get_distance_from_ultrasonic(4) > 30:
        pass

    machine.close_dispensing_servo()
    machine.stop_motor()

    umbrella_uuid = machine.scan_qrcode()

    # Save to database
    machine.rent_umbrella(id_number, umbrella_uuid, datetime.now())


machine.accepting_coin = True
while True:
    print(machine.inserted_coins)