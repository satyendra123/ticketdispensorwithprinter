'''
import serial
import time

ESC = b'\x1b'
GS  = b'\x1d'

ser = serial.Serial(port='COM7',baudrate=38400,timeout=1)

time.sleep(1)

# Init
ser.write(ESC + b'@')

# Force English
ser.write(ESC + b't' + b'\x00')

# Center + Bold
ser.write(ESC + b'a' + b'\x01')
ser.write(ESC + b'E' + b'\x01')
ser.write(b"MY SHOP NAME\n")

ser.write(ESC + b'E' + b'\x00')
ser.write(b"--------------------------\n")

ser.write(ESC + b'a' + b'\x00')
ser.write(b"Item 1        Rs. 50\n")
ser.write(b"Item 2        Rs. 30\n")
ser.write(b"Item 3        Rs. 20\n")

ser.write(b"--------------------------\n")
ser.write(ESC + b'E' + b'\x01')
ser.write(b"TOTAL         Rs. 100\n")
ser.write(ESC + b'E' + b'\x00')

ser.write(b"\nThank you!\nVisit Again\n\n")

# Cut
ser.write(GS + b'V' + b'\x00')

ser.flush()
ser.close()
'''
# this is the working code for the ticket dispensor code
import serial
import time

ESC = b'\x1b'
GS  = b'\x1d'

ser = serial.Serial(port='COM7',baudrate=38400,timeout=1,rtscts=False,dsrdtr=False)

time.sleep(2)

ser.write(ESC + b'@')       # init
ser.write(b'*** TEST PRINT ***\n\n')
ser.write(b'Hello ESC POS\n\n')
ser.write(GS + b'V' + b'\x00')  # cut

ser.close()
