initial_state([
    at(monkey, 1),
    at(chair, 2),
    at(stick, 3),
    bananas_at(4),
    monkey_on_floor
]).

% Goal: The bananas should be knocked down.
goal_state([bananas_down]).

% Actions the monkey can perform:

% Move the monkey to a new position
action([at(monkey, P1) | Rest], move(P1, P2), [at(monkey, P2) | Rest]) :-
    write('Monkey moves from position '), write(P1), write(' to position '), write(P2), nl.

% Monkey picks up the stick if it is at the same position as the monkey
action([at(monkey, P), at(stick, P) | Rest], pick_up(stick), [monkey_with_stick | Rest]) :-
    write('Monkey picks up the stick at position '), write(P), nl.

% Monkey moves the chair to a new position
action([at(monkey, P), at(chair, P) | Rest], push_chair(P, P2), [at(chair, P2), at(monkey, P2) | Rest]) :-
    write('Monkey pushes the chair from position '), write(P), write(' to position '), write(P2), nl.


action([at(monkey, P), at(chair, P), monkey_on_floor | Rest], climb(chair), [on(monkey, chair) | Rest]) :-
    write('Monkey climbs on the chair at position '), write(P), nl.

% Monkey waves the stick if it is on the chair and holding the stick, knocking down the bananas
action([on(monkey, chair), monkey_with_stick, bananas_at(P), at(chair, P) | Rest], wave_stick, [bananas_down | Rest]) :-
    write('Monkey waves the stick and knocks down the bananas'), nl.

% Plan: Find the sequence of actions that leads to knocking down the bananas
plan(State, Goal, Plan) :- 
    plan(State, Goal, [], Plan).

plan(State, Goal, _, []) :- 
    subset(Goal, State).

plan(State, Goal, Visited, [Action | Rest]) :-
    action(State, Action, NewState),
    \+ member(NewState, Visited), 
    plan(NewState, Goal, [NewState | Visited], Rest).

% Utility function to check if a subset of elements is in a list
subset([], _).
subset([X | Xs], Ys) :- member(X, Ys), subset(Xs, Ys).

% Starting the search
solve :-
    initial_state(Initial),
    goal_state(Goal),
    plan(Initial, Goal, Plan),
    write('Solution: '), nl,
    write_plan(Plan).

% Utility to print the plan
write_plan([]).
write_plan([Action | Rest]) :-
    write(Action), nl,
    write_plan(Rest).
