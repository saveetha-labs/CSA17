first_name(tonyblair, tony).
first_name(georgebush, georgedubya).
second_name(tonyblair, blair).
second_name(georgebush, bush).

fullname(M,F,S):-
    first_name(M,F),
    second_name(M,S).
