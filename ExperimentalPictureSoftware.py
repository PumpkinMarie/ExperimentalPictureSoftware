    '''Copyright (C) <2019>  <Monfouga Marie>
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.'''

from tkinter import *
import BirgittaPictureSoftware
import os

class Menu :

    def __init__(self):

        # initialisations 
        self.fenetre = Tk()
        self.fenetre.title("Welcome v2")
        largeur_ecran = self.fenetre.winfo_screenheight()
        longueur_ecran = self.fenetre.winfo_screenwidth()
        self.fenetre.geometry("250x600+"+str(int(longueur_ecran/2-125))+"+"+str(int(largeur_ecran/2-300)))
        
        # label de la fenêtre
        label = Label(self.fenetre, text="Welcome")
        label.pack(pady=5)

        # Sons 
        Frame1 = Frame(self.fenetre, borderwidth=2, relief=GROOVE)
        Frame1.pack(pady=10)
        Label(Frame1, text="Please choose the desired frequency").pack(padx=10, pady=10)
        self.son = IntVar() 
        bouton1 = Radiobutton(Frame1, text="No sound", variable=self.son, value=0)
        bouton2 = Radiobutton(Frame1, text="Low frequency", variable=self.son, value=1)
        bouton3 = Radiobutton(Frame1, text="Medium frequency", variable=self.son, value=2)
        bouton4 = Radiobutton(Frame1, text="High frequency", variable=self.son, value=3)
        bouton1.pack(pady=5)
        bouton2.pack(pady=5)
        bouton3.pack(pady=5)
        bouton4.pack(pady=5)
        bouton1.select()

        # Couleur du fond
        Frame2 = Frame(self.fenetre, borderwidth=2, relief=GROOVE)
        Frame2.pack(pady=10,padx=5)
        Label(Frame2, text="Please choose the background color").pack(padx=10, pady=10)
        self.fond = IntVar() 
        bouton1 = Radiobutton(Frame2, text="Bright background", variable=self.fond, value=0)
        bouton2 = Radiobutton(Frame2, text="Dark background", variable=self.fond, value=1)
        bouton1.pack(pady=5)
        bouton2.pack(pady=5)
        bouton1.select()

        # Nom du fichier excel
        self.file_xl_name = StringVar() 
        file_xl = Label(self.fenetre, text="Enter your initials and session number")
        file_xl.pack(pady=5)
        file_xl_ent = Entry(self.fenetre,textvariable=self.file_xl_name)
        file_xl_ent.pack()

        # Bouton pour lancer le test (fct begin)
        Begin = Button(self.fenetre, text = 'Begin the test', command=self.begin)
        Begin.pack(pady=10)

        # Bouton pour lancer le test (fct begin)
        BeginAll = Button(self.fenetre, text = 'Begin the complete test', command=self.beginAll)
        BeginAll.pack(pady=10)
        
        # Bouton pour terminer le test (fct end)
        End = Button(self.fenetre, text = 'End the test', command=self.end)
        End.pack(pady=10)

        self.fenetre.mainloop()

    def begin(self):
        if not os.path.exists("RESULTS/"):
            os.makedirs("RESULTS/")
        nom = self.file_xl_name.get()
        self.fenetre.destroy()
        birgittaPictureSoftware = BirgittaPictureSoftware.BirgittaPictureSoftware( nom,self.fond.get(),self.son.get())
        birgittaPictureSoftware.showPictures()
        
    def beginAll(self):
        self.fenetre.destroy()
        if not os.path.exists("RESULTS/" + self.file_xl_name.get()):
            os.makedirs("RESULTS/" +self.file_xl_name.get())
        for i in range(0,8):
            birgittaPictureSoftware = BirgittaPictureSoftware.BirgittaPictureSoftware( self.file_xl_name.get() + '/' + self.file_xl_name.get()+str(i+1),int(i/4),i%4)
            birgittaPictureSoftware.showPictures()  

    def end(self):
        self.fenetre.destroy()
        sys.exit()

if __name__ == '__main__':
    menu = Menu()
