import os, time, math
from datetime import datetime 
from Adafruit_LED_Backpack import SevenSegment
from datetime import date
from datetime import time
print ("Program OK!")
print ("OS, Time, DateTime, and Math: All Imports READY!!!")

now = date.today()
nowT= datetime.now()
SP17_StartDate = date (2017, 1, 17) # Date to Trigger
SP17_StartTime = time (13, 35, 00) #Time to Trigger
CountdownD = abs(now - SP17_StartDate)
CountDownM = abs(nowT- SP17_StartTime)
print (str(CountdownD.days) + " Days to Relax")
#print (str(CountdownT.hour) + " Hours to Relax")
#print (str(CountdownT.minute)+ " Minutes to Relax")
#print (str(CountdownT.second)+ " Seconds to Relax")
print (nowT.strftime("%H:%M %I")+ " Current Time")
