""" Main routine for PREDICTIVE SERVER LSH """
import asyncio
import time
from machine_connector import ConnectorMachine
from maszyny import maszyny


def czytaj_rejestry(maszyna, rejestr, buffor):
    """
    Funkcja zawiera sprawdzenie czy podany symbol maszyny został zadeklarowany w module maszyny.py Jeżeli tak to pobiera
    wartość przypisaną do klucza jakim jest nazwa maszyny "maszyna"
    W kolejnym kroku tworzony jest connector biblioteki pymcprotocol a następnie weryfikowane jest połączenie z maszyną
    jeżeli połączenie jest aktywne nastęuje wywołanie metody read.word() klasy ConnectorMachine.
    Metoda ta zwraca słownik zawierający klucz-> symbol maszyny i jego wartość -> słownik zawierjący pare rejestr- wartosć
    np :  {"symbol_maszyny":{ "D1":0,"D2":5, ...}}

    :param maszyna: -> str Symbol maszyny w formacie np.: "K_GHCD"
    :param rejestr: -> str Pierwszy adress buforu w zapytaniu np. "D1"
    :param buffor: -> int Wielkość buforu ( ile rejestrów )
    :return: -> dict {"symbol_maszyny":{ "D1":0,"D2":5, ...}}
    """
    machine_symbol = maszyna
    if machine_symbol in maszyny:
        connection_parameters = maszyny[machine_symbol]
        print(f'{connection_parameters} Actual connection_parameters')
        machineConnector = ConnectorMachine(connection_parameters)
        is_connected = machineConnector.make_connection()
        if is_connected:
            register = machineConnector.read_word(rejestr, buffor)
            ret = {
                maszyna: register,
            }
            return ret
    else:
        print('Machine shortcut not found ... ')


def bufor_maszyn():
    start = time.time()
    czytaj_rejestry("K_WWSD", "D1", 100)
    czytaj_rejestry("K_BFRD", "D1", 100)
    czytaj_rejestry("K_EXTD", "D1", 100)
    czytaj_rejestry("K_GHCD", "D1", 100)
    czytaj_rejestry("K_PDMD", "D1", 100)
    czytaj_rejestry("K_PCMD", "D1", 100)
    czytaj_rejestry("K_DDRD", "D1", 100)
    czytaj_rejestry("K_MWDD", "D1", 100)
    czytaj_rejestry("K_HADD", "D1", 100)
    czytaj_rejestry("K_CGMD", "D1", 100)
    czytaj_rejestry("K_FOGD", "D1", 100)
    stop = time.time()
    calosc = stop - start
    print(f' Calosc zajeła {calosc} sekund')


bufor_maszyn()