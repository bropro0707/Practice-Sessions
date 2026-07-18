class engine:
    def start(self):
        return "Engine started"
class Car(engine):
    def  __init__(self):
        self.start = engine.start()
    def drive(self):
        print(self.start)
        print("Car is moving")
my = Car()
my.drive()