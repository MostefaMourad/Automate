from Etat import Etat
from Transition import Transition


class Automate:

    def __init__(self, alphabet, Etats):

        self.ensEtatsInitiaux = set([])
        self.ensEtatsFinaux = set([])
        self.ensTransition = set([])
        self.ensAlphabet = alphabet
        self.ensEtats = Etats
        for etat in self.ensEtats:
            if(etat.initiale):
                self.ensEtatsInitiaux.add(etat)
            if(etat.finale):
                self.ensEtatsFinaux.add(etat)
    # L'affichage d'une automate sous forme A<X,  S,  S0,  F,  II>

    def __str__(self):
        ch1 = "A<X,  S,  S0,  F,  II> :\n"
        ch2 = "\tX  = " + str(self.ensAlphabet) + \
            " ("+str(len(self.ensAlphabet))+") ,\n"
        ch3 = "\tS  = {"
        ch31 = "\tS0  = {"
        ch4 = "\tF  = {"
        for x in self.ensEtats:
            ch3 += str(x)
            ch3 += " ,"
            if(x.initiale):
                ch31 += str(x)
                ch31 += " ,"
            if(x.finale):
                ch4 += str(x)
                ch4 += " ,"

        ch3 = ch3 + "}" + " ("+str(len(self.ensEtats))+") ,\n"
        ch31 = ch31 + "}" + " ("+str(len(self.ensEtatsInitiaux))+") ,\n"
        ch4 = ch4 + "}" + " ("+str(len(self.ensEtatsFinaux))+") ,\n"
        ch5 = "\tII  = {"
        for x in self.ensTransition:
            ch5 += str(x)
            ch5 += " ,"
        ch5 = ch5 + "}" + " ("+str(len(self.ensTransition))+") ,"
        return ch1+ch2+ch3+ch31+ch4+ch5
# Generer des setters et des getters pour la structure

    def setTransitions(self, transitions):
        self.ensTransition = transitions

    def getTransitions(self):
        return self.ensTransition

# Generer des methode d'ajout et suppresion des element etat , transition ect

    def addTransition(self, transtion):
        self.ensTransition.add(transtion)

    def delTransition(self, transition):
        self.ensTransition.discard(transition)

    def addEtat(self, etat):
        self.ensEtats.add(etat)
        if(etat.initiale):
            self.ensEtatsInitiaux.add(etat)
        if(etat.finale):
            self.ensEtatsFinaux.add(etat)

    def delEtat(self, etat):
        self.ensEtats.discard(etat)
        self.ensEtatsInitiaux.discard(etat)
        self.ensEtatsFinaux.discard(etat)

# la première fonctionalité , faire le complement d'une automate

    # La première fonctoin construire un automate complet a partir d'un automate de base .

    def completAutomate(self):
        autComp = Automate(self.ensAlphabet, self.ensEtats)
        autComp.setTransitions(self.ensTransition)
        for elm in autComp.ensEtats:  # Parcourir l'ensemble des etats
            for l in autComp.ensAlphabet:  # Parcourir l'ensemble d'alphabet
                # ajouter la transition qui relie l'etat avec l'etat 'P'
                autComp.addTransition(Transition(elm, l, Etat("P")))
        autComp.addEtat(Etat("P"))
        autComp.addTransition(Transition("P", str(self.ensAlphabet), "P"))
        return autComp
    # Fonctionalité principale

    def complementAutomate(self):
        temp = self.completAutomate()  # construire un automate complet
        etats = set([])
        for x in temp.ensEtats:  # parcourir l'ensembles d'états
            if(not(x.finale)):
                x.finale = True
            else:  # changer chaque etat non final par final , et final par non final
                x.finale = False
            etats.add(x)
        autComplnt = Automate(temp.ensAlphabet, etats)
        autComplnt.setTransitions(temp.getTransitions())
        return autComplnt

