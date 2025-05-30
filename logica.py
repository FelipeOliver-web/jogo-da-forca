import random
import tkinter as tk
from tkinter import messagebox
       FelipeDev
from tkinter import PhotoImage

       main

def escolher_palavra():
    # Felipe: Adicionadas mais palavras para aumentar a variedade
    palavras = ["python", "computador", "programacao", "forca", "teclado", "desenvolvimento", "inteligencia", "algoritmo"]
    return random.choice(palavras)

def atualizar_palavra():
        FelipeDev
    # Felipe: Exibição da palavra com espaços e atualização da interface
    palavra_display = ''.join([letra if letra in letras_certas else '_' for letra in palavra])
    palavra_label.config(text=" ".join(palavra_display))
    # Guilherme: Exibição ordenada das letras erradas
    letras_erradas_label.config(text="Letras erradas: " + ' '.join(sorted(list(letras_erradas))))
    # Guilherme: Atualização do contador de dicas
    dicas_label.config(text=f"Dicas restantes: {dicas_restantes.get()}")
    # Felipe: Atualização do contador de tentativas
    tentativas_label_valor.config(text=f"Tentativas restantes: {tentativas_restantes.get()}")
    desenhar_forca()

def tentar_letra():
    # Felipe: Validação da entrada do usuário

    palavra_display = ''.join([letra if letra in letras_certas else '_' for letra in palavra])
    palavra_label.config(text=" ".join(palavra_display))
    letras_erradas_label.config(text="Letras erradas: " + ' '.join(sorted(letras_erradas)))  # felipe: exibir letras erradas
    dicas_label.config(text=f"Dicas restantes: {dicas_restantes.get()}")
    desenhar_forca()  # felipe: atualizar boneco a cada tentativa errada

def tentar_letra():
         main
    letra = letra_entry.get().lower()
    letra_entry.delete(0, tk.END)

    if len(letra) != 1 or not letra.isalpha():
        FelipeDev
        messagebox.showerror("Erro de entrada", "Por favor, digite apenas uma letra válida!")
        return

    if letra in letras_certas or letra in letras_erradas:
        messagebox.showwarning("Letra repetida", f"Você já tentou a letra '{letra}'.")

        messagebox.showerror("Erro", "Por favor, digite apenas uma letra!")
        return

    if letra in letras_certas or letra in letras_erradas:
        messagebox.showwarning("Aviso", "Você já tentou essa letra.")
        main
        return

    if letra in palavra:
        letras_certas.add(letra)
        atualizar_palavra()
        if all(letra in letras_certas for letra in palavra):
        FelipeDev
            messagebox.showinfo("Parabéns!", f"Você venceu! A palavra era: {palavra.upper()}")
            desativar_jogo()

            messagebox.showinfo("Parabéns", "Você venceu!")
            desativar_jogo()  # felipe: desativa o jogo após vitória
         main
    else:
        letras_erradas.add(letra)
        tentativas_restantes.set(tentativas_restantes.get() - 1)
        atualizar_palavra()
        if tentativas_restantes.get() == 0:
        FelipeDev
            messagebox.showinfo("Fim de jogo", f"Você perdeu! A palavra era: {palavra.upper()}")
            desativar_jogo()

def desativar_jogo():
    # Felipe: Desativa os controles ao final do jogo
    letra_entry.config(state="disabled")
    tentar_button.config(state="disabled")
    dica_button.config(state="disabled")

def ativar_jogo():
    # Felipe: Reativa os controles ao reiniciar
    letra_entry.config(state="normal")
    tentar_button.config(state="normal")
    dica_button.config(state="normal")

            messagebox.showinfo("Fim de jogo", f"Você perdeu! A palavra era: {palavra}")
            desativar_jogo()  # felipe: desativa o jogo após derrota

def desativar_jogo():
    letra_entry.config(state="disabled")  # felipe: desativa entrada de texto
    tentar_button.config(state="disabled")  # felipe: desativa botão
       main

def reiniciar_jogo():
    global palavra, letras_certas, letras_erradas
    palavra = escolher_palavra()
    letras_certas = set()
    letras_erradas = set()
    tentativas_restantes.set(6)
        FelipeDev
    dicas_restantes.set(2)
    ativar_jogo()
    canvas.delete("all")
    desenhar_base()
    atualizar_palavra()

