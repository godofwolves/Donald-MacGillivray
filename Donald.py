import time
import gopigo
from gopigo import *	#Has the basic functions for controlling the GoPiGo Robot
import sys	#Used for closing the running program
print ("This is a basic example for the GoPiGo Robot control")
print ("Press:\n\tp: begin dance \n\tx: Stop GoPiGo Robot\n\tz: Exit\n")
set_left_speed(200)
set_right_speed(200)
def chorus():
    fwd()
    print("chorus")
    time.sleep(2)
    bwd()
    print ("back")
    time.sleep(1)		
    fwd()
    print("forward")
    time.sleep(.5)
    print("left")
    left()
    time.sleep(1)
    enc_tgt(1,1,36)
    print("one full rotation left")		
    left()
    print("left")
    time.sleep(1)
    print("chorus end")
def fun():
    fwd()
    print ("fun")
    time.sleep(1.5)
    bwd()
    print ("come like a weaver")
    time.sleep(1)
    left()
    print ("swing")
    time.sleep(1)
    right()
    print ("sway")
    time.sleep(1)
    print ("come like a tailor")

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
	    print("right")
	    time.sleep(10)
	    chorus()
	    right()
	    print("right")
	    time.sleep(1)
	    fun()
	    fwd()
	    print ("forward")
	    time.sleep(3)
	    bwd()
	    print ("backwards")
	    time.sleep(3)
	    print("round 2")
	    right()
	    time.sleep(10)
	    chorus()
	    print ("working")
	    right()
	    time.sleep(10)
	    print("working")
	    chorus()
	    right()
	    print("right")
	    time.sleep(1)
	    fun()
	    fwd()
	    print ("forward")
	    time.sleep(3)
	    bwd()
	    print ("backwards")
	    time.sleep(3)
	    set_left_speed(0)
	    set_right_speed(0)
	    speed=100
	    while speed <=255:

	        set_left_speed(0)
	        set_right_speed(speed)
	        speed = speed + 10
	        time.sleep(0.1)
	        print("working")
	    set_left_speed(255)
	    set_right_speed(255)
	    chorus()
	    fun()
	    chorus()
	    fun()
	    chorus()
	    chorus()
	
	elif a=='x':
		stop()	# Stop
	elif a=='t':
		fun()
	# Increase speed
	elif a=='g':
		decrease_speed()	# Decrease speed
	elif a=='z':
		print ("Exiting")		# Exit
		sys.exit()
	else:
		print ("Wrong Command, Please Enter Again")
	time.sleep(.1)
