import random

def escolher_palavra():
    palavras = ["python", "computador", "programacao", "forca", "teclado"]
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_certas):
    return ' '.join([letra if letra in letras_certas else '_' for letra in palavra])

def jogar_forca():
    palavra = escolher_palavra()
    letras_certas = set()
    letras_erradas = set()
    tentativas = 6

    print("🎮 Bem-vindo ao Jogo da Forca!\n")

    while tentativas > 0:
        print(f"\nPalavra: {mostrar_palavra(palavra, letras_certas)}")
        print(f"Letras erradas: {', '.join(sorted(letras_erradas))}")
        print(f"Tentativas restantes: {tentativas}")
        
        tentativa = input("Digite uma letra: ").lower()

        if not tentativa.isalpha() or len(tentativa) != 1:
            print("⚠️ Digite apenas uma letra.")
            continue

        if tentativa in letras_certas or tentativa in letras_erradas:
            print("⚠️ Você já tentou essa letra.")
            continue

        if tentativa in palavra:
            letras_certas.add(tentativa)
            print("✅ Acertou!")
        else:
            letras_erradas.add(tentativa)
            tentativas -= 1
            print("❌ Errou!")

        if all(letra in letras_certas for letra in palavra):
            print(f"\n🎉 Parabéns! Você acertou a palavra: {palavra}")
            break
    else:
        print(f"\n💀 Você perdeu! A palavra era: {palavra}")

# Executa o jogo
if __name__ == "__main__":
    jogar_forca()
