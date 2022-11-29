ORDOF -- This software is designed to rename, sort, store and organize files within a directory
    Copyright (C) 2022  Tripodi Matthieu

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.


/////////////////////////////////////////////////////////////////////////////////////////////


Ordof est un logiciel permettant d'effectuer plusieurs tâches sur tout types de fichiers comme :
>>> Rennomer un grand nombre de fichiers simultanement
>>> Trier et ranger un grand nombre de fichiers en créant des sous dossiers puis en déplacant les fichiers à l'interieur
>>> Extraire tous les fichiers de tous les sous-dossier au sein d'un répertoire principal

Détail des mode de fonctionnement :
>>> Ces informations sont disponible depuis le logiciel via les bouton "info" en haut à droite des fenêtres


/////////////////////////////////////////////////////////////////////////////////////////////



Mode Auto_rename :

Ce programme renomme tous les fichiers sélectionnés par un nouveau nom 
définit par l'utilisateur ainsi qu'un numéro automatiquement incrémenté

Utilisation:
1. Indiquez le chemin du dossier contenant les fichiers à renommer
>>> Méthode 1 : Localisez ce dossier sur votre machine puis copiez/collez le chemin ici
>>> Méthode 2 : Utilisez l'explorateur de fichiers en cliquant sur le logo "Dossier + Loupe"

2. Sélectionnez le mode de recherche de fichiers
>>> Soit par extension (tous les fichiers avec l'extension renseigné seront renommés)
>>> Soit par nom (tous les fichiers contenant les caractères renseignés seront renommés)
>>> Soit tous les fichiers sans disctinction

3. Renseignez le nouveau nom à attribuer
>>> Attention >>> Symbole interdit : ( . \\  / ? : * > < )

4. Renseignez le séparateur entre le nom et le numero attribué automatiquement
>>> Exemple : séparateur = " - " >>> Nouveau_nom - 1, Nouveau_nom - 2, Nouveau_nom - 3
>>> Attention >>> Symbole interdit : ( . \\  / ? : * > < )

5. Cliquez sur la flèche en bas à droite pour lancer l'opération


/////////////////////////////////////////////////////////////////////////////////////////////


Mode extraction :

Fonctionnement du programme :
1. Il identifie les dossiers contenu dans le répertoire renseigné
2. Il déplace les fichiers présent dans ces dossiers pour les placer dans le répertoire
3. Il supprime les dossiers à présent vide

Utilisation :
1. Indiquez le chemin du répertoire contenant les sous-dossiers à extraire
>>> Méthode 1 : Localisez ce dossier sur votre machine puis copiez/collez le chemin ici
>>> Méthode 2 : Utilisez l'explorateur de fichiers en cliquant sur le logo "Dossier + Loupe"

2. Indiquez le degré d'extraction
>>> C'est lui qui indique combien de fois le programme s'éxecute
>>> Degré 1 : Le programme va extraire les fichiers de tout les dossiers visible
>>> Degré 2 : Extraction des premiers dossiers puis des sous dossiers si ils existent
>>> Degré 3 : Extraction des premiers dossiers puis des sous-dossiers si ils existent
              puis des sous-sous-dossiers si ils existent

Il n'y à pas de limite de degré
exemple : "3500" est accepté

>>> Renseigner "ALL" pour extraire l'integralité des dossiers / sous-dossiers

3. Cliquez sur la flèche en bas à droite pour lancer l'opération


/////////////////////////////////////////////////////////////////////////////////////////////


Mode Tri

Ce programme permet de trier les fichiers d'un répertoire

Fonctionnement du programme :
1. Il sélectionne les fichiers selon les paramètres choisit par l'utilisateur
>>> Paramètre : Extension, Nom, Date
>>> Les paramètres sont cumulable
2. Il crée des sous-dossiers avec un nom personnalisable ainsi que les paramètres indiqués
3. Il déplace les fichiers dans les sous-dossiers correspondant


Utilisation :
1. Indiquez le chemin du répertoire contenant les fichiers à trier
>>> Méthode 1 : Localisez ce dossier sur votre machine puis copiez/collez le chemin ici
>>> Méthode 2 : Utilisez l'explorateur de fichiers en cliquant sur le logo "Dossier + Loupe"


Détails des paramètres :

Extension :
Regroupe les fichiers par extension
Exemple :
>>> 1 sous-dossier pour les .jpg
>>> 1 autre sous-dossier pour les .avi


Nom :
Range les fichiers portant le nom recherché dans un sous-dossier


Date :
Récupère la date de création dans les méta-données du fichier
Regroupe les fichiers par date de création ou à défaut par date de modification
La sensibilitée du tri est paramètrable :
>>> Par année
>>> Par mois
>>> Par jour


Extension + Nom :
Regroupe uniquement les fichiers portant le nom recherché par extension


Extension + Date :
Regroupe les fichiers par date en créant un sous-dossier pour chaque extension
Exemple :
>>> 1 sous-dossier pour les .mp4 de 2016
>>> 1 autre sous-dossier pour les .jpg de 2016


Extension + Nom + Date :
Regroupe uniquement les fichiers portant le nom recherché par date en créant
un sous-dossier pour chaque extension


Nom + Date :
Regroupe uniquement les fichiers portant le nom recherché par date