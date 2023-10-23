a = float(input("Sisesta esimese külje pikkus: "))
b = float(input("Sisesta teise külje pikkus: "))
c = float(input("Sisesta kolmanda külje pikkus: "))
if a + b > c and c + b > a and c + a > b:
  if a == b and b == c and c == a:
    print("Kolmnurk on võrdkülgne")
  elif a == b or b == c or c == a:
    print("Kolmnurk on võrdhaardne")
else:
    print("ei eksisteeri")