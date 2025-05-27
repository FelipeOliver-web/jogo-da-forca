import random
import tkinter as tk
from tkinter import messagebox

def escolher_palavra():
    palavras = ["python", "computador", "programacao", "forca", "teclado"]
    return random.choice(palavras)

def atualizar_palavra():
    palavra_display = ''.join([letra if letra in letras_certas else '_' for letra in palavra])
    palavra_label.config(text=" ".join(palavra_display))
    letras_erradas_label.config(text="Letras erradas: " + ' '.join(sorted(letras_erradas)))  # felipe: exibir letras erradas
    desenhar_forca()  # felipe: atualizar boneco a cada tentativa errada

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
            desativar_jogo()  # felipe: desativa o jogo após vitória
    else:
        letras_erradas.add(letra)
        tentativas_restantes.set(tentativas_restantes.get() - 1)
        atualizar_palavra()
        if tentativas_restantes.get() == 0:
            messagebox.showinfo("Fim de jogo", f"Você perdeu! A palavra era: {palavra}")
            desativar_jogo()  # felipe: desativa o jogo após derrota

def desativar_jogo():
    letra_entry.config(state="disabled")  # felipe: desativa entrada de texto
    tentar_button.config(state="disabled")  # felipe: desativa botão

def reiniciar_jogo():
    global palavra, letras_certas, letras_erradas
    palavra = escolher_palavra()
    letras_certas = set()
    letras_erradas = set()
    tentativas_restantes.set(6)
    letra_entry.config(state="normal")  # felipe: reativa entrada
    tentar_button.config(state="normal")  # felipe: reativa botão
    canvas.delete("all")  # felipe: limpa canvas
    desenhar_base()  # felipe: redesenha forca
    atualizar_palavra()

def desenhar_base():
    canvas.create_line(20, 180, 120, 180)  # felipe: base da forca
    canvas.create_line(70, 180, 70, 20)    # felipe: poste vertical
    canvas.create_line(70, 20, 150, 20)    # felipe: barra superior
    canvas.create_line(150, 20, 150, 40)   # felipe: corda

def desenhar_forca():
    erros = 6 - tentativas_restantes.get()

    if erros >= 1:
        # Cabeça com cor de pele
        canvas.create_oval(135, 40, 165, 70, fill="#ffe0bd")  # felipe: cabeça com cor

        # Olhos
        canvas.create_oval(142, 48, 146, 52, fill="black")  # felipe: olho esquerdo
        canvas.create_oval(154, 48, 158, 52, fill="black")  # felipe: olho direito

        # Boca
        if tentativas_restantes.get() > 0:
            canvas.create_arc(144, 55, 156, 65, start=0, extent=180, style=tk.ARC)  # felipe: boca feliz
        else:
            canvas.create_arc(144, 60, 156, 70, start=180, extent=180, style=tk.ARC)  # felipe: boca triste

    if erros >= 2:
        canvas.create_line(150, 70, 150, 120, fill="#0000cc", width=4)  # felipe: camisa (tronco azul)

    if erros >= 3:
        canvas.create_line(150, 80, 130, 100, fill="#0000cc", width=4)  # felipe: braço esquerdo

    if erros >= 4:
        canvas.create_line(150, 80, 170, 100, fill="#0000cc", width=4)  # felipe: braço direito

    if erros >= 5:
        canvas.create_line(150, 120, 130, 150, fill="#555555", width=4)  # felipe: perna esquerda
        canvas.create_oval(127, 148, 133, 154, fill="black")  # felipe: bota esquerda

    if erros >= 6:
        canvas.create_line(150, 120, 170, 150, fill="#555555", width=4)  # felipe: perna direita
        canvas.create_oval(167, 148, 173, 154, fill="black")  # felipe: bota direita

# --- Interface Gráfica ---
root = tk.Tk()
root.title("Jogo da Forca")
root.configure(bg="#e6f2ff")  # felipe: cor de fundo da janela

letras_certas = set()
letras_erradas = set()
tentativas_restantes = tk.IntVar(value=6)
palavra = escolher_palavra()

canvas = tk.Canvas(root, width=300, height=200, bg="#fff", highlightthickness=0)  # felipe: área de desenho do boneco
canvas.pack(pady=10)
desenhar_base()  # felipe: desenha estrutura da forca ao iniciar

palavra_label = tk.Label(root, text=" ".join(["_" for _ in palavra]), font=("Arial", 24), bg="#e6f2ff")  # felipe: fundo
palavra_label.pack(pady=10)

letra_entry = tk.Entry(root, font=("Arial", 20), width=5)
letra_entry.pack(pady=5)

tentar_button = tk.Button(root, text="Tentar", font=("Arial", 18), command=tentar_letra, bg="#b3d9ff")  # felipe: botão estilizado
tentar_button.pack(pady=5)

tentativas_label = tk.Label(root, textvariable=tentativas_restantes, font=("Arial", 16), bg="#e6f2ff")  # felipe: fundo azul claro
tentativas_label.pack(pady=5)

letras_erradas_label = tk.Label(root, text="", font=("Arial", 14), bg="#e6f2ff", fg="red")  # felipe: exibe letras erradas
letras_erradas_label.pack(pady=5)

reiniciar_button = tk.Button(root, text="Reiniciar", font=("Arial", 16), command=reiniciar_jogo, bg="#99ccff")  # felipe: botão estilizado
reiniciar_button.pack(pady=10)

root.bind('<Return>', lambda event: tentar_letra())  # felipe: permite apertar Enter para tentar

reiniciar_jogo()
root.mainloop()