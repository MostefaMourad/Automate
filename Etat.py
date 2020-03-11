class Etat:
    
    def __init__(self,nb,fin = False,init=False):
        self.nbEtat = nb
        self.finale = fin
        self.initiale = init

    def __str__(self):
        return str(self.nbEtat)

    def __eq__(self,other):
        return self.nbEtat == other.nbEtat

    def __hash__(self):
        return hash(self.nbEtat)                  