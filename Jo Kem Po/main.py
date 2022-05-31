import random
import tkinter as tk 
from tkinter import *
from tkinter import ttk
from turtle import bgcolor
from PIL import ImageTk, Image

global pontosbot
global seuspontos
global rodadas
global provabilidades

pontosbot = 0
seuspontos = 0
rodadas = 5
jogadas = ["tesoura", "pedra", "papel", "tesoura", "pedra"]
provabilidades = ["Win", "Lose", "Draw"]



co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha
fundo = "#3b3b3b"
### FUNÇÃO PRA STARTAR O GAME
def jogar(i):
    global pontosbot
    global seuspontos
    global escolhabot
    global suaescolha
    global rodadas
    if rodadas > 0:
        print(rodadas)
        escolhabot = random.choice(provabilidades)
        suaescolha = i
        if escolhabot == "Draw":
            print(f"Sua escolha:{jogadas[suaescolha]}, escolha do bot : {jogadas[suaescolha]}")
            app_linha["bg"] = co3
        elif escolhabot == "Win":
            print(f"Sua escolha:{jogadas[suaescolha]}, escolha do bot: {jogadas[suaescolha + 1]}")
            pontosbot += 1
            app_linha["bg"] = co5
            app_2_pontos["text"] = pontosbot

            print(f"Seus pontos: {seuspontos}, pontos bot: {pontosbot}")
        else:
            print(f"Sua escolha:{jogadas[suaescolha]}, escolha do bot: {jogadas[suaescolha - 1]}")
            seuspontos += 1
            app_linha["bg"] = co4
            app_1_pontos["text"] = seuspontos
            print(f"Seus pontos: {seuspontos}, pontos bot: {pontosbot}")
        rodadas -= 1
    else:
        fimdejogo()
def fimdejogo():
    print("Fim de jogo")
    b_icon1.destroy()
    b_icon2.destroy()
    b_icon3.destroy()


            

 ### FUNCIONALIDADES DO JOGO      

 ##CONFIGURANDO A JANELA
janela = Tk()
janela.title("Jokenpo")
janela.geometry("260x280")
janela.configure(bg=fundo)


frame_cima = Frame(janela, width=260, height=100, bg=co1, relief="raised")
frame_cima.grid(row = 0, column = 0, sticky=NW)

frame_baixo = Frame(janela, width=260, height=180, bg=co0, relief="flat")
frame_baixo.grid(row = 1, column = 0, sticky=NW)


estilo = ttk.Style(janela)
estilo.theme_use('clam')
###CONFIGURANDO A JANELA

app_1 = Label(frame_cima, text="Voce", height=1, anchor="center", font="Ivy 10 bold", bg=co1, fg= co0)
app_1.place(x=15, y=70)
app_1_linha =Label(frame_cima, text="", height=10, anchor="center", font="Ivy 10 bold", bg=co0, fg= co0)
app_1_linha.place(x=0, y=0, )

app_1_pontos =Label(frame_cima, text="0", height=1, anchor="center", font="Ivy 30 bold", bg=co1, fg= co0)
app_1_pontos.place(x=15, y=15)

app_ =Label(frame_cima, text=":", height=1, anchor="center", font="Ivy 30 bold", bg=co1, fg= co0)
app_.place(x=260, y=0)


app_2 = Label(frame_cima, text="Bot", height=1, anchor="center", font="Ivy 10 bold", bg=co1, fg= co0)
app_2.place(x= 200, y=70)
app_2_linha =Label(frame_cima, text="", height=10, anchor="center", font="Ivy 10 bold", bg=co0, fg= co0)
app_2_linha.place(x=255, y=0)

app_2_pontos =Label(frame_cima, text="0", height=1, anchor="center", font="Ivy 30 bold", bg=co1, fg= co0)
app_2_pontos.place(x=200, y=15)

app_linha = Label(frame_cima, text="", width=255, anchor="center", font="Ivy 1 bold", bg=co0, fg= co0)
app_linha.place(x=0, y=95)



def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon1
    global b_icon2
    global b_icon3

    b_jogar.destroy()

    icon_1 = Image.open("images/pedra.png")
    icon_1 = icon_1.resize((50,50),Image.ANTIALIAS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon1 = Button(frame_baixo, command= lambda: jogar(1)  ,width=50,image=icon_1, compound= CENTER, bg=co0,fg=co0, font= ("ivy 30 bold"),anchor=CENTER, relief=FLAT,  activebackground= co4, cursor= "arrow" )
    b_icon1.place(x=15, y=60)

    icon_2 = Image.open("images/papel.png")
    icon_2 = icon_2.resize((50,50),Image.ANTIALIAS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon2 = Button(frame_baixo, command= lambda: jogar(2) ,width=50,image=icon_2, compound= CENTER, bg=co0,fg=co0, font= ("ivy 30 bold"),anchor=CENTER, relief=FLAT,  activebackground= co4, cursor= "arrow" )
    b_icon2.place(x=95, y=60)

    icon_3 = Image.open("images/tesoura.png")
    icon_3 = icon_3.resize((50,50),Image.ANTIALIAS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon3 = Button(frame_baixo, command= lambda: jogar(3) ,width=50,image=icon_3, compound= CENTER, bg=co0,fg=co0, font= ("ivy 30 bold"),anchor=CENTER, relief=FLAT, activebackground= co4, cursor= "arrow" )
    b_icon3.place(x= 180, y=60)



b_jogar = Button(frame_baixo ,width=30, text= 'jogar' , bg=co1,fg=co0, font= ("Ivy 10 bold"),anchor=CENTER, relief=RAISED, overrelief= RIDGE, command= iniciar_jogo  )
b_jogar.place(x= 5, y=151)
janela.mainloop()