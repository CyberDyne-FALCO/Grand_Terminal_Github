import os, time, math, Tkinter
from datetime import datetime 
from Adafruit_LED_Backpack import SevenSegment
from datetime import date
print ("Program OK!")
print ("OS, Time, DateTime, and Math: All Imports READY!!!")
DisplayMins = SevenSegment.SevenSegment(address=0x70) # Declare
Tripline = False #Boolean Trigger Switch
Stepper = 0

def ChronosMins (DaysCount):
	D=DaysCount.days
	Days2Minutes = 1440
	Minutes = D * Days2Minutes
	return Minutes;
def CheckAlarm(nownow, nowTime, Tripline, TriggerDate, PanicTime):
	if (Tripline != True):	
		if (now.date == TriggerDate and nowTime == PanicTime):
			Tripline == True
			print ("alarm tripped")
		return Tripline;
	else: 
		return;
def ChronoTrigger(Tripline):	
 
	return
def ChronoPrint(DigitMins):
	print("Writing...")
	DisplayMins.clear()
	DisplayMins.set_digit(0, DigitMins[0])
	DisplayMins.set_digit(1, DigitMins[1])
	DisplayMins.set_digit(2, DigitMins[2])
	DisplayMins.set_digit(3, DigitMins[3])
	DisplayMins.set_left_colon(datetime.now().second%2)
	DisplayMins.write_display()
	return
	
	
DisplayMins.begin()	
while(Tripline == False):
	now = datetime.now()
	nownow = now.date()
	nowTime= now.time()
	StartDate = datetime(2017, 01, 17, 8, 00, 00)
	TriggerDate = StartDate.date()
	PanicTime = StartDate.time()
	DaysCount = abs(nownow - TriggerDate)
	print ("Math Completed")
	#Hours = ChronosHours(DaysCount)
	Minutes = ChronosMins(DaysCount)
	PreMins = Minutes
	print("Written " + str(PreMins) + " at "+str (now.minute) + " during pass " + str(Stepper))
	ReadyMins= Minutes/10 - now.minute
	print (str(ReadyMins) + " (converted by dividing by 10 and subtracting current minutes)")
	DigitMins= [int(m) for m in str(ReadyMins)]
	ChronoPrint(DigitMins)
	Stepper +=1	
	CheckAlarm(nownow,nowTime,Tripline, TriggerDate,PanicTime) 
	#time.sleep(0.25)
ChronoTrigger(Tripline)
	
