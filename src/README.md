Control software
====

<sub>This directory must contain code for control software which is used by the vehicle to participate in the competition and which was developed by the participants.
All artifacts required to resolve dependencies and build the project must be included in this directory as well. </sub>




# All code developed by us is listed here.
        - main.py
        - motors.py
        - servo.py
        - color_sensor
        **color_sensor.py is a library made by us, but it wouldn't work without the dependcies, thos being const.py, devide.py, exceptions.py and __init__.py** 

         Changes made as of 29SEP24
                -main.py has been updated to do a routine looking at the color of the track
                -servo.py has been updated to compensante for slack in the rack and pinion
                -color_sensor.py has been updated to see more colors
        
         Code added
                -buzzer.py
                -actions.py


# Code sourced from Github is listed here, mainly the libraries for the sensors used.

## [APDS-9960 library by by Liske, ThomasWaldmann, raceking37, pcgeek86, ristomatti](https://github.com/liske/python-apds9960)
        - const.py
        - device.py
        - exceptions.py
        - __init__.py
        

    
## [HC_SR04  by  Roberto Sánchez](https://github.com/rsc1975/micropython-hcsr04)
        - hc_sr04.py    


