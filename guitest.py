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
        self.title('URS')
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

    def show_scan_user_page(self):
        for child in self.winfo_children():
            child.destroy()
        scan_user_page = ScanUserPage(self, bg='#FEA633')
        scan_user_page.pack()

    def show_rent_page(self):
        for child in self.winfo_children():
            child.destroy()
        deposit_page = RentPage(self, bg='#FEA633')
        deposit_page.pack()

    def show_scan_umbrella_page(self):
        for child in self.winfo_children():
            child.destroy()
        scan_umbrella_page = ScanUmbrellaPage(self, bg='#1B1E2D')
        scan_umbrella_page.pack()

    def show_return_page(self):
        for child in self.winfo_children():
            child.destroy()
        return_page = ReturnPage(self, bg='#1B1E2D')
        return_page.pack()

    def show_payment_page(self, details):
        for child in self.winfo_children():
            child.destroy()
        payment_page = PaymentPage(self, details=details, bg='#1B1E2D')
        payment_page.pack()

    def show_thankyou_page(self):
        for child in self.winfo_children():
            child.destroy()
        thankyou_page = ThankYouPage(self, bg='#52B2B0')
        thankyou_page.pack()



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
        self.root.show_scan_user_page()



class ScanUserPage(tk.Canvas):
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
        # Check if qr is valid, if not valid show message then retry scan
        # valid = False
        # while not valid:
        #     user_id = self.machine.scan_qrcode()
        #     valid = self.machine.validate_user(user_id)
        #     if valid:
        #         self.machine.user = user_id
        #         break
        # rent_available = self.machine.check_availability(user_id)
        rent_available = False
        if rent_available:
            self.root.show_rent_page()
        else:
            self.root.show_scan_umbrella_page()
        


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
        # logout user
        time.sleep(5)
        self.root.show_thankyou_page()



class ScanUmbrellaPage(tk.Canvas):
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

        prompt = 'Place umbrella QR Code\nin front of the QR code\nScanner'
        self.create_text(520, 240, text=prompt, font=('Montserrat', 28, 'bold'), fill='white', anchor=tk.NW)

        # Temporary should handle the proceeding to next page via scan handler
        self.proceed_file = Image.open('assets/proceed_button.png').resize((215, 60))
        self.proceed_image = ImageTk.PhotoImage(self.proceed_file)
        self.proceed_button = self.create_image(700, 425, image=self.proceed_image, anchor=tk.NW)
        self.tag_bind(self.proceed_button, "<Button-1>", self.proceed)

    def proceed(self, event):
        # Check if qr is valid, if not valid show message then retry scan
        # valid = False
        # while not valid:
        #     umbrella_uuid = self.machine.scan_qrcode()
        #     valid = self.machine.confirm_umbrella(umbrella_uuid)
        #     if valid:
        #         self.show_return_page()
        time.sleep(5)
        self.root.show_return_page()



