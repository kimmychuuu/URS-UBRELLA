from urs_umbrella import Machine
import tkinter as tk
import time
import statistics

from tkinter import ttk as ttk
from tkinter import messagebox  as messagebox
from datetime import datetime
from PIL import Image, ImageTk


class Root(tk.Tk):
    # Initialize the GUI
    current_language = 'English'

    def __init__(self, machine: Machine):
        super().__init__()
        self.title('URS')
        self.geometry('1030x540')
        self.resizable(False, False)
        self.machine = machine

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
        scan_umbrella_page = ScanUmbrellaPage(self, bg='#FEA633')
        scan_umbrella_page.pack()

    def show_pre_damage_assessment_page(self, umbrella_uuid: str):
        for child in self.winfo_children():
            child.destroy()
        pre_damage_assessment_page = PreDamageAssessmentPage(self, 
                                                             umbrella_uuid=umbrella_uuid, 
                                                             bg='#1B1E2D')
        pre_damage_assessment_page.pack()
        
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

        self.after(1000, self.proceed)

    def proceed(self):
        # Check if qr is valid, if not valid show message then retry scan
        valid = False
        while not valid:
            user_id = self.root.machine.scan_qrcode(gui=True)
            valid = self.root.machine.validate_user(user_id)
            if valid:
                self.root.machine.set_current_user(user_id)
                break
            else:
                if not messagebox.askretrycancel('Invalid QR Code', 'User ID not found. Retry scanning?', parent=self):
                    self.root.show_home_page()

        rent_available = self.root.machine.check_availability(user_id)
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

        self.after(1000, self.deposit)

    def deposit(self):
        self.root.machine.accepting_coin = True
        deposit_amount = 5
        while self.root.machine.inserted_coins < deposit_amount:
            print(self.root.machine.inserted_coins)
        else:
            extra = self.root.machine.inserted_coins - deposit_amount
            self.root.machine.add_balance(self.root.machine.user, extra)
            self.root.machine.reset_inserted_coins()
        self.root.machine.accepting_coin = False
        time.sleep(5)
        self.dispense_umbrella()

    def dispense_umbrella(self):
        self.delete(self.image_placeholder)
        self.delete(self.title_label)
        self.delete(self.subtitle_label)
        self.image_placeholder = self.create_image(145, 140, image=self.dispense_image, anchor=tk.NW)
        self.title_label = self.create_text(540, 190, text='Please wait for the\numbrella to be dispensed', font=('Montserrat', 28, 'bold'), fill='white', anchor=tk.NW)
        self.subtitle_label = self.create_text(540, 280, text='This may take a moment.', font=('Montserrat', 18, 'bold'), fill='black', anchor=tk.NW)
        
        self.after(1000, self.dispense)

    def dispense(self):
        self.root.machine.start_motor()
        while self.root.machine.get_distance_from_ultrasonic(3) > 10:
            pass
        self.root.machine.open_dispensing_servo()
        while self.root.machine.get_distance_from_ultrasonic(4) > 10:
            pass
        self.root.machine.close_dispensing_servo()
        self.root.machine.stop_motor()
        self.root.machine.tone()

        self.scan_umbrella()

    def scan_umbrella(self):
        self.delete(self.image_placeholder)
        self.delete(self.title_label)
        self.delete(self.subtitle_label)
        self.image_placeholder = self.create_image(145, 140, image=self.scan_image, anchor=tk.NW)
        prompt = 'Place your umbrella QRCode\nin front of the QR code\nScanner'
        self.title_label = self.create_text(520, 240, text=prompt, font=('Montserrat', 28, 'bold'), fill='white', anchor=tk.NW)
        self.after(1000, self.scan)

    def scan(self):
        umbrella_uuid = self.root.machine.scan_qrcode(gui=True)
        try:
            self.root.machine.rent_umbrella(
                user_id=self.root.machine.user,
                umbrella_uuid=umbrella_uuid,
                rented_at=datetime.now(),
            )
        except Exception as e:
            messagebox.showerror('Exception', e)
        self.root.machine.logout()
        transaction = self.root.machine.get_latest_transaction(umbrella_uuid=umbrella_uuid)
        if transaction:
            damage_rating = transaction.get("damage_rating")
            if damage_rating == 'None':
                if messagebox.askyesno('No previous damage assessment',
                                       'No previous damage assessment found, would you like to assess umbrella damage?'):
                    self.root.show_pre_damage_assessment_page(umbrella_uuid)
        self.root.show_thankyou_page()

        


