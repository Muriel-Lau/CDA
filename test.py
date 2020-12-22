"""Premier exemple avec Tkinter.


"""

# On importe Tkinter et la boite de dialogue
from tkinter import *
from tkinter.messagebox import *


# Récupération d'uene valeur dans la variable nombre
def getEntry():
    nombre = Champ.get()
    

# Vérification que la valeur de la variable nombre est bien compris entre 0 et 99.
def verification():
    try:
        nombre = int(Champ.get())
        if nombre < 0 or nombre > 99:
            myError = ValueError('Le nombre doit être entre 0 et 99, choisis de nouveau.')
            raise myError
    except ValueError:
        showwarning('Erreur','Raté, il faut un nombre entier entre 0 et 99')


#Afficher le couplet en fonction du nombre
def test():
    try:
        nombre = int(Champ.get())
        if nombre < 0 or nombre > 99:
            myError = ValueError('Le nombre doit être entre 0 et 99, choisis de nouveau.')
            raise myError
        elif nombre > 1 and nombre <= 99:
            shooters = str(nombre)
            shootersinf = str(nombre - 1)
            reponse = askquestion("Couplet de 99 shooters", message = shooters + " shooters sans alcool sur le mur, " + shooters + \
                 " shooters sans alcool. \nBois en un et au suivant! " + shootersinf + " shooters sans alcool sur le mur." \
                 "\n \nVoulez-vous recommencer?")
            if reponse == 'no':
                fenetre.destroy()
            
        elif nombre == 0:
            reponse = askquestion("Couplet de 99 shooters", message ="Plus de shooters sans alcool sur le mur, plus de shooters sans alcool. \nVas au supermarché pour en acheter, 99 shooters sans alcool sur le mur."\
                        "\n \n Voulez-vous recommencer?")
            if reponse == 'no':
                fenetre.destroy()
        elif nombre == 1:
            reponse = askquestion("Couplet de 99 shooters", message ="1 shooter sans alcool sur le mur, 1 shooter sans alcool.\nBois en un et au suivant! Plus de shooters sans alcool sur le mur."\
                        "\n \nVoulez-vous recommencer?")
            if reponse == 'no':
                fenetre.destroy()
        else:
            {}
    except ValueError:
            showwarning('Erreur','Raté, il faut un nombre entier entre 0 et 99')        

# Quitter l'application
def Quitter():
    reponse = askyesno("terminer le 99 shooters","Voulez-vous réellement terminer\u00a0? \n cliquer «oui» pour finir")
    if reponse:
        fenetre.destroy()

# Création de la fenêtre principale et de son titre
fenetre = Tk()
fenetre.title('99 shooters')

#création d'un titre consigne
Label1 = Label(fenetre, text='Bonjour, voulez-vous écouter un couplet de la chanson 99 shooters? ')
Label1.grid(row = 1, column = 1, padx = 3, pady = 10)


#Création d'une case pour entrer une valeur:
#nombre = IntVar()
Champ = Entry(fenetre, textvariable= IntVar(), bg ='bisque',\
              fg='maroon')
Champ.focus_set()
Champ.grid(row = 2, column = 1, padx = 3, pady = 10)

#Création d'un bouton Voir le couplet choisi
Button(fenetre, text="Voir le couplet", command=lambda:[getEntry(), test()]).grid(row = 3, column = 0, padx=25, pady=3)

#Création d'un bouton voir toute la chanson

Button(fenetre, text="Voir toute la chanson", command=lambda:[getEntry(), test()]).grid(row = 3, column = 1, padx=0, pady=10)


# Création d'un bouton Quitter

Button(fenetre, text="Quitter", command=Quitter).grid(row = 3, column = 2, padx=25, pady=3)


# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
