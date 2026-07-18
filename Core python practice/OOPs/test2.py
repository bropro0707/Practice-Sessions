class Thermometer:
    def __init__(self,celsius):
        self._celsius = None
        self.celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self,value):
        if value <= -273.15:
            print("error")
        else:
            self._celsius = value

    @property
    def farenhite(self):
        farenhite = (self._celsius*1.8) +32
        return farenhite

i = Thermometer(0)
print(i._celsius)
print(i.farenhite)