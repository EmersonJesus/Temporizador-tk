from tkinter import *
from PIL import Image,ImageTk
from time import *

# Inicia o temporizador --------------------
def inicar():
    global rodando
    global iniciar_timer
    if not rodando:
        rodando = True
        inicar_timer = time()
        atualizar_timer()
        
# Para o temporizador ------------------------
def parar():
    global rodando
    rodando = False
    
# Atualiza o timer ---------------------------
def atualiza_timer():
    if rodando:
        tempo_passado = time() - inicar_timer
        tempo_label.config(text=f'{tempo_passado:.2f}')
        tempo_label.after(50, atualiza_timer)
        
# Criando a janela ----------------------------
janela = Tk()
janela.title('Temporizador')
janela.geometry('350x400')

# Configurando fundo --------------------------
imagem = Image.open('temporizador.jpg')
fundo_img = ImageTk.PhotoImage(image=imagem)
fundo = Label(janela, image=fundo_img)
fundo.place(x=0, y=0)