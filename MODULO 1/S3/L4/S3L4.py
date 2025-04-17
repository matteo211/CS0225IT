import string
import base64
import codecs

# primo approccio: sviluppo una funzione che prova a decifrare un cifrario di cesare, provando tutte le cifre da 1 a max
def decripta_per_sostituzione(key, cripted):
    decripted = ""

    for char in cripted:
        decripted += trasla_char(char, key)

    return decripted

# trasforma il carattere in un numero, trasla di quantity, e trasforma il numero in carattere
def trasla_char(char, quantity):
    return chr(ord(char) - quantity)

max = len(string.ascii_uppercase)

stringa_criptata_1 = "HSNFRGH"
stringa_criptata_2 = "QWJhIHZ6b2VidHl2bmdyIHB1ciB6ciBhciBucHBiZXRi"

for key in range(1, max + 1):
    print(f"with key: {key} -> {decripta_per_sostituzione(key, stringa_criptata_1)}")

# KEY: 3 -> EPKCODE (ipotesi piu' veritiera)

# la seconda stringa sembra essere codificata in base 64
str2_base64_decoded = base64.b64decode(stringa_criptata_2).decode("utf-8")

# proviamo uno shift di 13 
str2_rot13_decoded = codecs.decode(str2_base64_decoded, "rot-13")

# messaggio in chiaro
print(str2_rot13_decoded)
