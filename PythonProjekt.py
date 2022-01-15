import json
import  tkinter as tk
from tkinter import  *
from os.path import exists


class KsiazkaAdresowa:
    def __init__(self):
        self._kontakty = []
    def DodajKontakt(self, imie, nazwisko, telefon, email):
        kontakt=Kontakt(imie,nazwisko,telefon, email)
        self._kontakty.append(kontakt)
    def WyswietlKontakty(self):
        for kontakt in self._kontakty:
            print("\n imie: ",kontakt.imie, "\n nazwisko: ", kontakt.nazwisko,"\n telefon: ", kontakt.telefon, "\n email: ", kontakt.email)
            print("-" * 50)

    def EdytujKontakt(self, imie, nazwisko):
        for kontakt in self._kontakty:
            if (kontakt.imie.lower() and kontakt.nazwisko.lower()) == (imie.lower() and nazwisko.lower()):
                x = self._kontakty.index(kontakt)
                print("Podaj nowe dane dla kontaktu")
                print("-"*45)
                imie = input("Wprowadz imie: ")
                nazwisko = input("Wprowadz nazwisko: ")
                telefon = input("Wprowadz numer telefonu: ")
                email = input("Podaj adres email: ")
                dane=Kontakt(imie,nazwisko, telefon, email)
                self._kontakty[x]=dane

                print(self._kontakty)

    def WyszukajKontakt(self, imie, nazwisko):
        for kontakt in self._kontakty:
            if (kontakt.imie.lower() and kontakt.nazwisko.lower()) == (imie.lower() and nazwisko.lower()):
                print(kontakt.imie, kontakt.nazwisko, kontakt.telefon, kontakt.email)
    def UsunKontakt(self, imie, nazwisko):
        for kontakt in self._kontakty:
            if (kontakt.imie.lower() and kontakt.nazwisko.lower()) == (imie.lower() and nazwisko.lower()):
                self._kontakty.remove(kontakt)
    def UsunKontakty(self):
        self._kontakty=[]
    def EksportujKontakty(self):
        plik = 'kontakty.json'
        exp_kon=[]
        with open(plik, 'w') as f:
            for kontakt in self._kontakty:
                x=(kontakt.imie,kontakt.nazwisko,kontakt.telefon,kontakt.email)
                exp_kon.append(x)
            f.write(json.dumps(exp_kon))
    def ImportujKontakty(self):
        plik ="kontakty.json"
        if(exists(plik)):
            with open(plik, 'r') as f:
                test=json.loads(f.read())
                for x in test:
                    imie=x[0]
                    nazwisko=x[1]
                    telefon=x[2]
                    email=x[3]
                    KsiazkaAdresowa.DodajKontakt(self,imie,nazwisko,telefon,email)
        else:
            print("plik który próbujesz otworzyć nie istnieje")

class Kontakt:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email




ksiazkaAdresowa=KsiazkaAdresowa()
while True:
    choice=input("""\t
    Menu książki kontaktów
    [1] Wyświetl kontakty
    [2] Dodaj kontakt
    [3] Edytuj kontakty
    [4] Wyszukaj kontakt
    [5] Usuń kontakt
    [6] Usuń kontakty
    [7] Eksportuj kontakty
    [8] Importuj kontakty
    [9] Wyjdź 
    > \t""")
    if(choice=="1"):
        ksiazkaAdresowa.WyswietlKontakty()
    elif(choice=="2"):
        imie=input("Wprowadz imie: ")
        nazwisko=input("Wprowadz nazwisko: ")
        telefon=input("Wprowadz numer telefonu: ")
        email=input("Podaj adres email: ")

        ksiazkaAdresowa.DodajKontakt(imie, nazwisko, telefon, email)
    elif (choice == "3"):
        imie=input("Podaj imie: ")
        nazwisko=input("Podaj nazwisko: ")
        ksiazkaAdresowa.EdytujKontakt(imie, nazwisko)
    elif (choice == "4"):
        imie=input("Podaj imie ")
        nazwisko=input("Podaj nazwisko ")
        ksiazkaAdresowa.WyszukajKontakt(imie, nazwisko)
    elif (choice == "5"):
        imie = str(input("Podaj imie "))
        nazwisko = input("Podaj nazwisko ")
        ksiazkaAdresowa.UsunKontakt(imie, nazwisko )
    elif (choice == "6"):
        print("Czy na pewno chcesz usuną wszystkie kontakty")
        print("y/n ?")
        x=input(">")
        if(x.lower()=="n"):
            continue
        elif(x.lower()=="y"):
            ksiazkaAdresowa.UsunKontakty()
        else:
            print("Nie prawidłowa wartość")
            continue
    elif (choice == "7"):
        ksiazkaAdresowa.EksportujKontakty()
    elif (choice == "8"):
        ksiazkaAdresowa.ImportujKontakty()
    elif (choice == "9"):
        break
    else:
        continue
