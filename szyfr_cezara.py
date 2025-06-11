def szyfr_cezara(tekst, przesuniecie):
  zaszyfrowany = ""
  for znak in tekst:
    if znak.isalpha():
      baza = ord('A') if znak.isupper() else ord('a')
      zaszyfrowany += chr((ord(znak) - baza + przesuniecie) % 26 + baza)
    else:
      zaszyfrowany += znak
  return zaszyfrowany
