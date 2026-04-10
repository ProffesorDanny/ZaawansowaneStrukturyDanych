from Crypto.Cipher import AES
#Funkcja hashująca
def my_hash_function(server_key, message):
    cipher = AES.new(server_key, AES.MODE_ECB)
    if len(message) % 16 != 0:
        message += b'\x00' * (16 - len(message) % 16)
    hash_int = 0
    for i in range(0, len(message), 16):
        block = message[i:i + 16]
        en_block = cipher.encrypt(block)
        block_int = int.from_bytes(en_block, 'big')
        hash_int ^= block_int
    return hash_int.to_bytes(16, 'big')

#Funkcja do formowania drzewa
def form_merkel_tree(transactions, key):
    merkletree = []
    length = len(transactions)
    index = 0
    for transaction in transactions:
        merkletree.append(my_hash_function(key, transaction))
    while length > 1:
        if length%2 ==1:
            merkletree.append(merkletree[-1])
            length += 1
        for i in range(0, length, 2):
            combination = merkletree[index+i]+merkletree[index+i+1]
            merkletree.append(my_hash_function(key,combination))
        index += length
        length = length//2
    return merkletree

#Funkcja pokazująca drzewo (4 pierwsze znaki hasha)
def show_merkle_tree_exceptions(merkletree):
    idx = len(merkletree) - 1
    level = 0
    try:
        while idx >= 0:
            nodes_on_level = 2 ** level
            current_level_strings = []
            for _ in range(nodes_on_level):
                if idx < 0:
                    raise IndexError
                h = merkletree[idx].hex()[:4]
                current_level_strings.append(f"[{h}]")
                idx -= 1
            line = "  ".join(reversed(current_level_strings))
            print(line.center(80))
            if idx >= 0:
                print("/ \\".center(80))
            level += 1
    except IndexError:
        print("-" * 80)
        print("Koniec drzewa.")


#Program szyfrujący tranzakcje
server_key = "aaaaaaaaaaaaaaaa".encode('utf-8')
TRANSACTIONS = [
        " Od:PL10101010101010101010101010 Do:PL20202020202020202020202020",
        " Od:PL11111111111111111111111111 Do:PL21212121212121212121212121",
        " Od:PL12121212121212121212121212 Do:PL22222222222222222222222222",
        " Od:PL13131313131313131313131313 Do:PL23232323232323232323232323",
        " Od:PL14141414141414141414141414 Do:PL24242424242424242424242424",
        " Od:PL15151515151515151515151515 Do:PL25252525252525252525252525",
        " Od:PL16161616161616161616161616 Do:PL26262626262626262626262626",
        " Od:PL17171717171717171717171717 Do:PL27272727272727272727272727",
        " Od:PL18181818181818181818181818 Do:PL28282828282828282828282828",
        " Od:PL19191919191919191919191919 Do:PL29292929292929292929292929",
        " Od:PL20202020202020202020202020 Do:PL30303030303030303030303030",
        " Od:PL21212121212121212121212121 Do:PL31313131313131313131313131",
        " Od:PL22222222222222222222222222 Do:PL32323232323232323232323232",
        " Od:PL23232323232323232323232323 Do:PL33333333333333333333333333",
        " Od:PL24242424242424242424242424 Do:PL34343434343434343434343434",
        " Od:PL25252525252525252525252525 Do:PL35353535353535353535353535",
    ]

binary_messages = [m.encode('utf-8') for m in TRANSACTIONS]
tree = form_merkel_tree(binary_messages, server_key)
show_merkle_tree_exceptions(tree)
