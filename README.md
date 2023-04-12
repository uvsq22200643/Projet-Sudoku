# Projet-Sudoku

from random import randint, choice

import tkinter as tk

 

def creer_tableau_plein(lignes,colonnes):

    """Crée un tableau de valeurs comprises entre 1 et 9

    Pour chaque ligne dans un tableau déjà rempli, on prend une série de 3 lignes aléatoirement et on l'ajoute à un tableau, afin d'ajouter un peu de hasard dans sa structure"""

    tableau = [] ## créer un tableau

    list_of_choices = [0,3,6]

    full_tab = [[1,2,3,4,5,6,7,8,9],

                [4,5,6,7,8,9,1,2,3],

                [7,8,9,1,2,3,4,5,6],

                [2,3,4,5,6,7,8,9,1],

                [5,6,7,8,9,1,2,3,4],

                [8,9,1,2,3,4,5,6,7],

                [3,4,5,6,7,8,9,1,2],

                [6,7,8,9,1,2,3,4,5],

                [9,1,2,3,4,5,6,7,8]]

#renvoie un tableau de Sudoku

 

    for _ in range(0,lignes,3):

        c = choice(list_of_choices)

        list_of_choices.remove(c)

        tableau.append(full_tab[c])

        tableau.append(full_tab[c+1])

        tableau.append(full_tab[c+2])

    return tableau

 

def vider_tableau(tableau,n): #qui prend un tableau et vide aléatoirement n cases dans le tableau

    """Place aléatoirement n 0 dans un tableau"""

    for i in range(n):

        tableau[randint(0,len(tableau)-1)][randint(0,len(tableau[0])-1)] = 0

 

def afficher_tableau(tableau):#affiche le tableau dans la console

    """Affiche un tableau dans la console"""

    for ligne in range(len(tableau)): ## pour chaque ligne

        print(tableau[ligne]) ## afficher la ligne

 

def modifier_valeur_tableau(tableau,pos,v):#qui prend un tableau, un tuple (x,y) et une valeur qui remplace la valeur à la position tableau [x][y] par v (placer les chiffres du joueur ou à les enlever )    """Modifie la valeur présente aux coordonnées pos dans un tableau (tableau[x][y]) par la valeur v"""

    tableau[pos[0]][pos[1]] = v

 

def recuperer_carre(tableau):

    """Crée une liste contenant tous les sous-tableaux de taille 3x3 dans un tableau"""

    chunks = [tableau[x:x+3] for x in range(0, len(tableau), 3)]

    squares = []

    for i in range(3):

        grid1 = []

        grid2 = []

        grid3 = []

        for j in range(3):

            grid1.append(chunks[i][j][0:3])

            grid2.append(chunks[i][j][3:6])

            grid3.append(chunks[i][j][6:9])

        squares.append(grid1)

        squares.append(grid2)

        squares.append(grid3)

    return squares

 

def sommes_carres(carre):

    """Calcule la somme des valeurs d'un tableau"""

    sommes = [sum(carre[i]) for i in range(len(carre))]

    somme = sum(sommes)

 

def sudoku_ok(line):

    """Vérifie si une ligne d'un tableau est correcte"""

    return (len(line) == 9 and sum(line) == sum(set(line)))

 

def check_sudoku(grid):# qui prend un tableau et qui vérifie s'il est correctement rempli (en utilisant les fonctions recupere_carre,somme_carre et sudoku_ok)

    """Vérifie si un tableau répond bien aux règles de complétion d'un sudoku"""

    bad_rows = [row for row in grid if not sudoku_ok(row)]

    grid = list(zip(*grid))

    bad_cols = [col for col in grid if not sudoku_ok(col)]

    carres = recuperer_carre(grid)

    bad_squares = False

    for carre in carres:

        bad_squares = bad_squares or sommes_carres(carre) == sum(range(9+1))

    return not (bad_rows or bad_cols or bad_squares)

 

def afficher_tableau_tkinter(tableau,taille):#qui affiche un canvas avec une grille

    """Affiche une fenêtre ainsi qu'un canvas dont les cases dessinées correspondent à un tableau et sont de taille taille"""

    global canvas

    for i in range(len(tableau)):

        for j in range(len(tableau[i])):

            canvas.create_rectangle(i*taille,j*taille,i*taille+taille,j*taille+taille,outline = "black")

            texte = str(tableau[i][j])

            if texte=="0":

                texte = " "

            canvas.create_text(i*taille + taille//2, j*taille + taille//2, text=texte, fill="black", font=('Helvetica 15 bold'))




def get_mouse_pos(event): #qui recupere la position de la souris quand tu cliques

    """Affiche les coordonnées où l'utilisateur a cliqué"""

    global size

    global POSITION_SOURIS

    POSITION_SOURIS = (event.x//size, event.y//size)

 

size = 50

nb_cases_vides = 70

POSITION_SOURIS = (0,0)

 

sudoku = creer_tableau_plein(9, 9)

while not check_sudoku(sudoku):

    sudoku = creer_tableau_plein(9, 9)

vider_tableau(sudoku, nb_cases_vides)

 

fenetre = tk.Tk()

canvas = tk.Canvas(fenetre,height=len(sudoku)*size,width=len(sudoku[0])*size)

afficher_tableau_tkinter(sudoku,size)

canvas.bind("<Button-1>", get_mouse_pos)

canvas.grid()

 

def case_est_vide():

    x,y=POSITION_SOURIS

    return sudoku[x][y]==0

 

def boutonfermer():

    bouton=tk.Button(boutonfermer,text="nouveau",command=cree_grille)

    bouton.pack(side="left",padx=(0,0))

    bouton_quitter=tk.Button(boutonfermer,texte="Quiter",command=fenetre.destroy)

    bouton_quitter.pack(side="left", padx=(0,0))

   

fenetre.mainloop()

 

def fermer_fenetre():

    fenetre.destroy()

 

bouton=tk.Button(command=fermer_fenetre,bg="orange red",text="tu peux quitter la partie",font=(12))

bouton.grid(row=1,column=1)

def redemarer():

    fenetre.mainloop()

 

bouton2=tk.Button(command=redemarer, bg='Slateblue3',text="tu peut refaire une partie",font=(12))

bouton2.grid(row=2,column=1)

 

def sauvegarder():

    print("3")

   

 

bouton3=tk.Button(command=sauvegarder, bg="hot pink",text="sauvegarde ta partie")