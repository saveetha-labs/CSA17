born(mohan,20/12/1222).
dob(X,Y):-
    born(X,Y).
name(X,Y):-
    born(X,Y).
# ?- born(mohan,Y).
# Y = 20/12/1222.

# ?- born(X,20/12/1222).
# X = mohan.