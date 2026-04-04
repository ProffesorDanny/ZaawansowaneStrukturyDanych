import numpy as np

def main():
    instruction = (f"""
Instrukcja obsługi programu:
---------------------------
EXIT - wyjdź z programu
ADD (wyraz) - dodaj nowy wyraz
SHOW - pokaż aktualny stan tablicy
CHECK - sprawdź podany wyraz
---------------------------
UWAGA: Ze względu na rozmiar tablicy proszę nie dodawać zbyt wielu elementów""")

    print(instruction)
    continuation = False
    checktable = np.zeros(12, dtype=int)
    while not continuation:
        wejscie = input()
        wejscie = wejscie.split()
        if wejscie[0] == "EXIT":
            continuation = True
        elif wejscie[0] == "ADD":
            checktable = checktable | hashfunction(wejscie[1])
        elif wejscie[0] == "SHOW":
            print(checktable)
        elif wejscie[0] == "CHECK":
            if (hashfunction(wejscie[1]) & checktable == hashfunction(wejscie[1])).all():
                print("Wynik jest w tabeli")
            else:
                print("Wyniku nie ma w tabeli")
        else:
            print("Nieznana Operacja")

def hashfunction(word):
    suma = 0
    hashtable = np.zeros(12,dtype=int)
    for i in range(0, len(word)):
        suma += ord(word[i])
    for i in range(1,13):
        if suma%i == 0:
            hashtable[i] = 1
    return hashtable

if __name__ == "__main__":
    main()