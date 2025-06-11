def szyfr_vigenere(tekst, klucz):
  wynik = ''
  klucz = klucz.lower()
  klucz_len = len(klucz)
  indeks = 0

for znak in tekst:
  if 'a' <= znak <= 'z':
    przesuniecie = ord(klucz[indeks % klucz_len]) - ord('a')
    zaszufrowany = chr((ord(znak) - ord('a') + przesuniecie) % 26 + ord('a'))
    wynik += zaszyfrowany
    indeks += 1
  else:
    wynik += znak

return wynik
