american(robert).

hostile(country_a).

owns(country_a, missiles).
sold(robert, missiles, country_a).

criminal(Person) :-
    american(Person),
    sold(Person, Weapon, Country),
    owns(Country, Weapon),
    hostile(Country),
    write(Person), write(' is a criminal because they sold '), write(Weapon), write(' to a hostile country ('), write(Country), write(').'), nl.

% Starting point to prove that Robert is a criminal
prove_criminal :-
    criminal(robert).
