from machine import Pin, PWM, I2C
from time import sleep
from hc_sr04 import *

distance_left = 0
distance_right = 0
distance_front = 0

sensor_left = HCSR04(7,6)
sensor_right = HCSR04(5,4)
sensor_front = HCSR04(3,2)
        
class actions:
    def all_sides():
        global distance_left, distance_right, distance_front
        distance_left = sensor_left.distance_cm()
        distance_front = sensor_front.distance_cm()
        distance_right = sensor_right.distance_cm()
        print(distance_left, distance_front, distance_right)
    
    def side_distance():
        global distance_left, distance_right
        distance_left = sensor_left.distance_cm()
        distance_right = sensor_right.distance_cm()
        
        
    def centralizar(limite):
        actions.side_distance()   
        if distance_left < limite:
            compensation = int(-((distance_left * (90 / limite))-110))
            servo.degrees(0, compensation)
            print("Distance, left = " + str(distance_left) , compensation,  "degrees")

        elif distance_right < limite:
            compensation = int(((distance_right * (90 / limite))-110))
            servo.degrees(0, compensation)
            print("Distance, right = " + str(distance_right) , compensation,  "degrees")

        else:
            pass
        
 