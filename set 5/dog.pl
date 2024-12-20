% Facts: Dog names
dog(fido).
dog(rover).
dog(jane).
dog(tom).
dog(fred).
dog(henry).

% Facts: Cat names
cat(mary).
cat(harry).
cat(bill).
cat(steve).

% Size of the animals
small(henry).
medium(harry).
medium(fred).
large(fido).
large(mary).
large(tom).
large(fred).
large(steve).
large(jim).
large(mike).

% Rules:

% A small dog
small_dog(Name) :-
    dog(Name),
    small(Name),
    write(Name), write(' is a small dog.'), nl.

% A medium dog
medium_dog(Name) :-
    dog(Name),
    medium(Name),
    write(Name), write(' is a medium dog.'), nl.

% A large dog
large_dog(Name) :-
    dog(Name),
    large(Name),
    write(Name), write(' is a large dog.'), nl.

% A small cat
small_cat(Name) :-
    cat(Name),
    small(Name),
    write(Name), write(' is a small cat.'), nl.

% A large cat
large_cat(Name) :-
    cat(Name),
    large(Name),
    write(Name), write(' is a large cat.'), nl.

% Example queries:
% - Find all large dogs: ?- large_dog(X).
% - Find all medium dogs: ?- medium_dog(X).
% - Find all small dogs: ?- small_dog(X).
% - Find all large cats: ?- large_cat(X).
