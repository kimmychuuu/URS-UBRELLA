# from urs_umbrella import Machine
import tkinter as tk
import time

from tkinter import ttk as ttk
from tkinter import messagebox  as messagebox
from datetime import datetime
from PIL import Image, ImageTk


class Root(tk.Tk):
    # Initialize the GUI
    current_language = 'English'

    def __init__(self):
        super().__init__()
        self.title('Medbot')
        self.geometry('1030x540')
        self.resizable(False, False)

        self.show_home_page()
        self.mainloop()

    def show_home_page(self):
        for child in self.winfo_children():
            child.destroy()
        homepage = Homepage(self, bg='#52B2B0')
        homepage.pack()

    def show_register_page(self):
        for child in self.winfo_children():
            child.destroy()
        register_page = RegisterPage(self, bg='#FEA633')
        register_page.pack()

    def show_scan_page(self):
        for child in self.winfo_children():
            child.destroy()
        scan_page = ScanPage(self, bg='#FEA633')
        scan_page.pack()

    def show_rent_page(self):
        for child in self.winfo_children():
            child.destroy()
        deposit_page = RentPage(self, bg='#FEA633')
        deposit_page.pack()



class Homepage(tk.Canvas):
    def __init__(self, root: Root, **kwargs):
        super().__init__(root, width=1030, height=540, **kwargs)
        self.root = root

        self.msc_logo_file = Image.open('assets/msc_logo.png').resize((50, 50))
        self.msc_logo_image = ImageTk.PhotoImage(self.msc_logo_file)
        self.msc_logo = self.create_image(80, 50, image=self.msc_logo_image)

        self.coeng_logo_file = Image.open('assets/seng_logo.png').resize((50, 50))
        self.coeng_logo_image = ImageTk.PhotoImage(self.coeng_logo_file)
        self.coeng_logo = self.create_image(140, 50, image=self.coeng_logo_image)

        self.umbrella_logo_file = Image.open('assets/logo.png').resize((500, 500))
        self.umbrella_logo_image = ImageTk.PhotoImage(self.umbrella_logo_file)
        self.umbrella_logo = self.create_image(220, 280, image=self.umbrella_logo_image)

        self.create_text(180, 20, text='Marinduque State College', font=('Montserrat', 16), fill='white', anchor=tk.NW)
        self.create_text(180, 40, text='College of Engineering', font=('Montserrat', 18, 'bold'), fill='white', anchor=tk.NW)
        self.create_text(450, 180, text='U-BRELLA', font=('Montserrat', 40, 'bold'), fill='white', anchor=tk.NW)
        self.create_text(450, 240, text='Umbrella\nRenting Machine', font=('Montserrat', 34), fill='white', anchor=tk.NW)
        self.create_text(450, 340, text='You matter the most under the umbrella', font=('Montserrat', 18, 'bold'), fill='black', anchor=tk.NW)

        self.get_started_file = Image.open('assets/getstarted_button.png').resize((215, 60))
        self.get_started_image = ImageTk.PhotoImage(self.get_started_file)
        self.get_stated_button = self.create_image(550, 400, image=self.get_started_image, anchor=tk.NW)
        self.tag_bind(self.get_stated_button, "<Button-1>", self.proceed)

    def proceed(self, event):
        self.root.show_register_page()



class RegisterPage(tk.Canvas):
    def __init__(self, root: Root, **kwargs):
        super().__init__(root, width=1024, height=600, **kwargs)
        self.root = root

        self.umbrella_logo_file = Image.open('assets/logo.png').resize((128, 128))
        self.umbrella_logo_image = ImageTk.PhotoImage(self.umbrella_logo_file)
        self.create_image(15, 15, image=self.umbrella_logo_image, anchor=tk.NW)

        self.create_text(140, 40, text='Umbrella Renting Machine', font=('Montserrat', 34, 'bold'), fill='white', anchor=tk.NW)
        self.create_text(150, 90, text='You matter the most under the umbrella', font=('Montserrat', 18, 'bold'), fill='black', anchor=tk.NW)

        self.register_qrcode_file = Image.open('assets/register_qrcode.png').resize((350, 350))
        self.register_qrcode_image = ImageTk.PhotoImage(self.register_qrcode_file)
        self.create_image(145, 140, image=self.register_qrcode_image, anchor=tk.NW)

        self.create_text(475, 225, text='Step 1: Scan the QR code', font=('Montserrat', 28, 'bold'), fill='white', anchor=tk.NW)
        self.create_text(475, 275, text='Step 2: Register as user', font=('Montserrat', 28, 'bold'), fill='white', anchor=tk.NW)
        self.create_text(475, 325, text='Step 3: Proceed', font=('Montserrat', 28, 'bold'), fill='white', anchor=tk.NW)
        
        self.proceed_file = Image.open('assets/proceed_button.png').resize((215, 60))
        self.proceed_image = ImageTk.PhotoImage(self.proceed_file)
        self.proceed_button = self.create_image(700, 425, image=self.proceed_image, anchor=tk.NW)
        self.tag_bind(self.proceed_button, "<Button-1>", self.proceed)

    def proceed(self, event):
        self.root.show_scan_page()



