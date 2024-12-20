% Facts: person(FName, SName, Sex, Age, Occupation)
person(frances, wilson, female, 28, architect).
person(fred, jones, male, 62, doctor).
person(paul, smith, male, 45, plumber).
person(martin, williams, male, 23, chemist).
person(mary, jones, female, 24, programmer).
person(martin, johnson, male, 47, solicitor).

% Rule: A person is a man if their sex is male
man(FirstName, Surname) :-
    person(FirstName, Surname, male, _, _),
    write(FirstName), write(' '), write(Surname), write(' is a man'), nl.
    
% Example queries for finding men
% ?- man(A, B).
