#E edges as list of list of 2 verticies
#V verticies as int
#colors... integers uncolred = -1
#G already colored nodes

from random import *

def neighboars(v,E):
    S = []
    for e in E:
        if v in e:
            for w in e:
                if w != v:
                    S += [w]
    return(S)

def calc_delta(V,E):
    maxim = 0
    for v in V:
        length = len(neighboars(v,E))
        if length > maxim:
            maxim = length
    return(maxim)

def Init_colors(V):
    C = dict() #Dictonary
    for v in V:
        C[v] = -1;
    return(C)

def main_loop(V,E,C,G,delta):
    Canidate_Colors = Init_colors(V)
    colors = [i for i in range(delta)]
    #canidate colors
    for v in V:
        colors_v = [i for i in range(delta)]
        if v not in G:
            for w in neighboars(v,E):
                if w in G and C[w] in colors_v:
                    colors_v.remove(C[w])
            Canidate_Colors[v] = choice(colors_v)
    #permanent
    for v in V:
        if v not in G:
            boolean = 1
            for w in neighboars(v,E):
                if Canidate_Colors[w] == Canidate_Colors[v]:
                    boolean = 0
            if boolean == 1:
                C[v] = Canidate_Colors[v];
                G = G + [v]
    return(C,G)

#This takes V and E as an input and returns the colors from 0 to delta as a dictonary of the verticies to the colors
def main(V,E):
    C = Init_colors(V)
    G = []
    delta = calc_delta(V,E)
    while len(G) != len(V):
        [C,G] = main_loop(V,E,C,G,delta+1)
    return(C)

#Check coloring
def check_coloring(V,E,C):
    for e in E:
        list_c = []
        for v in e:
            list_c += [C[v]]
        if list_c[0] == list_c[1]:
            print("ERROR: wrong coloring\n")
            return(1)
    print("coloring is valid\n")
    return(0)

#To show that check_coloring detects errors
V = [1,2]
E = [[1,2]]
C = {1:0,2:0}
print("Error check:")
check_coloring(V,E,C)

#Example with 300 verticies and 3000 edges
V = [i for i in range(300)]
E = []
for j in range(3000):
    x = 0
    y = 0
    while x == y:
        x = int(random()*300)
        y = int(random()*300)
    E += [[x,y]]

C = main(V,E)
print("first example:")
check_coloring(V,E,C)

#Example with 250 verticies and 5000 edges
V = [i for i in range(250)]
E = []
for j in range(5000):
    x = 0
    y = 0
    while x == y:
        x = int(random()*250)
        y = int(random()*250)
    E += [[x,y]]

C = main(V,E)
print("second example:")
check_coloring(V,E,C)

#Example with 150 verticies and 15000 edges
V = [i for i in range(150)]
E = []
for j in range(15000):
    x = 0
    y = 0
    while x == y:
        x = int(random()*150)
        y = int(random()*150)
    E += [[x,y]]

C = main(V,E)
print("third example:")
check_coloring(V,E,C)

#Example with 500 verticies and 10000 edges
V = [i for i in range(500)]
E = []
for j in range(10000):
    x = 0
    y = 0
    while x == y:
        x = int(random()*500)
        y = int(random()*500)
    E += [[x,y]]

C = main(V,E)
print("fourth example:")
check_coloring(V,E,C)


