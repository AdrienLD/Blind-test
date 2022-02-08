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

def affichagedebut():
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


    

def creationaffichage():
    fenetre1.delete(ALL)
    if nombre_joueurs == 1:
        fenetre1.create_rectangle(0,0,l,h, fill="#ff0000")
        fenetre1.create_text(l/2, h/2, text = j1, fill = "black", font=("Constantia", 40))
    elif nombre_joueurs == 2:
        fenetre1.create_rectangle(0,0,l/2,h, fill="#ff0000")
        fenetre1.create_rectangle(l/2,0,l,h, fill="#00ff00")
        fenetre1.create_text(l/4, h/2, text = j1, fill = "black", font=("Constantia", 40))
        fenetre1.create_text(3*l/4, h/2, text = j2, fill = "black", font=("Constantia", 40))
    elif nombre_joueurs == 3:
        fenetre1.create_rectangle(0,0,l/3,h, fill="#ff0000")
        fenetre1.create_rectangle(l/3,0,2*l/3,h, fill="#00ff00")
        fenetre1.create_rectangle(2*l/3,0,l,h, fill="#0000ff")
        fenetre1.create_text(l/6, h/2, text = j1, fill = "black", font=("Constantia", 40))
        fenetre1.create_text(3*l/6, h/2, text = j2, fill = "black", font=("Constantia", 40))
        fenetre1.create_text(5*l/6, h/2, text = j3, fill = "black", font=("Constantia", 40))
    elif nombre_joueurs == 4:
        fenetre1.create_rectangle(0,0,l/2,h/2, fill="#ff0000")
        fenetre1.create_rectangle(l/2,0,l,h/2, fill="#00ff00")
        fenetre1.create_rectangle(0,h/2,l/2,h, fill="#0000ff")
        fenetre1.create_rectangle(l/2,h/2,l,h, fill="#fff000")
        fenetre1.create_text(l/4, h/4, text = j1, fill = "black", font=("Constantia", 40))
        fenetre1.create_text(3*l/4, h/4, text = j2, fill = "black", font=("Constantia", 40))
        fenetre1.create_text(l/4, 3*h/4, text = j3, fill = "black", font=("Constantia", 40))
        fenetre1.create_text(3*l/4, 3*h/4, text = j4, fill = "black", font=("Constantia", 40))
    fenetre1.update()
    
def recherche_musiques():
    global Disney, Actuel, Vieux, Rock, Films_Series
    Disney = os.listdir("Disney")
    Actuel = os.listdir("Actuel")
    Vieux = os.listdir("Vieux")
    Rock = os.listdir("Rock")
    Films_Series = os.listdir("Films_Series")

def choix_musique():
    theme = random.randint(0, 4)
    if (theme == 0):
        if len(Disney) >=1:
            musique = random.randint(0, len(Disney)-1)
            musiques("Disney", Disney, musique)
    elif (theme == 1):
        if len(Actuel) >=1:
            musique = random.randint(0, len(Actuel)-1)
            musiques("Actuel", Actuel, musique)
    elif (theme == 2):
        if len(Vieux) >=1:
            musique = random.randint(0, len(Vieux)-1)
            musiques("Vieux", Vieux, musique)
    elif (theme == 3):
        if len(Rock) >=1:
            musique = random.randint(0, len(Rock)-1)
            musiques("Rock", Rock, musique)
    elif (theme == 4):
        if len(Films_Series) >=1:
            musique = random.randint(0, len(Films_Series)-1)
            musiques("Films_Series", Films_Series, musique)

def fenetre(texte, color, temps):
    fenetre1.create_rectangle(0,0,l,h, fill= color)
    fenetre1.create_text(l/2, h/9, text = texte, fill = "black", font=("Bahnschrift", 70))
    fenetre1.create_text(l/2, 2*h/3, text = str(temps)[:4], fill = "black", font=("Fixedsys", 40))
    fenetre1.update()

def main():
    while (len(Disney) >= 1 or len(Actuel) >= 1 or len(Vieux) >= 1 or len(Rock) >= 1 or len(Films_Series) >= 1):
        print ("Taille de Disney : ", len(Disney))
        print ("Taille de Actuel : ", len(Actuel))
        print ("Taille de Vieux : ", len(Vieux))
        print ("Taille de Rock : ", len(Rock))
        print ("Taille de Films_Series : ", len(Films_Series))
        choix_musique()
    print("\n")
    file = open("Liste.txt", "w")
    for i in range (len(liste_musiques)):
        file.write(liste_musiques[i])
        file.write("&")
    file.close()

def musiques(nom, theme, musique):
    global pos
    titre = nom + "/" + str(theme[musique])
    print (titre)
    liste_musiques.append(titre)
    del theme[musique]
    
    
def mettre_musique():
    file = open("Liste.txt", "r")
    liste_des_musiques = file.read().split("&")
    file.close()
    for i in range (len(liste_des_musiques)):
        reponse = 0
        j = 1
        temps = 0
        debutdelai = 0
        print (liste_des_musiques[i])
        pygame.mixer.music.load(liste_des_musiques[i])
        pygame.mixer.music.play()
        time.sleep(.1)
        pygame.mixer.music.pause()
        if "Rock" in liste_des_musiques[i]:
            texte = "Indice : Rock"
        if "Disney" in liste_des_musiques[i]:
            texte = "Indice : Disney"
        if "Actuel" in liste_des_musiques[i]:
            texte = "Indice : Actuel"
        if "Vieux" in liste_des_musiques[i]:
            texte = "Indice : Vieux"
        if "Films_Series" in liste_des_musiques[i]:
            texte = "Indice : Films_Series"
        fenetre1.create_text(l/2, h/9, text = texte, fill = "black", font=("Bahnschrift", 70))
        fenetre1.update()
        while j:
            if keyboard.is_pressed(j1) and reponse:
                pygame.mixer.music.pause()
                findelai = time.time()
                temps += findelai - debutdelai
                fenetre(texte, "#ff0000", temps)
                reponse = 0
            if keyboard.is_pressed(j2) and reponse:
                pygame.mixer.music.pause()
                findelai = time.time()
                temps += findelai - debutdelai
                fenetre(texte, "#00ff00", temps)
                reponse = 0
            if keyboard.is_pressed(j3) and reponse:
                pygame.mixer.music.pause()
                findelai = time.time()
                temps += findelai - debutdelai
                fenetre(texte, "#0000ff", temps)
                reponse = 0
            if keyboard.is_pressed(j4) and reponse:
                pygame.mixer.music.pause()
                findelai = time.time()
                temps += findelai - debutdelai
                fenetre(texte, "#fff000", temps)
                reponse = 0
            if keyboard.is_pressed("0"):
                pygame.mixer.music.unpause()
                creationaffichage()
                fenetre1.create_text(l/2, h/9, text = texte, fill = "black", font=("Bahnschrift", 70))
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
creationaffichage()
print(Disney, Actuel, Vieux, Rock, Films_Series)
#main()
mettre_musique()



window.mainloop()