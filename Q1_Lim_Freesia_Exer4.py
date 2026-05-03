units=("F", "C", "K")
user_input=input("Choose the unit of measurements you prefer (F)ahrenheit, (C)elsius, or (K)elvin: ")

#Inputing temperature 
if user_input in units:
    temp=float(input(f"Enter temperature in {user_input}:"))

#Inputing invalid unit
else:
    exit("Invalid unit")
    
#Functions
def kelvin():
    user_input==units[2]
    c=temp-273.15
    if c<0:
        print("Too cold!")
    elif c>35:
        print("Too hot!")
    else:
        print("Safe temperature!")  
    return c

def fahrenheit():
    user_input==units[0]
    c=(temp-32)*5/9
    if c<0:
        print("Too cold!")
    elif c>35:
        print("Too hot!")
    else:
        print("Safe temperature!")  
    return c
    
def celsius():
        user_input==units[1]
        c=temp
        if c<0:
            print("Too cold!")
        elif c>35:
            print("Too hot!")
        else:
            print("Safe temperature!")  
        return c

#Calling my functionc
if user_input==units[0]:
    fahrenheit()
elif user_input==units[1]:
    celsius()
elif user_input==units[2]:
    kelvin()



    

        
