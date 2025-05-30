import random
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

def escolher_palavra():
    palavras = ["python", "computador", "programacao", "forca", "teclado"]
    return random.choice(palavras)

def atualizar_palavra():
    palavra_display = ''.join([letra if letra in letras_certas else '_' for letra in palavra])
    palavra_label.config(text=" ".join(palavra_display))
    letras_erradas_label.config(text="Letras erradas: " + ' '.join(sorted(letras_erradas)))  # Felipe: exibir letras erradas
    dicas_label.config(text=f"Dicas restantes: {dicas_restantes.get()}")  # Guilherme: contador de dicas
    desenhar_forca()  # Felipe: atualizar boneco a cada tentativa

def tentar_letra():
    letra = letra_entry.get().lower()
    letra_entry.delete(0, tk.END)

    if len(letra) != 1 or not letra.isalpha():
        messagebox.showerror("Erro", "Por favor, digite apenas uma letra!")  # Felipe: validação de entrada
        return

    if letra in letras_certas or letra in letras_erradas:
        messagebox.showwarning("Aviso", "Você já tentou essa letra.")  # Felipe: evitar repetição
        return

    if letra in palavra:
        letras_certas.add(letra)
        atualizar_palavra()
        if all(letra in letras_certas for letra in palavra):
            messagebox.showinfo("Parabéns", "Você venceu!")
            desativar_jogo()  # Felipe: desativa o jogo após vitória
    else:
        letras_erradas.add(letra)
        tentativas_restantes.set(tentativas_restantes.get() - 1)
        atualizar_palavra()
        if tentativas_restantes.get() == 0:
            messagebox.showinfo("Fim de jogo", f"Você perdeu! A palavra era: {palavra}")
            desativar_jogo()  # Felipe: desativa o jogo após derrota

def desativar_jogo():
    letra_entry.config(state="disabled")  # Felipe: desativa entrada
    tentar_button.config(state="disabled")  # Felipe: desativa botão

def reiniciar_jogo():
    global palavra, letras_certas, letras_erradas
    palavra = escolher_palavra()
    letras_certas = set()
    letras_erradas = set()
    tentativas_restantes.set(6)
    dicas_restantes.set(2)  # Guilherme: reinicia contador de dicas
    letra_entry.config(state="normal")  # Felipe: reativa entrada
    tentar_button.config(state="normal")  # Felipe: reativa botão
    canvas.delete("all")  # Felipe: limpa canvas
    desenhar_base()  # Felipe: redesenha forca
    atualizar_palavra()

def desenhar_base():
    canvas.create_line(20, 180, 120, 180)  # Felipe: base da forca
    canvas.create_line(70, 180, 70, 20)    # Felipe: poste vertical
    canvas.create_line(70, 20, 150, 20)    # Felipe: barra superior
    canvas.create_line(150, 20, 150, 40)   # Felipe: corda

def desenhar_forca():  # Felipe: desenho completo do boneco
    erros = 6 - tentativas_restantes.get()

    if erros >= 1:
        # Cabeça com cor de pele
        canvas.create_oval(135, 40, 165, 70, fill="#ffe0bd")

        # Olhos
        canvas.create_oval(142, 48, 146, 52, fill="black")
        canvas.create_oval(154, 48, 158, 52, fill="black")

        # Boca
        if tentativas_restantes.get() > 0:
            canvas.create_arc(144, 55, 156, 65, start=0, extent=180, style=tk.ARC)  # feliz
        else:
            canvas.create_arc(144, 60, 156, 70, start=180, extent=180, style=tk.ARC)  # triste

    if erros >= 2:
        canvas.create_line(150, 70, 150, 120, fill="#0000cc", width=4)  # tronco

    if erros >= 3:
        canvas.create_line(150, 80, 130, 100, fill="#0000cc", width=4)  # braço esquerdo

    if erros >= 4:
        canvas.create_line(150, 80, 170, 100, fill="#0000cc", width=4)  # braço direito

    if erros >= 5:
        canvas.create_line(150, 120, 130, 150, fill="#555555", width=4)  # perna esquerda
        canvas.create_oval(127, 148, 133, 154, fill="black")  # bota esquerda

    if erros >= 6:
        canvas.create_line(150, 120, 170, 150, fill="#555555", width=4)  # perna direita
        canvas.create_oval(167, 148, 173, 154, fill="black")  # bota direita

