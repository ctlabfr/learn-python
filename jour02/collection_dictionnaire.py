# Déclaration d'un dictionnaire
mondictionnaire = {
	'label1': 'valeur1',
	'label2': 'valeur2',
	'label3': 'valeur3',
}

# Accéder à un élement du dictionnaire en utilisant le label 
print("Affiche la valeur associée au label1: ", mondictionnaire['label1'])
print("Affiche la valeur associée au label2: ", mondictionnaire['label2'])
print("Affiche la valeur associée au label3: ", mondictionnaire['label3'])

# Le dictionnaire est une collection mutable
mondictionnaire['label1'] = 'nouvellevaleur1'
print("Affiche la valeur associée au label1: ", mondictionnaire['label1'])