def desenhar_base():
    # Felipe: Desenho da forca com linhas mais grossas
    canvas.create_line(20, 180, 120, 180, width=3)
    canvas.create_line(70, 180, 70, 20, width=3)
    canvas.create_line(70, 20, 150, 20, width=3)
    canvas.create_line(150, 20, 150, 40, width=3)

def desenhar_forca():
    # Felipe: Desenho completo do boneco com tags e detalhes aprimorados
    erros = 6 - tentativas_restantes.get()
    canvas.delete("boneco")

    if erros >= 1:
        canvas.create_oval(135, 40, 165, 70, fill="#ffddaa", outline="black", tags="boneco")
        canvas.create_oval(142, 48, 146, 52, fill="black", tags="boneco")
        canvas.create_oval(154, 48, 158, 52, fill="black", tags="boneco")
        if tentativas_restantes.get() > 0:
            canvas.create_arc(144, 55, 156, 65, start=0, extent=180, style=tk.ARC, outline="black", width=2, tags="boneco")
        else:
            canvas.create_line(144, 62, 156, 62, fill="black", width=2, tags="boneco")

    if erros >= 2:
        canvas.create_line(150, 70, 150, 120, fill="#3366cc", width=5, tags="boneco")

    if erros >= 3:
        canvas.create_line(150, 80, 130, 100, fill="#3366cc", width=5, tags="boneco")
        canvas.create_oval(127, 97, 133, 103, fill="black", tags="boneco")

    if erros >= 4:
        canvas.create_line(150, 80, 170, 100, fill="#3366cc", width=5, tags="boneco")
        canvas.create_oval(167, 97, 173, 103, fill="black", tags="boneco")

    if erros >= 5:
        canvas.create_line(150, 120, 130, 160, fill="#555555", width=5, tags="boneco")
        canvas.create_oval(125, 158, 135, 168, fill="black", tags="boneco")

    if erros >= 6:
        canvas.create_line(150, 120, 170, 160, fill="#555555", width=5, tags="boneco")
        canvas.create_oval(165, 158, 175, 168, fill="black", tags="boneco")

def dar_dica():
    # Guilherme: Sistema completo de dicas com contador
    if dicas_restantes.get() <= 0:
        messagebox.showinfo("Sem dicas", "Você não tem mais dicas disponíveis!")
        return


    dicas_restantes.set(1)  # Guilherme: número de dicas
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

def dar_dica(): # Guilherme: função das dicas
    if dicas_restantes.get() <= 0:
        messagebox.showinfo("Dicas", "Você não tem mais dicas disponíveis!")
        return

        main
    letras_disponiveis = [letra for letra in set(palavra) if letra not in letras_certas]
    if letras_disponiveis:
        dica = random.choice(letras_disponiveis)
        letras_certas.add(dica)
        FelipeDev
        dicas_restantes.set(dicas_restantes.get() - 1)
        messagebox.showinfo("Dica!", f"A letra '{dica.upper()}' faz parte da palavra.")
        atualizar_palavra()
        if all(letra in letras_certas for letra in palavra):
            messagebox.showinfo("Parabéns!", f"Você venceu! A palavra era: {palavra.upper()}")
            desativar_jogo()
    else:
        messagebox.showinfo("Dica", "Não há mais letras para revelar como dica.")

        dicas_restantes.set(dicas_restantes.get() - 1)  # Guilherme: Desconta uma dica
        atualizar_palavra()
        if all(letra in letras_certas for letra in palavra):
            messagebox.showinfo("Parabéns", "Você venceu!")
            desativar_jogo()
    else:
        messagebox.showinfo("Dica", "Não há mais letras para revelar!")
        main

# --- Interface Gráfica ---
root = tk.Tk()
root.title("Jogo da Forca")
        FelipeDev

# Felipe: Tentativa de carregar ícone com tratamento de erro
try:
    icone = PhotoImage(file="forcalogo.png")
    root.iconphoto(True, icone)
except tk.TclError:
    pass

# Felipe: Configuração do esquema de cores
root.configure(bg="#f1d8a1")

root.configure(bg="#e6f2ff")  # felipe: cor de fundo da janela
         main

