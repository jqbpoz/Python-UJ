import numpy as np
from tqdm import tqdm

def symulacja(N):
    p = 0
    for _ in tqdm(range(N)):
        x, y = np.random.uniform(-1, 1, 2)
        if np.pow(x,2) + np.pow(y,2) < 1:
            p = p+1
    pi = 4 * p / N
    return pi


if __name__ == "__main__":
    N = 1000000
    print(symulacja(N))
