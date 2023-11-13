tekst = input("Sisesta tekst, millest saaksin kokku korjata kõik täishäälikud: ")

taishaalikud_arv = 0

taishaalikud = "aeiouõäöü"

tekst = tekst.lower()

for taht in tekst:
    if taht in taishaalikud:
        taishaalikud_arv += 1

print("Täishäälikuid on tekstis:", taishaalikud_arv)
