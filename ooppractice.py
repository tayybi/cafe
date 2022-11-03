import os
class Vehicle():
    def __init__(self,max_speed,color):
        self.max_speed = max_speed
        self.color = color

    def set_color(self, color):
        self.color =color
    def set_speed(self, speed):
        self.max_speed=speed

class Bus(Vehicle):
    def __init__(self, max_speed, color,seating_cap):
        self.seating_cap = seating_cap
        super().__init__(max_speed, color)
    
    def calculate_price(self):
        total = self.seating_cap * 0.5
        extra = total * 0.10
        total += extra
        return total




veh = Bus("30mph","Black",200)
veh.set_color("red")
veh.set_speed("70mph")
os.system("cls")
total = veh.calculate_price()
print( f"{veh.color}     {veh.max_speed}   {total}")
print(type(veh))
print(type(veh.color))