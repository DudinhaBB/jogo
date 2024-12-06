import random

# Lista de palavras
palavras = ["python", "programacao", "jogo", "forca", "desenvolvimento"]

# Função para definir o número de tentativas com base na dificuldade
def escolher_dificuldade():
    print("Escolha a dificuldade:")
    print("1 - Fácil (8 tentativas)")
    print("2 - Médio (6 tentativas)")
    print("3 - Difícil (4 tentativas)")
    dificuldade = input("Digite o número da dificuldade: ")
    
    if dificuldade == "1":
        return 8
    elif dificuldade == "2":
        return 6
    elif dificuldade == "3":
        return 4
    else:
        print("Opção inválida. Usando a dificuldade média por padrão.")
        return 6

# Escolher dificuldade
tentativas = escolher_dificuldade()

# Escolha aleatória de palavra
palavra = random.choice(palavras)
letras_corretas = ["_"] * len(palavra)
letras_erradas = []

print("Bem-vindo ao Jogo da Forca!")
print(f"Você tem {tentativas} tentativas para adivinhar a palavra.")

while tentativas > 0 and "_" in letras_corretas:
    print("\nPalavra:", " ".join(letras_corretas))
    print(f"Tentativas restantes: {tentativas}")
    print(f"Letras erradas: {', '.join(letras_erradas)}")
    
    letra = input("Digite uma letra: ").lower()
    
    if letra in palavra:
        for idx, char in enumerate(palavra):
            if char == letra:
                letras_corretas[idx] = letra
        print("Boa! Letra correta!")
    else:
        tentativas -= 1
        letras_erradas.append(letra)
        print("Ops! Letra incorreta.")
    
if "_" not in letras_corretas:
    print("\nParabéns! Você venceu!")
    print(f"A palavra era: {palavra}")
else:
    print("\nVocê perdeu! Suas tentativas acabaram.")
    print(f"A palavra era: {palavra}")
