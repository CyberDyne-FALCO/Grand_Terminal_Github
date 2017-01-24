import os, time, math, Tkinter
from datetime import datetime 
from Adafruit_LED_Backpack import SevenSegment
from datetime import date
print ("Program OK!")
print ("OS, Time, DateTime, and Math: All Imports READY!!!")

Display = SevenSegment.SevenSegment(address=0x70)

# Initialize the display. Must be called once before using the display.
Display.begin()
Display.clear()

now = date.today()
SP17_StartDate = date (2017, 1, 17) #Time to Trigger
DaysCount = abs(now - SP17_StartDate)
print (str(DaysCount.days)+ " Days Left")
def ChronosHours(DaysCount):
	D=DaysCount.days
	Days2Hours = 24
	Hours = D * 24
	return Hours;
def ChronosMins (DaysCount):
	D=DaysCount.days
	Days2Minutes = 1440
	Minutes = D * Days2Minutes
	return Minutes;
def ChronosSecs(DaysCount):
	D=DaysCount.days
	Days2Seconds = 86400
	Seconds = D * Days2Seconds
	return Seconds;
Hours = ChronosHours(DaysCount)
Minutes = ChronosMins(DaysCount)
Seconds = ChronosSecs(DaysCount)
print (str(Hours) +" Hours Remaining")
print (str(Minutes) + " Minutes Remaining")
print (str(Seconds) + " Seconds Remaining")
print ("Conversions Completed, sending to SevenSegment!")
#while (now > SP17_StartDate):
while(True):
	Display.clear()
	now = datetime.now()
	nownow = now.date()
	SP17_StartDate = date (2017, 1, 17) #Time to Trigger
	DaysCount = abs(nownow - SP17_StartDate)
	Hours = ChronosHours(DaysCount)
	Minutes = ChronosMins(DaysCount)
	Seconds = ChronosSecs(DaysCount)
	#ReadySeconds = Seconds/10
	#DigitsSecs = [int(s) for s in str(ReadySeconds)]
	ReadyMins= Minutes/10
	DigitMins= [int(m) for m in str(ReadyMins)]
	#ChronoPrint()
	Display.clear
	Display.set_digit(0, DigitMins[0])
	Display.set_digit(1, DigitMins[1])
	Display.set_digit(2, DigitMins[2])
	Display.set_digit(3, DigitMins[3])
	#for c in Digits:
		#Display.clear()
		#Display.print_float(c)
	#Write the display buffer to the hardware.  This must be called to
	# update the actual display LEDs.
	Display.write_display()
	# Delay for a second.
	time.sleep(0.25)
