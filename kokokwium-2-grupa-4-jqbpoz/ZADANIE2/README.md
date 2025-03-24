# ZADANIE 1

Zdefiniuj abstrakcyjną klasę `Animal` (dziedziczącą po `ABC`) z metodą abstrakcyjną `make_sound`.

1. **Abstrakcyjna klasa `Animal`**  
   - Dziedziczy po `ABC`.  
   - Posiada metodę abstrakcyjną `make_sound()`.  

2. **Klasy bazowe: `LandAnimal` i `WaterAnimal`**  
   - Obie dziedziczą po `Animal`.  
   - Każda implementuje (nadpisuje) metodę `make_sound()`.  

3. **Klasa `Amphibian`**  
   - Dziedziczy wielokrotnie po `LandAnimal` i `WaterAnimal`.  
   - Jej metoda `make_sound()` powinna:  
     - Wywołać implementację `make_sound` z `LandAnimal`,  
     - Wywołać implementację `make_sound` z `WaterAnimal`,  
     - Zwrócić łańcuch łączący oba dźwięki (np. `"Land sound & Water sound"`).  
