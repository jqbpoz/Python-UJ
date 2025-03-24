import time
from datetime import datetime

def wyswietl_zegar():
    while True:
        now = datetime.now()
        clock_data = [now.hour,now.minute,now.second]
        hour,minute,second = [str(t).rjust(2,"0") for t in clock_data ]
        print(f'\r{hour}:{minute}:{second}',end='')
        time.sleep(0.5)
        pass

if __name__ == "__main__":
    wyswietl_zegar()
