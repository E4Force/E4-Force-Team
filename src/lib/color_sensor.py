from machine import Pin, PWM, I2C
from time import sleep, sleep_ms
from apds9960.const import *					# https://github.com/liske/python-apds9960.git
from apds9960 import uAPDS9960 as APDS9960		#   


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
comp_g_frente = 1
comp_b_frente = 1

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
                
            print("calibracion completada")
                
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
            print("calibracion completada")
                
        except NameError as e:
            print("ERROR!", e)
        

class color:
    
    def read_frente():
        global raw_r_frente, raw_g_frente, raw_b_frente
        color_frente.enableLightSensor()
        sleep(.11)
        raw_r_frente = color_frente.readRedLight()
        raw_g_frente = color_frente.readGreenLight()
        raw_b_frente = color_frente.readBlueLight()
        refresh()
        

            
    def read_abajo():
        global raw_r_abajo, raw_g_abajo, raw_b_abajo
        color_abajo.enableLightSensor()
        sleep(.11)
        raw_r_abajo = color_abajo.readRedLight()
        raw_g_abajo = color_abajo.readGreenLight()
        raw_b_abajo = color_abajo.readBlueLight()
        refresh()
        
        


    def simple_frente():
        
        global red_frente, green_frente, blue_frente, color_frente_actual
        color.read_frente()
        if red_frente > green_frente and red_frente > blue_frente:
            if (green_frente / red_frente) >= .90 and (blue_frente / red_frente) >= .90:
              
                color_frente_actual = "White"
            elif green_frente > blue_frente:
                if (green_frente / red_frente) <= .35 and (blue_frente / green_frente) >= .55:
                  
                    color_frente_actual = red_frente
                elif (green_frente / red_frente) > .35 and (green_frente / red_frente) < .80:
               
                    color_frente_actual = "Orange"
            elif blue_frente > green_frente:
                if (blue_frente / red_frente) <= .70:
                 
                    color_frente_actual = "Red"
                elif (blue_frente / red_frente) > .70:
                    
                    color_frente_actual = "Magenta"
            else:
                
                color_frente_actual = "Red"
                pass
            
            
        elif green_frente > red_frente and green_frente > blue_frente:
            if (red_frente / green_frente) > .90 and (blue_frente / green_frente) > .90:
               
                color_frente_actual = "White"
            elif (red_frente / green_frente) < .65 and (blue_frente / green_frente) < .75:
                
                color_frente_actual = "Green"                
            else:
                
                color_frente_actual = "Green"
            
        elif blue_frente > red_frente and  blue_frente > green_frente:
            if (green_frente / blue_frente) > .9 and (red_frente / blue_frente) > .9:
                
                color_frente_actual = "White"
            else:
               
                color_frente_actual = "Blue"  
  
        print("color frente =", color_frente_actual)



    def simple_abajo():
        global red_abajo, green_abajo, blue_abajo, color_abajo_actual
        color.read_abajo()
        if red_abajo > green_abajo and red_abajo > blue_abajo:
            if (green_abajo / red_abajo) >= .85 and (blue_abajo / red_abajo) >= .85:
           
                color_abajo_actual = "White"
            elif green_abajo > blue_abajo:
                if (green_abajo / red_abajo) <= .35 and (blue_abajo / green_abajo) >= .55:
         
                    color_abajo_actual = red_abajo
                elif (green_abajo / red_abajo) > .35 and (green_abajo / red_abajo) < .80:
                   
                    color_abajo_actual = "Orange"
            elif blue_abajo > green_abajo:
                if (blue_abajo / red_abajo) <= .70:
                 
                    color_abajo_actual = "Red"
                elif (blue_abajo / red_abajo) > .70:
                 
                    color_abajo_actual = "Magenta"
            else:
               
                color_abajo_actual = "Red"
                pass
            
            
        elif green_abajo > red_abajo and green_abajo > blue_abajo:
            if (red_abajo / green_abajo) > .85 and (blue_abajo / green_abajo) > .85:
                
                color_abajo_actual = "White"
            elif (red_abajo / green_abajo) < .65 and (blue_abajo / green_abajo) < .75:
                
                color_abajo_actual = "Green"                
            else:
                
                color_abajo_actual = "Green"
            
        elif blue_abajo > red_abajo and  blue_abajo > green_abajo:
            if (green_abajo / blue_abajo) > .9 and (red_abajo / blue_abajo) > .9:
                
                color_abajo_actual = "White"
            else:
              
                color_abajo_actual = "Blue"  

        print("color abajo =", color_abajo_actual)
