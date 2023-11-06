failname = input("Sisesta failinimi koos laiendiga (näiteks failinimi.ext): ")

parts = failname.split(".")

if len(parts) > 1:
    laiend = osad[-1]
    print("Faililaiend on:", laiend)
else:
    print("Faililaiendit ei leitud.")