class ReturnPage(tk.Canvas):
    def __init__(self, root: Root, **kwargs):
        super().__init__(root, width=1024, height=600, **kwargs)
        self.root = root

        self.umbrella_logo_file = Image.open('assets/logo.png').resize((128, 128))
        self.umbrella_logo_image = ImageTk.PhotoImage(self.umbrella_logo_file)
        self.create_image(15, 15, image=self.umbrella_logo_image, anchor=tk.NW)

        self.create_text(140, 40, text='Umbrella Renting Machine', font=('Montserrat', 34, 'bold'), fill='white', anchor=tk.NW)
        self.create_text(150, 90, text='You matter the most under the umbrella', font=('Montserrat', 18, 'bold'), fill='white', anchor=tk.NW)

        self.deposit_file = Image.open('assets/assess.png').resize((350, 350))
        self.deposit_image = ImageTk.PhotoImage(self.deposit_file)
        self.create_image(30, 140, image=self.deposit_image, anchor=tk.NW)

        self.container_file = Image.open('assets/container.png').resize((620, 350))
        self.container_image = ImageTk.PhotoImage(self.container_file)
        self.create_image(400, 140, image=self.container_image, anchor=tk.NW)

        self.create_text(640, 175, text='None', font=('Montserrat', 14, 'bold'), fill='black')
        self.create_text(730, 175, text='Minor', font=('Montserrat', 14, 'bold'), fill='black')
        self.create_text(830, 175, text='Moderate', font=('Montserrat', 14, 'bold'), fill='black')
        self.create_text(930, 175, text='Sever', font=('Montserrat', 14, 'bold'), fill='black')

        self.create_text(450, 210, text='Handle Damage', font=('Montserrat', 14), fill='black', anchor=tk.NW)
        self.create_text(450, 250, text='Canopy Damage', font=('Montserrat', 14), fill='black', anchor=tk.NW)
        self.create_text(450, 290, text='Runner Damage', font=('Montserrat', 14), fill='black', anchor=tk.NW)
        self.create_text(450, 330, text='Rib Damage', font=('Montserrat', 14), fill='black', anchor=tk.NW)
        self.create_text(450, 370, text='Button Damage', font=('Montserrat', 14), fill='black', anchor=tk.NW)
        self.create_text(450, 410, text='Shaft Damage', font=('Montserrat', 14), fill='black', anchor=tk.NW)
        
        handle_damage = tk.IntVar()
        canopy_damage = tk.IntVar()
        runner_damage = tk.IntVar()
        rib_damage = tk.IntVar()
        button_damage = tk.IntVar()
        shaft_damage = tk.IntVar()
        handle_damage.set(0)
        canopy_damage.set(0)
        runner_damage.set(0)
        rib_damage.set(0)
        button_damage.set(0)
        shaft_damage.set(0)

        tk.Radiobutton(self, variable=handle_damage, value=0, bg='white').place(x=630, y=210)
        tk.Radiobutton(self, variable=handle_damage, value=1, bg='white').place(x=720, y=210)
        tk.Radiobutton(self, variable=handle_damage, value=2, bg='white').place(x=820, y=210)
        tk.Radiobutton(self, variable=handle_damage, value=3, bg='white').place(x=920, y=210)

        tk.Radiobutton(self, variable=canopy_damage, value=0, bg='white').place(x=630, y=250)
        tk.Radiobutton(self, variable=canopy_damage, value=1, bg='white').place(x=720, y=250)
        tk.Radiobutton(self, variable=canopy_damage, value=2, bg='white').place(x=820, y=250)
        tk.Radiobutton(self, variable=canopy_damage, value=3, bg='white').place(x=920, y=250)

        tk.Radiobutton(self, variable=runner_damage, value=0, bg='white').place(x=630, y=290)
        tk.Radiobutton(self, variable=runner_damage, value=1, bg='white').place(x=720, y=290)
        tk.Radiobutton(self, variable=runner_damage, value=2, bg='white').place(x=820, y=290)
        tk.Radiobutton(self, variable=runner_damage, value=3, bg='white').place(x=920, y=290)

        tk.Radiobutton(self, variable=rib_damage, value=0, bg='white').place(x=630, y=330)
        tk.Radiobutton(self, variable=rib_damage, value=1, bg='white').place(x=720, y=330)
        tk.Radiobutton(self, variable=rib_damage, value=2, bg='white').place(x=820, y=330)
        tk.Radiobutton(self, variable=rib_damage, value=3, bg='white').place(x=920, y=330)

        tk.Radiobutton(self, variable=button_damage, value=0, bg='white').place(x=630, y=370)
        tk.Radiobutton(self, variable=button_damage, value=1, bg='white').place(x=720, y=370)
        tk.Radiobutton(self, variable=button_damage, value=2, bg='white').place(x=820, y=370)
        tk.Radiobutton(self, variable=button_damage, value=3, bg='white').place(x=920, y=370)

        tk.Radiobutton(self, variable=shaft_damage, value=0, bg='white').place(x=630, y=410)
        tk.Radiobutton(self, variable=shaft_damage, value=1, bg='white').place(x=720, y=410)
        tk.Radiobutton(self, variable=shaft_damage, value=2, bg='white').place(x=820, y=410)
        tk.Radiobutton(self, variable=shaft_damage, value=3, bg='white').place(x=920, y=410)

        self.proceed_file = Image.open('assets/proceed_button.png').resize((215, 60))
        self.proceed_image = ImageTk.PhotoImage(self.proceed_file)
        self.proceed_button = self.create_image(750, 450, image=self.proceed_image, anchor=tk.NW)
        self.tag_bind(self.proceed_button, "<Button-1>", self.assess_damage)

    def assess_damage(self, event):
        # Insert damage assessment logic
        # save damage assessment to a variable as this is needed later on
        # self.machine.damage_rating = rating
        # compute for the total payment
        transaction_details = {
            'rented_at': datetime.now(),
            'returned_at': datetime.now(),
            'duration': '0 days, 3 hours, 3 mins',
            'rent_fee': 15,
            'damage_rating': 'Minor',
            'damage_fee': 10,
            'total_fee': 25
        }
        self.root.show_payment_page(transaction_details)



