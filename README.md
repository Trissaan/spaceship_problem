# spaceship_problem

An alien spacecraft on earth uses a space warp engine to moves in a 2-D plane starting from the original point (0,0).

The engine can only move the ship in North-East, South-East, South-West & North-West, in that order. Further, the MAXIMUM steps the engine can take the ship in a given direction are given as inputs.

Eg: NE↗ = 5 (d1) SE↘ = 4 (d2) SW↙= 3 (d3) NW↖= 2 (d4) So, if the ship moves 5 steps in direction NE at a stretch - it has to move in SE, SW, and NW - before again going in the direction NE.

1.1. Write a function to take (d1, d2, d3, d4) and coordinates (x, y) as inputs. The function should plot the path of the spaceship from (0, 0) to (x, y).

d1, d2, d3, d4, x, y are all integers.
