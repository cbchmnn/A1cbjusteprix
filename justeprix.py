import random
print("Trouver le prix de l'objet X..")
cible = (random.randint(1,10))
#print(f"cible={cible}")

# récupération de la proposition du joueur
essai = int(input("Votre proposition entre 1 et 10 : "))

if essai < 1 or essai > 10 :
    print("Erreur, il faut saisir une valeur entre 1 et 10...")
    exit()


#else et elif sont contextuels, ils sous entendent que 'if cible == essai: ' est faux
if cible == essai:
    print("Bravo !!!")
elif cible < essai :
    print("Trop élevé")
else:
    print("Trop peu")