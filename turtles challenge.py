import turtle
from random import randint



# Initialisation du jeu
ts = turtle.getscreen()
ts.clear()
ts.bgpic("champcourse2.gif")

ts.title("Bienvenue à la course des tortues !")
ts.setup(width=1400, height=800, startx=0, starty=0)






# Déclarez les 5 tortues et positionnez-les sur leurs hexagones respectifs
myfirst = turtle
myfirst.color('red')
myfirst.shape('turtle')
myfirst.penup()
myfirst.goto(-700, 400)
myfirst.pendown()

mysec = turtle
mysec.color('blue')
mysec.shape('turtle')
mysec.penup()
mysec.goto(-700, 300)
mysec.pendown()

mythir = turtle
mythir.color('green')
mythir.shape('turtle')
mythir.penup()
mythir.goto(-700, 200)
mythir.pendown()

myfor = turtle
myfor.color('green')
myfor.shape('turtle')
myfor.penup()
myfor.goto(-700, 100)
myfor.pendown()

# Demander de saisir dans la console les prédictions des joeurus 1 et 2 dans le format 1,2,3
# A IMPLEMENTER


# A l'aide d'une boucle while, faire courir les tortues en tirant un nombre entre 0 et 5 qui représente le nombre de pixels du déplacement vers la droite
i = 0
while i < 200:
    myfirst.forward(randint(1, 5))
    mysec.forward(randint(1, 5))
    mythir.forward(randint(1, 5))
    myfor.forward(randint(1, 5))
    i = i+1



# Comparer les résultats de la course avec les pronostics des joueurs 
# et afficher le résultat de la course
# et le joueur gagnant avec la tortue arbitre et l'instruction turtle.Write à la position 0,0
# A IMPLEMENTER



turtle_arbitre = turtle.Turtle()
turtle_arbitre.goto(0,0)
turtle_arbitre.color("Black")
turtle_arbitre.write("Le joueur 1 à gagné", move=True, align="left", font=("Arial", 16, "normal"))



turtle.mainloop()



