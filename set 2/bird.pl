bird(eagle).
canfly(X):-
    bird(X).
# ?- canfly(X).
# X = eagle.

# ?- canfly(eagle).
# true.