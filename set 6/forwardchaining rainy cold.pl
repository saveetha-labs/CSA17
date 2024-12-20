rainy(chennai).
rainy(coimbatore).
rainy(ooty).
cold(ooty).
wet(X):-rainy(X).
cold_and_wet(X):-cold(X),rainy(X).