prenom = 'john'
nom = 'doe'
note = 'note: l\'homme générique.'

# capitalize pour mettre la première lettre de la chaîne de caractère
# en majuscule
prenom_cap = prenom.capitalize()
nom_cap = nom.capitalize()
print(prenom_cap)
print(nom_cap)

# find('pattern'): trouver la position d'un mot dans une chaîne de caractère
# ici renverra 0 puis que le chaîne 'note: ' démarre à la première position de 
# la chaîne contenu dans la variable note.
# En python les index commence à la position 0
# Si le pattern n'est pas trouvé la fonction find renvoit -1
note_position = note.find('note: ') 
print('position du mot "note": ' + str(note_position))
generique_position = note.find('générique')
print('position du mot "générique": ' + str(generique_position))
patate_position = note.find('patate')
print('position du mot "patate": ' + str(patate_position))

# string[start:end]: Extraire une partie de la chaîne de caractère
note_texte = note[6:]
print(note_texte)

# Expression régulère
import re

nombre_cinq_chiffres = '29539'
nombre_neuf_chiffres = '49206-5623'
numero_telephone = '01.53.24.23.42'

# pattern pour rechercher 5 chiffres 
pattern_cinq_chiffres = r'\d{5}'
print(re.search(pattern_cinq_chiffres, nombre_cinq_chiffres))
print(re.search(pattern_cinq_chiffres, nombre_neuf_chiffres))
print(re.search(pattern_cinq_chiffres, numero_telephone))
