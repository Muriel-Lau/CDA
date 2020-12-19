#-----------Programme qui affiche un couplet de la musique \
#-----------préférée 99 shooters sans alcool dépendant du nombre de shooters en entrée.
#----------------------TEST CDA GRETA VANNES
#----------------------par Muriel Laurencin

# Gestion des exceptions  et erreurs si l'utilisateur choisi un caractère \
# ou un nombre non compris entre 0 et 99.
prenom = input("Veuillez entrez votre prénom: ")
print("Bonjour", prenom, ", je vous propose d'écouter un couplet de votre chanson préférée : \
99 shooters.") 
while True:
	try:
		nombre = int(input("Veuillez entrer un nombre entier compris \
entre 0 et 99 :"))
		if nombre < 0 or nombre > 99:
			myError = ValueError('Le nombre doit être entre 0 et 99, choisis de nouveau.')
			raise myError
		break
	except ValueError:
		print("Raté, il faut un nombre entier entre 0 et 99")

#Choix du couplet à visualiser en fonction du nombre choisis
if nombre == 1:
	print(nombre, "shooter sans alcool sur le mur,", nombre, "shooter sans alcool. \
Bois en un et au suivant ! Plus de shooters sans alcool sur le mur.")
elif nombre == 0:
	print("Plus de shooters sans alcool sur le mur, plus de shooters sans alcool. \
Vas au supermarché pour en acheter, 99 shooters sans alcool sur le mur.")
else:
	print(nombre, "shooters sans alcool sur le mur,", nombre, "shooters sans alcool. \
Bois en un et au suivant! ", nombre - 1, "shooters sans alcool sur le mur.")
