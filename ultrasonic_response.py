from urs_umbrella import Machine
from datetime import datetime, timedelta

machine = Machine(
    arduino_port='/dev/ttyUSB1',
    sim808_port='/dev/ttyUSB0',
    api_key='URSUmbrella@2023',
    api_url='https://ursubrella.online/api',
    hardware_callbacks='thread'
)

# Change based on distance required
#distance_to_detect = 0 

#print(f'Starting detection distance: {distance_to_detect}')
#start = datetime.now()
#while machine.get_distance_from_ultrasonic(1) > 7:
#   pass
#end = datetime.now()
#elapsed_time = end - start
machine.get_distance_from_ultrasonic(1)
print(machine.get_distance_from_ultrasonic(1))
machine.get_distance_from_ultrasonic(2)
print(machine.get_distance_from_ultrasonic(2))
machine.get_distance_from_ultrasonic(3)
print(machine.get_distance_from_ultrasonic(3))
machine.get_distance_from_ultrasonic(4)
print(machine.get_distance_from_ultrasonic(4 ))


