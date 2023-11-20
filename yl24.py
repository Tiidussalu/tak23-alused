koosta_dict = {
    "eesnimi": "Koosta",
    "perenimi": "Koostane",
    "sünniaasta": 1990,
    "elukoht": "Tallinn",
    "lemmik_magustoit": "Šokolaadikook",
}

print("Elukoht (get meetod):", koosta_dict.get("elukoht"))
print("Elukoht (ilma get meetodita):", koosta_dict["elukoht"])

koosta_dict["lemmik_magustoit"] = "Pannkoogid"

print("Kõik võtmed:", koosta_dict.keys())

print("Kõik väärtused (meetod 1):", koosta_dict.values())
print("Kõik väärtused (meetod 2):", list(koosta_dict.values()))
print("Kõik väärtused (meetod 3):", [value for value in koosta_dict.values()])

isikukood_olemas = "isikukood" in koosta_dict
print("Isikukood olemas:", isikukood_olemas)

dictionary_suurus = len(koosta_dict)
print("Dictionary suurus:", dictionary_suurus)

koosta_dict["pikkus"] = 180

del koosta_dict["sünniaasta"]

print("Uuendatud dictionary:", koosta_dict)