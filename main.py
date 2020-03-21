from Automate import Automate
from Transition import Transition
from Etat import Etat

alph = set(["a", "b", "c", "d", "e"])
etats = set([Etat(1, init=True), Etat(2), Etat(3),
             Etat(4), Etat(5), Etat(6, fin=True)])
trans = set([Transition(Etat(1), 'a', Etat(2)), Transition(Etat(2), 'a', Etat(2)), Transition(Etat(2), 'b', Etat(
    3)), Transition(Etat(1), 'b', Etat(4)), Transition(Etat(3), 'b', Etat(4)), Transition(Etat(4), 'b', Etat(4)), Transition(Etat(2), 'c', Etat(5)), Transition(Etat(2), 'd', Etat(5)), Transition(Etat(4), 'c', Etat(5)), Transition(Etat(4), 'd', Etat(5)), Transition(Etat(5), 'e', Etat(6, fin=True))])
aut = Automate(alph, etats)
aut.setTransitions(trans)
aut.passageDeterministe()
