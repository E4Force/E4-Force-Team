from machine import Pin, PWM
class servo:
    def left(pin):
        move = PWM(Pin(pin))
        move.freq(50)
        move.duty_ns(600000)        
    def center(pin):
        move = PWM(Pin(pin))
        move.freq(50)
        move.duty_ns(1500000)        
    def right(pin):
        move = PWM(Pin(pin))
        move.freq(50)
        move.duty_ns(2400000)        
    def degrees(pin, deg):
        calculated_duty = (1500000 + (10000*deg))        
        if calculated_duty >= 600000 and calculated_duty <= 2400000:
            move = PWM(Pin(pin))
            move.freq(50)
            move.duty_ns(int(calculated_duty))        
        elif calculated_duty < 600000:
            move = PWM(Pin(pin))
            move.freq(50)
            move.duty_ns(600000)                        
        elif calculated_duty > 2400000:
            move = PWM(Pin(pin))
            move.freq(50)
            move.duty_ns(2400000)            
        else:
            print("Not allowed")
            print()        
    def stop(pin):
        move = PWM(Pin(pin))
        move.deinit()
        

        