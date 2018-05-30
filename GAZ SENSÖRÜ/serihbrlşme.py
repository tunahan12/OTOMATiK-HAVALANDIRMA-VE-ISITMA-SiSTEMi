import serial
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
GPIO.setwarnings(False)

ser = serial.Serial('/dev/ttyACM0',9600)
s = [0]
while True:
     #read_serial=ser.readline()
     s[0] = str(int (ser.readline(),16))
     print ("Gaz değeri:",s[0])
     time.sleep(1)
     if int(s[0]) >300:
         GPIO.output(24, GPIO.HIGH)
     if int(s[0]) <300:
         GPIO.output(24, GPIO.LOW)
    
            
	
	
	