from tkinter import *
from PIL import Image,ImageTk
from time import *

# Inicia o temporizador --------------------
def iniciar():
    global rodando
    global iniciar_timer
    if not rodando:
        rodando = True
        iniciar_timer = time()
        atualiza_timer()
        
# Para o temporizador ------------------------
def parar():
    global rodando
    rodando = False
    
# Atualiza o timer ---------------------------
def atualiza_timer():
    if rodando:
        tempo_passado = time() - iniciar_timer
        minuto = int(tempo_passado / 60)
        if minuto >= 1:
            parar()
        tempo_label.config(text=f'{tempo_passado:.2f}')
        tempo_label.after(50, atualiza_timer)
        
# Criando a janela ----------------------------
janela = Tk()
janela.title('Temporizador')
janela.geometry('350x400')
janela.resizable(width=False, height=False)


# Configurando fundo --------------------------
imagem = Image.open('temporizador.jpg')
fundo_img = ImageTk.PhotoImage(image=imagem)
fundo = Label(janela, image=fundo_img)
fundo.place(x=0, y=0)

# Criando o label que mostra o tempo ----------
tempo_label = Label(janela, text='0.00', font='Helvetica 48', bg='white')
tempo_label.place(x=110, y=190)

# Criando botões ------------------------------
botao_iniciar = Button(janela, text='Iniciar', height=1, command=iniciar, relief='groove', bg='black', fg='white')
botao_iniciar.place(x=10, y=10)
botao_parar = Button(janela, text='Parar', height=1, command=parar, relief='groove', bg='black', fg='white')
botao_parar.place(x=260, y=10)

# Loop da janela -----------------------------
rodando = False
janela.mainloop()