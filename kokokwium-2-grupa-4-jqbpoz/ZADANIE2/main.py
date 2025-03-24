# Zdefiniuj abstrakcyjną klasę Animal (dziedziczącą po ABC) z metodą abstrakcyjną make_sound.
# Zdefiniuj dwie klasy bazowe, np. LandAnimal i WaterAnimal, obie dziedziczące po Animal. Każda z nich implementuje (nadpisuje) metodę make_sound.
# Zdefiniuj klasę Amphibian, która dziedziczy wielokrotnie po LandAnimal i WaterAnimal. Metoda make_sound w Amphibian powinna:
# Wywołać implementację make_sound z LandAnimal,
# Wywołać implementację make_sound z WaterAnimal,
# Zwrócić łańcuch łączący oba dźwięki (np. "Land sound & Water sound").


from abc import ABC, abstractmethod

# Zdefiniuj klasę Animal dziedziczącą po ABC z metodą abstrakcyjną make_sound
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Zdefiniuj klasę LandAnimal dziedziczącą po Animal
#       - implementuj metodę make_sound
class LandAnimal(Animal):
    def make_sound(self):
        return "LandAnimal sound"

# Zdefiniuj klasę WaterAnimal dziedziczącą po Animal
#       - implementuj metodę make_sound
class WaterAnimal(Animal):
    def make_sound(self):
        return "WaterAnimal sound"

# Zdefiniuj klasę Amphibian dziedziczącą wielokrotnie
#       - w metodzie make_sound wywołaj LandAnimal.make_sound(self) oraz WaterAnimal.make_sound(self)
class Amphibian(LandAnimal, WaterAnimal):
    def make_sound(self):
        land_sound = LandAnimal.make_sound(self)
        water_sound = WaterAnimal.make_sound(self)
        return f"{land_sound} & {water_sound}"

if __name__ == '__main__':
    # Przykładowe wywołania:
    land = LandAnimal()
    water = WaterAnimal()
    frog = Amphibian()
    
    print("LandAnimal:", land.make_sound())
    print("WaterAnimal:", water.make_sound())
    print("Amphibian:", frog.make_sound())