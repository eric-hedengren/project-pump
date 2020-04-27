from pyfirmata import Arduino, util
import time

board = Arduino('COM12')

it = util.Iterator(board)
it.start()

board.analog[0].enable_reporting()
level_analog_0 = board.get_pin('a:0:o') # Analog port, Port 0, Mode output
while True:
    print(level_analog_0.read())
    time.sleep(.1)

    #When connected with the pump the sensor gives a reading of 0 every once in a while