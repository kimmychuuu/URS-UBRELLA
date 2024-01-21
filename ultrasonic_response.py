from urs_umbrella import Machine
from datetime import datetime, timedelta

machine = Machine(
    arduino_port='/dev/ttyUSB0',
    sim808_port='/dev/ttyUSB0',
    api_key='URSUmbrella@2023',
    api_url='https://ursubrella.online/api',
    hardware_callbacks='thread'
)

# Change based on distance required
distance_to_detect = 0 

print(f'Starting detection distance: {distance_to_detect}')
start = datetime.now()
while machine.get_distance_from_ultrasonic(4) > distance_to_detect:
    pass
end = datetime.now()
elapsed_time = end - start
print(f'Object detected! Elapsed time: {elapsed_time.total_seconds()} seconds')