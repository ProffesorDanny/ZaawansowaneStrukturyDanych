def main():
    # Inicjalizacja: QuadTree potrzebuje obszaru (Rectangle)
    # Tworzymy obszar od -100 do 100 w obu osiach (środek 0,0, szer/2=100, wys/2=100)
    boundary = Rectangle(0, 0, 100, 100)
    qt = QuadTree(boundary, capacity=4)

    running = True
    print("System QuadTree gotowy. Komendy: INSERT x y [data], SEARCH x y, QUERY x y w h, DELETE x y, EXIT")

    while running:
        try:
            line = input("> ").split()
            if not line:
                continue

            command = line[0].upper()

            if command == "EXIT":
                running = False

            elif command == "INSERT":
                x, y = float(line[1]), float(line[2])
                data = line[3] if len(line) > 3 else None
                p = Point(x, y, data)
                if qt.insert(p):
                    print(f"Dodano punkt ({x}, {y})")
                else:
                    print("Punkt poza granicami drzewa!")

            elif command == "SEARCH":
                x, y = float(line[1]), float(line[2])
                search_area = Rectangle(x, y, 0.001, 0.001)
                found = qt.query(search_area)
                if found:
                    print(f"Znaleziono: {found[0].data} na pozycji ({found[0].x}, {found[0].y})")
                else:
                    print("Nie ma takiego punktu.")


            elif command == "QUERY":
                if len(line) < 5:
                    print("Błąd: Wymagane parametry: QUERY x y w h")
                    continue
                x, y, w, h = map(float, line[1:5])
                area = Rectangle(x, y, w, h)
                results = qt.query(area)
                if results:
                    print(f"Znaleziono {len(results)} punktów w obszarze [{x - w}, {x + w}] x [{y - h}, {y + h}]:")
                    for p in results:
                        dane = f" (dane: {p.data})" if p.data else ""
                        print(f"  • Punkt({p.x}, {p.y}){dane}")
                else:
                    print("Brak punktów w podanym obszarze.")
            elif command == "DELETE_AREA":
                if len(line) < 5:
                    print("Błąd: Wymagane parametry: DELETE_AREA x y w h")
                    continue
                x, y, w, h = map(float, line[1:5])
                area = Rectangle(x, y, w, h)
                #result = tu wpisz wywołanie funkcji i ewentualnie dopisz jakieś potwierdzenie


            elif command == "DELETE":
                x, y = float(line[1]), float(line[2])
                if qt.delete(Point(x, y)):
                    print("Usunięto punkt.")
                else:
                    print("Nie znaleziono punktu do usunięcia.")
            else:
                print("Nieznana operacja.")

        except (IndexError, ValueError):
            print("Błąd: Niepoprawna liczba argumentów lub format danych.")
        except Exception as e:
            print(f"Wystąpił błąd: {e}")

class Point:
    def __init__(self, x, y, data=None):
        self.x = x
        self.y = y
        self.data = data  # Dodatkowe dane, np. obiekt gracza, nazwa miasta


class Rectangle:
    """Reprezentuje prostokątny obszar. x, y to ŚRODEK prostokąta. w, h to POŁOWA szerokości i wysokości."""

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def contains(self, point):
        """Sprawdza, czy punkt znajduje się w tym obszarze."""
        return (self.x - self.w <= point.x <= self.x + self.w and
                self.y - self.h <= point.y <= self.y + self.h)

    def intersects(self, other_rect):
        """Sprawdza, czy ten prostokąt przecina się z innym. Służy do optymalizacji wyszukiwania."""
        return not (other_rect.x - other_rect.w > self.x + self.w or
                    other_rect.x + other_rect.w < self.x - self.w or
                    other_rect.y - other_rect.h > self.y + self.h or
                    other_rect.y + other_rect.h < self.y - self.h)


