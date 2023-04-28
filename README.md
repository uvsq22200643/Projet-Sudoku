
## Installation

Install my-project with npm

```bash
  npm install my-project
  cd my-project
```
https://github.com/uvsq22205739/Projet-Sudoku 
# Project Sudoku

TD°2 Biologie-Informatique
Kelly MBEMBA
Amel AROUA

https://github.com/uvsq22205739/Projet-Sudoku

Ceci est le projet d'un jeu Sudoku qui est un jeu populaire de placement de nombres basé sur la logique combinatoire. L’objectif est de remplir une grille 9 × 9 avec des chiffres de sorte que chaque colonne, chaque ligne et chacune des neuf
sous-grilles 3 × 3 qui composent la grille (également appelées "boîtes", "blocs" ou "régions") contiennent
tous les chiffres de 1 à 9.

EXPLICATION DU PROGRAMME:

from random import randint, choice
import tkinter as tk: C'est deux fonctions permettent d'ouvrir une interphase graphique 

valeurspossibles correspond au au valeurs qu'il doit y avoir dans le tableau

def creer_tableau_plein(lignes,colonnes): Crée un tableau de valeurs comprises entre 1 et 9
Pour chaque ligne dans un tableau déjà rempli, on prend une série de 3 lignes aléatoirement et on l'ajoute à un tableau, afin d'ajouter un peu de hasard dans sa structure

tableau = [] : créer un tableau

list_of_choices = [0,3,6] : 3 listes au choix qu'on ajoute au tableau pour ajouter du hasard aux tableau 

full_tab = tableau avec toutes les valeurs
#renvoie un tableau de Sudoku

for _ in range(0,lignes,3):
        c = choice(list_of_choices)
        list_of_choices.remove(c)
        tableau.append(full_tab[c])
        tableau.append(full_tab[c+1])
        tableau.append(full_tab[c+2])
    return tableau
    
La foncrions Choice permet que le tableau soi pas toujours le même à xhaque nouvelles partie. Et c est un des nombres choisis au hasard, puis on l'enlève de la liste et on s'enser pour crée les colonnes du jeux( 3 lignes, puis les 3 suivantes)  

def vider_tableau(tableau,n): #qui prend un tableau et vide aléatoirement n cases dans le tableau et Place aléatoirement n 0 dans un tableau où les 0 correspondent au cases vides

def afficher_tableau(tableau):#affiche le tableau dans la console 
for ligne in range(len(tableau)): pour chaque ligne
        print(tableau[ligne]) ## afficher la ligne

def modifier_valeur_tableau(tableau,pos,v): qui prend un tableau, un tuple (x,y) et une valeur qui remplace la valeur à la position tableau [x][y] par v (placer les chiffres du joueur ou à les enlever ). Modifie la valeur présente aux coordonnées pos dans un tableau (tableau[x][y]) par la valeurv.
Un tuple(x,y) est une liste ordonné d'éléments. 

def recuperer_carre(tableau): Crée une liste contenant tous les sous-tableaux de taille 3x3 dans un tableau( ptre,nd ke sudoku et le découpe en 9 petits carrés)

def sommes_carres(carre): Calcule la somme des valeurs d'un tableau et notament renvoie  la somme des ombrse dans un petit carrée

def sudoku_ok(line):(fonction prise sur internet) Vérifie si une ligne d'un tableau est correcte et qu'il n'y est donc pas de répétitions. 
    
def check_sudoku(grid):(fonction prise sur internet) qui prend un tableau et qui vérifie s'il est correctement rempli (en utilisant les fonctions recupere_carre,somme_carre et sudoku_ok). Vérifie si un tableau répond bien aux règles de complétion d'un sudoku. Va ensuite verifier les lignes, puis les colonnes et enfin les petits carrés pour voirs si c'est égal à ce que l'on veut51+2+3+4+5+6+7+8+9). 
   
def afficher_tableau_tkinter(tableau,taille): affiche un canvas avec une grille .Affiche une fenêtre ainsi qu'un canvas dont les cases dessinées correspondent à un tableau et sont de taille taille
  
def update_texte(): Cette fonction permet de retourner si l'utilisateur a bien rempli avec les valeurs possible sinon elle affiche que ces valeurs ne respecte pas les contrainte du jeux. Et lorsque le jeux est fini et qu'il a bien était réaliser ce programme affiche "Vous avez gangné"
    
def get_mouse_pos(event): recupere la position de la souris quand tu cliques. Affiche les coordonnées où l'utilisateur a cliqué
    
size = 50
nb_cases_vides = 60: permet de vider 60 cases pour que l'utilisateur puisser jouer en les remplissent
POSITION_SOURIS = (0,0)
tableau_texte=[[0]*9 for _ in range(9)]: cela creer un tableau 9*9 contenant des 0


def case_est_vide(): Si une cases contient un 0 , donc permet de savoir si une case est vide pour pouvoir la remplir par un chiffre te donc si ca rentre dans le Sudoku 

def fermer_fenetre(): permet de fermer la fenetre

bouton_texte= bouton qui affiche "ecrire une valeur"   

bouton= un autre bouton qui permet de fermer la fenetre

bouton2=un autre bouton qui permet de refaire un partie. Donc la grille se vide et il y aure donc 60 cases de remplis qui seront aléatoires

def sauvegarder(): fonctions qui permet de sauvegarder la partie mais nous avons pas pu la finir 

def aide(): fonction prise sur inetrent et qui permet de proposer uen aide pour le joueur quand il remplit les cases avec les valeurs. 
    
Label=tk.Label(fenetre, text="")
Label.grid(row=0, column=1)

bouton3= troisième bouton qui permet de quvegarder la partie 

my_entry = tk.Entry(fenetre) /(fonction prise sur internet)
cette fonction permet de changer l’icone par défaut de la fenêtre Tkinter Python. Lie la touche Entrée à une fonction dans Tkinter Python. Efface le contenu d’un widget Text Tkinter Python. Augmenter la hauteur et largeur d’un widget Entry Tkinter. Récupérer la valeur d’un Entry saisi par l’utilisateur. Permet donc a l'utilisateur de remplir la cases q'il veut avec le chiffres qu'il veut de 1 à 9. 
    
fenetre.mainloop()


###Souces internet pour les fonctions:

def aide():
    webbrowser.open("https://www.assistant-sudoku.com/")
    #bouton4.config(text="copie colle ce lien : https://www.assistant-sudoku.com/")
