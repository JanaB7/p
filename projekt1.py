'''
projekt_1

author: Jana Boucníková
email: boucnikova.j@gmail.com
discord: jana4555
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
cara = "-" * 28
uzivatel = input("Enter your name: ")
if uzivatel in uzivatele:
    heslo = input("Enter your password: ")
    print(cara)
    if uzivatele[uzivatel] == heslo:
        print(f" Welcome to the app, {uzivatel}.")
    else:
        print("Wrong password")
        quit()
else:
    print(f"{uzivatel} is not registered, terminating program.")
    quit()


pocet_textu = len(TEXTS)
print(f"Nr. of text to analyze: {pocet_textu}\n{cara}")

cislo_textu = input("Enter a nr. of text  btw. 1 and 3 to select:")
print(cara)
if cislo_textu.isnumeric():
    index = int(cislo_textu)
    if 1 <= index <= len(TEXTS):
        text = TEXTS[index -1].strip(",.!")
        slova = text.split()
        pocet_slov = len(slova)
        title_pismena = 0
        velka_slova = 0
        mala_slova = 0
        cisla = 0
        soucet_cisel = 0
        for slovo in slova:
            if slovo.istitle(): 
                title_pismena += 1
            if slovo.isupper() and slovo.isalpha():
                velka_slova += 1
            if slovo.islower():
                mala_slova += 1
            if slovo.isnumeric():
                cisla += 1
                soucet_cisel += int(slovo)
print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {title_pismena} titlecase words.")
print(f"There are {velka_slova} uppercase words.")
print(f"There are {mala_slova} lowercase words.")
print(f"There are {cisla} numeric strings")
print(f"The sum of all the numbers {soucet_cisel}")
cetnosti = {}
for slovo in text.strip(",.?:/").split():
    delka = len(slovo)
    cetnosti[delka] = cetnosti.get(delka, 0) + 1

max_cetnost = max(cetnosti.values())

print(f"{cara}\n LEN| OCCURENCES | NR.")
print(cara)

for delka in range (1, max_cetnost + 1):
    cetnost = cetnosti.get(delka, 0)
    oc = "*" * cetnost
    print(f"{delka:2d}|{oc:13s}|{cetnost}")

