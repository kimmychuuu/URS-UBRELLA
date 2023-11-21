from urs_umbrella import Machine
from datetime import datetime

import tkinter as tk

class Root(tk.Tk):
    # Initialize the GUI
    current_language = "English"

    def __init__(self, machine):
        super().__init__()
        self.medbot = machine
        self.title('Medbot')
        self.geometry("1030x540")
        self.resizable(False, False)

        self.show_homepage()
        self.mainloop()

    def show_homepage(self):
        for child in self.winfo_children():
            child.destroy()
        homepage = Homepage(self, self.medbot)
        homepage.pack()

    def show_insert_page(self):
        for child in self.winfo_children():
            child.destroy()
        insert_page = InsertPage(self, self.medbot)
        insert_page.pack()


class Homepage(tk.Canvas):
    def __init__(self, root: Root, machine: Machine, **kwargs):
        super().__init__(root, width=1030, height=540, **kwargs)
        self.machine = machine
        self.root = root

        '''
        '''

    
    def scan_and_proceed(self):
        user_id = self.machine.scan_qrcode()
        self.machine.user = user_id
        self.master.show_scan_page()

class InsertPage(tk.Canvas):
    def __init__(self, root: Root, machine: Machine, **kwargs):
        super().__init__(root, width=1030, height=540, **kwargs)
        self.machine = machine
        self.root = root

        ...

if __name__ == "__main__":
    machine = Machine()
    root = Root(machine)