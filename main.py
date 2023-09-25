import requests
from bs4 import BeautifulSoup
import html.parser
from tkinter import *
from tkinter import ttk


url = "https://ru.wikipedia.org/wiki/Статический_сайт"
req = requests.get(url)

soup = BeautifulSoup(req.text,"html.parser")
root = Tk()
root.geometry("500x500")
root.title("ПРОСТОЙ ПАРСЕР С ПРОСТЫМ ИТЕРФЕЙСОМ")

with open("monitor.html","w") as file:
    file.write(req.text)

def click():
    all_monitor = soup.find_all(class_="mw-headline")
    for i in all_monitor:
        Label = ttk.Label(text=i.text)
        Label.pack()

def info():
    label2 = ttk.Label(text="Самый простой парсер проект + самый простой интерфейс к нему")
    label2.pack()

knopka = ttk.Button(text = "АКТИВИРОВАТЬ ПОИСК ", command= click)
knopka.place(x= 20,y = 20)
knopka.pack()

knopka1= ttk.Button(text = "ИНФО",command = info)
knopka1.pack()

root.mainloop()


