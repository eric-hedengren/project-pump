from pyfirmata import Arduino, util
import time

board = Arduino('COM12')

pump_digital_11 = board.get_pin('d:11:p')

pump_digital_11.write(.25)
time.sleep(5)
pump_digital_11.write(0)
time.sleep(2)