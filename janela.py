from tkinter import *
from tkinter import messagebox
from os import system
from clipboard import paste
from salvar import lancar


class Janela(object):
    """Classe que implementa a janela do cliente."""
    def __init__(self, master):
        # Janela principal
        self.janela = master

        # Frame dos potoẽs de cima da tela
        self.frame = Frame(self.janela)
        self.frame.pack()
        
        self.botao_adicionar = Button(self.frame, text="Adicionar", command=self.__novo_entry, bd=3)
        self.botao_adicionar['font'] = ('Arial', 12)
        self.botao_adicionar.pack(pady=10, padx=30, side=LEFT)
        
        self.botao_deletar = Button(self.frame, text="Deletar", command=self.__deletar, bd=3)
        self.botao_deletar['font'] = ('Arial', 12)
        self.botao_deletar.pack(padx=30, side="right")
        
        self.frame2 = Frame(self.janela)
        self.frame2.pack()

        # Barra de rolagem vertical
        self.scrollbary = Scrollbar(self.frame2)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        
        # Barra de rolagem horizontal
        self.scrollbarx = Scrollbar(self.frame2, orient=HORIZONTAL)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        
        # cria uma listbox
        self.listbox = Listbox(self.frame2, width=50, height=10, selectmode=EXTENDED)
        # selectmode=EXTENDED permite seleção de mais de um item
        self.listbox.pack()
        
        # anexa listbox para scrollbar vertical e horizontal
        self.listbox.config(yscrollcommand=self.scrollbary.set)
        self.scrollbary.config(command=self.listbox.yview)
        self.listbox.config(xscrollcommand=self.scrollbarx.set)
        self.scrollbarx.config(command=self.listbox.xview)

        self.frame3 = Frame(self.janela)
        self.frame3.pack()
        self.botao_baixar = Button(self.frame3, text="Baixar", command=self.__baixar, bd=3)
        self.botao_baixar['font'] = ('Arial', 12)
        self.botao_baixar.pack(pady=10)

        self.plot_menu()
        system('echo "src: $(pwd)/" > config.txt')

    def plot_menu(self):
        """
        Plota o menu de opções.

        :return: Sem retorno.
        """
        self.menu = Menu(self.janela)
        self.janela.config(menu=self.menu)

        self.menu_config = Menu(self.menu)
        self.menu.add_cascade(label="Editar", menu=self.menu_config)
        self.menu_config.add_command(label="Configurações", command=lancar)

    def __novo_entry(self):
        """
        Adiciona um novo link à lista de links.
        :return: Sem retorno.
        """
        self.listbox.insert(END, self.__link_copiado())

    @staticmethod
    def __link_copiado():
        """
        Retorna a string atual da área de transferência.
        :return: String.
        """
        try:
            link = paste()
            return link
        except Exception:
            # TODO: Fazer janela de diálogo para pegar o link.
            return ''

    def __deletar(self):
        """
        Deleta os links selecionados da lista de links.
        :return: Sem retorno.
        """
        items = self.listbox.curselection()  # obtem lista de índices dos itens
        if len(items) == 0:
            messagebox.showwarning("tkImg-dl", "Selecione pelo menos um item!")
        else:
            pos = 0
            for i in items:
                item_pos = int(i) - pos  # obtem a posição do item selecionado
                self.listbox.delete(item_pos, item_pos)  # deleta um item selecionado
                pos += 1

    def __baixar(self):
        """
        Faz o download dos links da lista de links.
        :return: Sem retorno.
        """
        links = self.listbox.get(0, END)
        for img in range(len(self.listbox.get(0, END))):
            # print("cd %s && wget %s -O %02d.jpg" %(self.__get_diretorio(), links[img], img))
            # system("cd %s && wget %s -O %02d.jpg && pwd" % (self.__get_diretorio(), links[img], img))
            system("./baixar.sh %s %s %s" % (self.__get_diretorio(), links[img], img))
        messagebox.showinfo("Download", "Download Completo")
        exit()

    def __get_diretorio(self):
        """
        Pega o caminho da pasta de destino.

        :return: String.
        """
        file = open("config.txt", 'r')
        for line in file.readlines():
            pass
            if("src:" in line):
                return line.split("src: ")[-1].split("\n")[0]
