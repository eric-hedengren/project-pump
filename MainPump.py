from pyfirmata import Arduino, util
import time

board = Arduino('COM12')
it = util.Iterator(board)
it.start()

pump = board.get_pin('d:11:p') # Digital port, Port 11, Mode PWM
level = board.get_pin('a:0:o') # Analog port, Port 0, Mode output
level.enable_reporting()

while True:
    x = level.read()
    time.sleep(.1)
    if x != None:
        if x < 1:
            pump.write(.5)
            print(1, x)
        else:
            pump.write(0)
            print(0, x)