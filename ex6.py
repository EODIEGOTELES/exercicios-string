# Solicita ao usuário para digitar uma frase
frase = input("Digite uma frase: ")

# Converte para minúsculo para facilitar a busca (case insensitive)
frase_minuscula = frase.lower()

# Conta quantas letras 'a' aparecem na frase
quantidade_a = frase_minuscula.count('a')

# Encontra a primeira posição onde 'a' aparece
primeira_posicao = frase_minuscula.find('a')

# Encontra a última posição onde 'a' aparece
ultima_posicao = frase_minuscula.rfind('a')

# Exibe os resultados
print(f"\nFrase digitada: {frase}")
print(f"Quantidade de letras 'a': {quantidade_a}")

if primeira_posicao != -1:
    print(f"Primeira posição que 'a' aparece: {primeira_posicao + 1}° caractere")
else:
    print("A letra 'a' não foi encontrada na frase")

if ultima_posicao != -1:
    print(f"Última posição que 'a' aparece: {ultima_posicao + 1}° caractere")
else:
    print("A letra 'a' não foi encontrada na frase")