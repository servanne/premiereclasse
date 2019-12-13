# coding: utf-8

"""attributs :
nom (str), prenom (str), age (int), sexe (str), formationPrecedante (str), motivation (int valant 100 à l'instanciation), progression (int valant 0 à l'instanciation)
méthode :
suivreFormation() : chaque fois qu'elle est utilisé diminue la motivation d'une valeur random entre 5 et 25 et augmente la progression d'une valeur random entre 20 et 30
bosserPlus() : chaque fois qu'elle est utilisée augmente la motivation et la progression d'une valeur random entre 10 et 30
echouer() : chaque fois qu'elle est utilisée baisse la motivation d'une valeur random entre 20 et 40 et augmente la progression d'une valeur random entre 20 et 40
reussir() : chaque fois qu'elle est utilisée augmente la motivation d'une valeur random entre 20 et 40 et augmente la progression d'une valeur random entre 10 et 20

Instancie un objet dataAnalyst et indique un nom, un prenom, le sexe et la formationPrecedante. L'attribut motivation vaudra 100 au début et l'attribut progression vaudra 0.

Le programme va automatiquement et aléatoirement lancer des méthodes et afficher le récapitulatif de l'état des attributs motivation et progression. Le programme s'arrête quand la motivation tombe à zéro  et affiche "BRAVO TU AS GAGNÉ !!!" ou quand progression atteint 100 et affiche "BRAVO TU AS APPRIS !!!"."""

import random


class dataAnalyst:
    def __init__(self, nom, prenom, sexe, formationPrecedente):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 40
        self.sexe = sexe
        self._formationPrecedente = formationPrecedente
        self.motivation = 100
        self.progression = 0

    def suivreFormation(self):
        """chaque fois qu'elle est utilisé diminue la motivation d'une valeur random entre 5 et 25 et augmente la progression d'une valeur random entre 20 et 30"""
        generateur_motivation = random.randint(5, 25)
        generateur_progression = random.randint(20, 30)
        self.motivation = self.motivation - generateur_motivation
        self.progression = self.progression + generateur_progression

    def bosserPlus(self):
        """chaque fois qu'elle est utilisée augmente la motivation et la progression d'une valeur random entre 10 et 30"""
        generateur_motivation = random.randint(10, 30)
        generateur_progression = random.randint(10, 30)
        self.motivation = self.motivation + generateur_motivation
        self.progression = self.progression + generateur_progression

    def echouer(self):
        """chaque fois qu'elle est utilisée baisse la motivation d'une valeur random entre 20 et 40 et augmente la progression d'une valeur random entre 20 et 40"""
        generateur_motivation = random.randint(20, 40)
        generateur_progression = random.randint(20, 40)
        self.motivation = self.motivation - generateur_motivation
        self.progression = self.progression + generateur_progression

    def reussir(self):
        """chaque fois qu'elle est utilisée augmente la motivation d'une valeur random entre 20 et 40 et augmente la progression d'une valeur random entre 10 et 20"""
        """self.motivation = 100 ?"""
        generateur_motivation = random.randint(20, 40)
        generateur_progression = random.randint(10, 20)
        self.motivation = self.motivation + generateur_motivation
        self.progression = self.progression + generateur_progression

    def travaillerAleatoirement(self):
        """Le programme va automatiquement et aléatoirement lancer des méthodes"""
        generateur_methodes = random.randint(1, 4)
        if generateur_methodes == 1:
            self.suivreFormation()
        elif generateur_methodes == 2:
            self.bosserPlus()
        elif generateur_methodes == 3:
            self.echouer()
        elif generateur_methodes == 4:
            self.reussir()
        """Afficher le récapitulatif de l'état des attributs motivation et progression."""
        print(self.prenom, "a une motivation à", self.motivation,
              "et une progression à", self.progression)

    def prog(self):
        """Le programme s'arrête quand la motivation tombe à zéro  et affiche "BRAVO TU AS GAGNÉ !!!" ou quand progression atteint 100 et affiche "BRAVO TU AS APPRIS !!!"."""
        while True:
            self.travaillerAleatoirement()
            if self.motivation <= 0:
                print("BRAVO TU AS GAGNÉ !!!")
                break
            elif self.progression >= 100:
                print("BRAVO TU AS APPRIS !!!")
                break


servanne = dataAnalyst("de Galbert", "Servanne", "F", "dev")
servanne.prog()
