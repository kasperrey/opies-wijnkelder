eerste_lijst_biertjes = {
    'duvel' : 0,
    'pils' : 0,
    'trappist' : 0,
    'abdijbier' : 0,
    'geuze' : 0,
    'guinness' : 0
    }

from tkinter import *
import pickle
import time

class Spel:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("opi's wijnkelder")
        self.tk.resizable(0, 0)
        self.canvas = Canvas(self.tk, width=500, height=500)

def drink_een_biertje():
    load_file = open('c://Users//Janick//Documents//biertjes.txt', 'rb')
    biertjes = pickle.load(load_file)
    load_file.close()
    for key in biertjes:
        print( "{}:{}".format( key, biertjes[key] ))
    biertje_naam = input("welk biertje of wijntje ga je drinken?")
    if biertjes[biertje_naam] < 0:
        biertjes[biertje_naam] -= 1
    else:
        print('je hebt geen %s meer' % (biertje_naam))
    save_file = open('c://Users//Janick//Documents//biertjes.txt', 'wb')
    pickle.dump(biertjes, save_file)
    save_file.close()
    
def zien():
    load_file = open('c://Users//Janick//Documents//biertjes.txt', 'rb')
    loaded_biertjes = pickle.load(load_file)
    load_file.close()
    for key in loaded_biertjes:
        print( "{}:{}".format( key, loaded_biertjes[key] ))
        
def koop_een_biertje():
    load_file = open('c://Users//Janick//Documents//biertjes.txt', 'rb')
    biertjes = pickle.load(load_file)
    load_file.close()
    for key in biertjes:
        print( "{}:{}".format( key, biertjes[key] ))
    gekocht_biertje = input('welk biertje of wijntje heb je gekocht?')
    if gekocht_biertje in biertjes.keys():
        biertjes[gekocht_biertje] = 1
    else:
        biertjes[gekocht_biertje] += 1
    for key in biertjes:
        print( "{}:{}".format( key, biertjes[key] ))
    save_file = open('c://Users//Janick//Documents//biertjes.txt', 'wb')
    pickle.dump(biertjes, save_file)
    save_file.close

spel = Spel()

btn = Button(spel.tk, text="klik hier als je een biertje of wijntje drinkt", command=drink_een_biertje)
btn.pack()

btn = Button(spel.tk, text="klik hier om te zien hoeveel biertjes en wijntjes je nog hebt", command=zien)
btn.pack()

btn = Button(spel.tk, text="klik hier als je een biertje of wijntje koopt", command=koop_een_biertje)
btn.pack()

