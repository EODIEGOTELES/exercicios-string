nome = input("Digite seu nome: ").strip()
print("Nome em maiúsculo:", nome.upper())
print("Nome em minúsculo:", nome.lower())
print("Quantidade de letras: ", len(nome.replace(" ","" )))
primeiro_nome = nome.split()[0]
print("Quantidade de letras no primeiro nome: ",len(primeiro_nome))