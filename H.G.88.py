mport random
def random_listy(a):
    # w liscie ans beda docelowe listy (krotki), i pozniej tworzymy kazda liste o odpowiedniej dlugosci za pomoca randint, które
    # zwraca losowa liczbe w danym zakresie
    ans = []
    for l in a:
        ans.append([random.randint(1, 100) for i in range(l)])
    return ans
def random_krotki(a):
    ans = []
    for l in a:
        ans.append(tuple(random.randint(1, 100) for i in range(l)))
    return ans

print(random_listy([4,5,6]))
print(random_krotki([4,5,6]))
