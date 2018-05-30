import RPi.GPIO as GPIO
import dht11
import time
import datetime

#GPIO Ayarları
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#Veriyi pin 14' ü kullanarak okuduk
instance = dht11.DHT11(pin=14)

while True:
    result = instance.read()
    
    if result.is_valid():
        print("Son Okuma Zamanı: " + str(datetime.datetime.now()))
        print("Sıcaklık        : %d C" % result.temperature)
        print("Nem             : %d %%" % result.humidity)

    time.sleep(0.05)
    
    GPIO.setup(18,  GPIO.OUT)
    
    if result.temperature>=26:
        GPIO.output(18, GPIO.HIGH)
    else:
        GPIO.output(18, GPIO.LOW)
        
        
