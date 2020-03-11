class Transition:

    def __init__(self , Si , Xi , Sj):
        self.debut = (Si,Xi)
        self.suivant = Sj
        self.instruction = (Si , Xi , Sj)

    def __str__(self):
        x , y = self.debut
        return "("+ str(x)+","+str(y)+","+str(self.suivant)+")" 

    def __eq__(self,other):
        return self.debut == other.debut  

    def __hash__(self):
        return hash(self.instruction)         