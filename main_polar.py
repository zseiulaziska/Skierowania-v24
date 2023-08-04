import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
from tkinter import filedialog as fd
from tkinter import scrolledtext as st
from tkinter import Menu
from tkinter import Spinbox
from tkcalendar import Calendar
from datetime import date
# import pandas as pd
import polars as pl

import csv   


class App:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Skierowania 0.24")
        # self.window.geometry("500x500")
        # self.window.minsize(500, 500)
        # self.window.maxsize(500, 500)
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        # self.window.resizable(0,0)

        self.create_widgets()
        self.create_menu()

        
        self.window.mainloop()


    def open_file(self):
        self.filename = fd.askopenfilename(title="Open file", filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
        if self.filename:
            try:
                self.df = pl.read_excel(self.filename)
                
                #make dictionary from column "specjalnosc"
                


            except:
                mBox.showerror("Open file", "Could not open file")
            finally:
                pass # nie trzeba zamykac pliku, bo pandas to robi za nas
            # print (self.file)
                self.specjalnosc = self.df["Specjalność/Zawód"].unique()
                self.klasy = self.df["Dane oddziału"].unique()
                print(self.specjalnosc)
                print(self.klasy)
                self.set_klasy_combobox()

    def set_klasy_combobox(self):
        self.combobox_klasy["values"] = self.klasy

    

    def create_widgets(self):

        self.klasy = []


        #define style
        self.style = ttk.Style()
        self.style.configure("TButton", foreground="red", background="white")
        self.style.configure("TLabel", foreground="blue")
        self.style.configure("TFrame", foreground="green")
        self.style.configure("TLabelFrame", foreground="yellow")
        self.style.configure("TRadiobutton", foreground="black", background="white")
        self.style.configure("TCheckbutton", foreground="black", background="white")
        self.style.configure("TCombobox", foreground="black", background="white")
        self.style.configure("TEntry", foreground="black", background="white")
        self.style.configure("TNotebook", foreground="black", background="white")
        self.style.configure("Treeview", foreground="black", background="white")
        self.style.configure("TProgressbar", foreground="black", background="white")
        self.style.configure("Vertical.TScrollbar", foreground="black", background="white")
        self.style.configure("Horizontal.TScrollbar", foreground="black", background="white")
        self.style.configure("TSpinbox", foreground="black", background="white")
        self.style.configure("TSizegrip", foreground="black", background="white")
        self.style.configure("TProgressbar", foreground="black", background="white")
        self.style.configure("TNotebook.Tab", foreground="black", background="white")
        
        self.ramka = ttk.Frame(self.window)
        self.ramka.grid(column=0, row=0, padx=0, pady=0, sticky="NSEW", ipadx=0, ipady=0)
        self.ramka.columnconfigure(0, weight=1)
        self.ramka.rowconfigure(0, weight=1)


        #add ramka_dane_klasy 100% width and height
        self.ramka_dane_klasy = ttk.LabelFrame(self.ramka, text="Dane klasy")
        self.ramka_dane_klasy.grid(column=0, row=0, padx=10, pady=10, sticky="NSEW", ipadx=0, ipady=0, columnspan=3)
        self.ramka_dane_klasy.columnconfigure(0, weight=1)
        self.ramka_dane_klasy.rowconfigure(0, weight=1)

        #add combobox with klasy
        self.combobox_klasy = ttk.Combobox(self.ramka_dane_klasy, values=self.klasy)
        self.combobox_klasy.grid(column=0, row=0, sticky="NSEW", padx=10, pady=10)
        # self.combobox_klasy.bind("<<ComboboxSelected>>", self.combobox_klasy_selected)
        

        # self.label_klasa = ttk.Label(self.ramka_dane_klasy, text="Klasa")
        # self.label_klasa.grid(column=0, row=0, sticky="SNWE", padx=10)


        # ramka_data_wystawienia
        self.ramka_data_wystawienia = ttk.LabelFrame(self.ramka, text="Data wystawienia")
        self.ramka_data_wystawienia.grid(column=0, row=1, padx=10, pady=10)
        self.ramka_data_wystawienia.columnconfigure(0, weight=1)
        self.ramka_data_wystawienia.rowconfigure(0, weight=1)

        # ramka_data_rozpoczęcia
        self.ramka_data_rozpoczęcia = ttk.LabelFrame(self.ramka, text="Data rozpoczęcia")
        self.ramka_data_rozpoczęcia.grid(column=1, row=1, padx=10, pady=10)
        self.ramka_data_rozpoczęcia.columnconfigure(0, weight=1)
        self.ramka_data_rozpoczęcia.rowconfigure(0, weight=1)

        # ramka_data_zakonczenia
        self.ramka_data_zakonczenia = ttk.LabelFrame(self.ramka, text="Data zakończenia")
        self.ramka_data_zakonczenia.grid(column=2, row=1, padx=10, pady=10)
        self.ramka_data_zakonczenia.columnconfigure(0, weight=1)
        self.ramka_data_zakonczenia.rowconfigure(0, weight=1)
        
        # self.label_wystawienie = ttk.Label(self.frame, text="Wystawiono")
        # self.label_wystawienie.grid(column=0, row=0, sticky="W", padx=10)

        # self.label_rozpoczecie = ttk.Label(self.frame, text="Rozpoczęcie")
        # self.label_rozpoczecie.grid(column=1, row=0, sticky="W", padx=10)

        # self.label_zakonczenia = ttk.Label(self.frame, text="Zakończenie")
        # self.label_zakonczenia.grid(column=2, row=0, sticky="W", padx=10)

        #pobranie aktualnej daty z systemu operacyjnego
        self.today = date.today()
        dzien = self.today.day
        miesiac = self.today.month
        rok = self.today.year
        # self.today = self.today.strftime("%d.%m.%Y")
        print(self.today.day)

        



        #add 3 dateentry
        # self.datepicker1 = Calendar(self.ramka_data_wystawienia, selectmode="day", year=rok, month=miesiac, day=dzien)
        # self.datepicker1.grid(column=0, row=1, padx=10, pady=10)
        # self.datepicker2 = Calendar(self.ramka_data_rozpoczęcia, selectmode="day", year=rok, month=miesiac, day=dzien)
        # self.datepicker2.grid(column=1, row=1, padx=10, pady=10)
        # self.datepicker3 = Calendar(self.ramka_data_zakonczenia, selectmode="day", year=rok, month=miesiac, day=dzien)
        # self.datepicker3.grid(column=2, row=1, padx=10, pady=10)

        


    def create_menu(self):
        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)
        #add menu
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.window.quit)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        #add help
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="About")
        self.menu.add_cascade(label="Help", menu=self.help_menu)








if __name__ == "__main__":
    App()