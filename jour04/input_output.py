fichier_entree = open ('valeur.txt', 'rt')
fichier_sortie = open ('valeur-total.txt','wt')
print('Traitement des données en entrée')
somme = 0
for ligne in fichier_entree:
    somme += int(ligne)
    print(ligne.rstrip(), file=fichier_sortie)
print('\nTotal: ' + str(somme), file=fichier_sortie)
fichier_sortie.close()
print('Sortie terminée')