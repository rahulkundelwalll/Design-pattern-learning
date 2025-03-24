from abc import ABC, abstractmethod
# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Concrete Commands
class LightOnCommand(Command):
    def __init__(self,light):
        self.light = light
    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self,light):
        self.light = light
    
    def execute(self):
        self.light.turn_off()
# Receiver: Light
class Light:
    def turn_on(self):
        print("light is on")
    def turn_off(self):
        print("light is off")

# Invoker: Remote Control
class RemoteControl:
    def __init__(self):
        self.command = {}
    def setCommand(self,button,cmd):
        self.command[button] = cmd
    def press_button(self,button):
            self.command[button].execute()

light = Light()
remote = RemoteControl()
remote.setCommand("up",LightOnCommand(light))
remote.setCommand("down",LightOffCommand(light))

remote.press_button("down")