letras_certas = set()
letras_erradas = set()
tentativas_restantes = tk.IntVar(value=6)
        FelipeDev
dicas_restantes = tk.IntVar(value=2)
palavra = escolher_palavra()

# Felipe: Canvas com efeitos visuais melhorados
canvas = tk.Canvas(root, width=300, height=200, bg="white", bd=5, relief="ridge", highlightbackground="#a7d9ed", highlightthickness=2)
canvas.pack(pady=15, padx=15)
desenhar_base()

# Felipe: Organização dos elementos de interface
input_frame = tk.Frame(root, bg="#f1d8a1")
input_frame.pack(pady=10)

palavra_label = tk.Label(input_frame, text=" ".join(["_" for _ in palavra]), font=("Arial", 32, "bold"), bg="#e0f2f7", fg="#333333")
palavra_label.pack(side=tk.TOP, pady=(0, 10))

letra_entry = tk.Entry(input_frame, font=("Arial", 24), width=4, justify='center', bd=3, relief="sunken", highlightbackground="#87ceeb", highlightthickness=1)
letra_entry.pack(side=tk.LEFT, padx=5)

tentar_button = tk.Button(input_frame, text="Tentar", font=("Arial", 16, "bold"), command=tentar_letra,
                          bg="#4CAF50", fg="white", padx=15, pady=8, relief="raised", bd=3,
                          activebackground="#45a049", activeforeground="white")
tentar_button.pack(side=tk.LEFT, padx=5)

info_frame = tk.Frame(root, bg="#e0f2f7")
info_frame.pack(pady=10)

tentativas_label_valor = tk.Label(info_frame, textvariable=tentativas_restantes, font=("Arial", 18), bg="#e0f2f7", fg="#d32f2f")
tentativas_label_valor.pack(side=tk.LEFT, padx=10)

letras_erradas_label = tk.Label(info_frame, text="", font=("Arial", 16), bg="#e0f2f7", fg="#f44336")
letras_erradas_label.pack(side=tk.LEFT, padx=10)

dicas_label = tk.Label(info_frame, textvariable=dicas_restantes, font=("Arial", 16), bg="#e0f2f7", fg="#2196F3")
dicas_label.pack(side=tk.LEFT, padx=10)

# Guilherme: Botão de dica estilizado
dica_button = tk.Button(root, text="Pedir Dica", font=("Arial", 14, "bold"), command=dar_dica,
                       bg="#03A9F4", fg="white", padx=12, pady=7, relief="raised", bd=3,
                       activebackground="#0288d1", activeforeground="white")
dica_button.pack(pady=5)

# Felipe: Botão de reiniciar estilizado
reiniciar_button = tk.Button(root, text="Reiniciar Jogo", font=("Arial", 14, "bold"), command=reiniciar_jogo,
                            bg="#FF9800", fg="white", padx=12, pady=7, relief="raised", bd=3,
                            activebackground="#fb8c00", activeforeground="white")
reiniciar_button.pack(pady=10)

# Felipe: Configuração de teclado e foco
root.bind('<Return>', lambda event: tentar_letra())
letra_entry.focus_set()

reiniciar_jogo()
root.mainloop()

dicas_restantes = tk.IntVar(value=2)  # Guilherme: define quantas dicas o jogador tem
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

dicas_label = tk.Label(root, text=f"Dicas restantes: {dicas_restantes.get()}", font=("Arial", 14), bg="#e6f2ff")
dicas_label.pack(pady=5)

letras_erradas_label = tk.Label(root, text="", font=("Arial", 14), bg="#e6f2ff", fg="red")  # felipe: exibe letras erradas
letras_erradas_label.pack(pady=5)

dica_button = tk.Button(root, text="Dica", font=("Arial", 16), command=dar_dica, bg="#cce5ff") # Guilherme: botão para as dicas 
dica_button.pack(pady=5)

reiniciar_button = tk.Button(root, text="Reiniciar", font=("Arial", 16), command=reiniciar_jogo, bg="#99ccff")  # felipe: botão estilizado
reiniciar_button.pack(pady=10)

root.bind('<Return>', lambda event: tentar_letra())  # felipe: permite apertar Enter para tentar

reiniciar_jogo()
root.mainloop()
        main
