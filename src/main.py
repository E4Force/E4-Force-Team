from machine import Pin, PWM, I2C
from time import sleep
from servo import *
from motors import *
from hc_sr04 import *			# Library made by Roberto Sánchez, https://github.com/rsc1975/micropython-hcsr04.git
from color_sensors import *

# Sensor setup
sensor_izquierda = HCSR04(7,6)
sensor_derecha = HCSR04(5,4)

# Variables
distancia_iz = 0
distancia_de = 0


white_balance.abajo(10)
print("Code start")
print(color_frente_actual)

while True:
    
    distancia_iz = sensor_izquierda.distance_cm()
    distancia_de = sensor_derecha.distance_cm()
    color.simple_frente()
    print(color_frente_actual)
    
    if color_frente_actual == "Red":
        servo.degrees(0, 90)
        while True:
            color.simple_frente()
            if color_frente_actual == "Blue":
                servo.center(0)
                break
       
    elif distancia_de > distancia_iz:
        if (distancia_de / distancia_iz) > 90:
            servo.degrees(0, -90)
        
        else:
            servo.degrees(0, -(distancia_de / distancia_iz))
            
    elif distancia_de < distancia_iz:
        if (distancia_iz / distancia_de) > 90:
            servo.degrees(0, 90)
        
        else:
            servo.degrees(0, (distancia_de / distancia_iz))