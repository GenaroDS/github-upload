# Write your solution here:
import string


class Pet:
    def __init__(self, name : string, species : string, year_of_birth: int):
        self.name = name
        self.species = species
        self.year_of_birth =  year_of_birth
    
def new_pet(name:str,species:str,year_of_birth:int):
    pet = Pet(name,species,year_of_birth)
    return pet