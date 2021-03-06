# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 08:42:55 2016

@author: Fausto Biazzi de Sousa
@modulo: interface gráfica Cético + funções.
@programa = "Cético"
@versão = "Alpha 0.0.2.5"

"""


programa = "Cético"
versao = "Alpha 0.0.2.5"

from funcoes import *
from __error import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import time


class Cetico():
    path = ""
    marcas = []
    corAutoMark = "#00FF00"  # verde
    corManualMark = "#FF0000"  # vermelho
    coordXmouse = 0
    coordYmouse = 0
    VarLVetW = False
    Varabout = False
    VarFDetc = False
    VarIllum = False
    VarMenu = False
    VarCanvas = False
    janelas = []
    areaImgH = 0
    areaImgW = 0


    def __init__(self, master):

        self.interface = master
        self.interface.title(programa + "- Versão " + versao)
        try:
            self.interface.iconbitmap("icone.ico")
        except:
            print("não foi possivel carregar icone")
        self.interface.wm_protocol("WM_DELETE_WINDOW", dialogofechar)
        self.shown = BooleanVar()
        self.shown.set(False)
        w = self.interface.winfo_screenwidth()
        h = self.interface.winfo_screenheight()

        # redimendiona janela pro tamanho definido
        self.interface.geometry("%dx%d" % (w, h))

        self.ocultarMenu()

        self.criarCanvas()
        # hotkeys
        # FUNCTIONS KEYS
        self.interface.bind_all("<F1>", lambda e: dialogo())
        self.interface.bind_all("<Control-F6>", lambda e: self.ocultarMenu())
        self.interface.bind_all("<Control-Alt-M>", lambda e: self.ocultaCanvas())
        self.interface.bind_all("<Control-Alt-m>", lambda e: self.ocultaCanvas())

        # control + key min
        self.interface.bind_all("<Control-a>", lambda e: self.abrirImagem())
        self.interface.bind_all("<Control-q>", lambda e: self.fecharImagem())
        self.interface.bind_all("<Control-d>", lambda e: self.configDetecta())
        self.interface.bind_all("<Control-r>", lambda e: self.removeUltimaMarca())
        self.interface.bind_all("<Control-l>", lambda e: self.limparTodasMarcas())
        self.interface.bind_all("<Control-g>", lambda e: self.gerarRelatorios())
        self.interface.bind_all("<Control-p>", lambda e: self.imprimir())


        # control + key caps
        self.interface.bind_all("<Control-A>", lambda e: self.abrirImagem())
        self.interface.bind_all("<Control-Q>", lambda e: self.fecharImagem())
        self.interface.bind_all("<Control-D>", lambda e: self.configDetecta())
        self.interface.bind_all("<Control-R>", lambda e: self.removeUltimaMarca())
        self.interface.bind_all("<Control-L>", lambda e: self.limparTodasMarcas())
        self.interface.bind_all("<Control-G>", lambda e: self.gerarRelatorios())
        self.interface.bind_all("<Control-P>", lambda e: self.imprimir())

    # comandos de área de trabalho
    def ocultarMenu(self):
        if self.VarMenu:
            self.interface.config(menu="")
            self.VarMenu = False
        else:
            self.VarMenu = True

            # criação do menu

            # menu arquivo
            menubar = Menu(self.interface)


            # menu arquivo
            filemenu = Menu(menubar, tearoff=0)
            filemenu.add_command(label="Carregar imagem", underline=0, command=self.abrirImagem, accelerator="Ctrl+A")
            filemenu.add_command(label="Fechar imagem", underline=0, command=self.fecharImagem, accelerator="Ctrl+Q")
            filemenu.add_separator()
            filemenu.add_command(label="Gerar relatório", command = self.imprimir, accelerator="Ctrl+G")
            filemenu.add_command(label="Imprimir relatório", command = self.gerarRelatorios, accelerator="Ctrl+P")
            filemenu.add_separator()
            filemenu.add_command(label="Sair", underline=3, command=dialogofechar, accelerator="Alt+F4")
            menubar.add_cascade(label="Arquivo", underline=0, menu=filemenu)

            # menu exibir
            # viewmenu = Menu(menubar, tearoff=0)
            # viewmenu.add_command(label="Zoom +", command=dialogo)
            # viewmenu.add_command(label="Zoom -", command=dialogo)
            # viewmenu.add_command(label="Ajustar imagem a janela", command=dialogo)
            # viewmenu.add_separator()
            # menubar.add_cascade(label="Exibir", underline=1, menu=viewmenu)

            # menu ferramentas
            toolsmenu = Menu(menubar, tearoff=0)
            toolsmenu.add_command(label="Detector de rostos", command=self.configDetecta,accelerator="Ctrl+D")
            toolsmenu.add_command(label="Ler EXIF da imagem", command=self.propriedadesImg)
            toolsmenu.add_separator()

            # entradas de menu para códigos de terceiros
            toolsmenu.add_command(label="illuminants", command=self.illuminants)
            toolsmenu.add_command(label="copy-move detetector", command=dialogo)
            toolsmenu.add_command(label="fingersprint", command=dialogo)
            toolsmenu.add_command(label="face recognition", command=dialogo)

            # fim de entrada de menu para códigos de terceiros
            toolsmenu.add_separator()
            toolsmenu.add_command(label="Limpar Marcas", command=self.limparTodasMarcas, accelerator="Ctrl+L")
            toolsmenu.add_command(label="Remover última Marca", command=self.removeUltimaMarca, accelerator="Ctrl+R")
            toolsmenu.add_separator()
            toolsmenu.add_checkbutton(label='habilitar marcação', command=self.desenharMarcasManual, variable=self.shown,
                                      onvalue=True, offvalue=False)
            menubar.add_cascade(label="Ferramentas", underline=0, menu=toolsmenu)

            # menu Janela
            windPrincipal = Menu(menubar, tearoff=0)
            windPrincipal.add_command(label="Exibir/Remover Menu", command=self.ocultarMenu, accelerator="Ctrl+F6")
            windPrincipal.add_command(label="Ocultar imagem", command=self.ocultaCanvas, accelerator="Ctrl+Alt+M")
            #windPrincipal.add_command(label="Fechar janelas auxiliares", command=lambda:self.fecharJanelasSubordinadas("todas"))
            menubar.add_cascade(label="Janela", underline=1, menu=windPrincipal)


            # menu ajuda
            helpmenu = Menu(menubar, tearoff=0)
            helpmenu.add_command(label="Tópicos de ajuda", underline=0, command=dialogo)
            helpmenu.add_command(label="Sobre...", underline=0, command=self.sobreCetico)
            menubar.add_cascade(label="Ajuda", underline=1, menu=helpmenu)
            self.interface.config(menu=menubar)

    def ocultaCanvas(self):
        if self.VarCanvas:
            self.canvas.pack_forget()
            self.VarCanvas = False
        else:
            self.canvas.pack()
            self.VarCanvas = True

    def criarCanvas(self):
        w = self.interface.winfo_screenwidth()
        h = self.interface.winfo_screenheight()

        # redimendiona janela pro tamanho definido
        self.interface.geometry("%dx%d" % (w, h))

        # area util
        self.canvasX = 0
        self.canvasY = 0
        self.canvas = Canvas(width=w, height=h, cursor="cross")
        self.canvas.pack(side="top", fill="none", expand=True)
        self.VarCanvas = True

    def fecharJanelasSubordinadas(self, janela):
        if janela == "Illuminants":
            self.VarIllum = False
            self.j_illuminants.destroy()

        if janela == "resultadoIllu":
            self.VarIllum = False
            self.j_Resultilluminants.destroy()

        if janela == "Sobre":
            self.Varabout = False
            self.about.destroy()

        if janela == "Detecta":
            self.VarFDetc = False
            self.confDetecta.destroy()

        if janela == "Lista":
            self.VarLVetW = False
            self.vetReceb.destroy()

    # comandos de arquivo
    def abrirImagem(self):
        try:
            self.path = askopenfilename(
            filetypes=(("Todos os Arquivos", "*.*"), ("imagem JPG", "*.jpg\;*.jpeg"), ("imagem bitmap", "*.bmp"),
                       ("imagem PNG", "*.png")),
            title="Selecione um arquivo.")
            if self.path !="":
                if self.marcas != []:
                    try:
                        self.canvas.delete(ALL)
                        self.marcas = []
                        #self.atualizarMarcas()
                        self.vetReceb.destroy()
                    except:
                        pass
                if not self.VarCanvas:
                    self.ocultaCanvas()
                self.interface.title(programa + "- Versão " + versao + " - [" + self.path + "]")
                self.imagem = ImageTk.PhotoImage(Image.open(self.path))
                self.canvas.create_image(self.canvasX, self.canvasY, anchor=NW, image=self.imagem)
        except:
            erroAbrirArquivo()

    def fecharImagem(self):
        self.canvas.delete("all")
        self.path = ""
        self.interface.title(programa + "- Versão " + versao)
        if self.marcas != []:
            self.marcas = []
            self.fecharJanelasSubordinadas("Lista")

    def gerarRelatorios(self):
        dialogo()

    def imprimir(self):
        dialogo()

    # comandos de marcação
    def desenharMarcasManual(self):
        if self.shown.get():
            print("função desenho habilitada")
            # desenhar retangulo

            self.canvas.bind("<ButtonPress-1>", self.marca_cliqueDireito_mouse)
            self.canvas.bind("<ButtonRelease-1>", self.marca_liberaClique_mouse)
        else:
            print("função desenho desabilitada")

    def marca_cliqueDireito_mouse(self, event):
        self.coordXmouse = event.x
        self.coordYmouse = event.y

    def marca_liberaClique_mouse(self, event):
        x0, y0 = (self.coordXmouse, self.coordYmouse)
        x1, y1 = (event.x, event.y)
        w1 = x1-x0
        h1 = y1-y0
        if self.shown.get():
            self.canvas.create_rectangle(x0, y0, x0 + w1, y0 + h1, outline=self.corManualMark, width=2)
            self.marcas.append([x0, y0, w1, h1])
            #self.atualizarMarcas()

    def limparTodasMarcas(self):
        if self.marcas!=[]:
            if messagebox.askyesno("Limpar marcas",
                                   "isso ira remover todas as marcações feitas na imagem.\n"
                                   "Tem certeza que deseja fazer isso?"):
                self.canvas.delete("all")
                self.marcas = []
                self.canvas.create_image(self.canvasX, self.canvasY, anchor=NW, image=self.imagem)
                print("marcas limpas")
                print(self.marcas)
            #elf.atualizarMarcas()

    def removeUltimaMarca(self):
        if messagebox.askyesno("remover última marcação",
                               "isso ira remover a última marcação feitas na imagem.\n"
                               "Tem certeza que deseja fazer isso?"):
            self.canvas.delete("all")

            self.marcas.pop()

            self.canvas.create_image(self.canvasX, self.canvasY, anchor=NW, image=self.imagem)
            for (x0, y0, w1, h1) in self.marcas:
                self.canvas.create_rectangle(x0, y0, x0 + w1, y0 + h1, fill=None, outline=self.corAutoMark, width=2)
            #self.atualizarMarcas()

    def atualizarMarcas(self):
        if self.VarLVetW:
            self.vetReceb.destroy()
            self.listaMarcas()
        else:
            self.VarLVetW = False
            self.listaMarcas()

    def listaMarcas(self):
        self.VarLVetW = True
        self.vetReceb = Tk()
        self.vetReceb.title("Coordenadas")
        self.vetReceb.wm_attributes("-topmost", 1)
        self.vetReceb.wm_protocol("WM_DELETE_WINDOW", lambda: self.fecharJanelasSubordinadas("Lista"))
        self.vetReceb.resizable(width=FALSE, height=FALSE)
        self.vetReceb.bind("<Escape>", (lambda e: self.fecharJanelasSubordinadas("Lista")))
        scrollbar = Scrollbar(self.vetReceb)
        scrollbar.pack(side=RIGHT, fill=Y)
        w = 150
        h = 400

        lista = Listbox(self.vetReceb, yscrollcommand=scrollbar.set)
        for item in self.marcas:
            lista.insert(END, str(item))

        lista.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=lista.yview)

        self.vetReceb.geometry("%dx%d+%d+%d" % (w, h, self.vetReceb.winfo_screenwidth()-(w+10), 100))


    # Ajuda

    def sobreCetico(self):
        if self.Varabout == False:
            self.Varabout= True
            self.about = Toplevel(self.interface)
            self.about.title("Sobre " + programa + " " + versao)
            self.about.wm_protocol("WM_DELETE_WINDOW", lambda: self.fecharJanelasSubordinadas("Sobre"))

            self.about.resizable(width=FALSE, height=FALSE)

            label = Label(self.about, text="Sobre o Cético... \n"
                                                  + "Cético é um programa \ndesenvolvido pelo" +
                                                    "Aluno Fausto Biazzi de Sousa \n como parte" +
                                                    "integrante de seu \nTrabalho de Conclusão de Curso" +
                                                    "\n(TCC) do Curso de graduação \nem tecnologia de Analise e" +
                                                    "Desenvolvimento\n de Sistema no IFSP-Campinas.")
            label.pack(side=TOP)
            self.about.bind("<Escape>", (lambda e: self.fecharJanelasSubordinadas("Sobre")))
            button = Button(self.about, text="Fechar", underline=0, command=lambda: self.fecharJanelasSubordinadas("Sobre"))
            button.pack(side=BOTTOM)

            w = 300
            h = 400
            # redimendiona janela pro tamanho definido
            self.about.geometry("%dx%d" % (w, h))

    # Inserir comandos de módulos a partir dessa seção

    # Detecção de rostos

    def configDetecta(self):
        if self.path != "":

            if self.VarFDetc == False:
                self.confDetecta = Toplevel(self.interface)
                self.confDetecta.title("Configurar Detecção automatica de rostos")
                self.confDetecta.wm_protocol("WM_DELETE_WINDOW", lambda: self.fecharJanelasSubordinadas("Detecta"))
                self.confDetecta.resizable(width=FALSE, height=FALSE)

                self.confDetecta.geometry("%dx%d+%d+%d" % (250, 200, self.confDetecta.winfo_screenwidth()/2-125,
                                                           self.confDetecta.winfo_screenmmheight()/2+100))
                label1 = Label(self.confDetecta, text="Mínimo X: ")
                label2 = Label(self.confDetecta, text="Mínimo Y: ")
                label3 = Label(self.confDetecta, text="Mínimo Vizinhos: ")
                label4 = Label(self.confDetecta, text="Escala: ")

                self.input1 = Entry(self.confDetecta)
                self.input2 = Entry(self.confDetecta)
                self.input3 = Entry(self.confDetecta)
                self.input4 = Entry(self.confDetecta)

                button = Button(self.confDetecta, text="Fechar", underline=0, command=lambda: self.fecharJanelasSubordinadas("Detecta"))
                button2 = Button(self.confDetecta,text="Setar Valores", underline=0, command=self.setarConfigDetecta)
                self.confDetecta.bind("<Escape>", (lambda e: self.fecharJanelasSubordinadas("Detecta")))
                self.confDetecta.bind("<Return>", (lambda e: self.setarConfigDetecta()))
                label1.pack(anchor=W)
                self.input1.insert(0, 30)
                self.input1.pack(anchor=E)

                label2.pack(anchor=W)
                self.input2.insert(0, 30)
                self.input2.pack(anchor=E)

                label3.pack(anchor=W)
                self.input3.insert(0, 1)
                self.input3.pack(anchor=E)

                label4.pack(anchor=W)
                self.input4.insert(0, 1.1)
                self.input4.pack(anchor=E)

                button.pack(side=LEFT)
                button2.pack(side=RIGHT)
                self.VarFDetc = True

        else:
            erroImagemNaoCarregada()

    def setarConfigDetecta(self):
        parametros = [int(self.input1.get()), int(self.input2.get()), int(self.input3.get()), float(self.input4.get())]

        if not self.marcas == []:
            if messagebox.askyesno("Alerta!",
                                   "já existem marcações feitas na imagem.\n Deseja apaga-las?"):
                self.limparTodasMarcas()
                self.aplicaDetectaRosto(parametros)

                self.fecharJanelasSubordinadas("Detecta")
            else:
                self.aplicaDetectaRosto(parametros)

                self.fecharJanelasSubordinadas("Detecta")
        else:
            self.aplicaDetectaRosto(parametros)
            self.fecharJanelasSubordinadas("Detecta")

    def aplicaDetectaRosto(self, parametros):

        try:
            face = buscarRosto(self.path, parametros)
        except:
            erroImp_Detecface()

        for (x0, y0, w1, h1) in face:
            self.marcas.append([x0, y0, w1, h1])
            self.canvas.create_rectangle(x0, y0, x0 + w1, y0 + h1, fill=None, outline=self.corAutoMark, width=2)
        #self.atualizarMarcas()


    # Pegar propriedade das imagens
    def propriedadesImg(self):
        print(propriedadesImagem(self.path))

    # acesso a módulos de terceiros

    def illuminants(self):
        if self.VarIllum == False:
            if self.path != "":
                if self.marcas != [] and len(self.marcas)>1:
                    try:
                        self.janelaIlluminants()
                        self.VarIllum = True
                    except NameError:
                        erroModuloGenerico(str(NameError))
                else:
                    erro_Illuminants()
            else:
                erroImagemNaoCarregada()

    def janelaIlluminants(self):

        sub = self

        def extrairDescritoresdaImagem(_self, v1, v2, v3, v4, v5, v6, v7, v8, v9, v0):
            comando =[]
            if v0:
                comando = [ "acc","bic", "ccv", "eoac", "las", "lch", "sasi", "spytec", "unser"]

            else:
                if v1:
                    comando.append("acc")

                if v2:
                        comando.append("bic")

                if v3:
                    comando.append("ccv")

                if v4:
                    comando.append("eoac")

                if v5:
                    comando.append("las")

                if v6:
                    comando.append("lch")

                if v7:
                    comando.append("sasi")

                if v8:
                    comando.append("spytec")

                if v9:
                    comando.append("UNSER")
            resultado = Moduloilluminant(comando, self.path, self.marcas)
            janelaResultado(_self,resultado)
            _self.fecharJanelasSubordinadas("Illuminants")

        def janelaResultado(_self, resultado):

            outClassification, votesNormal, votesFake, finalClass = resultado

            normal = IntVar()
            normal.set(votesNormal)
            fake = IntVar()
            fake.set(votesFake)
            final = IntVar()
            final.set(finalClass)
            #saida = IntVar()
            #saida.set(outClassification)


            _self.j_Resultilluminants = Toplevel(self.interface)
            _self.j_Resultilluminants .title("Resultado")
            _self.j_Resultilluminants.wm_protocol("WM_DELETE_WINDOW", lambda: _self.fecharJanelasSubordinadas("resultadoIllu"))
            _self.j_Resultilluminants .resizable(width=FALSE, height=FALSE)
            Label(_self.j_Resultilluminants , text="Resultado:", anchor=CENTER)
            Label(_self.j_Resultilluminants, text="Normal :").grid(column=0, row=1)
            Label(_self.j_Resultilluminants, text="Modificada :").grid(column=0, row=2)
            Label(_self.j_Resultilluminants, text="Classificação Final:").grid(column=0, row=3)
            Label(_self.j_Resultilluminants, textvariable = normal).grid(column=1, row=1)
            Label(_self.j_Resultilluminants, textvariable = fake).grid(column=1, row=2)
            Label(_self.j_Resultilluminants, textvariable = final).grid(column=1, row=3)
            #Label(_self.j_Resultilluminants, textvariable = saida).grid(column=1, row=4)
            Button(_self.j_Resultilluminants, underline=0, text=u"Fechar", command=lambda: _self.fecharJanelasSubordinadas("resultadoIllu")).grid(row=5, column=1)

        def janelaModulosExtracao(_self):

            def executar():
                extrairDescritoresdaImagem(_self, var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get(), var9.get(), var0.get())

            def verificaChkBox():
                if var0.get():
                    var1.set(0), var2.set(0), var3.set(0), var4.set(0), var5.set(0), var6.set(0), var7.set(0), var8.set(
                        0), var9.set(0)
                if var1.get() or var2.get() or var3.get() or var4.get() or var5.get() or var6.get() or var7.get() or var8.get() or var9.get():
                    var0.set(0)
                if var1.get() and var2.get() and var3.get() and var4.get() and var5.get() and var6.get() and var7.get() and var8.get() and var9.get():
                    var0.set(0)

            _self.j_illuminants = Toplevel(self.interface)
            _self.j_illuminants.title("Illuminants")
            _self.j_illuminants.resizable(width=FALSE, height=FALSE)
            _self.j_illuminants.wm_protocol("WM_DELETE_WINDOW", lambda : _self.fecharJanelasSubordinadas("Illuminants"))
            Label(_self.j_illuminants, text="Selecione os descritores desejados:").grid(column=0, row=0)

            var1 = IntVar()
            var2 = IntVar()
            var3 = IntVar()
            var4 = IntVar()
            var5 = IntVar()
            var6 = IntVar()
            var7 = IntVar()
            var8 = IntVar()
            var9 = IntVar()
            var0 = IntVar()

            Checkbutton(_self.j_illuminants, anchor=W, text="ACC - COR", variable=var1, offvalue=0,
                        width=20, command=verificaChkBox).grid(column=0, row=1)
            Checkbutton(_self.j_illuminants, anchor=W, text="BIC - COR", variable=var2, offvalue=0,
                        width=20, command=verificaChkBox).grid(column=0, row=2)
            Checkbutton(_self.j_illuminants, anchor=W, text="CCV - COR", variable=var3, offvalue=0,
                        width=20, command=verificaChkBox).grid(column=0, row=3)
            Checkbutton(_self.j_illuminants, anchor=W, text="EOAC - ARESTAS", variable=var4, offvalue=0,
                        width=20, command=verificaChkBox).grid(column=0, row=4)
            Checkbutton(_self.j_illuminants, anchor=W, text="LAS - TEXTURA", variable=var5, offvalue=0,
                        width=20, command=verificaChkBox).grid(column=0, row=5)
            Checkbutton(_self.j_illuminants, anchor=W, text="LCH - COR", variable=var6, offvalue=0,
                        width=20, command=verificaChkBox).grid(column=0, row=6)
            Checkbutton(_self.j_illuminants, anchor=W, text="SASI - TEXTURA", variable=var7, offvalue=0,
                        width=20, command=verificaChkBox).grid(column=0, row=7)
            Checkbutton(_self.j_illuminants, anchor=W, text="SPYTEC - ARESTAS", variable=var8, offvalue=0,
                        width=20, command=verificaChkBox).grid(column=0, row=8)
            Checkbutton(_self.j_illuminants, anchor=W, text="UNSER - TEXTURA", variable=var9, offvalue=0,
                        onvalue=1, width=20, command=verificaChkBox).grid(column=0, row=9)

            Checkbutton(_self.j_illuminants, anchor=W, text="TODOS", variable=var0, offvalue=0,
                        width=20, command=verificaChkBox).grid(column=0, row=10)
            Button(_self.j_illuminants, underline= 0, text=u"Cancelar", command=lambda: _self.fecharJanelasSubordinadas("Illuminants")).grid(row=10, column=1)
            Button(_self.j_illuminants, underline= 2,text=u"Executar",
                   command=executar).grid(row=10, column=2)

        janelaModulosExtracao(self)

def main():
    root = Tk()
    app = Cetico(root)

    root.mainloop()

    root.after(1, app.abrirImagem())

if __name__ == '__main__':
    main()

