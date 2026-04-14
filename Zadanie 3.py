def main(trie):
    continuation = False
    while not continuation:
        consoleIn = input()
        consoleIn = consoleIn.split()
        if consoleIn[0] == "EXIT":
            continuation = True
        elif consoleIn[0] == "INSERT":
            trie.insert(consoleIn[1])
        elif consoleIn[0] == "SEARCH":
            if trie.search(consoleIn[1]):
                print("Wyraz jest w tabeli")
            else:
                print("Wyrazu nie ma w tabeli")
        elif consoleIn[0] == "PREFIX":
            if trie.isPrefix(consoleIn[1]):
                print("Prefix jest w tabeli")
            else:
                print("Prefixu nie ma w tabeli")
        elif consoleIn[0] == "DELETE":
            pass
        elif consoleIn[0] == "NAJDLUZSZY":
            pass #POLECAM JAKĄŚ REKURENCJE
        else:
            print("Nieznana Operacja")


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                new_node = TrieNode()
                curr.children[index] = new_node
            curr = curr.children[index]
        curr.isEndOfWord = True

    def search(self, key):

        curr = self.root

        for c in key:

            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False

            curr = curr.children[index]

        return curr.isEndOfWord

    def isPrefix(self, prefix):
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True

if __name__ == "__main__":
    trie = Trie()
    #Wypełnienie kodu przykładowymi Stringami
    words = ["anakonda", "banan", "banonowiec", "ala", "bieda","biolgi","biologiczny"]
    for word in words:
        trie.insert(word)
    print(f"""
        Instrukcja obsługi programu:
        ---------------------------
        EXIT - wyjdź z programu
        INSERT (wyraz) - dodaj nowy wyraz
        SEARCH (wyraz) - sprawdź podany wyraz
        PREFIX (wyraz) - sprawdź podany prefix
        DELETE (wyraz) - usuwa wyraz z listy
        NAJDLUZSZY - zwraca najdłuższy wyraz
        ---------------------------
        Uwaga: Nie używaj polskich znaków""")
    main(trie)