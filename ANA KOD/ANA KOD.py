import RPi.GPIO as GPIO
import dht11
import time
import datetime
import serial

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,  GPIO.OUT)
GPIO.setup(24,  GPIO.OUT)
GPIO.cleanup()

instance = dht11.DHT11(pin=14)

ser = serial.Serial('/dev/ttyACM0',9600)
s = [0]
#s[0] = str(int (ser.readline(),16))
while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18,  GPIO.OUT)
    GPIO.setup(24,  GPIO.OUT)
    
    result = instance.read()
    s[0]=str(int(ser.readline(),16))
    #time.sleep(1)
    
    if   int(s[0])>300 and result.temperature>26:
        
        if result.is_valid():
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(24, GPIO.HIGH)
            
            #print("\nİlk if")
            print("\nSon Okuma Zamanı  : " + str(datetime.datetime.now()))
            print("\nGaz değeri        :" ,s[0],"ppm")
            print("Sıcaklık          : %d C" % result.temperature)
            print("Nem               : %d %%" % result.humidity)
            
    elif int(s[0]) >300 and result.temperature<26:
        
        if result.is_valid():
            GPIO.output(18, GPIO.LOW)
            GPIO.output(24, GPIO.HIGH)
            
            #print("\nİkinci if")
            print("\nSon Okuma Zamanı  : " + str(datetime.datetime.now()))
            print("\nGaz değeri        :" ,s[0],"ppm")
            print("Sıcaklık          : %d C" % result.temperature)
            print("Nem               : %d %%" % result.humidity)
            
    elif int(s[0]) <300 and result.temperature>26:
        
        if result.is_valid():
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(24, GPIO.LOW)
            
            #print("\nÜçüncü if")
            print("\nSon Okuma Zamanı  : " + str(datetime.datetime.now()))
            print("\nGaz değeri        :" ,s[0],"ppm")
            print("Sıcaklık          : %d C" % result.temperature)
            print("Nem               : %d %%" % result.humidity)
            
    elif int(s[0]) <300 and result.temperature<26:
        
        if result.is_valid():
            GPIO.output(18, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
            
            #print("\nDördüncü if")
            print("\nSon Okuma Zamanı  : " + str(datetime.datetime.now()))
            print("\nGaz değeri        :" ,s[0],"ppm")
            print("Sıcaklık          : %d C" % result.temperature)
            print("Nem               : %d %%" % result.humidity)
    else:
            GPIO.cleanup()
