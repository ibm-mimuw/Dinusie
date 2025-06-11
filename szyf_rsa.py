import random
from math import ceil, gcd, isqrt
from colorama import Fore
import time

def klucze(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi)
    d = pow(e, -1, phi)
    return [(e, n), (d, n)]

def zaszyfruj(klucz_pub, wiadomosc):
    e, n = klucz_pub
    ans = [pow(ord(char), e, n) for char in wiadomosc]
    return ans

def odszyfruj(klucz_pryw, wiadomosc_zaszyfrowana):
    d, n = klucz_pryw
    ans = [chr(pow(char, d, n)) for char in wiadomosc_zaszyfrowana]
    return ''.join(ans)

# p = {13, 101, 1007, 10007, 1000003, 10000019, 100000007, 1000000007, 1000000007, 100123456789, 1050100100501, 5783272917893,  1000000000100011, 99999999999999999991999}
# q = {17, 103, 1009, 10009, 1000199, 10000169, 100000037, 1000000033, 1000000009, 100529784361, 1100011100011, 5942636062289, 1011001110001111, 99999999999999999999977}
p = 1000003
q = 1000199

klucz_pub, klucz_pryw = klucze(p, q)
print(Fore.RED + str(p))
print(Fore.RED + str(q))
print(Fore.WHITE)
print(f"Publiczny klucz: {klucz_pub}")
print(f"Prywatny klucz: {klucz_pryw}")

wiadomosc = "Programowanie"
zaszyfrowana_wiad = zaszyfruj(klucz_pub, wiadomosc)
print(f"Wiadomość zaszyfrowana: {zaszyfrowana_wiad}")

odszyfrowana_wiad = odszyfruj(klucz_pryw, zaszyfrowana_wiad)
print(f"Wiadomość odszyfrowana: {odszyfrowana_wiad}")

def rozloz(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i, n // i
    return -1, -1

def brute_force(e, n):
    p, q = rozloz(n)
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    return (d, n)

start = time.time()
odgadniety_klucz = brute_force(klucz_pub[0], klucz_pub[1])
end = time.time()
print(f"Klucz odgadnięty brute forcem: {odgadniety_klucz}")
print(f"Wiadomość odszyfrowana odgadniętym kluczem: {odszyfruj(odgadniety_klucz, zaszyfrowana_wiad)}")
print(f"Czas bruteforce: {end - start:.6f} sekund")

def kwadrat(n):
    m = isqrt(n)
    return m * m == n

def algorytm_fermata(n):
    a = ceil(n ** 0.5)
    b1 = a * a - n
    while b1 >= 0 and not kwadrat(b1):
        a += 1
        b1 = a * a - n
    b = int(b1 ** 0.5)
    return a - b, a + b

def fermat(e, n):
    p, q = algorytm_fermata(n)
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    return (d, n)

start = time.time()
odgadniety_klucz_fermat = fermat(klucz_pub[0], klucz_pub[1])
end = time.time()
print(f"Klucz odgadnięty algorytmem Fermata: {odgadniety_klucz_fermat}")
print(f"Wiadomość odszyfrowana odgadniętym kluczem z fermata: {odszyfruj(odgadniety_klucz_fermat, zaszyfrowana_wiad)}")
print(f"Czas Fermata: {end - start:.6f} sekund")
