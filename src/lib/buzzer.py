from machine import Pin, PWM
from time import sleep

buzz_pin = PWM(Pin(22))

class buzzer:
    def tone(freq, volume):
        buzz_pin.freq(freq)
        buzz_pin.duty_u16(2**volume)
    
    def beep(freq, volume, times, duration):
        for i in range(times):
            buzz_pin.freq(freq)
            buzz_pin.duty_u16(2 ** volume)
            sleep(duration / (times*2))
            buzz_pin.duty_u16(0)
            sleep(duration / (times*2))
    
    def stop():
        buzz_pin.deinit()
        
        
