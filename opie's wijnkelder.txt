import pickle
def nummer_van(lijst, element):
    for x in range(0, len(lijst)):
        if lijst[x] == element:
            return x
    return -1
def drink_een_biertje():
    biertje_naam = input("welk biertje of wijntje ga je drinken?")
    load_file = open('c://Users//Janick//Documents//biertjes.txt', 'rb')
    biertjes = pickle.load(load_file)
    load_file.close()
    del_biertje = nummer_van(biertjes, biertje_naam)
    del biertjes[del_biertje]
    save_file = open('c://Users//Janick//Documents//biertjes.txt', 'wb')
    pickle.dump(biertjes, save_file)
    save_file.close()
def zien():
    load_file = open('c://Users//Janick//Documents//biertjes.txt', 'rb')
    loaded_biertjes = pickle.load(load_file)
    load_file.close()
    print(loaded_biertjes)
def koop_een_biertje():
    gekocht_biertje = input('welk biertje of wijntje heb je gekocht?')
    load_file = open('c://Users//Janick//Documents//biertjes.txt', 'rb')
    biertjes = pickle.load(load_file)
    load_file.close()
    biertjes.append(gekocht_biertje)
    save_file = open('c://Users//Janick//Documents//biertjes.txt', 'wb')
    pickle.dump(biertjes, save_file)
    save_file.close()
from tkinter import *
tk = Tk()
btn = Button(tk, text="klik hier als je een biertje of wijntje drinkt", command=drink_een_biertje)
btn.pack()
tk = Tk()
btn = Button(tk, text="klik hier om te zien hoeveel biertjes en wijntjes je nog hebt", command=zien)
btn.pack()
tk = Tk()
btn = Button(tk, text="klik hier als je een biertje of wijntje koopt", command=koop_een_biertje)
btn.pack()
biertjes = ['pils', 'trappist', 'abdijbier', 'geuze', 'duvel', 'guinness']
eerste_lijst_biertjes = biertjes
del biertjes
