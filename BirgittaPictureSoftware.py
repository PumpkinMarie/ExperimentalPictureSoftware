
import sys
import cv2

import py2exe
import os
import numpy as np
import time
import random
from distutils.core import setup
import winsound
from tkinter import *

# écrire et lire des fichiers excel
import xlrd
import xlwt


# en secondes
delai_clavier_son = 0.8
# en ms
duree_son = 0.1

class BirgittaPictureSoftware:

    def __init__(self,file_xl_name,fond,son):



        # initialisation du fichier de résultat 
        self.dir_path = os.path.dirname(os.path.realpath('__file__'))
  
        # initialisation du fichier de résultat excel 
        if file_xl_name== "":
            file_xl_name = "test1"
        self.excel = file_xl_name
        self.wb = xlwt.Workbook()
        self.ws = self.wb.add_sheet('A Test Sheet')

        
        # initialisation des chemins vers les images et le fond    
        if fond == 0:
            self.path = "Pictures/PicturesW\\"
            self.path_fond = "Pictures\\FondBlanc.jpg"
            self.ws.write(2, 3, "Fond d'écran: White")
        else:
            self.path = "Pictures/PicturesB\\"
            self.path_fond = "Pictures\\FondNoir.jpg"
            self.ws.write(2, 3, "Fond d'écran: Black")

        # initialisation des fréquences
        if son == 0:
            self.ws.write(1, 3, "FrequenceSonore: 0 Hz")
            self.sound = None
        elif son == 1:
            self.ws.write(1, 3, "FrequenceSonore: 200 Hz")
            self.sound = "Sons/200Hz.wav"
        elif son == 2:
            self.ws.write(1, 3, "FrequenceSonore: 1000 Hz")
            self.sound = "Sons/1000Hz.wav"
        else:
            self.ws.write(1, 3, "FrequenceSonore: 2000 Hz")
            self.sound = "Sons/2000Hz.wav"

        # création de la fenêtre et affichage du fond
        img_fond = cv2.imread(self.path_fond,1)
        cv2.namedWindow("fond",cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("fond", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN);
        cv2.imshow("fond",img_fond)

        cv2.waitKey(0) & 0xFF

    def showPictures(self):
        dirs = os.listdir( self.path )

        # récupération des infos sur l'écran
        fenetre = Tk()
        largeur_ecran = fenetre.winfo_screenheight()
        longueur_ecran = fenetre.winfo_screenwidth()
        cote_image = int(largeur_ecran/1.5)
        fenetre.destroy()

        # pour chaque image dans le fichier donné
        for i in range(0,len(dirs)):

            # Tirage aléatoire d'une image
            picChoiceFirst = random.choice(dirs)
            dirs.remove(picChoiceFirst)
            print(picChoiceFirst)
            # attente et son
            time.sleep(delai_clavier_son)
            winsound.PlaySound(self.sound,winsound.SND_ASYNC)
            time.sleep(duree_son)
            winsound.PlaySound(None,winsound.SND_NODEFAULT)

            # création de la fenêtre et affichage de l'image
            img = cv2.imread(os.path.join(self.dir_path, self.path, picChoiceFirst),1)
            img = cv2.resize(img,(cote_image,cote_image))
            cv2.imshow("",img)
            cv2.moveWindow("",int(longueur_ecran/2-cote_image/2),int(largeur_ecran/2-cote_image/2))
            cv2.namedWindow("",cv2.WND_PROP_FULLSCREEN)

            # temps 
            timestamp = time.time()

            # attente d'une réponse clavier
            k = cv2.waitKey(0) & 0xFF

            # tant que la réponse diffère de 1 ou 2 relancer, ou si fenêtre fermée puis appui clavier fin du prog
            while True:
                if cv2.getWindowProperty("",1) == -1 :
                    cv2.destroyAllWindows()
                    print("WINDOW CLOSED")
                    sys.exit()
                if k == ord('1'):
                    break
                if k== ord('2'):
                    break
                print ("PLEASE PRESS 1 or 2 FROM THE KEYBOARD")
                k = cv2.waitKey(0) & 0xFF

            # écrit dans le fichier texte le bon chiffre (1 ou 2) appuyé puis ferme la fenêtre
            if k == ord('1'):      
                self.ws.write(i, 0, 1)            
                
            elif k == ord('2'): 
                self.ws.write(i, 0, 2)

            cv2.destroyWindow("")

            # écrit dans le fichier excel le bon chiffre
            self.ws.write(i, 1, (time.time()-timestamp)*1000)            
            self.ws.write(i, 2, picChoiceFirst)            

        # sauvegarde du fichier excel, fermeture du fichier txt et des fenêtres
        self.ws.write(0, 3, "NomSujetSession: " + self.excel)

        self.wb.save("RESULTS/" + self.excel + ".xls")
        cv2.destroyAllWindows()


if __name__ == '__main__':
        birgittaPictureSoftware = BirgittaPictureSoftware("",1,1)
        birgittaPictureSoftware.showPictures()
