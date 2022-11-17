from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter import *
from data import beforeIntercept, afterIntercept

# INTERFACE GRAFICA DO PROJETO

xo_robot = None
yo_robot = None
a = 0.8
v = 2
raio = 0.10
afterList = []

firstwindow = Tk()

class Funcs():

    def verifyCoordinates(self, xo, yo):
        
        try:
            if xo == '' or yo == '':
                messagebox.showinfo("Erro!", "Você não digitou as coordenadas")
                return False
            elif float(xo) <= 9 and float(yo) <= 6:
                return True
            elif(float(xo) > 9):
                messagebox.showinfo("Erro!", "A posição xo não pode ultrapassar mais de 9m")
                return False
            elif(float(yo) > 6):
                messagebox.showinfo("Erro!", "A posição yo não pode ultrapassar mais de 6m")
                return False
    
        except ValueError:
            print("Erro!")

    def ok(self):
        global xo_robot, yo_robot, afterList
        xo = self.vposx.get()
        yo = self.vposy.get()
        verification = self.verifyCoordinates(xo, yo)
        if(verification):
            messagebox.showinfo("Coordenadas escolhidas", "As coordenadas escolhidas foram: Xo: %s e Yo: %s" % (xo, yo))
            self.screen = ScrolledText(self.firstwindow, wrap = WORD, width = 72, height = 11, font= ('Times New Roman', 14))
            self.screen.grid(column = 0, pady= 255, padx = 95)
            
            xo_robot = float(xo)
            yo_robot = float(yo)
            
            beforeList = beforeIntercept(xo_robot, yo_robot, a, v)
            afterList = afterIntercept(beforeList[0], beforeList[1], raio, v)
            data_interception = afterList[0]
            
            if (data_interception["interception"]):
                self.screen.insert(INSERT, "Bola interceptada!\n")
                self.screen.insert(INSERT, "Distância entre o robo e a bola: %.3fm\n" % data_interception["distance"])
                self.screen.insert(INSERT, "Robô (x: %.2f, y: %.2f)\n" % (data_interception["robotX"], data_interception["robotY"]))
                self.screen.insert(INSERT, "Bola (x: %.2f, y: %.2f)\n" % (data_interception["ballX"], data_interception["ballY"]))
                self.screen.insert(INSERT, "Tempo de interceptação: %.2fs\n" % data_interception["time"])
                self.screen.insert(INSERT, "Deslocamento do Robô em x: %.2fm\n" % data_interception["robotDislocationX"])
                self.screen.insert(INSERT, "Deslocamento do Robô em y: %.2fm\n" % data_interception["robotDislocationY"])
                self.screen.insert(INSERT, "Distância percorrida: %.2fm\n" % data_interception["distTraveled"])
                self.screen.insert(INSERT, "Velocidade média do robô: %.2fm/s\n" % data_interception["robotVm"])
                self.screen.insert(INSERT, "Aceleração média do robô: %.2fm/s²\n" % data_interception["robotAm"])
                self.screen.configure(state = 'disable')
                self.screen.update()
            

        self.vposx.delete(0, END)
        self.vposy.delete(0, END)
            

class Projeto(Funcs):
    def __init__(self):
        self.firstwindow = firstwindow
        self.tela()
        firstwindow.mainloop()

    def tela(self):
        self.firstwindow.title("Projeto Ora Bolas")
        # tela_i.iconphoto(False, bolapng)
        self.firstwindow.configure(background = '#283747')
        self.firstwindow.resizable(True, True)

        # --------- Centralizando e delimitando a tela do menu no windows. --------- #
        largura = self.firstwindow.winfo_screenwidth()
        altura = self.firstwindow.winfo_screenheight()
        alt_tela = 550
        lrg_tela = 850
        telax = largura/2 - lrg_tela/2
        telay = altura/2 - alt_tela/2
        self.firstwindow.geometry("%dx%d+%d+%d" % (largura, altura, telax, telay))
        self.firstwindow.maxsize(width= 850, height= 550)
        self.firstwindow.minsize(width = 850, height = 550)

        # --------- criação de labels e botões para referenciar as funcionalidades na janela. --------- #

        #Nome do Projeto "Projeto Ora Bolas"
        self.proj_name = Label(self.firstwindow, text="2° APROFUNDAMENTO", background="#283747", font="Verdana 20 bold italic", foreground="white").place(relx=0.30, rely=0.01, width=330, height=50)
        self.ra1 = Label(self.firstwindow, text="Ana Dias RA: 22.122.073-4 |", background="#283747", font="Verdana 10 bold italic", foreground="white").place(x=80, rely=0.90, width=220, height=50)
        self.ra2 = Label(self.firstwindow, text="Luiggi P. Garcia RA: 22.122.006-4 |", background="#283747", font="Verdana 10 bold italic", foreground="white").place(x=300, rely=0.90, width=240, height=50)
        self.ra3 = Label(self.firstwindow, text="Thiago Garcia RA: 22.122.003-1", background="#283747", font="Verdana 10 bold italic", foreground="white").place(x=547, rely=0.90, width=230, height=50)

        # --------- Nomes acima das caixas de "resposta" --------- #
        #Nome X
        self.lbposx = Label(self.firstwindow, text="Digite o Xo do Robô", background="#283747", font="Arial 14", foreground="white").place(relx=0.20, rely=0.15, width=225, height=40)
        #Nome Y
        self.lbposy = Label(self.firstwindow, text="Digite o Yo do Robô", background="#283747", font="Arial 14", foreground="white").place(relx=0.55, rely=0.15, width=225, height=40)

        # --------- Caixinhas de respostas --------- #
        self.vposx = Entry(self.firstwindow, font="Arial 13") #Caixa de resposta X
        self.vposx.place(relx=0.20, rely=0.23, width=225, height=40)

        self.vposy = Entry(self.firstwindow, font="Arial 13") #Caixa de resposta Y
        self.vposy.place(relx=0.55, rely=0.23, width=225, height=40)

        # --------- Botões --------- #
        botao_start = Button(self.firstwindow, text= "Iniciar!", width=15, height=1, background="#283747", font="Arial 14", foreground="white", bd=2, relief="solid", command= self.ok) #Botao para chamar a funcao main()
        botao_start.place(relx=0.23, rely=0.35)
    

Projeto()