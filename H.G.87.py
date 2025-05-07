def liczba_unikalnych(a, b):
    i, j = 0, 0
    poprzedni = None
    licznik = 0

    while i < len(a) and j < len(b):
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
        else:  # a[i] == b[j]
            if a[i] != poprzedni:
                licznik += 1
