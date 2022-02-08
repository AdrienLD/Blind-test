#   Author  :   Adrien LD
#   Date    :   08/02/2022
#   Desc    :   Ultimate Buvery


import pygame
import time
import keyboard
from tkinter import * 
import os
import random

nombre_joueurs = 4
l = 1706
h = 720
window = Tk()
window.title ('Blind test')
fenetre1 = Canvas (window, width = l, height = h)
fenetre1.pack(padx = 0, pady = 0)
fenetre1.update()
pygame.init()
pygame.mixer.init()
pos = 0
liste_musiques = []
j1 = "w"
j2 = "p"
j3 = "j"
j4 = "f"

def affichagedebut():           #Creates the first view in tkinter
    global nombre_joueurs
    i = 1
    while i:
        fenetre1.delete(ALL)
        fenetre1.create_rectangle(0,0,l,h, fill="black")
        fenetre1.create_text(l/2, h/6, text = "Bienvenue dans LE Blind Test", fill = "white", font=("Impact", 80))
        fenetre1.create_text(l/2, h/2, text = "Indiquez votre nombre de joueurs", fill = "white", font=("Impact", 60))
        fenetre1.update()
        if keyboard.is_pressed("1"):
            i = 0
            nombre_joueurs = 1
        if keyboard.is_pressed("2"):
            i = 0
            nombre_joueurs = 2
        if keyboard.is_pressed("3"):
            i = 0
            nombre_joueurs = 3
        if keyboard.is_pressed("4"):
            i = 0
            nombre_joueurs = 4


    

def creationaffichage():               #Creates the tkinter window qith the number of players
    fenetre1.delete(ALL)
    fenetre1.create_rectangle(0,0,l,h, fill="black")
    if nombre_joueurs == 1:
        fenetre1.create_text(l/2, h/2, text = j1, fill = "#ff0000", font=("Impact", 80))
    elif nombre_joueurs == 2:
        fenetre1.create_text(l/4, h/2, text = j1, fill = "#ff0000", font=("Impact", 80))
        fenetre1.create_text(3*l/4, h/2, text = j2, fill = "#00ff00", font=("Impact", 80))
    elif nombre_joueurs == 3:
        fenetre1.create_text(l/6, h/2, text = j1, fill = "#ff0000", font=("Impact", 80))
        fenetre1.create_text(3*l/6, h/2, text = j2, fill = "#00ff00", font=("Impact", 80))
        fenetre1.create_text(5*l/6, h/2, text = j3, fill = "#0000ff", font=("Impact", 80))
    elif nombre_joueurs == 4:
        fenetre1.create_text(l/4, h/4, text = j1, fill = "#ff0000", font=("Impact", 80))
        fenetre1.create_text(3*l/4, h/4, text = j2, fill = "#00ff00", font=("Impact", 80))
        fenetre1.create_text(l/4, 3*h/4, text = j3, fill = "#0000ff", font=("Impact", 80))
        fenetre1.create_text(3*l/4, 3*h/4, text = j4, fill = "#fff000", font=("Impact", 80))
    fenetre1.update()
    
def recherche_musiques():           #Scan the Musiques folder
    global Musiques
    Musiques = os.listdir("Musiques")

def main():                         #Creates the random playlist in Liste.txt
    while (len(Musiques) >= 1):
        musiqueajouter = random.randint(0, len(Musiques)-1)
        musiques(musiqueajouter)
    print("Playlist aléatoire créée !\n")
    file = open("Liste.txt", "w")
    for i in range (len(liste_musiques)):
        file.write(liste_musiques[i])
        file.write("&")
    file.close()
    print("Playlist aléatoire sauvegardée !\n")

def musiques(musiqueajouter):       #Add musics to the playlist
    titre = Musiques[musiqueajouter]
    liste_musiques.append(titre)
    del Musiques[musiqueajouter]
    

def fenetre(texte, color, temps):      
    fenetre1.create_rectangle(0,0,l,h, fill= color)
    fenetre1.create_text(l/2, h/9, text = texte, fill = "white", font=("Bahnschrift", 70))
    fenetre1.create_text(l/2, 2*h/3, text = str(temps)[:4], fill = "white", font=("Fixedsys", 40))
    fenetre1.update()  

def mettre_musique():
    file = open("Liste.txt", "r")
    string = file.read()
    liste_des_musiques = string.split("&")
    file.close()
    print("Playlist aléatoire trouvée dans Liste.txt !\n")
    for i in range (len(liste_des_musiques)):
        reponse = 0
        j = 1
        temps = 0
        debutdelai = 0
        print (liste_des_musiques[i])
        music = "Musiques/" + liste_des_musiques[i]
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
        time.sleep(.1)
        pygame.mixer.music.pause()
        index = liste_musiques[i].index(" - ")
        texte = liste_musiques[i]
        texte = texte[:index]
        fenetre1.create_text(l/2, h/9, text = texte, fill = "white", font=("Bahnschrift", 70))
        fenetre1.update()
        while j:
            if keyboard.is_pressed(j1) and reponse:
                print("PAUSE - Joueur 1")
                pygame.mixer.music.pause()
                findelai = time.time()
                temps += findelai - debutdelai
                fenetre(texte, "#ff0000", temps)
                reponse = 0
            if keyboard.is_pressed(j2) and reponse:
                print("PAUSE - Joueur 2")
                pygame.mixer.music.pause()
                findelai = time.time()
                temps += findelai - debutdelai
                fenetre(texte, "#00ff00", temps)
                reponse = 0
            if keyboard.is_pressed(j3) and reponse:
                print("PAUSE - Joueur 3")
                pygame.mixer.music.pause()
                findelai = time.time()
                temps += findelai - debutdelai
                fenetre(texte, "#0000ff", temps)
                reponse = 0
            if keyboard.is_pressed(j4) and reponse:
                print("PAUSE - Joueur 4")
                pygame.mixer.music.pause()
                findelai = time.time()
                temps += findelai - debutdelai
                fenetre(texte, "#fff000", temps)
                reponse = 0
            if keyboard.is_pressed("0"):
                print("PLAY")
                time.sleep(.1)
                pygame.mixer.music.unpause()
                creationaffichage()
                fenetre1.create_text(l/2, h/9, text = texte, fill = "white", font=("Bahnschrift", 70))
                fenetre1.update()
                reponse = 1
                debutdelai = time.time()
            if keyboard.is_pressed("."):
                time.sleep(.1)
                creationaffichage()
                pygame.mixer.music.stop()
                j = 0
                
        print("Nouvelle musique")


affichagedebut()
recherche_musiques()
main()
creationaffichage()
mettre_musique()



window.mainloop()