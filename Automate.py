from Etat import Etat
from Transition import Transition

class Automate:

    def __init__(self,alphabet,Etats):

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
        
    def __str__(self):
        ch1 =  "A<X,  S,  S0,  F,  II> :\n"
        ch2 = "\tX  = " + str(self.ensAlphabet)+" ("+str(len(self.ensAlphabet))+") ,\n"
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

    def setTransitions(self,transitions):
        self.ensTransition=transitions

    def getTransitions(self):
        return self.ensTransition    

    def addTransition(self,transtion):
        self.ensTransition.add(transtion)
    
    def delTransition(self,transition):
        self.ensTransition.discard(transition)

    def addEtat(self,etat):
        self.ensEtats.add(etat)
        if(etat.initiale):
            self.ensEtatsInitiaux.add(etat)
        if(etat.finale):
            self.ensEtatsFinaux.add(etat)

    def delEtat(self,etat):
        self.ensEtats.discard(etat)
        self.ensEtatsInitiaux.discard(etat)
        self.ensEtatsFinaux.discard(etat)

    def completAutomate(self):
        autComp = Automate(self.ensAlphabet,self.ensEtats)
        autComp.setTransitions(self.ensTransition)
        for elm in autComp.ensEtats:
            for l in autComp.ensAlphabet:
                autComp.addTransition(Transition(elm,l,Etat("P")))
        autComp.addEtat(Etat("P"))
        autComp.addTransition(Transition("P",str(self.ensAlphabet),"P"))
        return autComp 

    def complementAutomate(self):
        temp = self.completAutomate()
        etats = set([])
        for x in temp.ensEtats:
            if(not(x.finale)):
                x.finale=True
            else:
                x.finale=False
            etats.add(x) 
        autComplnt = Automate(temp.ensAlphabet,etats)
        autComplnt.setTransitions(temp.getTransitions())    
        return autComplnt   
    
    def miroirAutomate(self):
        etats = set([])

        for x in self.ensEtats:
            y = x.finale
            x.finale = x.initiale
            x.initiale = y
            etats.add(x)
        transition = set([])

        for x in self.ensTransition:
            trans  = Transition(x.instruction[2],x.instruction[1],x.instruction[0])
            transition.add(trans)

        autMir = Automate(self.ensAlphabet,etats)
        autMir.setTransitions(transition)
        if(len(autMir.ensEtatsInitiaux)>1):
            for x in autMir.ensEtatsInitiaux:
                autMir.addTransition(Transition(Etat("P",init=True),"#",x))
                autMir.ensEtats.discard(x)
                autMir.ensEtats.add(Etat(x.nbEtat))

            autMir.ensEtatsInitiaux = set([])
            autMir.addEtat(Etat("P",init=True))

        return autMir





    


