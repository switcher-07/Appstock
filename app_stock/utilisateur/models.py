from django.db import models

class Utilisateur(models.Model):
    identifiant = models.CharField(max_length=30, unique=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=128)  # À gérer toi-même (hash)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.identifiant} ({self.nom})"



#
#On a le model utilisateur de base que  Manager et caissier utilise
#Mais pas d'heritage , c'est ma facon defaire , j'ai adopté cette methode 
#Ca evite les soucis lorsqu'on a plus plusieurs heritage complexe ... bref 
#


class Manager(models.Model):
    #le manager a pour "clé primaire" ou on va dire 'une equivalent de clé priamire' un objet utilisateur pour dire qu'il ai lié a l'utilisateur....
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='manager_profil')
    # Ajoute ici les autres cahmps du manager si besoin


    def __str__(self):
        return f"Manager : {self.utilisateur}"


class Caissier(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='caissier_profil')
    # Ajoute ici des champs pour le caissier si besoin


    def __str__(self):
        return f"Caissier : {self.utilisateur}"


##
##De cette facon on a la meme logique d'heritage on ecrit toutes les fonctiosn commun a manager et caissier en les 
##  ecrivant pour utilisateur.....'heirtage' bref...
##
