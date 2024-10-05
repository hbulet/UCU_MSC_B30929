
class Vehicle:
    def __init__(me, _color):
        me.color = _color
    
    def getColor(me):
        return me.color
    
    def toString(me):
        return "This vehicle is " + me.color
    

class Car(Vehicle):
    def __init__(me, _color):
        super().__init__(_color)
        me.hasWinterTires = False

    def toString(me):
        _toString = super().toString() + ", has winter tires: "
        if me.hasWinterTires:
            _toString += "true" 
        else: 
            _toString += "false"
        return _toString
    
class Truck(Car):
    def __init__(me, _color):
        super().__init__(_color)
        me.hasATrailer = False

    def toString(me):
        _toString = super().toString() + ", has trailer: "
        if me.hasATrailer:
            _toString += "true" 
        else: 
            _toString += "false"
        return _toString 