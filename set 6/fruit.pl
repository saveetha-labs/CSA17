fruit_color(apple,red).
fruit_color(banana,yellow).
fruit_color(grapes,purple).
fruit_color(strawberry,red).
get_fruit(Fruit,Color):-
    fruit_color(Fruit,Color).