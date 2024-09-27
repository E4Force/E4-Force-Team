from machine import Pin, PWM, I2C
from time import sleep, sleep_ms
from apds9960.const import *					# https://github.com/liske/python-apds9960.git
from apds9960 import uAPDS9960 as APDS9960		# by Liske, ThomasWaldmann, raceking37, pcgeek86, ristomatti


try:
    
    i2c_frente = I2C(0, scl = Pin(17), sda = Pin(16), freq = 200000)
    color_frente = APDS9960(i2c_frente)
    print("Front Sensor Connected")
    
except OSError as e:
    print("Error initializing", e)

try:
    
    i2c_abajo = I2C(1, scl = Pin(27), sda = Pin(26), freq = 200000)
    color_abajo = APDS9960(i2c_abajo)
    print("Lower Sensor Connected")
    
except OSError as e:
    print("Error initializing", e)


# Raw RGB values as read by the color sensor
raw_r_frente = 1
raw_g_frente = 1
raw_b_frente = 1

raw_r_abajo = 1
raw_g_abajo = 1
raw_b_abajo = 1	

# Compensation used for white balance
comp_r_frente = 1
comp_g_frente = 1.2
comp_b_frente = 1.2

comp_r_abajo = 1
comp_g_abajo = 1
comp_b_abajo = 1

# Color value after white balance

red_frente = raw_r_frente * comp_r_frente
green_frente = raw_g_frente * comp_g_frente
blue_frente = raw_b_frente * comp_b_frente

red_abajo = raw_r_abajo * comp_r_abajo
green_abajo = raw_g_abajo * comp_g_abajo
blue_abajo = raw_b_abajo * comp_b_abajo


#Other variables

color_frente_actual = "Nada"
color_abajo_actual = "Nada"

def refresh():
    
    global comp_r_frente, comp_g_frente, comp_b_frente
    global raw_r_frente, raw_g_frente, raw_b_frente
    global red_frente, green_frente, blue_frente
    global comp_r_abajo, comp_g_abajo, comp_b_abajo
    global raw_r_abajo, raw_g_abajo, raw_b_abajo
    global red_abajo, green_abajo, blue_abajo
       
    red_frente = raw_r_frente * comp_r_frente
    green_frente = raw_g_frente * comp_g_frente
    blue_frente = raw_b_frente * comp_b_frente

    red_abajo = raw_r_abajo * comp_r_abajo
    green_abajo = raw_g_abajo * comp_g_abajo
    blue_abajo = raw_b_abajo * comp_b_abajo

    
