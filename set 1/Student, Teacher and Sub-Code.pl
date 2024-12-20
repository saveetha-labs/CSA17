studies(oliva,csc135).
studies(jack,csc131).
studies(arthur,csc134).
teaches(kirke,csc135).
teaches(collins,csc131).
teaches(juniper,csc134).
professor(X,Y):-
    teaches(X,C),
    studies(Y,C).
%professor(collins,Y).
%Y = jack