class PreDamageAssessmentPage(tk.Canvas):
    def __init__(self, root: Root, umbrella_uuid: str, **kwargs):
        super().__init__(root, width=1024, height=600, **kwargs)
        self.root = root
        self.umbrella_uuid = umbrella_uuid

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
        
        self.handle_damage = tk.IntVar()
        self.canopy_damage = tk.IntVar()
        self.runner_damage = tk.IntVar()
        self.rib_damage = tk.IntVar()
        self.button_damage = tk.IntVar()
        self.shaft_damage = tk.IntVar()
        self.handle_damage.set(0)
        self.canopy_damage.set(0)
        self.runner_damage.set(0)
        self.rib_damage.set(0)
        self.button_damage.set(0)
        self.shaft_damage.set(0)

        tk.Radiobutton(self, variable=self.handle_damage, value=0, bg='white').place(x=630, y=210)
        tk.Radiobutton(self, variable=self.handle_damage, value=1, bg='white').place(x=720, y=210)
        tk.Radiobutton(self, variable=self.handle_damage, value=2, bg='white').place(x=820, y=210)
        tk.Radiobutton(self, variable=self.handle_damage, value=3, bg='white').place(x=920, y=210)

        tk.Radiobutton(self, variable=self.canopy_damage, value=0, bg='white').place(x=630, y=250)
        tk.Radiobutton(self, variable=self.canopy_damage, value=1, bg='white').place(x=720, y=250)
        tk.Radiobutton(self, variable=self.canopy_damage, value=2, bg='white').place(x=820, y=250)
        tk.Radiobutton(self, variable=self.canopy_damage, value=3, bg='white').place(x=920, y=250)

        tk.Radiobutton(self, variable=self.runner_damage, value=0, bg='white').place(x=630, y=290)
        tk.Radiobutton(self, variable=self.runner_damage, value=1, bg='white').place(x=720, y=290)
        tk.Radiobutton(self, variable=self.runner_damage, value=2, bg='white').place(x=820, y=290)
        tk.Radiobutton(self, variable=self.runner_damage, value=3, bg='white').place(x=920, y=290)

        tk.Radiobutton(self, variable=self.rib_damage, value=0, bg='white').place(x=630, y=330)
        tk.Radiobutton(self, variable=self.rib_damage, value=1, bg='white').place(x=720, y=330)
        tk.Radiobutton(self, variable=self.rib_damage, value=2, bg='white').place(x=820, y=330)
        tk.Radiobutton(self, variable=self.rib_damage, value=3, bg='white').place(x=920, y=330)

        tk.Radiobutton(self, variable=self.button_damage, value=0, bg='white').place(x=630, y=370)
        tk.Radiobutton(self, variable=self.button_damage, value=1, bg='white').place(x=720, y=370)
        tk.Radiobutton(self, variable=self.button_damage, value=2, bg='white').place(x=820, y=370)
        tk.Radiobutton(self, variable=self.button_damage, value=3, bg='white').place(x=920, y=370)

        tk.Radiobutton(self, variable=self.shaft_damage, value=0, bg='white').place(x=630, y=410)
        tk.Radiobutton(self, variable=self.shaft_damage, value=1, bg='white').place(x=720, y=410)
        tk.Radiobutton(self, variable=self.shaft_damage, value=2, bg='white').place(x=820, y=410)
        tk.Radiobutton(self, variable=self.shaft_damage, value=3, bg='white').place(x=920, y=410)

        self.proceed_file = Image.open('assets/proceed_button.png').resize((215, 60))
        self.proceed_image = ImageTk.PhotoImage(self.proceed_file)
        self.proceed_button = self.create_image(750, 450, image=self.proceed_image, anchor=tk.NW)
        self.tag_bind(self.proceed_button, "<Button-1>", self.assess_damage)

    def assess_damage(self, event):
        damages = [
            self.handle_damage.get(),
            self.canopy_damage.get(),
            self.runner_damage.get(),
            self.rib_damage.get(),
            self.button_damage.get(),
            self.shaft_damage.get(),
        ]
        damage_score = statistics.mean(damages)
        damage_rating = self.get_damage_interpretation(damage_score)
        damage_fee = 0
        for damage in damages:
            damage_fee += self.get_damage_fee(damage)
            
        previous_transaction = self.root.machine.get_latest_transaction(umbrella_uuid=self.umbrella_uuid)
        self.root.machine.deduct_balance(previous_transaction['user']['id'], damage_fee)
        self.root.show_thankyou_page()

    @staticmethod
    def get_damage_interpretation(value):
        if value <= 0:
            return 'None'
        elif value == 1:
            return 'Minor'
        elif value == 2:
            return 'Moderate'
        else:
            return 'Severe'
        
    @staticmethod 
    def get_damage_fee(score: int):
        if score == 1:
            return 15
        if score == 2:
            return 40
        if score == 3:
            return 70
        return 0
    



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

        self.after(1000, self.proceed)

    def proceed(self):
        # Check if qr is valid, if not valid show message then retry scan
        valid = False
        while not valid:
            umbrella_uuid = self.root.machine.scan_qrcode(gui=True)
            valid = self.root.machine.confirm_umbrella(self.root.machine.user, umbrella_uuid)
            if valid:
                self.root.show_return_page()
            else:
                if not messagebox.askretrycancel('Invalid QR Code', 'User ID not found. Retry scanning?', parent=self):
                    self.root.show_home_page()



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
        
        self.handle_damage = tk.IntVar()
        self.canopy_damage = tk.IntVar()
        self.runner_damage = tk.IntVar()
        self.rib_damage = tk.IntVar()
        self.button_damage = tk.IntVar()
        self.shaft_damage = tk.IntVar()
        self.handle_damage.set(0)
        self.canopy_damage.set(0)
        self.runner_damage.set(0)
        self.rib_damage.set(0)
        self.button_damage.set(0)
        self.shaft_damage.set(0)

        tk.Radiobutton(self, variable=self.handle_damage, value=0, bg='white').place(x=630, y=210)
        tk.Radiobutton(self, variable=self.handle_damage, value=1, bg='white').place(x=720, y=210)
        tk.Radiobutton(self, variable=self.handle_damage, value=2, bg='white').place(x=820, y=210)
        tk.Radiobutton(self, variable=self.handle_damage, value=3, bg='white').place(x=920, y=210)

        tk.Radiobutton(self, variable=self.canopy_damage, value=0, bg='white').place(x=630, y=250)
        tk.Radiobutton(self, variable=self.canopy_damage, value=1, bg='white').place(x=720, y=250)
        tk.Radiobutton(self, variable=self.canopy_damage, value=2, bg='white').place(x=820, y=250)
        tk.Radiobutton(self, variable=self.canopy_damage, value=3, bg='white').place(x=920, y=250)

        tk.Radiobutton(self, variable=self.runner_damage, value=0, bg='white').place(x=630, y=290)
        tk.Radiobutton(self, variable=self.runner_damage, value=1, bg='white').place(x=720, y=290)
        tk.Radiobutton(self, variable=self.runner_damage, value=2, bg='white').place(x=820, y=290)
        tk.Radiobutton(self, variable=self.runner_damage, value=3, bg='white').place(x=920, y=290)

        tk.Radiobutton(self, variable=self.rib_damage, value=0, bg='white').place(x=630, y=330)
        tk.Radiobutton(self, variable=self.rib_damage, value=1, bg='white').place(x=720, y=330)
        tk.Radiobutton(self, variable=self.rib_damage, value=2, bg='white').place(x=820, y=330)
        tk.Radiobutton(self, variable=self.rib_damage, value=3, bg='white').place(x=920, y=330)

        tk.Radiobutton(self, variable=self.button_damage, value=0, bg='white').place(x=630, y=370)
        tk.Radiobutton(self, variable=self.button_damage, value=1, bg='white').place(x=720, y=370)
        tk.Radiobutton(self, variable=self.button_damage, value=2, bg='white').place(x=820, y=370)
        tk.Radiobutton(self, variable=self.button_damage, value=3, bg='white').place(x=920, y=370)

        tk.Radiobutton(self, variable=self.shaft_damage, value=0, bg='white').place(x=630, y=410)
        tk.Radiobutton(self, variable=self.shaft_damage, value=1, bg='white').place(x=720, y=410)
        tk.Radiobutton(self, variable=self.shaft_damage, value=2, bg='white').place(x=820, y=410)
        tk.Radiobutton(self, variable=self.shaft_damage, value=3, bg='white').place(x=920, y=410)

        self.proceed_file = Image.open('assets/proceed_button.png').resize((215, 60))
        self.proceed_image = ImageTk.PhotoImage(self.proceed_file)
        self.proceed_button = self.create_image(750, 450, image=self.proceed_image, anchor=tk.NW)
        self.tag_bind(self.proceed_button, "<Button-1>", self.assess_damage)

    def assess_damage(self, event):
        latest_transaction = self.root.machine.get_latest_transaction(user_id=self.root.machine.user)
        damages = [
            self.handle_damage.get(),
            self.canopy_damage.get(),
            self.runner_damage.get(),
            self.rib_damage.get(),
            self.button_damage.get(),
            self.shaft_damage.get(),
        ]
        damage_score = statistics.mean(damages)
        damage_rating = self.get_damage_interpretation(damage_score)
        damage_fee = 0
        for damage in damages:
            damage_fee += self.get_damage_fee(damage)
            
        rent_date = datetime.strptime(latest_transaction['rented_at'], "%Y-%m-%d %H:%M:%S")
        return_date = datetime.now()
        # Add excluded times
        rent_fee = self.root.machine.compute_rent_fee(rent_date, return_date)
        transaction_details = {
            'rented_at': rent_date,
            'returned_at': return_date,
            'duration': self.get_duration(rent_date, return_date),
            'rent_fee': rent_fee,
            'damage_rating': damage_rating,
            'damage_fee': damage_fee,
            'total_fee': rent_fee + damage_fee
        }
        self.root.show_payment_page(transaction_details)

    @staticmethod
    def get_damage_interpretation(value):
        if value <= 0:
            return 'None'
        elif value == 1:
            return 'Minor'
        elif value == 2:
            return 'Moderate'
        else:
            return 'Severe'
        
    @staticmethod 
    def get_damage_fee(score: int):
        if score == 1:
            return 15
        if score == 2:
            return 40
        if score == 3:
            return 70
        return 0
        
    @staticmethod
    def get_duration(rent_date, return_date) -> str:
        duration_time = return_date - rent_date
        duration_string = f'{duration_time.days} days, {duration_time.seconds//3600} hours, {(duration_time.seconds//60)%60} mins'
        return duration_string