# la deuxieme fonctionalité , faire le miroir d'une automate ,

    def miroirAutomate(self):
        etats = set([])

        for x in self.ensEtats:  # boucle , pour regler les etat initial , final ect
            y = x.finale
            x.finale = x.initiale
            x.initiale = y
            etats.add(x)
        transition = set([])

        for x in self.ensTransition:  # inverser les transitions dans l'automate
            trans = Transition(
                x.instruction[2], x.instruction[1], x.instruction[0])
            transition.add(trans)

        autMir = Automate(self.ensAlphabet, etats)
        autMir.setTransitions(transition)
        if(len(autMir.ensEtatsInitiaux) > 1):  # traiter le cas ou on trouve plusieurs etat initiax
            for x in autMir.ensEtatsInitiaux:
                autMir.addTransition(Transition(Etat("P", init=True), "#", x))
                autMir.ensEtats.discard(x)
                autMir.ensEtats.add(Etat(x.nbEtat))

            autMir.ensEtatsInitiaux = set([])
            # ajouter le nouveau etat initial
            autMir.addEtat(Etat("P", init=True))

        return autMir

# la troisiéme fonctionalité reduction d'un automate :

    # Fonction 1 : retourne une liste de touts les etats accessible dans une automate

    def etatsAccessible(self):
        etats = []
        index = 0
        n = 0

        # Initialisation
        for etat in self.ensEtatsInitiaux:
            etats.insert(index, etat)
            index += 1

        index = 0
        n = len(etats)
        while n > 0:
            etat = etats[index]
            for trans in self.ensTransition:
                if (etat == trans.Si):
                    if (etats.count(trans.suivant) == 0):
                        etats.insert(len(etats), trans.suivant)
            n = len(etats)-index-1
            index += 1
        return set(etats)

    # Fonction 2 : retourne une liste de touts les etats co-accessible dans une automate

    def etatsCoAccessible(self):
        etats = []
        index = 0
        n = 0

        # Initialisation
        for etat in self.ensEtatsFinaux:
            etats.insert(index, etat)
            index += 1

        index = 0
        n = len(etats)
        while n > 0:
            etat = etats[index]
            for trans in self.ensTransition:
                if (etat == trans.suivant):
                    if (etats.count(trans.Si) == 0):
                        etats.insert(len(etats), trans.Si)
            n = len(etats)-index-1
            index += 1
        return set(etats)

    # La fonctionalité principale

    def reductionAutomate(self):
        etats = set([])
        etats.update(self.etatsAccessible(), self.etatsCoAccessible())
        etats.symmetric_difference_update(self.ensEtats)
        transitions = set([])
        for etat in etats:
            for trans in self.ensTransition:
                if ((etat != trans.Si) and (etat != trans.suivant)):
                    transitions.add(trans)
        kk = set([])
        kk.update(self.etatsAccessible(), self.etatsCoAccessible())
        autRed = Automate(self.ensAlphabet, kk)
        autRed.setTransitions(transitions)
        return autRed

# la quatrieme fonctionalité la reconnaissance de mots dans un automate deterministe:

    def reconnaissanceMot(self, mot):
        for elm in self.ensEtatsInitiaux:
            etat_courant = elm
        etat_courant
        n = len(mot)
        index = 0
        stop = False
        while n > 0 and not (stop):
            stop = True
            lettre = mot[index]
            for trans in self.ensTransition:
                si, xi = trans.debut
                if ((si == etat_courant) and (xi == lettre)):
                    etat_courant = trans.suivant
                    stop = False
                    break

            index += 1
            n -= 1
        if (etat_courant.finale):
            return True
        return False

# la cinqième fonctionalité le passage d'un automate non deterministe a un automate deterministe

    # Fonction 1 : Affichage d'une liste

    def afficherLigne(self, liste):
        ch = '{'
        for case in liste:
            ch += '{'
            for elm in case:
                ch += str(elm)
            ch += '}'
        ch += '}'
        return ch

    def passageDeterministe(self):
        # Declaration des variables necessaire
        listPar = []
        listResult = []
        index = 0
        # Initialisation
        listResult.append([])
        listResult[0].append(None)
        listResult[0].extend(self.ensAlphabet)
        print(self.afficherLigne(listResult[0]))
