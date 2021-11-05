import serial
ser = serial.Serial('/dev/ttyACM1', 9600)
ser.flushInput()
ser_bytes = ser.readline()
decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
mystring = "<test>"
b = mystring.encode('utf-8')
ser.write(b)
while True:
    ser_bytes = ser.readline()
    decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
    print(decoded_bytes)