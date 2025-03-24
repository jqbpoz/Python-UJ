import time
from decorator import decorator

@decorator
def pomiar_powtorzen(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time




@pomiar_powtorzen
def funkcja(*args, delay=1):
    for arg in args:
        print(arg)
        time.sleep(delay)

if __name__ == "__main__":
    czas = funkcja("Hello", "World", "to", "jest", "test", delay=0.5)
    print(f"Czas wykonania funkcji '{funkcja.__name__}': {czas:.4f} sekundy")
