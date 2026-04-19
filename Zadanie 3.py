


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
            trie.delete(consoleIn[1])
            print("Usunięto zbędną zawartość")
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

    def delete(self, key, curr=None, depth=0):

        if curr is None:
            curr = self.root

        if depth == len(key):
            if not curr.isEndOfWord:
                return False

            curr.isEndOfWord = False
            if all(c is None for c in curr.children):
                return True
            return False

        index = ord(key[depth]) - ord('a')
        child_node = curr.children[index]

        if child_node is None:
            return False

        should_delete_child = self.delete(key, child_node, depth + 1)

        if should_delete_child:
            curr.children[index] = None
            return not curr.isEndOfWord and all(c is None for c in curr.children)

        return False



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