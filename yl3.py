n = int(input("Sistestage täisarv vahemikus 1-9: "))

if n < 1 or n > 9:
    print("Sisestatud arv ei ole vahemikus 1-9.")
    else:
        nn = n * 10 + n
        nnn = nn * 10 + n
        tulemus = n + nn + nnn
        print(f"{n} + {nn} + {nnn} = {tulemus}")