from tkinter import *
from janela import Janela


root = Tk()
root.title("tkImg-dl")
root.geometry("+{}+{}".format( ((root.winfo_screenwidth() // 4) - (root.winfo_width() // 4)),
                               ((root.winfo_screenheight() // 4) - (root.winfo_height() // 4)) ))
root.resizable(False, False)
Janela(root)

root.mainloop()
