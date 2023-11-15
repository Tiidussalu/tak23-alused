import random

def kivi_paber_kaared_mang(kasutaja_valik):
    võimalused = ["kivi", "paber", "käärid"]
    arvuti_valik = random.choice(võimalused)

    print(f"Arvuti valis: {arvuti_valik}")

    if kasutaja_valik == arvuti_valik:
        return "Viik!"
    elif (kasutaja_valik == "kivi" and arvuti_valik == "käärid") or \
         (kasutaja_valik == "paber" and arvuti_valik == "kivi") or \
         (kasutaja_valik == "käärid" and arvuti_valik == "paber"):
        return "Kasutaja võitis!"
    else:
        return "Arvuti võitis!"

def main():
    while True:
        kasutaja_valik = input("Vali kivi, paber või käärid: ").lower()

        if kasutaja_valik not in ["kivi", "paber", "käärid"]:
            print("Vigane valik.")
            continue

        tulemus = kivi_paber_kaared_mang(kasutaja_valik)
        print(tulemus)

if __name__ == "__main__":
    main()
    