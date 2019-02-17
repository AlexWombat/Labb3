
from bintreeFile import Bintree
svenska = Bintree()

with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()
        if ordet in svenska:
            print(ordet, end=" ")
        else:
            svenska.put(ordet)
print("\n")
engelska = Bintree()
with open("engelska.txt", "r", encoding="utf-8") as engelskfil:
    text = engelskfil.read()
    words = text.split()
    for word in words:
        if word not in engelska:
            engelska.put(word)         # sorterar in engelska ord i trädet (inga dubletter)
            if word in svenska:        # printar ut alla ord som är samma som de svenska
                print(word, end=' ')





