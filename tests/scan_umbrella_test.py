import sys
sys.path.append('../')

from urs_umbrella
import Machine

machine = Machine(
        arduino_port='/dev/ttyUSB1',
        sim808_port='/dev/ttyUSB0',
        api_key='URSUmbrella@2023',
        api_url='https://ursubrella.online/api',
        hardware_callbacks='thread'
    )
umbrella_id = machine.scan_qrcode()

machine.confirm_umbrella('1','23URS01')
print(machine.confirm_umbrella('1','23URS01'))