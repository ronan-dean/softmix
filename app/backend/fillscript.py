import serial
import time
ser = serial.Serial('/dev/ttyACM1', 9600)
ser.flushInput()
ser_bytes = ser.readline()
decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
print(decoded_bytes)

def dispense(ml, pump):
    filled = False
    detected = False
    bottleWeight = 0
    ser_bytes = ser.readline()
    decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
    if int(decoded_bytes <= 1):
        print("Place a bottle on the sensor to continue")
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        while detected == False:
            if int(decoded_bytes) >= 60:
                print("filling now")
                ser_bytes = ser.readline()
                decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                bottleWeight = int(decoded_bytes)
                detected = True
                time.sleep(3)
                b = pump.encode('utf-8')
                ser.write(b)
                while filled == False:
                    if int(decoded_bytes) - bottleWeight >= int(ml):
                        ser.write(b'o') 
                        filled = True
                    else:
                        ser_bytes = ser.readline()
                        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                        print(decoded_bytes)
            else:
                ser_bytes = ser.readline()
                decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                print(decoded_bytes)