class ScanPage(tk.Canvas):
    def __init__(self, root: Root, **kwargs):
        super().__init__(root, width=1024, height=600, **kwargs)
        self.root = root

        self.umbrella_logo_file = Image.open('assets/logo.png').resize((128, 128))
        self.umbrella_logo_image = ImageTk.PhotoImage(self.umbrella_logo_file)
        self.create_image(15, 15, image=self.umbrella_logo_image, anchor=tk.NW)

        self.create_text(140, 40, text='Umbrella Renting Machine', font=('Montserrat', 34, 'bold'), fill='white', anchor=tk.NW)
        self.create_text(150, 90, text='You matter the most under the umbrella', font=('Montserrat', 18, 'bold'), fill='black', anchor=tk.NW)

        self.scan_file = Image.open('assets/scan.png').resize((350, 350))
        self.scan_image = ImageTk.PhotoImage(self.scan_file)
        self.create_image(145, 140, image=self.scan_image, anchor=tk.NW)

        prompt = 'Place your student I.D.\nin front of the QR code\nScanner'
        self.create_text(520, 240, text=prompt, font=('Montserrat', 28, 'bold'), fill='white', anchor=tk.NW)

        # Temporary should handle the proceeding to next page via scan handler
        self.proceed_file = Image.open('assets/proceed_button.png').resize((215, 60))
        self.proceed_image = ImageTk.PhotoImage(self.proceed_file)
        self.proceed_button = self.create_image(700, 425, image=self.proceed_image, anchor=tk.NW)
        self.tag_bind(self.proceed_button, "<Button-1>", self.proceed)

    def proceed(self, event):
        # Insert scan logic
        # Then check if valid, if not valid show message then retry scan
        # valid = False
        # while not valid:
        #     user_id = self.machine.scan_qrcode()
        #     valid = self.machine.validate_user(user_id)
        #     if valid:
        #         self.machine.user = user_id
        #         break
        # rent_available = self.machine.check_availability(user_id)
        rent_available = True
        if rent_available:
            self.root.show_rent_page()
        


class RentPage(tk.Canvas):
    def __init__(self, root: Root, **kwargs):
        super().__init__(root, width=1024, height=600, **kwargs)
        self.root = root

        self.umbrella_logo_file = Image.open('assets/logo.png').resize((128, 128))
        self.umbrella_logo_image = ImageTk.PhotoImage(self.umbrella_logo_file)
        self.create_image(15, 15, image=self.umbrella_logo_image, anchor=tk.NW)

        self.create_text(140, 40, text='Umbrella Renting Machine', font=('Montserrat', 34, 'bold'), fill='white', anchor=tk.NW)
        self.create_text(150, 90, text='You matter the most under the umbrella', font=('Montserrat', 18, 'bold'), fill='black', anchor=tk.NW)

        self.deposit_file = Image.open('assets/deposit.png').resize((350, 350))
        self.deposit_image = ImageTk.PhotoImage(self.deposit_file)
        self.image_placeholder = self.create_image(145, 140, image=self.deposit_image, anchor=tk.NW)

        self.title_label = self.create_text(540, 220, text='Please deposit ₱5', font=('Montserrat', 28, 'bold'), fill='white', anchor=tk.NW)
        tip = 'Tip: Any change will be\n     automatically added to your wallet,\n     which can be used later on :)'
        self.subtitle_label = self.create_text(540, 275, text=tip, font=('Montserrat', 16, 'bold'), fill='black', anchor=tk.NW)

        # Preload other assets
        self.dispense_file = Image.open('assets/dispense.png').resize((350, 350))
        self.dispense_image = ImageTk.PhotoImage(self.dispense_file)

        self.scan_file = Image.open('assets/scan.png').resize((350, 350))
        self.scan_image = ImageTk.PhotoImage(self.scan_file)

        # Temporary should handle the proceeding to next page via deposit handler
        self.proceed_file = Image.open('assets/proceed_button.png').resize((215, 60))
        self.proceed_image = ImageTk.PhotoImage(self.proceed_file)
        self.proceed_button = self.create_image(700, 425, image=self.proceed_image, anchor=tk.NW)
        self.tag_bind(self.proceed_button, "<Button-1>", self.dispense_umbrella)

        # Call deposit directly instead of button
        # self.deposit()

    def deposit(self):
        # Insert deposit logic then call dispense umbrella
        self.dispense_umbrella()

    # remove event param
    def dispense_umbrella(self, event):
        self.delete(self.image_placeholder)
        self.delete(self.title_label)
        self.delete(self.subtitle_label)
        self.image_placeholder = self.create_image(145, 140, image=self.dispense_image, anchor=tk.NW)
        self.title_label = self.create_text(540, 190, text='Please wait for the\numbrella to be dispensed', font=('Montserrat', 28, 'bold'), fill='white', anchor=tk.NW)
        self.subtitle_label = self.create_text(540, 280, text='This may take a moment.', font=('Montserrat', 18, 'bold'), fill='black', anchor=tk.NW)
        # Insert dispense logic
        self.after(1000, self.dispense)

    def dispense(self):
        # Insert dispense logic
        # time.sleep is only temporary
        time.sleep(5)
        self.scan_umbrella()

    def scan_umbrella(self):
        self.delete(self.image_placeholder)
        self.delete(self.title_label)
        self.delete(self.subtitle_label)
        self.image_placeholder = self.create_image(145, 140, image=self.scan_image, anchor=tk.NW)
        prompt = 'Place your student I.D.\nin front of the QR code\nScanner'
        self.title_label = self.create_text(520, 240, text=prompt, font=('Montserrat', 28, 'bold'), fill='white', anchor=tk.NW)
        self.after(1000, self.scan)

    def scan(self):
        # Insert scan logic
        # Insert save logic
        # time.sleep is only temporary
        time.sleep(5)
        self.after(3000, self.root.show_home_page)
        messagebox.showinfo('Success', 'Transaction Completed', parent=self)


if __name__ == '__main__':
    # machine = Machine()
    root = Root()