class QuadTree:
    def __init__(self, boundary, capacity=4):
        self.boundary = boundary  # Obiekt Rectangle
        self.capacity = capacity  # Ile punktów mieści się zanim nastąpi podział
        self.points = []  # Punkty przechowywane w TYM węźle (tylko dla liści)
        self.divided = False  # Czy węzeł podzielił się na 4 dzieci?

        # Wskaźniki na dzieci (NW = Północny-Zachód, itd.)
        self.nw = None
        self.ne = None
        self.sw = None
        self.se = None

    def subdivide(self):
        """Dzieli węzeł na 4 równe ćwiartki."""
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w / 2
        h = self.boundary.h / 2
        self.nw = QuadTree(Rectangle(x - w, y + h, w, h), self.capacity)
        self.ne = QuadTree(Rectangle(x + w, y + h, w, h), self.capacity)
        self.sw = QuadTree(Rectangle(x - w, y - h, w, h), self.capacity)
        self.se = QuadTree(Rectangle(x + w, y - h, w, h), self.capacity)
        self.divided = True

    def insert(self, point):
        """Dodaje punkt do drzewa."""
        # 1. Ignoruj, jeśli punkt jest poza granicami
        if not self.boundary.contains(point):
            return False

        # 2. Zabezpieczenie przed duplikatami (zapobiega nieskończonej rekurencji)
        for p in self.points:
            if p.x == point.x and p.y == point.y:
                p.data = point.data  # Aktualizujemy dane zamiast tworzyć nową gałąź
                return True

        # 3. Jeśli węzeł ma miejsce i nie jest podzielony - dodaj punkt
        if len(self.points) < self.capacity and not self.divided:
            self.points.append(point)
            return True

        # 4. Jeśli nie ma miejsca, a węzeł nie jest podzielony - podziel go
        if not self.divided:
            self.subdivide()
            # Przenieś istniejące punkty z tego węzła do jego nowych dzieci
            for p in self.points:
                self._insert_into_children(p)
            self.points = []  # Opróżnij ten węzeł, staje się węzłem wewnętrznym

        # 5. Przekaż nowy punkt niżej do odpowiedniego dziecka
        return self._insert_into_children(point)

    def _insert_into_children(self, point):
        """Metoda pomocnicza wrzucająca punkt do pierwszej pasującej ćwiartki."""
        return (self.nw.insert(point) or self.ne.insert(point) or
                self.sw.insert(point) or self.se.insert(point))

    def query(self, range_rect, found=None):
        """Zwraca wszystkie punkty w danym prostokątnym obszarze."""
        if found is None:
            found = []

        # Optymalizacja: Jeśli obszar wyszukiwania nie przecina się z tym węzłem, przerwij
        if not self.boundary.intersects(range_rect):
            return found

        if not self.divided:
            for p in self.points:
                if range_rect.contains(p):
                    found.append(p)
        else:
            # Szukaj głębiej we wszystkich dzieciach
            self.nw.query(range_rect, found)
            self.ne.query(range_rect, found)
            self.sw.query(range_rect, found)
            self.se.query(range_rect, found)

        return found

    def delete(self, point):
        """Usuwa punkt. Zwraca True, jeśli się udało."""
        if not self.boundary.contains(point):
            return False

        if not self.divided:
            for i, p in enumerate(self.points):
                if p.x == point.x and p.y == point.y:
                    del self.points[i]
                    return True
            return False
        else:
            # Próbuj usunąć z dzieci
            deleted = (self.nw.delete(point) or self.ne.delete(point) or
                       self.sw.delete(point) or self.se.delete(point))

            # Jeśli usunięto, sprawdź, czy można "zwinąć" puste węzły
            if deleted:
                self._collapse()

            return deleted

    def _collapse(self):
        """Zwinie węzeł (połączy dzieci w jeden liść), jeśli suma punktów we wszystkich dzieciach mieści się w limicie."""
        if not self.divided:
            return

        total_points = self._get_all_points()

        # Jeśli punkty ze wszystkich dzieci zmieszczą się w jednym węźle
        if len(total_points) <= self.capacity:
            self.points = total_points
            self.divided = False
            self.nw = self.ne = self.sw = self.se = None

    def _get_all_points(self):
        """Rekurencyjnie zbiera wszystkie punkty z tego węzła i jego dzieci."""
        if not self.divided:
            return self.points
        return (self.nw._get_all_points() + self.ne._get_all_points() +
                self.sw._get_all_points() + self.se._get_all_points())

if __name__ == "__main__":
    print(f"""
            Instrukcja obsługi QuadTree:
            ---------------------------
            EXIT                     - wyjdź z programu
            INSERT x y [opis]        - dodaj punkt o współrzędnych x, y
            SEARCH x y               - sprawdź, czy punkt istnieje w danej lokalizacji
            QUERY x y w h            - szukaj punktów w obszarze (środek x,y i zasięg w,h)
            DELETE x y               - usuń punkt z podanej lokalizacji
            DELETE_AREA x y w h      - usuń wszystkie punkty z obszaru      
            ---------------------------
            Uwaga: Współrzędne podawaj jako liczby (np. 10.5 20)""")
    main()