class PaymentPage(tk.Canvas):
    def __init__(self, root: Root, details: dict, **kwargs):
        super().__init__(root, width=1024, height=600, **kwargs)
        self.root = root

        self.umbrella_logo_file = Image.open('assets/logo.png').resize((128, 128))
        self.umbrella_logo_image = ImageTk.PhotoImage(self.umbrella_logo_file)
        self.create_image(15, 15, image=self.umbrella_logo_image, anchor=tk.NW)

        self.create_text(140, 40, text='Umbrella Renting Machine', font=('Montserrat', 34, 'bold'), fill='white', anchor=tk.NW)
        self.create_text(150, 90, text='You matter the most under the umbrella', font=('Montserrat', 18, 'bold'), fill='white', anchor=tk.NW)

        self.accept_umbrella_file = Image.open('assets/return.png').resize((350, 350))
        self.accept_umbrella_image = ImageTk.PhotoImage(self.accept_umbrella_file)

        self.container_file = Image.open('assets/container.png').resize((540, 350))
        self.container_image = ImageTk.PhotoImage(self.container_file)
        self.container = self.create_image(80, 180, image=self.container_image, anchor=tk.NW)

        self.rent_date_label = self.create_text(100, 200, text=f'Rent Date:           {datetime.strftime(details["rented_at"], "%b %d, %Y %I:%M:%S %p")}', font=('Montserrat', 18), fill='black', anchor=tk.NW)
        self.return_date_label = self.create_text(100, 235, text=f'Return Date:        {datetime.strftime(details["rented_at"], "%b %d, %Y %I:%M:%S %p")}', font=('Montserrat', 18), fill='black', anchor=tk.NW)
        self.duration_label = self.create_text(100, 270, text=f'Rent Duration:      {details["duration"]}', font=('Montserrat', 18), fill='black', anchor=tk.NW)
        self.damage_rating_label = self.create_text(100, 305, text=f'Damage Rating:   {details["damage_rating"]}', font=('Montserrat', 18), fill='black', anchor=tk.NW)

        self.rent_fee_label = self.create_text(100, 360, text=f'Rent Fee:         ₱{details["rent_fee"]}', font=('Montserrat', 22, 'bold'), fill='black', anchor=tk.NW)
        self.damage_fee_label = self.create_text(100, 400, text=f'Damage Fee:   ₱{details["damage_fee"]}', font=('Montserrat', 22, 'bold'), fill='black', anchor=tk.NW)
        self.line = self.create_line(100, 450, 590, 450,  width=2)
        self.total_fee_label = self.create_text(100, 460, text=f'Total Fee:        ₱{details["total_fee"]}', font=('Montserrat', 22, 'bold'), fill='black', anchor=tk.NW)

        self.insert_coin_label = self.create_text(820, 230, text='Insert coins', font=('Montserrat', 22, 'bold'), fill='white', anchor=tk.CENTER)

        self.counter_container_file = Image.open('assets/counter_container.png').resize((256, 256))
        self.counter_container_image = ImageTk.PhotoImage(self.counter_container_file)
        self.counter_container = self.create_image(820, 390, image=self.counter_container_image, anchor=tk.CENTER)

        self.counter_label = tk.Label(self, text=f'{details["total_fee"]}', font=('Montserrat', 96, 'bold'), bg='#D9D9D9', anchor=tk.NW)
        self.counter_label.place(x=750, y=310)

        self.after(1000, self.wait_for_payment)

    def wait_for_payment(self):
        # Insert wait for payment logic
        time.sleep(5)
        self.after(1000, self.accept_umbrella)

    def accept_umbrella(self):
        self.delete(self.container)
        self.delete(self.rent_date_label)
        self.delete(self.return_date_label)
        self.delete(self.duration_label)
        self.delete(self.damage_rating_label)
        self.delete(self.rent_fee_label)
        self.delete(self.damage_fee_label)
        self.delete(self.line)
        self.delete(self.total_fee_label)
        self.delete(self.insert_coin_label)
        self.delete(self.counter_container)
        self.counter_label.destroy()
        self.create_image(145, 140, image=self.accept_umbrella_image, anchor=tk.NW)
        self.create_text(540, 190, text='Please return the\numbrella to the machine', font=('Montserrat', 28, 'bold'), fill='white', anchor=tk.NW)
        self.create_text(540, 280, text='This may take a moment.', font=('Montserrat', 18, 'bold'), fill='white', anchor=tk.NW)
        self.after(1000, self.wait_for_umbrella)

    def wait_for_umbrella(self):
        time.sleep(5)
        self.root.show_thankyou_page()


class ThankYouPage(tk.Canvas):
    def __init__(self, root: Root, **kwargs):
        super().__init__(root, width=1024, height=600, **kwargs)
        self.root = root

        self.umbrella_logo_file = Image.open('assets/logo.png').resize((128, 128))
        self.umbrella_logo_image = ImageTk.PhotoImage(self.umbrella_logo_file)
        self.create_image(15, 15, image=self.umbrella_logo_image, anchor=tk.NW)

        self.create_text(140, 40, text='Umbrella Renting Machine', font=('Montserrat', 34, 'bold'), fill='white', anchor=tk.NW)
        self.create_text(150, 90, text='You matter the most under the umbrella', font=('Montserrat', 18, 'bold'), fill='white', anchor=tk.NW)

        self.container_file = Image.open('assets/container.png').resize((980, 260))
        self.container_image = ImageTk.PhotoImage(self.container_file)
        self.create_image(515, 300, image=self.container_image, anchor=tk.CENTER)

        self.create_text(515, 300, text='Thank you for using Umbrella Renting System', font=('Montserrat', 26, 'bold'), fill='black', anchor=tk.CENTER)

        self.after(2000, self.return_to_homepage)

    def return_to_homepage(self):
        time.sleep(3)
        self.root.show_home_page()



if __name__ == '__main__':
    # machine = Machine()
    root = Root()