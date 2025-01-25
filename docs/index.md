# Tp Expérimentations


## État du TP

Décrivez ici l'état d'avancement du TP.

## Réponses aux questions

Indiquez ici les réponses aux questions posées dans le TP. Vous
reprendrez le numéro de la section et le numéro de la question. Par
exemple pour répondre à la question 3 de la section 2.4 vous indiquerez :

### Question 1.1.a
Pour analyser la complexité de l'algorithme, je propose de compter le nombre de comparaisons effectuées entre les éléments de la liste des marqueurs `(markers)` et ceux de la liste des marqueurs positifs `(positive)`.

### Question 1.1.b
Oui, il existe un **pire** des cas pour cet algorithme. Il se produit lorsque tous les marqueurs de la liste markers ne se trouvent pas dans la liste `positive`.

Donc pour chaque marqueur de markers de taille **n**, l’algorithme parcourt entièrement la liste positive de taille **p**.

Donc dans ce **pire** cas, notre algorithme aura besoin de **`n*p`** comparaisons.

### Question 1.1.c

Dans le **pire** des cas, aucun des marqueurs de la liste `markers` ne se trouve dans la liste `positive`. Cela implique que pour chaque marqueur `m`, nous devons parcourir toute la liste `positive` taille **p** pour pour conclure qu'il est négatif.

Le nombre total de comparaisons dans ce cas est donc:
```math
C1(m,p) = m*p
```
