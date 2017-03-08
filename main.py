from tkinter import *
from janela import Janela

root = Tk()
root.title("tkImg-dl")
root.geometry("+{}+{}".format( ((root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)),
                               ((root.winfo_screenheight() // 2) - (root.winfo_height() // 2)) ))
root.resizable(False, False)
Janela(root)

root.mainloop()
