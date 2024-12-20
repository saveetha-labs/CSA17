male(tom).
male(ram).
male(jack).
female(sri).
female(clin).
female(geeta).
parent(sri,tom).
parent(tom,clin).
parent(geeta,jack).

mother(X,Y):-
    parent(X,Y),
    female(X).
