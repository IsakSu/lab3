from bintreeFile import Bintree
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()           # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ")
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")

engelska = Bintree()
with open("english.txt", "r", encoding = "utf-8") as engfil:
    for rad in engfil:
        for i in range(len(rad.split())):
            ordet = rad.split()[i].strip('".,')         # Ett trebokstavsord per rad
            if ordet in engelska:
                break
            else:
                if(len(ordet) == 3):
                    if ordet in svenska:
                        print(ordet, end = " ")
                engelska.put(ordet)             # in i sökträdet
print("\n")
