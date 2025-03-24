# ZADANIE 1

Napisz funkcję `transform_texts`, która przyjmuje listę napisów (łańcuchów znaków). Funkcja powinna:

1. **Odfiltrować** puste napisy lub takie, które składają się wyłącznie z białych znaków (spacji, tabulatorów itp.).
2. **Dla pozostałych napisów** zastosować przekształcenie przy użyciu `map` i wyrażenia `lambda`, które:
   - Konwertuje napis do wersji **wielkich liter** (np. `"abc"` → `"ABC"`),
   - Odwraca kolejność znaków w napisie (np. `"ABC"` → `"CBA"`).
3. **Zwrócić** listę zawierającą przetworzone napisy.

Przetestuje tutaj czy działa push