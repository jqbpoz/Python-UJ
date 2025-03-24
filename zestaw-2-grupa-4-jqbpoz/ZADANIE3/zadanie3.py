import re
def rzymskie_na_arabskie(rzymskie):

    def is_valid_roman(roman):
        if not re.match(r'^[IVXLCDM]+$', rzymskie):
            return False
        pattern = r'^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
        return bool(re.match(pattern, rzymskie))

    if not is_valid_roman(rzymskie):
        raise ValueError("Liczba musi być w zakresie 1‐3999")

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    previous = 0

    for char in reversed(rzymskie):
        value = roman_numerals[char]
        if value < previous:
            total -= value
        else:
            total += value
        previous = value

    return total

def arabskie_na_rzymskie(arabskie):

    if not (1 <= arabskie <= 3999):
        raise ValueError("Liczba musi być w zakresie 1‐3999")

    arabic_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }

    roman = ""
    for value in sorted(arabic_numerals.keys(), reverse=True):
        while arabskie >= value:
            roman += arabic_numerals[value]
            arabskie -= value

    return roman

if __name__ == '__main__':
    try:
        # Przykłady konwersji rzymskiej na arabską
        rzymska = "MCMXCIV"
        print(f"Liczba rzymska {rzymska} to {rzymskie_na_arabskie(rzymska)} w arabskich.")
        
        # Przykłady konwersji arabskiej na rzymską
        arabska = 1994
        print(f"Liczba arabska {arabska} to {arabskie_na_rzymskie(arabska)} w rzymskich.")
        
    except ValueError as e:
        print(e)