class white_balance:
    
    def frente(samples):
        try:
            color_frente.enableLightSensor()
            global raw_r_frente, raw_g_frente, raw_b_frente
            global comp_r_frente, comp_g_frente, comp_b_frente
        
            for i in range(samples):
                sleep(.11)
                raw_r_frente += color_frente.readRedLight()
                raw_g_frente += color_frente.readGreenLight()
                raw_b_frente += color_frente.readBlueLight()
                
            raw_r_frente = raw_r_frente / samples
            raw_g_frente = raw_g_frente / samples
            raw_b_frente = raw_b_frente / samples
            
            if raw_r_frente > raw_g_frente and raw_r_frente > raw_b_frente:
                comp_r_frente = 1
                comp_g_frente = raw_r_frente / raw_g_frente
                comp_b_frente = raw_r_frente / raw_b_frente
                
            elif raw_g_frente > raw_r_frente and raw_g_frente > raw_b_frente:
                comp_r_frente = raw_g_frente / raw_r_frente
                comp_g_frente = 1
                comp_b_frente = raw_g_frente / raw_b_frente
                
            elif raw_b_frente > raw_r_frente and raw_b_frente > raw_g_frente:
                comp_r_frente = raw_b_frente / raw_r_frente
                comp_g_frente = raw_b_frente / raw_g_frente
                comp_b_frente = 1
                
        except NameError as e:
            print("Error!", e)
                
        finally:
            pass

    def abajo(samples):

        try:
            color_abajo.enableLightSensor()
            global raw_r_abajo, raw_g_abajo, raw_b_abajo
            global comp_r_abajo, comp_g_abajo, comp_b_abajo
        
            for i in range(samples):
                sleep(.11)
                raw_r_abajo += color_abajo.readRedLight()
                raw_g_abajo += color_abajo.readGreenLight()
                raw_b_abajo += color_abajo.readBlueLight()
                
            raw_r_abajo = raw_r_abajo / samples
            raw_g_abajo = raw_g_abajo / samples
            raw_b_abajo = raw_b_abajo / samples
            
            if raw_r_abajo > raw_g_abajo and raw_r_abajo > raw_b_abajo:
                comp_r_abajo = 1
                comp_g_abajo = raw_r_abajo / raw_g_abajo
                comp_b_abajo = raw_r_abajo / raw_b_abajo
                
            elif raw_g_abajo > raw_r_abajo and raw_g_abajo > raw_b_abajo:
                comp_r_abajo = raw_g_abajo / raw_r_abajo
                comp_g_abajo = 1
                comp_b_abajo = raw_g_abajo / raw_b_abajo
                
            elif raw_b_abajo > raw_r_abajo and raw_b_abajo > raw_g_abajo:
                comp_r_abajo = raw_b_abajo / raw_r_abajo
                comp_g_abajo = raw_b_abajo / raw_g_abajo
                comp_b_abajo = 1
                
        except NameError as e:
            print("ERROR!", e)
        

class color:
    
    def raw_frente():
        try:
            color_frente.enableLightSensor()
            sleep(.11)
            print()
            print("r =", color_frente.readRedLight())
            print("g =",  color_frente.readGreenLight())
            print("b =", color_frente.readBlueLight())
            print()
            
        except NameError:
            print("ERROR!")
  
    def raw_abajo():
        try:
            color_abajo.enableLightSensor()
            sleep(.11)
            print()
            print("r =", color_abajo.readRedLight())
            print("g =",  color_abajo.readGreenLight())
            print("b =", color_abajo.readBlueLight())
            print()
            
        except NameError:
            print("ERROR!")
    
    def simple_frente():
        try:
            global color_frente_actual
            global raw_r_frente, raw_g_frente, raw_b_frente
            global red_frente, green_frente, blue_frente
            color_frente.enableLightSensor()
            sleep(.11)
            raw_r_frente = color_frente.readRedLight()
            raw_g_frente = color_frente.readGreenLight()
            raw_b_frente = color_frente.readBlueLight()
            refresh()

            if red_frente > green_frente and red_frente > blue_frente:
                color_frente_actual = "Red"
                global color_frente_actual
                
            elif green_frente > red_frente and green_frente > blue_frente:
                color_frente_actual = "Green"
                global color_frente_actual
                
            elif blue_frente > red_frente and blue_frente > green_frente:
                color_frente_actual = "Blue"
                global color_frente_actual
                
            else:
                print("Something went wrong")
                           
        except NameError:
            print("ERROR!")   
            
    def simple_abajo():
        try:
            global color_abajo_actual
            global raw_r_abajo, raw_g_abajo, raw_b_abajo
            global red_abajo, green_abajo, blue_abajo
            color_abajo.enableLightSensor()
            sleep(.11)
            raw_r_abajo = color_abajo.readRedLight()
            raw_g_abajo = color_abajo.readGreenLight()
            raw_b_abajo = color_abajo.readBlueLight()
            refresh()

            if red_abajo > green_abajo and red_abajo > blue_abajo:
                color_abajo_actual = "Red"
                global color_abajo_actual
                
            elif green_abajo > red_abajo and green_abajo > blue_abajo:
                color_abajo_actual = "Green"
                global color_abajo_actual
                
            elif blue_abajo > red_abajo and blue_abajo > green_abajo:
                color_abajo_actual = "Blue"
                global color_abajo_actual
                
            else:
                print("Something went wrong")
                           
        except NameError:
            print("ERROR!")   
