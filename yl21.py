import random

def arva_arv():
    arvuti_arv = random.randint(0, 100)
    katsete_arv = 0

    while True:
        kasutaja_pakkumine = int(input("Paku arv 0-st 100-ni: "))
        katsete_arv += 1

        if kasutaja_pakkumine < arvuti_arv:
            print("Pakkumine on liiga väike. Proovi uuesti.")
        elif kasutaja_pakkumine > arvuti_arv:
            print("Pakkumine on liiga suur. Proovi uuesti.")
        else:
            print(f"Õige arv! Arvuti mõtles arvu {arvuti_arv}. Sa pakkusid õigesti {katsete_arv}ndal korral.")
            break

if __name__ == "__main__":
    arva_arv()