import time
import RPi.GPIO as GPIO
import requests
import serial
import pynmea2
import time
import location
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
prev='http://maps.google.com/?q='+(str(0))+','+str(0)

link = "http://192.168.0.7/availableusers.php"
def convert_to_degrees(raw_value):
    decimal_value = raw_value/100.00
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - int(decimal_value))/0.6
    position = degrees + mm_mmmm
    position = "%.4f" %(position)
    return position

def parseGPS(str):
    if str.find('GGA') > 0:
      msg = pynmea2.parse(str)
      if(float(msg.lat)>0):
       return(convert_to_degrees(float(msg.lat)),convert_to_degrees(float(msg.lon)))
    else:
       return (0.0,0.0)   
def getlink(count):
   #count=count+1
   time.sleep(1)
   str1='test'
   (a,b)=(0.0,0.0)
   try:
    str1 = serialPort.readline().decode()
   except:
    print('error') 
 #print(str(str1))
   (a,b)=parseGPS(str1)
   #if()
   print(a,b)
   if(a>0):
    link='http://maps.google.com/?q='+(str(a))+','+str(b)
    prev=link
    
   else:
    link=prev
    print(link)
   return (link)

def send_sms(no,text):
    r=requests.get('http://www.kit19.com/ComposeSMS.aspx?username=ramson587165&password=24172&sender=RTLABS&to='+no+'&message='+text+'&priority=1&dnd=1&unicode=0')
    print(r.text)
    print("sms sent")

# If button is pushed, light up LED
try:
    while True:
       time.sleep(1)
       str1='test'
       (a,b)=(0.0,0.0)
       try:
         str1 = serialPort.readline().decode()
       except:
        print('error') 
 #print(str(str1))
       (a,b)=parseGPS(str1)
   #if()
       print(a,b)
       if(float(a)>0):
        link1='http://maps.google.com/?q='+(str(a))+','+str(b)
        prev=link1
    
       else:
        link1=prev
        print(link1)
   
        #gpsmod.getlink(con)
        con=con+1
        print(count)
        if GPIO.input(btn_pin)and count==0:
            count=1
            getrequest = requests.get(link)
            textData=str(getrequest.text)
            data=textData.split('\n')
            print(data)
            for phoneno in data:
                 #print("send sms"+str(phoneno))
                 if(len(phoneno)==10):
                   print(link1)  
                   send_sms(phoneno,"Please help me.I am in danger Mylocation is at  "+link1)
            break;     
        else:
            print("no input")
            #GPIO.output(led_pin, GPIO.HIGH)

finally:
    GPIO.cleanup()