class PaymentPage(tk.Canvas):
    def __init__(self, root: Root, details: dict, **kwargs):
        super().__init__(root, width=1024, height=600, **kwargs)
        self.root = root
        self.details = details

        self.umbrella_logo_file = Image.open('assets/logo.png').resize((128, 128))
        self.umbrella_logo_image = ImageTk.PhotoImage(self.umbrella_logo_file)
        self.create_image(15, 15, image=self.umbrella_logo_image, anchor=tk.NW)

        self.create_text(140, 40, text='Umbrella Renting Machine', font=('Montserrat', 34, 'bold'), fill='white', anchor=tk.NW)
        self.create_text(150, 90, text='You matter the most under the umbrella', font=('Montserrat', 18, 'bold'), fill='white', anchor=tk.NW)

        self.accept_umbrella_file = Image.open('assets/return.png').resize((540, 350))
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
        self.root.machine.accepting_coin = True
        total_payment = self.details['total_fee']
        while self.root.machine.inserted_coins < total_payment:
            remaining = total_payment - self.root.machine.inserted_coins
            self.counter_label.configure(text=f'{remaining}')
        else:
            extra = self.root.machine.inserted_coins - total_payment
            self.root.machine.add_balance(self.root.machine.user, extra)
            self.root.machine.reset_inserted_coins()
        self.root.machine.accepting_coin = False
        self.counter_label.configure(text='0')
        try:
            self.root.machine.return_umbrella(
                damage_fee=self.details.get('damage_fee'),
                damage_rating=self.details.get('damage_rating'),
                rent_fee=self.details.get('rent_fee'),
                returned_at=self.details.get('returned_at'),
                user_id=self.root.machine.user,
            )
        except Exception as e:
            messagebox.showerror('Exception', e)
        self.accept_umbrella()

    def accept_umbrella(self):
        self.delete(self.container)
        self.delete(self.rent_date_label)
        self.delete(self.return_date_label)
        self.delete(self.duration_label)
        self.delete(self.damage_rating_label)
        self.delete(self.rent_date_label)
        self.delete(self.damage_fee_label)
        self.delete(self.total_fee_label)
        self.delete(self.insert_coin_label)
        self.delete(self.counter_container)
        self.counter_label.destroy()
        self.image_placeholder = self.create_image(145, 140, image=self.accept_umbrella_image, anchor=tk.NW)
        self.title_label = self.create_text(560, 190, text='Please return the\numbrella to the machine', font=('Montserrat', 28, 'bold'), fill='white', anchor=tk.NW)
        self.subtitle_label = self.create_text(540, 280, text='This may take a moment.', font=('Montserrat', 18, 'bold'), fill='black', anchor=tk.NW)
        self.after(1000, self.wait_for_umbrella)

    def wait_for_umbrella(self):
        while self.root.machine.get_distance_from_ultrasonic(1) > 8:
            pass
        self.root.machine.open_returning_servo()
        self.root.machine.start_motor()
        while self.root.machine.get_distance_from_ultrasonic(2) > 12:
            pass
        self.root.machine.close_returning_servo()
        self.root.machine.stop_motor()
        self.root.machine.tone()
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
    machine = Machine(
        arduino_port='/dev/ttyUSB1',
        sim808_port='/dev/ttyUSB0',
        api_key='URSUmbrella@2023',
        api_url='https://ursubrella.online/api',
        hardware_callbacks='thread'
    )
    root = Root(machine)