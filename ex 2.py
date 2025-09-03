nm = input("digite seu nome ae: ").strip()

print(f"Nome em maiuscula: {nm.upper()}")
print(f"Nome em minuscula: {nm.lower()}")

lt = len(nm.replace("", ""))
print(f"Total de letras no nome: {lt}")

pn = nm.split()[0]
print(f"Seu primeiro nome tem {len(pn)} letras.")

