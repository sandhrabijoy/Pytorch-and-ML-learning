class Microwave:
    def __init__(self,brand:str,power_rating:str)->None:
        self.brand=brand
        self.power_rating=power_rating
        self.turned_on:bool=False
    
    def turn_on(self)->None:
        if self.turned_on:
            print(f'Microwave({self.brand}) is already turned on')
        else:
            self.turned_on=True
            print(f'Microwave({self.brand})is now turned on')
    
    def turn_off(self)->None:
        if self.turned_on:
            self.turned_on=False
            print(f'Microwave({self.brand})is now turned off')
        else:
            print(f'Microwave({self.brand})is now turned off')
    
    def run(self,seconds:int)->None:
        if self.turned_on:
            print(f'Microwave({self.brand})for {seconds} seconds')
        else:
            print('Microwave needs to be turned on for it to run')
    def __add__(self,other):
        return f'{self.brand}+{other.brand}' 

smeg:Microwave=Microwave(brand='Smeg',power_rating='B')
smeg.turn_on()
smeg.turn_on()
bosch:Microwave=Microwave(brand='Bosch',power_rating='C')
bosch.turn_on()
bosch.turn_on()
bosch.run(50)
bosch.turn_on
bosch.turn_off()
print(smeg+bosch)