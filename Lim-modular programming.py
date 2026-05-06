distance=42.195
speed=float(input("Input Speed (km/h):"))

def hour ():
hours= distance//speed
return hours

def min():
minu= distance/speed%1
minutes= minu*60
minutes= int(minutes)
return minutes

print ("It took you", hour(), "hours and", min(), "minutes to finish a marathon in",speed,"km/h.")

#1. The purpose of this function is to help figure out the time someone took while running a marathon
#2. A global variable is distance and speed, while a local variable I have is hours and minutes
#3. It is important to give us more information and guides us when coding.
