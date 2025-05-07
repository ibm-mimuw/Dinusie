def liczba_unikalnych(a, b):
    n = len(a)
    m = len(b)
    i = j = 0
    licznik = 0
    poprzedni = None

    while i < n and j < m:
        if a[i] < b[j]:
            if a[i] != poprzedni:
                licznik += 1
                poprzedni = a[i]
            i += 1
        elif a[i] > b[j]:
            if b[j] != poprzedni:
                licznik += 1
                poprzedni = b[j]
            j += 1
        else:  # równe elementy
            if a[i] != poprzedni:
                licznik += 1
                poprzedni = a[i]
            i += 1
            j += 1

    while i < n:
        if a[i] != poprzedni:
            licznik += 1
            poprzedni = a[i]
        i += 1

    while j < m:
        if b[j] != poprzedni:
            licznik += 1
            poprzedni = b[j]
        j += 1

    return licznik

a = [1, 2, 2, 3, 5]
b = [2, 4, 5, 6]
print(liczba_unikalnych(a, b))
