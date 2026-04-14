Zadanie 1 

W pliku z kodem zaimplementowany jest prosty filtr blooma z jedną funkcją haszującą złożoną z operacji modulo. Przeanalizuj kod i wpisz do filtru jakieś dane 
(ze względu na ilość "kubełków" w filtrze zalecamy używania trójznakowych słów). Wpisz jakieś przykładowe dane i zobacz jak zachowa się nasz filtr. Zobacz kiedy się
myli i spróbuj zlokalizować jego podatności:
-zwróć uwagę na to jak funkcja przyporządkowuje słowom wartości
-wobacz jak wygląda proces operacji modulo, czy formułowanie go w podany sposób, to dobry pomysł?

Jak mogłeś już zobaczyć funkcja haszująca jest napisana w sposób nieoptymalny, spróbuj ją poprawić, aby choć trochę zmniejszyć prawdopodobieństwo pomyłki filtru
Podczas modyfikacji postaraj się nie odchodzić za bardzo od struktury funkcji haszującej. Nie chodzi tu przecież o napisanie jej od nowa, ale o wprowadzenie
drobnych poprawek, które zwiększą skuteczność filtru.

Zadanie 2

Podany mamy przykład implementacji drzewa Merkla korzystające z funkcji hashującej wykorzystującej szyfrowanie AES, ale w dość nietypowy sposób. Szyfrowane są
pewne transakcje między klientami w formacie do odczytywania przez jakiś algorytm lub maszynę, ale też czytelne dla człowieka
-zastanów się, czy istnieje możliwość zmiany danych w sposób, aby sama struktura drzewa pozostała niezmieniona
-jeżeli tak, to jakie mogą być konsekwencje tego niedociągnięcia
-popraw funkcję hashującą tak, aby uniknąć sytuacji. Znowu nie musi być to jakaś skomplikowana poprawka (tak naprawdę wystarczą 2-3 linijki kodu) 

Zadanie 3

W zadaniu umieszczony jest kod z wykładu dotyczący drzew Prefiksowych. Dodany do niego jest prosty fragment kodu, który pozwoli na interakcję z drzewem za pomocą konsoli
-dla przykładu dodana została funkcja wyszukująca najkrótszy wyraz. Może będzie ona jakimś punktem odniesienia (dodam ją w najbliższym czasie)
-do istniejących funkcji dopisz jedną pozwalającą na wypisanie najdłuższego z wyrazów
-dodaj też funkcję, która pozwoli usunąć wyraz z tabeli, zwróć uwagę na to, że niektóre wyrazy mogą być wyrazami ze wspólnej rodziny jak zwierzę i zwierzęta. Weź to pod uwagę.

Zadanie 4

Mamy tym razem przykład implementacji drzew czwórkowych. Zadaniem znowu będzie dodanie funkcji usuwającej, tym razem punkty z zaznaczonego obszaru.
Jako że kod jest dość długi i może być lekko ciężko szybko przeanalizować, to podczas pisania funkcji zwróć uwagę na kilka rzeczy
-przydatna będzie tu funkcja querry, która znajduje punkty w danym obszarze i zwraca ich współrzędne 
-zaimlementowan jest też funkcja delete, która usuwa, ale jeden konkretny punkt o podanych współrzędnych
-spróbuj połączyć te dwie funkcje i rozwiązać zadanie