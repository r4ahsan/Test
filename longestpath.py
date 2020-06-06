##
## ====================================================
##   Redwan Ahsan (20813199)
##   CS 231 Spring 2020
##   Assignment 01, Problem P2
## ====================================================
##
## longest_path(g) finds the length of the longest path in the graph g, where 
## a simple path is a sequence of distinct vertices in g, each connected by an
## edge minus 1
## longest_path: Graph -> Nat
## Example:
##        g = make_graph("samplegraph1.txt")
##        longest_path(g) -> 6

from graphs import *
from itertools import permutations



def longest_path(g):
    vertices = g.vertices()
    perms = list(permutations(vertices,2))
    path_lst = []
    for v in vertices:
        path = [v]
        for p in perms:
            for a in p:
                b = path[-1]
                if g.are_adjacent(a,b):
                    if a not in path:
                        path.append(a)
        path_lst.append(path)
    length_of_longest_path = max(map(len,path_lst)) - 1
    return length_of_longest_path

