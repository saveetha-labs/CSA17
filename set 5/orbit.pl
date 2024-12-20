% Facts: orbits(Body, OrbitAround)
orbits(mercury, sun).
orbits(venus, sun).
orbits(earth, sun).
orbits(mars, sun).
orbits(moon, earth).
orbits(phobos, mars).
orbits(deimos, mars).

% Rule to find all celestial bodies that orbit around a given body
orbits_around(Body, OrbitAround) :-
    orbits(Body, OrbitAround),
    write(Body), write(' orbits around '), write(OrbitAround), nl.

% Rule to find all celestial bodies that orbit around a specific body
orbits_of(Body, OrbitAround) :-
    orbits(Body, OrbitAround),
    write(Body), write(' orbits around '), write(OrbitAround), nl.

% Rule to find the moons of a planet
moons_of(Planet, Moon) :-
    orbits(Moon, Planet),
    write(Moon), write(' is a moon of '), write(Planet), nl.

% Rule to find planets that orbit around the sun
planets :-
    orbits(Planet, sun),
    write(Planet), write(' is a planet orbiting the Sun'), nl.

% Rule to find moons that orbit around a planet
moons :-
    orbits(Moon, Planet),
    \+ orbits(Planet, sun),
    write(Moon), write(' is a moon of '), write(Planet), nl.

% Example queries:
% - Find all celestial bodies orbiting the sun: ?- orbits_around(Body, sun).
% - Find moons of a specific planet: ?- moons_of(earth, Moon).
% - List all planets: ?- planets.
% - List all moons: ?- moons.
