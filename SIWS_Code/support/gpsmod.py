import serial
import pynmea2
import time
serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
prev='https://www.latlong.net/c/?lat='+(str(0))+'&long='+str(0)
count=0;
def parseGPS(str):
    if str.find('GGA') > 0:
      msg = pynmea2.parse(str)
      if(float(msg.lat)>0):
       return(float(msg.lat)/100,float(msg.lon)/100)
    else:
       return (0.0,0.0)   
def getlink(count):
   if(count==0):
      prev='https://www.latlong.net/c/?lat='+(str(0))+'&long='+str(0)
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
   #print(a,b)
   if(a>0):
    link='https://www.latlong.net/c/?lat='+(str(a))+'&long='+str(b)
    prev=link
    
   else:
    link=prev
    print(link)
   return (link) 