"""
----- Application pour afficher un couplet, la fin de la chanson et la chanson entière----
----- Créée par M. Laurencin - dernire- version le 24 décembre 2020 ----


"""

# On importe Tkinter et la boite de dialogue
from tkinter import *
from tkinter.messagebox import *


# Fonction pour afficher un couplet en fonction du nombre choisir par l'utilisateur
def afficherCouplet():
    global nombre #definition de nombre en variable globale
    global phrase   #definition de phrase en variable globale
    nombre = Champ.get()    # definition de la variable locale nombre à partir de ce que l'utilisateur à entrer
    global nombreIsOK       #definition de nombreIsOk en variable globale

    #vérification que l'utilisateur entre bien un nombre entre 0 et 99 et sinon afficher une erreur
    try:                
        nombre = int(Champ.get())
        if nombre < 0 or nombre > 99:
            nombreIsOk = 0   
            myError = ValueError('Le nombre doit être entre 0 et 99, choisis de nouveau.')
            raise myError
        else:           #si c'est un nombre compris entre 0 et 99, appeler les fonctions creationPhrase et afficherPhrase
            
            nombreIsOk = 1
            creationPhrase(nombre, nombreIsOk)      #appel de la fonction creationPhrase
            afficherPhrase(phrase)      # appel de la fonction afficherPhrase
            phrase = ""
    except ValueError:
        showwarning('Erreur','Raté, il faut un nombre entier entre 0 et 99')

#Fonction pour afficher la chanson entiere
def afficherChanson():
    global phrase
    x = 99
    #boucle à partir de 99 pour afficher toute la chanson
    while x >= 0:
        creationPhrase(x, 1)
        x = x - 1
    afficherPhrase(phrase)
    phrase=""       #permet de remettre la variable phrase à l'initial


#Fonction pour afficher la chanson à partir du nombre choisi
def afficherChansonNombre():
    global nombre #definition de nombre en variable globale
    global phrase   #definition de phrase en variable globale
    nombre = Champ.get()    # definition de la variable locale nombre à partir de ce que l'utilisateur à entrer
    global nombreIsOK       #definition de nombreIsOk en variable globale

    #vérification que l'utilisateur entre bien un nombre entre 0 et 99 et sinon afficher une erreur
    try:
        nombre = int(Champ.get())
        if nombre < 0 or nombre > 99:
            nombreIsOk = 0   
            myError = ValueError('Le nombre doit être entre 0 et 99, choisis de nouveau.')
            raise myError
        else:           #si c'est bien un nombre entre 0 et 99, faire la suite
            x = nombre
            while x >= 0 and x <= nombre:  # boucle du nombre choisi jusqu'à 0 et appel des fonction creationPhrase et afficherPhrase
                creationPhrase(x, 1)
                x = x - 1
            afficherPhrase(phrase)
            phrase = ""
    except ValueError:
        showwarning('Erreur','Raté, il faut un nombre entier entre 0 et 99')    
    
# Création de la fonction qui permet de créer les paroles de la chanson (seulement si le nombre choisi est OK), en fonction du nombre choisi par l'utilisateur
def creationPhrase(nombre, nombreIsOk):
    if nombreIsOk == 1:
        if nombre > 1:
            shooters = str(nombre)
            shootersinf = str(nombre - 1)
            global phrase

            # la variable phrase est des caractères et se cumule lorsqu'il y a plusieurs couplets à afficher
            phrase = phrase + shooters + " shooters sans alcool sur le mur, " + shooters + \
                 " shooters sans alcool. \nBois en un et au suivant! " + shootersinf + " shooters sans alcool sur le mur.\n\n"
        elif nombre == 1:
            phrase = phrase + "1 shooter sans alcool sur le mur, 1 shooter sans alcool.\nBois en un et au suivant! Plus de shooters sans alcool sur le mur.\n\n"
        else:
            phrase = phrase + "Plus de shooters sans alcool sur le mur, plus de shooters sans alcool. \nVas au supermarché pour en acheter, 99 shooters sans alcool sur le mur.\n\n"
        return phrase


# Définition d'une fonction pour afficher les phrases / couplets de la chanson
def afficherPhrase(phrase):
    global newWindow
    
    newWindow = Toplevel(fenetre)       # nouvelle fenetre
    
    frame = Frame(newWindow, width=300, height=16)      #taille de la fenêtre
    frame.pack(side=BOTTOM)

    sc1 = Scrollbar(newWindow)          #création d'une bar de défilement
    sc1.pack(side=RIGHT, fill=Y)
    
    textaff = Text(newWindow, height=20, yscrollcommand=sc1.set)        # création d'une zone à texte
    textaff.pack(side=LEFT, fill=BOTH)
    textaff.insert(1.0, phrase )            #afficher la variable phrase
    
    sc1.config(command=textaff.yview)
    
    Button(frame, text = "Quitter", command = newWindow.destroy).pack(side = BOTTOM)        #création d'un bouton quitter et qui ferme la fenetre

def QuitterPopUp():
    fenetre.quit()

# Quitter l'application génèrale après une demande oui non à l'utilisateur
def Quitter():
    reponse = askyesno("Terminer le 99 shooters","Voulez-vous réellement terminer\u00a0? \n Cliquer «oui» pour finir")
    if reponse:
        fenetre.destroy()

# Création de la fenêtre principale et de son titre
fenetre = Tk()
fenetre.title('99 shooters')


#création d'un titre consigne
Label1 = Label(fenetre, text='99 shooters', font=("Comic Sans MS",15))
Label1.pack()

Label2 = Label(fenetre, text='Bonjour, voici une application pour écouter partiellement ou entièrement la chanson.')
Label2.pack()


#Définition des variables

nombreIsOk = IntVar()
phrase = ""
numerocouplet = IntVar()
nombre = IntVar()

#Insérer une image musique
photo = PhotoImage(file="musique.gif")
Can = Canvas(fenetre,width = photo.width(), height =photo.height())    # Création d'un widget Canvas (zone graphique)
item = Can.create_image(0,0,anchor=NW, image=photo)
Can.pack()

#Texte explicatif
Label2 = Label(fenetre, text='Veuillez choisir un nombre entre 0 et 99 et choisir l\'option que vous voulez pour l\'affichage.')
Label2.pack(pady=5)

#Création d'une case pour entrer une valeur:
Champ = Entry(fenetre, textvariable= IntVar(), bg ='bisque',\
              fg='maroon')
Champ.focus_set()
Champ.pack(padx=5,pady=5) 

#Création d'un bouton Voir le couplet choisi
Button(fenetre, text="Voir le couplet", command=afficherCouplet).pack(side = LEFT,padx=15,pady=15)

#Création d'un bouton voir la fin de la chanson

Button(fenetre, text="Voir la fin de la chanson", command=afficherChansonNombre).pack(side=LEFT, padx=15,pady=15)

# Création d'un bouton Quitter

Button(fenetre, text="Quitter", command=Quitter).pack(side=RIGHT, padx=15,pady=15)

#Création d'un bouton voir toute la chanson

Button(fenetre, text="Voir toute la chanson", command=afficherChanson).pack(side = RIGHT, padx=15,pady=15)




# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
