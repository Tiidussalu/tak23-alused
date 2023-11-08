tekst = "mulle meeldivad mõrud jäätised krõbedate äärtega"

taishaalikud_arv = 0

taishaalikud = "aeiouõäöü"

tekst = tekst.lower()

for taht in tekst:
    if taht in taishaalikud:
        taishaalikud_arv += 1

print("Täishäälikuid on tekstis:", taishaalikud_arv)