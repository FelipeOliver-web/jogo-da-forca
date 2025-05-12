import random
import tkinter as tk
from tkinter import messagebox

def escolher_palavra():
    palavras = ["python", "computador", "programacao", "forca", "teclado"]
    return random.choice(palavras)

def atualizar_palavra():
    palavra_display = ''.join([letra if letra in letras_certas else '_' for letra in palavra])
    palavra_label.config(text=" ".join(palavra_display))

def tentar_letra():
    letra = letra_entry.get().lower()
    letra_entry.delete(0, tk.END)

    if len(letra) != 1 or not letra.isalpha():
        messagebox.showerror("Erro", "Por favor, digite apenas uma letra!")
        return

    if letra in letras_certas or letra in letras_erradas:
        messagebox.showwarning("Aviso", "Você já tentou essa letra.")
        return

    if letra in palavra:
        letras_certas.add(letra)
        atualizar_palavra()
        if all(letra in letras_certas for letra in palavra):
            messagebox.showinfo("Parabéns", "Você venceu!")
    else:
        letras_erradas.add(letra)
        tentativas_restantes.set(tentativas_restantes.get() - 1)
        if tentativas_restantes.get() == 0:
            messagebox.showinfo("Fim de jogo", f"Você perdeu! A palavra era: {palavra}")
            reiniciar_jogo()

def reiniciar_jogo():
    global palavra, letras_certas, letras_erradas
    palavra = escolher_palavra()
    letras_certas = set()
    letras_erradas = set()
    tentativas_restantes.set(6)
    atualizar_palavra()

root = tk.Tk()
root.title("Jogo da Forca")

letras_certas = set()
letras_erradas = set()
tentativas_restantes = tk.IntVar(value=6)
palavra = escolher_palavra()

palavra_label = tk.Label(root, text=" ".join(["_" for _ in palavra]), font=("Arial", 24))
palavra_label.pack(pady=20)

letra_entry = tk.Entry(root, font=("Arial", 20), width=5)
letra_entry.pack(pady=10)


tentar_button = tk.Button(root, text="Tentar", font=("Arial", 18), command=tentar_letra)
tentar_button.pack(pady=10)

tentativas_label = tk.Label(root, textvariable=tentativas_restantes, font=("Arial", 18))
tentativas_label.pack(pady=10)

reiniciar_button = tk.Button(root, text="Reiniciar", font=("Arial", 18), command=reiniciar_jogo)
reiniciar_button.pack(pady=20)

reiniciar_jogo()

root.mainloop()