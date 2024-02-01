import time
import RPi.GPIO as GPIO
import requests
import serial
import pynmea2
import time
import gpsloc
import gpsmod
count=0
con=0
# Pins definitions
btn_pin = 16
#led_pin = 12

# Set up pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(btn_pin, GPIO.IN)
#GPIO.setup(led_pin, GPIO.OUT)
serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
prev='https://www.latlong.net/c/?lat='+(str(0))+'&long='+str(0)

link = "http://192.168.0.3/availableusers.php"

def send_sms(no,text):
    r=requests.get('http://www.kit19.com/ComposeSMS.aspx?username=ramson587165&password=24172&sender=RTLABS&to='+no+'&message='+text+'&priority=1&dnd=1&unicode=0')
    print(r.text)
    print("sms sent")

# If button is pushed, light up LED
try:
    while True:
        link2=gpsloc.gpsloc1()
        
        if GPIO.input(btn_pin)and count==0:
            count=1
            getrequest = requests.get(link)
            textData=str(getrequest.text)
            data=textData.split('\n')
            print(data)
            for phoneno in data:
                 #print("send sms"+str(phoneno))
                 if(len(phoneno)==10):
                  print(link2)   
                  #send_sms(phoneno,"Please help me.I am in danger Mylocation is at"+link1)
            break;     
        else:
            print("no input")
            #GPIO.output(led_pin, GPIO.HIGH)

finally:
    GPIO.cleanup()
