import time
import gopigo
from gopigo import *	#Has the basic functions for controlling the GoPiGo Robot
import sys	#Used for closing the running program
print ("This is a basic example for the GoPiGo Robot control")
print ("Press:\n\tp: begin dance \n\tx: Stop GoPiGo Robot\n\tz: Exit\n")
set_left_motor(200)
set_right_motot(200)
def chorus():
    fwd()
    time.sleep(0.05)
    time.sleep(2)
    bwd()
    print ("working")
    time.sleep(1)		
    fwd()
    time.sleep(.5)
    print("working")
    left()
    time.sleep(1)
    enc_tgt(1,1,36) #one full rotation left		
    left()
    time.sleep(1)
    print("working")
while True:
	print ("Enter the Command:"),
	a=raw_input()	# Fetch the input from the terminal
	
	if a=='p':
	    print("Donald MacGillivray")
	    right()
	    time.sleep(10)
	    chorus()
	    print ("working")
	    right()
	    time.sleep(10)
	    print("working")
	    chorus
	    set_left_speed(0)
	    set_right_speed(0)
	    speed=20
	    right()
	    while speed <=255:
	        
	        set_left_speed(0)
	        set_right_speed(speed)
	        speed = speed + 10
	        time.sleep(0.01)
	        print("working")
	    set_left_speed(255)
	    set_right_speed(255)
	    set
	    chorus()
	   
	
	elif a=='x':
		stop()	# Stop
	elif a=='t':
		increase_speed()	# Increase speed
	elif a=='g':
		decrease_speed()	# Decrease speed
	elif a=='z':
		print ("Exiting")		# Exit
		sys.exit()
	else:
		print ("Wrong Command, Please Enter Again")
	time.sleep(.1)
