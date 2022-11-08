from tkinter import *

# --------- criação da tela com o tela_i = tk --------- #
tela_i = Tk()

# --------- adicionando responsividade e alterando detalhes estéticos da página criada. --------- #

# bolapng = PhotoImage(file='C:\\Users\\Thiaguera1\\Desktop\\Ora bolas\\Dev projeto\\imagemk.png')
tela_i.title("Projeto Ora Bolas")
# tela_i.iconphoto(False, bolapng)
tela_i.configure(background = '#283747')
tela_i.resizable(True, True)

# --------- Centralizando e delimitando a tela do menu no windows. --------- #
largura = tela_i.winfo_screenwidth()
altura = tela_i.winfo_screenheight()
alt_tela = 550
lrg_tela = 850
telax = largura/2 - lrg_tela/2
telay = altura/2 - alt_tela/2
tela_i.geometry("%dx%d+%d+%d" % (largura, altura, telax, telay))
tela_i.maxsize(width= 850, height= 550)
tela_i.minsize(width = 650, height = 400)

# --------- criação de labels e botões para referenciar as funcionalidades na janela. --------- #

#Nome do Projeto "Projeto Ora Bolas"
proj_name = Label(tela_i, text="PROJETO ORA BOLAS", background="#283747", font="Verdana 20 bold italic", foreground="white").place(relx=0.30, rely=0.01, width=330, height=50)
ra1 = Label(tela_i, text="Ana Dias RA: 22.122.073-4", background="#283747", font="Verdana 10 bold italic", foreground="white").place(x=115, rely=0.90, width=200, height=50)
ra2 = Label(tela_i, text="Luiggi Garcia RA: 22.122.006-4", background="#283747", font="Verdana 10 bold italic", foreground="white").place(x=322, rely=0.90, width=220, height=50)
ra3 = Label(tela_i, text="Thiago Garcia RA: 22.122.003-1", background="#283747", font="Verdana 10 bold italic", foreground="white").place(x=550, rely=0.90, width=220, height=50)


# --------- Nomes acima das caixas de "resposta" --------- #

#Nome X
lbposx = Label(tela_i, text="Digite o Xo do Robô", background="#283747", font="Arial 14", foreground="white").place(relx=0.20, rely=0.15, width=225, height=40)
#Nome Y
lbposy = Label(tela_i, text="Digite a Yo do Robô", background="#283747", font="Arial 14", foreground="white").place(relx=0.55, rely=0.15, width=225, height=40)

# --------- Caixinhas de respostas --------- #

vposx = Entry(tela_i, font="Arial 13") #Caixa de resposta X
vposx.place(relx=0.20, rely=0.23, width=225, height=40)

vposy = Entry(tela_i, font="Arial 13") #Caixa de resposta Y
vposy.place(relx=0.55, rely=0.23, width=225, height=40)

# --------- funcao teste --------- #
def test(msg):
    print(msg)

# --------- Função para armazenar os dados digitados pelo usuário --------- #

def ok():
    cd1 = vposx.get()
    cd2 = vposy.get()
    print("Xo: %s, Yo: %s" % (cd1, cd2))

    if cd1 == '' and cd2 == '':
        print("Sem coordenadas")
# --------- Botoes para iniciar o algoritmo e gerar os graficos --------- #

botao_start = Button(tela_i, text= "Iniciar!", width=15, height=1, background="#283747", font="Arial 14", foreground="white", bd=2, relief="solid", command=ok) #Botao para chamar a funcao main()
botao_start.place(relx=0.41, rely=0.35)

botao_g1 = Button(tela_i, text= "GRAFICO 1", width=15, height=1, background="#283747", font="Arial 14", foreground="white", bd=2, relief="solid", command=lambda: test("test")) #Botao para chamar o grafico 1()
botao_g1.place(relx=0.18, rely=0.48, width=256)

botao_g2 = Button(tela_i, text= "GRAFICO 2", width=15, height=1, background="#283747", font="Arial 14", foreground="white", bd=2, relief="solid", command=lambda: test("test")) #Botao para chamar o grafico 2()
botao_g2.place(relx=0.18, rely=0.62, width=256)

botao_g3 = Button(tela_i, text= "GRAFICO 3", width=15, height=1, background="#283747", font="Arial 14", foreground="white", bd=2, relief="solid", command=lambda: test("test")) #Botao para chamar o grafico 3()
botao_g3.place(relx=0.18, rely=0.76, width=256)

botao_g4 = Button(tela_i, text= "GRAFICO 4", width=15, height=1, background="#283747", font="Arial 14", foreground="white", bd=2, relief="solid", command=lambda: test("test")) #Botao para chamar o grafico 4()
botao_g4.place(relx=0.54, rely=0.48, width=256)

botao_g5 = Button(tela_i, text= "GRAFICO 5", width=15, height=1, background="#283747", font="Arial 14", foreground="white", bd=2, relief="solid", command=lambda: test("test")) #Botao para chamar o grafico 5()
botao_g5.place(relx=0.54, rely=0.62, width=256)

botao_g6 = Button(tela_i, text= "GRAFICO 6", width=15, height=1, background="#283747", font="Arial 14", foreground="white", bd=2, relief="solid", command=lambda: test("test")) #Botao para chamar o grafico 6()
botao_g6.place(relx=0.54, rely=0.76, width=256)

tela_i.mainloop()