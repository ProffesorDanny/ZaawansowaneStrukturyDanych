Zadanie 1 

W pliku z kodem zaimterpretowany jest prosty filtr blooma z jedną funkcją haszującą złożoną z operacji modulo. Przeanalizuj kod i wpisz do filtru jakieś dane 
(ze względu na ilość "kubełków w filtrze zalecamy używania trójnakowych słów). Wpisz jakieś przykładowe dane i zobacz jak zachwa się nasz filtr. Zobacz kiedy się
myli i spróbuj zlokalizować jego podatności:
-zwróć uwagę na to jak funkcja przyporządkowywuje słowom wartości
-wobacz jak wygląda proces operacji modulo, czy formułowanie go w podany sposób, to dobry pomysł?

Jak mogłeś już zobaczyć funkcja haszująca jest napisana w sposób nieoptymalny, spróbuj ją poprawić, aby choć trochę zmniejszyć prawdopodobieństwo pomyłki filtru
Podczas modyfikacji postaraj się nie odchodzić za bardzo od struktury funkcji haszującej. Nie chodzi tu przecierz o napisanie jej od nowa, ale o wprowadzenie
drobnych poprawek, które zwiększą skuteczność fitru.

Zadanie 2

Podany Mamy przykład implementacji drzewa Merkla korzystające z funkcji hashującej wykorzystującej szyfrowanie AES, ale w dość nietypowy sposób. Szyfrowane są
pewne tranzakcje między klientami w formacie do odczytywania przez jakiś algorytm lub maszyne, ale też czytelne dla człowieka
-zastanów się, czy istnieje możliwość zmiany danych w sposób, aby sama struktura drzewa pozostała niezmieniona
-jeżeli tak, to jakie mogą być konsekwencje tego niedociągnięcia
-popraw funkcję hashującą tak, aby uniknąć sytuacji. Znowu nie musi być to jakaś skomplikowana poprawka (tak na prawdę wystarczą 2-3 linijki kodu) 
