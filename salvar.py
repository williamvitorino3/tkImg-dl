# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.filedialog import askdirectory
from os import system as term


class Salvar():
    """ Classe que implementa a janela de condiguração de salvamento dos arquivos. """
    def __init__(self, window, config):
        """
        Construtor da classe.
        :param config: Endereço do arquivo de configuração.
        :return: Sem retorno.
        """
        self.janela = window
        self.config_file = config
        
        # Frame dos widgets para escolha.
        self.frame_escolha = Frame(self.janela)
        self.frame_escolha.pack()

        # Entrada de texto do destino das imagens.
        self.src_entry = Entry(self.frame_escolha)
        self.src_entry.insert(0, self.get_diretorio_atual())
        self.src_entry.pack(side=LEFT)

        # Botão para escolher a pasta de destino.
        self.botao_escolha = Button(self.frame_escolha, text="Escolher", command=self.set_diretorio)
        self.botao_escolha.pack(side=RIGHT)

        # Botão de salvar
        self.botao_salvar = Button(self.janela, text="Salvar", command=self.salvar)
        self.botao_salvar.pack(side=BOTTOM)

    def set_diretorio(self):
        """
        Atera o diretório de download para o escolhido.

        :return: Sem retorno.
        """
        self.src_entry.delete(0, END)
        self.src_entry.insert(0, askdirectory())

    def get_diretorio_atual(self):
        """
        Pega o endereço de salvamento atual.

        :return: String.
        """
        term("pwd > out.txt")
        file = open("out.txt", 'r')
        src = file.read().split('\n')[0] + '/'
        file.close()
        term("rm out.txt")
        return src
    
    def salvar(self):
        """
        Abre o diretório de destino das imagens.

        :return: Sem retorno.
        """
        file = open("config.txt", 'w')
        file.write("src: %s/" % self.src_entry.get())
        file.close()
        self.janela.destroy()


def lancar():
    janela = Tk()
    janela.title("tkImg-dl")
    janela.geometry("+{}+{}".format( ((janela.winfo_screenwidth() // 4) - (janela.winfo_width() // 4)),
                                ((janela.winfo_screenheight() // 4) - (janela.winfo_height() // 4)) ))
    Salvar(janela, "")
    janela.resizable(False, False)
    janela.mainloop()