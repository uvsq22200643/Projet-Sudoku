#Merci d'écrire tes codes ici
from random import randint, choice
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import webbrowser
valeurspossibles=range(1,10)



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

    for _ in range(0,lignes,3):#de 0 à 9 par saut de 3
        c = choice(list_of_choices)#permet de choisir au hasard l'une des trois valeur de la liste associer a la variable list_of_choices
        list_of_choices.remove(c)#on va supprimer lelement selectionnner au hasard
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

def recuperer_carre(tableau):#permet la division de la grille en 9*9 et carrés 3*3
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

def sudoku_ok(line): # fonction prise sur internet 
    """Vérifie si une ligne d'un tableau est correcte"""#en reg, elle verifie si les lignes sont correcte avec tout les chiffres et donc qu'il n'y a pas de répetion 
    return (len(line) == 9 and sum(line) == sum(set(line)))

def check_sudoku(grid):# fonctions prise sur internet prend en paramètre toute la grille du sudoku
    # qui prend un tableau et qui vérifie s'il est correctement rempli (en utilisant les fonctions recupere_carre,somme_carre et sudoku_ok)
    """Vérifie si un tableau répond bien aux règles de complétion d'un sudoku"""
    bad_rows = [row for row in grid if not sudoku_ok(row)]#stocke les lignes qui se répètent
    grid = list(zip(*grid))#permet d'inverser les colonnes et les lignes de la grille
    bad_cols = [col for col in grid if not sudoku_ok(col)]
    carres = recuperer_carre(grid)#divise la grille en 9 carrés
    bad_squares = False
    for carre in carres:
        bad_squares = bad_squares or sommes_carres(carre) == sum(range(9+1))
    return not (bad_rows or bad_cols or bad_squares)
 #la fonction return True ou false en fonction de si la grille est correctement remplie ou non 

def afficher_tableau_tkinter(tableau,taille):#qui affiche un canvas avec une grille
    """Affiche une fenêtre ainsi qu'un canvas dont les cases dessinées correspondent à un tableau et sont de taille taille"""
    global canvas
    global tableau_texte
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            rectangle = canvas.create_rectangle(i*taille,j*taille,i*taille+taille,j*taille+taille,outline = "black", width=3)
            texte = str(tableau[i][j])
            if texte=="0" or int(texte) not in valeurspossibles:
                texte = " "
            texte_item=canvas.create_text(i*taille + taille//2, j*taille + taille//2, text=texte, fill="black", font=('Helvetica 15 bold'))
            tableau_texte[i][j]=texte_item

def update_texte():#permet dactualiser le tableau avec les chiffres rentrer par le joueur
    global POSITION_SOURIS
    item = canvas.find_closest(*POSITION_SOURIS)[0]#permet de rouver la case vide la plus proche du click de la souris
    texte=my_entry.get()#l'espace qui nous permet decrire le chiffre qui apparaitra sur la case
    if int(texte) not in valeurspossibles:
        Label["text"] = "CHOISIS UN CHIFFRE ENTRE 1 ET 9 :(, tu ne respecte pas les contraintes du jeux"
        return 
    else:
        Label["text"]="TON CHIFFRE EST VALABLE :D"
        
    sudoku[POSITION_SOURIS[0]//size][POSITION_SOURIS[1]//size] = int(texte)
    if check_sudoku(sudoku):
        Label["text"]="Vous avez gagné !"
    print(texte)
    print(item)
    canvas.itemconfigure(item,text=texte)# permet de dire si la personne a fait une erreur en saisissant le mauvais chiffre et affiche si l'on a réussi




def get_mouse_pos(event): #qui recupere la position de la souris quand tu cliques
    """Affiche les coordonnées où l'utilisateur a cliqué"""
    global size
    global POSITION_SOURIS
    #POSITION_SOURIS = (event.x//size, event.y//size)
    POSITION_SOURIS=(event.x,event.y)
    
    

size = 50
nb_cases_vides = 60# le nombre de cases remplis et le reste des cases son vide pour que l'utilisateur puisse les remplires
POSITION_SOURIS = (0,0)
tableau_texte=[[0]*9 for _ in range(9)]#creer un tableau 9*9 contenant des 0 (0=cases vides)
sudoku = creer_tableau_plein(9, 9)
while not check_sudoku(sudoku):
    sudoku = creer_tableau_plein(9, 9)
vider_tableau(sudoku, nb_cases_vides)

fenetre = tk.Tk()
fenetre.title("Jeu du Sudoku")
canvas = tk.Canvas(fenetre,height=len(sudoku)*size,width=len(sudoku[0])*size,bg="light goldenrod")
afficher_tableau_tkinter(sudoku,size)
canvas.bind("<Button-1>", get_mouse_pos)
canvas.grid()

def case_est_vide():
    x,y=POSITION_SOURIS
    return sudoku[x][y]==0

def fermer_fenetre():
    fenetre.destroy()

bouton_texte=tk.Button(command=update_texte,text="clique ici pour valider ta valeur")
bouton_texte.grid(row=4,column=2)    

bouton=tk.Button(command=fermer_fenetre,bg="orange red",text="tu peux quitter la partie",font=(12))#bouton pour quiter la partie 
bouton.grid(row=1,column=1)

def redemarer():
    bouton2.config(text="commence ta nouvelle partie :)")

bouton2=tk.Button(command=redemarer, bg='Slateblue3',text="tu peut refaire une partie",font=(12))# bouton pour refaire une partie 
bouton2.grid(row=2,column=1)

def sauvegarder():#fonction qui permet de sauveagredr avec la fonction filedialogue qui permet de sauvegarder des fichiers
    filename = filedialog.asksaveasfilename(defaultextension=".eps")
    canvas.postscript(file=filename, colormode='color')

def aide():
    webbrowser.open("https://www.assistant-sudoku.com/")
    #bouton4.config(text="copie colle ce lien : https://www.assistant-sudoku.com/")
    
Label=tk.Label(fenetre, text="")
Label.grid(row=0, column=1)

bouton3=tk.Button(command=sauvegarder, bg="hot pink",text="sauvegarder la partie",font=(12))# bouton sauvegarder la partie
bouton3.grid(row=3,column=1)

bouton4=tk.Button(command=aide,bg="pink",text="help",font=9)# bouton help
bouton4.grid(row=4,column=1)

my_entry = tk.Entry(fenetre) # fonctions prise sur internet 
my_entry.grid()
# entry = tk.Entry(fenetre,
#                  font='Arial 60 bold',
#                  width='5',
#                  bg='lavender',
#                  insertofftime=500,
#                  relief=FLAT)
my_entry.grid(row=2, column=2)
my_entry.focus_set()
    
fenetre.mainloop()
