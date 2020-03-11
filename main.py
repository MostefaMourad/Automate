from Automate import Automate
from Transition import Transition
from Etat import Etat

alph = set(["a","b","c"])
etats = set([Etat(0,init=True),Etat(1),Etat(2,fin=True)])
trans = set([Transition(Etat(0),'a',Etat(1)),Transition(Etat(0),'a',Etat(0)),Transition(Etat(1),'#',Etat(0)),Transition(Etat(1),'b',Etat(2)),Transition(Etat(2),'#',Etat(1)),Transition(Etat(2),'c',Etat(0))])
aut = Automate(alph,etats)
aut.setTransitions(trans)

print(aut.miroirAutomate())

