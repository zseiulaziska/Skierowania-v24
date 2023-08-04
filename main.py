import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
from tkinter import filedialog as fd
from tkinter import scrolledtext as st
from tkinter import Menu
from tkinter import Spinbox, LabelFrame, Entry, font, StringVar
from tkcalendar import Calendar
from datetime import date
import pandas as pd

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

        czcionka = font.Font(size=12)  # Tworzenie obiektu czcionki z większym rozmiarem
        self.window.option_add("*Font", czcionka)  # Ustawienie większej czcionki dla wszystkich widgetów

        self.create_widgets()
        self.create_menu()

        
        self.window.mainloop()


    def open_file(self):
        self.filename = fd.askopenfilename(title="Open file", filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
        if self.filename:
            try:
                self.df = pd.read_excel(self.filename)

            except:
                mBox.showerror("Open file", "Could not open file")

            finally:
                pass # nie trzeba zamykac pliku, bo pandas to robi za nas
                self.specjalnosc = self.df["Specjalność/Zawód"].unique().tolist()
                self.klasy = self.df["Dane oddziału"].unique().tolist()
                self.zawody = self.df["Specjalność/Zawód"].unique().tolist()

                # self.wybrani_uczniowie = self.df['Imię', 'Nazwisko'].tolist()


                print(self.specjalnosc)
                print(self.klasy)
                self.set_klasy_combobox()
                self.set_zawody_comboboc()
                self.set_wybrani_uczniowie_treeview()

    def set_klasy_combobox(self):
        self.combobox_klasy["values"] = self.klasy

    def set_zawody_comboboc(self):
        self.combobox_zawody["values"] = self.zawody

    
    def set_wybrani_uczniowie_treeview(self):

        self.contacts = []


        print(self.df.shape[0])

        for i in range(self.df.shape[0]):
            self.contacts.append((self.df.iloc[i, 0], self.df.iloc[i, 1], self.df.iloc[i, 8], self.df.iloc[i, 9]))
        
        print(self.contacts)

        # # wypełnienie trreewiew przykładowymi danymi
        # # for n in range(1, 100):
        # #     contacts.append((f'imie {n}', f'nazwisko {n}', f'klasa{n}', f'specjalnosc{n}'))

        # add data to the treeview
        for contact in self.contacts:
            self.tree.insert('', tk.END, values=contact)




        # for n in range(1, 100):
        #     self.contacts.append((f'imie {n}', f'nazwisko {n}', f'klasa{n}', f'specjalnosc{n}'))


        # pass
        # # self.treeview_wybrani_uczniowie.delete(*self.treeview_wybrani_uczniowie.get_children())
        # # for i in self.wybrani_uczniowie:
        # #     self.treeview_wybrani_uczniowie.insert("", "end", text=i)


        # for i, uczen in enumerate(self.wybrani_uczniowie):
        #     self.tree.insert('', 'end', text=str(i+1), values=(uczen,))

        # for column in self.df.columns:
        #     self.tree.heading(column, text=column)

        #     # print(column)

        # for i, row in self.df.iterrows():
        #     self.tree.insert('', 'end', values=list(row))


    def generuj_skierowania():
        pass

    def generuj_wykazy():
        pass

    def otwórz_plik():
        pass

    def otworz_folder_wykazow():
        pass

    def otworz_folder_skierowan():
        pass





    def create_widgets(self):

        self.klasy = []
        self.zawody = []


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
        
        self.ramka = ttk.Frame(self.window, padding=10, relief="raised", borderwidth=5)
        self.ramka.grid(column=0, row=0, padx=5, pady=5, sticky="NSEW")

        self.ramka.columnconfigure(0, weight=1)
        self.ramka.columnconfigure(1, weight=1)
        self.ramka.columnconfigure(2, weight=1)
        
        # self.ramka.rowconfigure(0, weight=0)
        # self.ramka.rowconfigure(1, weight=0)
        # self.ramka.rowconfigure(2, weight=0)
        self.ramka.rowconfigure(3, weight=1)


        # add ramka_dane_klasy 100% width and height
        self.ramka_dane_klasy = ttk.LabelFrame(self.ramka, text="Dane klasy")
        self.ramka_dane_klasy.grid(column=0, row=0, padx=10, pady=10, sticky="NSEW", ipadx=0, ipady=0, columnspan=3)
        self.ramka_dane_klasy.columnconfigure(0, weight=1)
        # self.ramka_dane_klasy.rowconfigure(0, weight=1)

        # add combobox with klasy
        self.combobox_klasy = ttk.Combobox(self.ramka_dane_klasy, values=self.klasy, state="readonly")
        self.combobox_klasy.grid(column=0, row=0, sticky="NSEW", padx=10, pady=10)
        # self.combobox_klasy.bind("<<ComboboxSelected>>", self.combobox_klasy_selected)

        # add combobox with zawody
        self.combobox_zawody = ttk.Combobox(self.ramka_dane_klasy, values=self.zawody, state="readonly")
        self.combobox_zawody.grid(column=0, row=1, sticky="NSEW", padx=10, pady=10)
        # self.combobox_klasy.bind("<<ComboboxSelected>>", self.combobox_klasy_selected)




        # self.label_klasa = ttk.Label(self.ramka_dane_klasy, text="Klasa")
        # self.label_klasa.grid(column=0, row=0, sticky="SNWE", padx=10)


        # ramka_data_wystawienia
        self.ramka_data_wystawienia = ttk.LabelFrame(self.ramka, text="Data wystawienia")
        self.ramka_data_wystawienia.grid(column=0, row=1, padx=10, pady=10, sticky="NSEW", ipadx=0, ipady=0)
        # self.ramka_data_wystawienia.columnconfigure(0, weight=1)
        # self.ramka_data_wystawienia.rowconfigure(0, weight=1)

        # ramka_data_rozpoczęcia
        self.ramka_data_rozpoczęcia = ttk.LabelFrame(self.ramka, text="Data rozpoczęcia")
        self.ramka_data_rozpoczęcia.grid(column=1, row=1, padx=10, pady=10, sticky="NSEW", ipadx=0, ipady=0)
        # self.ramka_data_rozpoczęcia.columnconfigure(1, weight=1)
        # self.ramka_data_rozpoczęcia.rowconfigure(0, weight=1)

        # ramka_data_zakonczenia
        self.ramka_data_zakonczenia = ttk.LabelFrame(self.ramka, text="Data zakończenia")
        self.ramka_data_zakonczenia.grid(column=2, row=1, padx=10, pady=10, sticky="NSEW", ipadx=0, ipady=0)
        # self.ramka_data_zakonczenia.columnconfigure(2, weight=1)
        # self.ramka_data_zakonczenia.rowconfigure(0, weight=1)
        
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

        
        #add 3 date entry
        self.datepicker1 = Calendar(self.ramka_data_wystawienia, selectmode="day", year=rok, month=miesiac, day=dzien, locale="pl")
        self.datepicker1.grid(column=0, row=1, padx=10, pady=10)
        
        self.datepicker2 = Calendar(self.ramka_data_rozpoczęcia, selectmode="day", year=rok, month=miesiac, day=dzien, locale="pl")
        self.datepicker2.grid(column=1, row=1, padx=10, pady=10)
        
        self.datepicker3 = Calendar(self.ramka_data_zakonczenia, selectmode="day", year=rok, month=miesiac, day=dzien, locale="pl")
        self.datepicker3.grid(column=2, row=1, padx=10, pady=10)


        # ramka_czas_wystawienia
        self.ramka_czas_wystawienia = ttk.LabelFrame(self.ramka, text="Godzina rozpoczęcia")
        self.ramka_czas_wystawienia.grid(column=0, row=2, padx=10, pady=10, sticky="NSEW", ipadx=0, ipady=0)     
        self.ramka_czas_wystawienia.columnconfigure(0, weight=1)
        self.ramka_czas_wystawienia.rowconfigure(0, weight=1)


        default_value = StringVar(value="00:00")
        
        self.time_entry = Entry(self.ramka_czas_wystawienia, width=10, justify="center", textvariable=default_value)
        self.time_entry.grid(column=0, row=0, padx=10, pady=10, sticky="SNEW", ipadx=10, ipady=10)  


        #ramka typu Label frame na dwa przyciski do generowania plików
        self.ramka_przyciski_generowanie = ttk.LabelFrame(self.ramka, text="Generowanie plików")
        self.ramka_przyciski_generowanie.grid(column=1, row=2, padx=10, pady=10, sticky="NSEW", ipadx=0, ipady=0)
        self.ramka_przyciski_generowanie.columnconfigure(0, weight=1)
        self.ramka_przyciski_generowanie.rowconfigure(0, weight=1)

        #wstawienie dwóch butonów: skierowania, wykazy
        self.button_skierowania = ttk.Button(self.ramka_przyciski_generowanie, text="Skierowania", command=self.generuj_skierowania)
        self.button_skierowania.grid(column=0, row=0, padx=10, pady=10, sticky="NSEW", ipadx=0, ipady=0)
        self.button_wykazy = ttk.Button(self.ramka_przyciski_generowanie, text="Wykazy", command=self.generuj_wykazy)
        self.button_wykazy.grid(column=0, row=1, padx=10, pady=10, sticky="NSEW", ipadx=0, ipady=0)


        #ramka typu Label frame na dwa przyciski do otwierania folderów
        self.ramka_przyciski_otwieranie = ttk.LabelFrame(self.ramka, text="Otwieranie folderów")
        self.ramka_przyciski_otwieranie.grid(column=2, row=2, padx=10, pady=10, sticky="NSEW", ipadx=0, ipady=0)
        self.ramka_przyciski_otwieranie.columnconfigure(0, weight=1)
        self.ramka_przyciski_otwieranie.rowconfigure(0, weight=1)

 
        self.button_otworz_folder_wykazow = ttk.Button(self.ramka_przyciski_otwieranie, text="Otwórz folder z wykazami", command=self.otworz_folder_wykazow)
        self.button_otworz_folder_wykazow.grid(column=0, row=0, padx=10, pady=10, sticky="NSEW", ipadx=0, ipady=0)
        self.button_otworz_folder_skierowan = ttk.Button(self.ramka_przyciski_otwieranie, text="Otwórz folder ze skierowaniami", command=self.otworz_folder_skierowan)
        self.button_otworz_folder_skierowan.grid(column=0, row=1, padx=10, pady=10, sticky="NSEW", ipadx=0, ipady=0)

        #ramka dla widżetu do wypisywania danych uczniów
        self.ramka_wypisywanie_danych = ttk.LabelFrame(self.ramka, text="Lista uczniów")
        self.ramka_wypisywanie_danych.grid(column=0, row=3, padx=10, pady=10, sticky="SNEW", columnspan=3)
        self.ramka_wypisywanie_danych.columnconfigure(0, weight=1)
        self.ramka_wypisywanie_danych.columnconfigure(1, weight=0)

        self.ramka_wypisywanie_danych.rowconfigure(0, weight=1)


        # define columns
        self.columns = ('imie', 'nazwisko', 'klasa', 'specjalnosc')
        
        # pole tekstowe do wypisania listy wybranych uczniów
        self.tree = ttk.Treeview(self.ramka_wypisywanie_danych, columns=self.columns, show='headings')
        self.tree.grid(column=0, row=0, padx=10, pady=10, sticky="NSEW", ipadx=0, ipady=0)        

        # define headings
        self.tree.heading('imie', text='Imię')
        self.tree.heading('nazwisko', text='Nazwisko')
        self.tree.heading('klasa', text='Klasa')
        self.tree.heading('specjalnosc', text='Specjalność')


        # add a scrollbar
        self.scrollbar = ttk.Scrollbar(self.ramka_wypisywanie_danych, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=3, sticky='ns', padx=0, pady=10)


        # etykieta na statusbara
        self.status_bar = ttk.Label(self.ramka, text="Gotowy", justify="center")
        self.status_bar.grid(column=0, row=4, padx=1, pady=1, sticky="SNEW", ipadx=0, ipady=0, columnspan=3)



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