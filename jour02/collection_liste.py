# Déclaration d'une liste
maliste = [
	'valeur1',
	'valeur2',
	'valeur3',
]

# Accéder à un élement de la liste en utilisant l'index
# Note: le premier élement d'une liste à un index de 0
print("affiche le premier élement de malsite: ",maliste[0])
print("affiche le deuxième élement de malsite: ",maliste[1])
print("affiche le troisième élement de malsite: ",maliste[2])

# La liste est une collection mutable
maliste[0] = 'nouvellevaleur1'
print("affiche le premier élement de malsite: ",maliste[0])
