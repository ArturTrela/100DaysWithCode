import time
import pandas as pd
import concurrent.futures
zakres = 100000

def adam(zakres_max):
    timestart1 = time.time()

    for liczba in range(1,zakres_max+1):
        licznik = 0

        for dzielnik in range(1,liczba+1):
            if (float(liczba % dzielnik) == 0):
                licznik = licznik + 1
            if (licznik > 2):
                break
        if (licznik == 2):
            print(f"{liczba} jest to liczba pierwsza")
            print("------------")

    timestop1 = time.time()
    print(f"Czas operacji  {timestop1-timestart1}")

def adrian(zakres_max):

    timestart2 = time.time()
    output=''
    licznik1 = False
    for liczba in range(1,zakres_max+1):
        licznik1 = False

        for dzielnik in range(2,liczba):
            if (liczba % dzielnik) == 0:
                licznik1 = True
                break

        if not licznik1:
            # print(f"{liczba} jest to liczba pierwsza")
            output+=f"{liczba} jest to liczba pierwsza"
            # print("------------")
        else:
            licznik1 = False

    timestop2 = time.time()
    print(output)
    print(f"Czas operacji drugiej metody {timestop2-timestart2}")


def artur(zakres_max):
    timestart2 = time.time()
    output = []
    licznik2 = False
    for liczba in range(1, zakres_max + 1):
        licznik2 = False

        for dzielnik in range(2, liczba):
            if (liczba % dzielnik) == 0:
                licznik2 = True
                break

        if not licznik2:
            output.append(liczba)
        else:
            licznik2 = False

    df = pd.Series(output)
    timestop2 = time.time()
    print(f"Czas operacji trzeciej metody {timestop2 - timestart2}")
    return df

out = artur(zakres)
print(out)



def jest_pierwsza(liczba):
    if liczba < 2:
        return False
    for dzielnik in range(2, int(liczba ** 0.5) + 1):
        if liczba % dzielnik == 0:
            return False
    return True

def artur(zakres_max):
    timestart2 = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(jest_pierwsza, liczba): liczba for liczba in range(1, zakres_max + 1)}
        output = [liczba for future, liczba in futures.items() if future.result()]

    df = pd.Series(output)
    timestop2 = time.time()
    print(f"Czas operacji czwartek metody {timestop2 - timestart2}")
    return df

out = artur(zakres)
print(out)
