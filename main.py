from turtle import st
import serial
import time

def getTemp():
    # make sure the 'COM#' is set according the Windows Device Manager
    ser = serial.Serial('COM4', 9800, timeout=1)
    time.sleep(4)
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        #print(string)
    # time.sleep(5)
    return string
    ser.close()

T = getTemp()
print(T)
