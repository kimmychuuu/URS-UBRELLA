from urs_umbrella import Machine
from datetime import datetime, timedelta

machine = Machine(
    arduino_port='/dev/ttyUSB0',
    sim808_port='/dev/ttyUSB1',
    api_key='URSUmbrella@2023',
    api_url='https://ursubrella.online/api',
    hardware_callbacks='thread'
)

machine.send_sms('+639663784023','This is Ubrella~!')