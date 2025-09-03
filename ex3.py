cidade = input("Digite o nome de uma cidade: ").strip()

# Verifica se começa com "Santo" (sem considerar maiúsculas/minúsculas)
if cidade[:5].lower() == "santo":
    print("A cidade começa com 'Santo'.")
else:
    print("A cidade NÃO começa com 'Santo'.")