
Noms des auteurs :  Patureau Bastien
Date de réalisation : 03/02/2025


## 1. Premier container

### 1.1. Hello World 

Pouvez-vous expliquer avec vos mots ce qui s'est passé suite à l'exécution de cette commande? 



### 1.2.  Observer un container


Retrouvez les informations suivantes sur le container lancé précédemment : 
1. Quel est son identifiant ? 
2. Quel est son nom ? 
3. Quel est son état ? 
4. Quel est le nom de son image?  Avez-vous vu au point 1.1. d''où cette image provenait?  
5. Quelle commande le container a-t-il exécuté? 
6. Si vous avez installer Docker Desktop, pouvez-vous retrouver ces mêmes informations dans l'interface graphique? 

### 1.3. Les images 

1. Quelles informations voyez-vous?  Quel est le lien avec ce que vous avez observé auparavant? 
2. Comparez l'output de cette commande avec la vue correspondante de l'interface graphique.  
3. Essayez de trouver la commande qui vous permettra de supprimer cette image.  C'est une bonne idée de ne pas conserver les images non utilisées sur votre système de fichiers : même avec la mutualisation de couches, elles prennent de l'espace sur le disque! 

## 2. Utiliser un container

### 2.1. Interagir avec un container

1. A quoi servent les options ```i``` et ```t```dans la commande ci-dessus? 
2. Chaque container Docker est destiné à exécuter une commande unique.  Quelle est-elle dans ce cas-ci? 
3. Dans le container, quels sont les processus présents?  Et leurs PIDs? 
4. Avec quel utilisateur êtes-vous loggé? 
5. Votre container a-t'il accès à Internet?  Qui est son résolveur? 

### 2.2. Inspecter un container


1. Chaque container dispose d'une interface réseau.  Quelle est l'adresse **IP** de l'interface de votre container? 
2.  Votre container a-t'il des **ports** ouverts?  


### 2.3. Faire tourner un service dans un container



- Qu'avez-vous observé au niveau des "ports" ?  Expliquez et illustrez votre réponse avec des screenshots. 


## 3. Construire des images

### 3.1. Figer un container 


### 3.2. Créer une image sur base d'un Dockerfile


## Exercices récapitulatifs

Documentez ici la réalisation des exercices, via des explications et des snapshots. 
### 4.1. Démarrer un serveur Web Apache


### 4.2. Lancer un résolveur Bind dans un container Docker

1. Quelle configuration avez-vous effectuée au niveau des ports ? 
2. Qu'avez-vous observé dans la trace Wireshark qui prouve que la configuration est correcte?  Illustrez avec un screenshot de la capture. 

### 4.3. Container avec script Python
