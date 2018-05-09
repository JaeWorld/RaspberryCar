######################################################################
### Date: 2017/10/5
### file name: project3_student.py
### Purpose: this code has been generated for the three-wheeled moving
###         object to perform the project3 with ultra sensor
###         swing turn, and point turn
### this code is used for the student only
######################################################################

# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
from time import sleep

# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)

# =======================================================================
# import getDistance() method in the ultraModule
# =======================================================================
from ultraModule import getDistance

# =======================================================================
# import TurnModule() method
# =======================================================================
from TurnModule import *
from trackingModule import *
# =======================================================================
# rightPointTurn() and leftPointTurn() in TurnModule module
# =======================================================================


# =======================================================================
# import go_forward_any(), go_backward_any(), stop(), LeftPwm(),
# RightPwm(), pwm_setup(), and pwm_low() methods in the module of go_any
# =======================================================================
from go_any import *

# implement rightmotor(x)  # student assignment (3)
# implement go_forward_any(speed): # student assignment (4)
# implement go_backward_any(speed): # student assignment (5)
# implement go_forward(speed, running_time)  # student assignment (6)
# implement go_backward(speed, running_time)  # student assignment (7)

# =======================================================================
# setup and initilaize the left motor and right motor
# =======================================================================
pwm_setup()

# =======================================================================
#  define your variables and find out each value of variables
#  to perform the project3 with ultra sensor
#  and swing turn
# =======================================================================
dis = 20 
obstacle = 1

# when obstacle=1, the power and
# running time of the first turn
SwingPr = 55 
SwingTr = 0.35  

# when obstacle=2, the power and
# running time of the second turn
PointPr = 44
PointTr = 0.04


try:
    while True:

        distance = getDistance()
        print('distance= ', distance)
        
        if distance > dis:
            A=GPIO.input(centerled)
            B=GPIO.input(leftlessled)
            C=GPIO.input(rightlessled)
            D=GPIO.input(leftmostled)
            E=GPIO.input(rightmostled)
            ledList=[D,B,A,C,E]
       
            print "ledList"
        
            if ledList==[1,1,0,1,1] or ledList==[1,0,0,0,1]:
                Line(30, 30)

            elif ledList==[0,1,1,1,1]:
                Line(12, 38)

            elif ledList==[0,0,1,1,1] or ledList==[1,0,1,1,1] or ledList==[1,0,0,1,1]:
                Line(25, 38)

            elif ledList==[0,0,0,1,1]:
                Line(38, 8)

            elif ledList==[0,0,0,0,1]:
                Line(38, 4) 

            elif ledList==[1,1,1,1,0]:
                Line(38, 12)
        
            elif ledList==[1,1,1,0,0] or ledList==[1,1,1,0,1] or ledList==[1,1,0,0,1]:
                Line(38, 25)
            
            elif ledList==[1,1,1,1,1]:
                Line(5, 38)

            elif ledList==[0,0,0,0,0]:
                stop()
                
        elif distance <= dis :
            
            stop()
            rightSwingTurn(35,0.62)
            go_forward(40,0.9)
            leftSwingTurn(40,1)
            go_forward_any(25, 25)

except KeyboardInterrupt:
        GPIO.cleanup()
        pwm_low()

            ### please continue the code or change the above code
            ### # student assignment (10)
            ########################################################