def dar_dica():  # Guilherme: função completa do sistema de dicas
    if dicas_restantes.get() <= 0:
        messagebox.showinfo("Dicas", "Você não tem mais dicas disponíveis!")
        return

    letras_disponiveis = [letra for letra in set(palavra) if letra not in letras_certas]
    if letras_disponiveis:
        dica = random.choice(letras_disponiveis)
        letras_certas.add(dica)
        dicas_restantes.set(dicas_restantes.get() - 1)
        atualizar_palavra()
        if all(letra in letras_certas for letra in palavra):
            messagebox.showinfo("Parabéns", "Você venceu!")
            desativar_jogo()
    else:
        messagebox.showinfo("Dica", "Não há mais letras para revelar!")

# --- Interface Gráfica ---
root = tk.Tk()
root.title("Jogo da Forca")

# Felipe: Tentativa de carregar ícone 
try:
    icone = PhotoImage(file="forcalogo.png")
    root.iconphoto(True, icone)
except:
    pass

root.configure(bg="#f5c598")  # Felipe: cor de fundo azul claro

letras_certas = set()
letras_erradas = set()
tentativas_restantes = tk.IntVar(value=6)
dicas_restantes = tk.IntVar(value=2)  # Guilherme: define 2 dicas por jogo
palavra = escolher_palavra()

# Felipe: Canvas com borda visível
canvas = tk.Canvas(root, width=300, height=200, bg="white", highlightthickness=2, highlightbackground="#cccccc")
canvas.pack(pady=10)
desenhar_base()

# Felipe: Estilo moderno para os elementos de interface
palavra_label = tk.Label(root, text=" ".join(["_" for _ in palavra]), font=("Helvetica", 28, "bold"), bg="#d0e7ff")
palavra_label.pack(pady=10)

letra_entry = tk.Entry(root, font=("Helvetica", 20), width=3, bd=2, relief="groove")  # Felipe: campo de entrada estilizado
letra_entry.pack(pady=5)

tentar_button = tk.Button(root, text="Tentar", font=("Helvetica", 16), command=tentar_letra, 
                         bg="#4da6ff", fg="white", padx=10, pady=5)  # Felipe: botão azul estilizado
tentar_button.pack(pady=5)

# Felipe: Exibição organizada das tentativas
tentativas_label = tk.Label(root, text="Tentativas: ", font=("Helvetica", 16), bg="#d0e7ff")
tentativas_valor = tk.Label(root, textvariable=tentativas_restantes, font=("Helvetica", 16, "bold"), bg="#d0e7ff") 
tentativas_label.pack(pady=5)
tentativas_valor.pack(pady=5)

letras_erradas_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#d0e7ff", fg="#cc0000")  # Felipe: vermelho para erros
letras_erradas_label.pack(pady=5)

dicas_label = tk.Label(root, textvariable=dicas_restantes, font=("Helvetica", 14), bg="#d0e7ff")  # Guilherme: mostra dicas restantes
dicas_label.pack(pady=5)

dica_button = tk.Button(root, text="Dica", font=("Helvetica", 16), command=dar_dica, 
                       bg="#80dfff", fg="white", padx=10, pady=5)  # Guilherme: botão de dica azul claro
dica_button.pack(pady=5)

reiniciar_button = tk.Button(root, text="Reiniciar", font=("Helvetica", 16), command=reiniciar_jogo, 
                            bg="#0059b3", fg="white", padx=10, pady=5)  # Felipe: botão azul escuro
reiniciar_button.pack(pady=10)

root.bind('<Return>', lambda event: tentar_letra())  # Felipe: ativar com Enter

reiniciar_jogo()
root.mainloop()