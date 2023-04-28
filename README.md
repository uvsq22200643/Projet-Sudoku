
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

Ceci est le projet d'un jeu Sudoku creer dans une interface graphique avec Tkinter.

Le sudoku est un jeu de logique qui consiste à compléter un tableau de 81 cases (9*9) divisés en 9 colonnes,9 lignes et 9 blocs. Tout en respectant la règle qui est de compléter chaque case avec un chiffre allant de 1 à 9 en suivant 3 contraintes :
- Le chiffre ne doit pas déjà se trouver sur la même colonne
- il ne doit pas se trouver sur la même ligne 
- il ne doit pas déjà se trouver dans le bloc


EXPLICATION DU PROGRAMME:

AU TOTAL NOUS AVONS CREE 15 FONCTIONS QUI NOUS ONT PERMISE DE GENERER LE JEU DONT 3 TROUVER SUR INTERNET

from random import randint, choice --> pour mettre du hasard dans le tableau de facon aléatoire
import tkinter as tk : nous permet d'importer la librairie liée à tkinter pour notre interface graphique 


valeurspossibles est une variable qui correspond aux valeurs que l’utilisateur est censé pouvoir entrer dans le tableau. 

1) def creer_tableau_plein(lignes,colonnes): Crée un tableau de valeurs comprises entre 1 et 9
Pour chaque ligne dans un tableau déjà rempli, on prend une série de 3 lignes aléatoirement et on l'ajoute à un tableau vide, afin d'ajouter un peu de hasard dans sa structure. ce qui permettra par la suite de vider les cases.
    
  Choice permet que le tableau soi pas toujours le même à chaque nouvelles partie. Et c est un des nombres choisis au hasard. 
  
2) def vider_tableau(tableau,n): #qui prend un tableau et vide aléatoirement n cases dans le tableau et Place n 0 dans un tableau où les 0 correspondent au cases vides

3) def afficher_tableau(tableau):fonction qui permet l'affichage du tableau dans la fenetre en affichant ligne par ligne 

4) def modifier_valeur_tableau(tableau,pos,v): qui prend un tableau, un tuple (x,y) et une valeur qui remplace la valeur à la position tableau [x][y] par v (placer les chiffres du joueur ou à les enlever ). Modifie la valeur présente aux coordonnées pos dans un tableau (tableau[x][y]) par la valeurv.
Un tuple(x,y) est une liste ordonné d'éléments. 

5) def recuperer_carre(tableau): Crée une liste contenant tous les sous-tableaux de taille 3x3 dans un tableau( prend le sudoku et le découpe en 9 petits carrés qui seront les 9 blocs a remplir)

6) def sommes_carres(carre): Calcule la somme des valeurs d'un tableau et notament renvoie  la somme des nombre dans un "bloc" de taille 3*3

7) def sudoku_ok(line):(FONCTION PRISE SUR INTERNET ) Vérifie si une ligne d'un tableau est correcte et qu'il n'y est donc pas de répétitions d'un meme chiffre. 
    
8) def check_sudoku(grid):(FONCTION PRISE SUR INTERNET)qui prend un tableau et qui vérifie s'il est correctement rempli (en utilisant les fonctions recupere_carre,somme_carre et sudoku_ok). Vérifie si un tableau répond bien aux règles de complétion d'un sudoku. Va ensuite verifier les lignes, puis les colonnes et enfin les petits carrés pour voirs si c'est égal à ce que l'on veut(51+2+3+4+5+6+7+8+9). 
   
9) def afficher_tableau_tkinter(tableau,taille): affiche un canvas avec une grille .Affiche une fenêtre ainsi qu'un canvas dont les cases dessinées correspondent à un tableau et sont de taille taille
  
10) def update_texte(): Cette fonction permet de retourner si l'utilisateur a bien rempli avec les valeurs possible sinon elle affiche que ces valeurs ne respecte pas les contrainte du jeux. Et lorsque le jeux est fini et qu'il a bien était réaliser ce programme affiche "Vous avez gangné"
    
11) def get_mouse_pos(event): recupere la position de la souris quand tu cliques. cette variable contient coordonnées où l'utilisateur a cliqué
    
12) def case_est_vide(): permet de savoir si une case est vide en fonction de si elle contient un 0 dans le programme ou non pour pouvoir la remplir par un chiffre a l'aide de la fonction update texte.

13) def fermer_fenetre(): permet de fermer la fenetre

14) def sauvegarder(): fonction qui permet de sauvegarder la partie en ou emmenant dans l'espace document afin que l'on puisse l'enregistrer dans un dossier

15) def aide():  et qui permet de proposer uen aide pour le joueur quand il remplit les cases avec les valeurs. 

NOUS AVONS CREER 5 BOUTONS :

1) bouton_texte= bouton qui affiche "valide ta valeur en cliquant" et qui lorsque l'on clique dessus va permettre la mise à jour de la case vide selectionnée avec  cette fois ci un chiffre choisis par l'utilisateur grace à la fonction "update texte" s'il est bien entre 1 et 9

2) bouton = un autre bouton qui permet de fermer la fenetre grace à la fonction "fermer_fenetre" 

3) bouton2= un bouton qui permet de refaire une partie. Il est censé faire en sorte que la grille se vide afin de générer un tableau remplie aléatoirement avec des cases vides. mais nous avons pas reussi

4) bouton3= troisième bouton qui permet de sauvegarder la partie à l'aide de la fonction "sauvegarder"

5) bouton4 : lorsque l'on qui sur le bouton une page web est génerer permettant un assistant sudoku 


1 LABEL CREER POUR LA FENETRE:

Label=tk.Label(fenetre, text="")
Label.grid(row=0, column=1)



my_entry = tk.Entry(fenetre) : variable qui permet lapparition d'un "rectangle" dans la fenetre ainsi l'utilisateur peut remplir la cases qu'il veut un chiffre allant de 1 à 9. Lie la touche Entrée à une fonction dans Tkinter Python.
    
fenetre.mainloop() -> permet l'ouverture de la fenetre
