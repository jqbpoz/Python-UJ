import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify

def rysuj_wielomian(wejscie):
    poly, x_range = wejscie.split(', ')
    x_range = list(map(int, x_range.split()))
    x = np.linspace(x_range[0], x_range[1], 200)
    try:
        y = eval(poly.replace('x', 'x'))
        if np.isscalar(y):
            y = np.full_like(x, y)
    except NameError:
        y = np.full_like(x, eval(poly))
    plt.plot(x, y, label=f'Wielomian: {poly}')
    plt.grid(True)
    plt.title("Wykres wielomianu")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    return y[0], y[-1]

def rysuj_wielomian_sympy(wejscie):
    poly, range = wejscie.split(', ')
    range = list(map(int, range.split()))
    x = symbols('x')
    expr = sympify(poly)
    func = lambdify(x, expr, 'numpy')
    x_vals = np.linspace(range[0], range[1], 200)
    y_vals = func(x_vals)
    plt.plot(x_vals, y_vals, label=f'Wielomian (SymPy): {poly}')
    plt.grid(True)
    plt.title("Wykres wielomianu")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    return y_vals[0], y_vals[-1]


if __name__ == '__main__':
    # Przykładowe wywołanie pierwszej funkcji
    wejscie1 = "x**3 + 3*x + 1, -10 10"
    
    # Pierwszy wykres z eval
    wynik_eval = rysuj_wielomian(wejscie1)
    print("Wynik (eval):", wynik_eval)
    
    # Drugie wejście dla funkcji SymPy - bardziej złożona funkcja 
    wejscie2 = "x**4 - 5*x**2 + 3*sin(x), -10 10"  
    
    # Drugi wykres z SymPy
    wynik_sympy = rysuj_wielomian_sympy(wejscie2)
    print("Wynik (SymPy):", wynik_sympy)
    
    # Wyświetlanie obu wykresów
    plt.show()
