# ORDOF -- This software is designed to rename, sort, store and organize files within a directory
#     Copyright (C) 2022  Tripodi Matthieu

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.


from tkinter import *


# ______________________________________________________________ Ressources ______________________________________________________________ #


class ICON:
    Logo = 'Ressources/Logo.ico'

    rename_img = PhotoImage(file="Ressources/Rename_logo.png")
    rename_img_max = PhotoImage(file="Ressources/Rename_logo_max.png")

    pack_img = PhotoImage(file="Ressources/Pack_logo.png")
    pack_img_max = PhotoImage(file="Ressources/Pack_logo_max.png")

    back_img = PhotoImage(file="Ressources/Back_logo.png")
    back_img_max = PhotoImage(file="Ressources/Back_logo_max.png")

    browser_img = PhotoImage(file="Ressources/Browser_logo.png")
    browser_img_max = PhotoImage(file="Ressources/Browser_logo_max.png")

    info_img = PhotoImage(file="Ressources/Info_logo.png")
    info_img_max = PhotoImage(file="Ressources/Info_logo_max.png")
    
    go_img = PhotoImage(file="Ressources/Go_logo.png")
    go_img_max = PhotoImage(file="Ressources/Go_logo_max.png")

    goback_img = PhotoImage(file="Ressources/Goback_logo.png")
    goback_img_max = PhotoImage(file="Ressources/Goback_logo_max.png")

    tri_img = PhotoImage(file="Ressources/Tri_logo.png")
    tri_img_max = PhotoImage(file="Ressources/Tri_logo_max.png")

    extract_img = PhotoImage(file="Ressources/Extract_logo.png")
    extract_img_max = PhotoImage(file="Ressources/Extract_logo_max.png")

    ext_img = PhotoImage(file="Ressources/Ext_logo.png")
    ext_img_max = PhotoImage(file="Ressources/Ext_logo_max.png")

    name_img = PhotoImage(file="Ressources/Name_logo.png")
    name_img_max = PhotoImage(file="Ressources/Name_logo_max.png")

    all_img = PhotoImage(file="Ressources/All_logo.png")
    all_img_max = PhotoImage(file="Ressources/All_logo_max.png")

    date_img = PhotoImage(file="Ressources/Date_logo.png")
    date_img_max = PhotoImage(file="Ressources/Date_logo_max.png")

    an_img = PhotoImage(file="Ressources/An_logo.png")
    an_img_max = PhotoImage(file="Ressources/An_logo_max.png")

    mois_img = PhotoImage(file="Ressources/Mois_logo.png")
    mois_img_max = PhotoImage(file="Ressources/Mois_logo_max.png")

    jour_img = PhotoImage(file="Ressources/Jour_logo.png")
    jour_img_max = PhotoImage(file="Ressources/Jour_logo_max.png")

    suppSD_img = PhotoImage(file="Ressources/SuppSD_logo.png")
    suppSD_img_max = PhotoImage(file="Ressources/SuppSD_logo_max.png")

    keepSD_img = PhotoImage(file="Ressources/KeepSD_logo.png")
    keepSD_img_max = PhotoImage(file="Ressources/KeepSD_logo_max.png")

# ______________________________________________________________ Colors Dimensions Text ______________________________________________________________ #



class CDT:
    # _____________________________________________ COULEUR _____________________________________________ #

    bg_color = '#202020'
    bg_entry = '#bbbbbb'
    fg_color = '#909191'

    # _____________________________________________ POLICE ECRITURE _____________________________________________ #

    title_caly = "Electronic"
    title_size = 45

    sub_title_caly = "ink free"
    sub_title_size = 20

    text_caly = "Calibri"
    text_size = 15

    text_big_caly = "Calibri"
    text_big_size = 20

    text_list_caly = "Calibri"
    text_list_size = 11

    text_entry_caly = "Calibri"
    text_entry_size = 13

    # _____________________________________________ DIMENSIONS _____________________________________________ #

    can_litle_bp_size = 75
    can_nav_icon = 50
    xy_icon_nav = 25

    width_entry_path = 60

    # _____________________________________________ MARGE _____________________________________________ #

    title_marge = 10

    bp_bk_mrg_x = 10
    bp_bk_mrg_y = 15

    bp_info_mrg_x = 720
    bp_info_mrg_y = 0

    entry_rep_mrg_x = 0
    entry_rep_mrg_y = 160

    bp_browser_mrg_x = 610
    bp_browser_mrg_y = 135

    sous_menu_mrg_y = 10

    # _____________________________________________ INFO _____________________________________________ #

    # Auto_rename
    text_subtitle_rename_info = "Guide Auto-Rename"
    text_corps_rename_info =[
    '\n',
    'Ce programme renomme tous les fichiers s??lectionn??s par un nouveau nom ',
    'd??finit par l\'utilisateur ainsi qu\'un num??ro automatiquement incr??ment??',
    '\n',
    '_______________________________________________',
    'Utilisation:',
    '1. Indiquez le chemin du dossier contenant les fichiers ?? renommer :',
    '>>> Utilisez l\'explorateur de fichiers en cliquant sur le logo \"Dossier + Loupe\"',
    '\n',
    '2. S??lectionnez le mode de recherche de fichiers',
    '>>> Soit par extension (tous les fichiers avec l\'extension renseign?? seront renomm??s)',
    '>>> Soit par nom (tous les fichiers contenant les caract??res renseign??s seront renomm??s)',
    '>>> Soit tous les fichiers sans disctinction',
    '\n',
    '3. Renseignez le nouveau nom ?? attribuer',
    '>>> Attention >>> Symbole interdit : ( . \\  / ? : * > < )',
    '\n',
    '4. Renseignez le s??parateur entre le nom et le numero attribu?? automatiquement',
    '>>> Exemple : s??parateur = " - " >>> Nouveau_nom - 1, Nouveau_nom - 2, Nouveau_nom - 3',
    '>>> Attention >>> Symbole interdit : ( . \\  / ? : * > < )',
    '\n',
    '5. Cliquez sur la fl??che en bas ?? droite pour lancer l\'op??ration']




    # Extraction fichiers
    text_subtitle_depack_info = "Guide Extraction"
    text_corps_depack_info = [
    '\n',
    'Fonctionnement du programme :',
    '1. Il identifie les dossiers contenu dans le r??pertoire renseign??',
    '2. Il d??place les fichiers pr??sent dans ces dossiers pour les placer dans le r??pertoire',
    '3. Il supprime les dossiers ?? pr??sent vide',
    '\n',
    '_______________________________________________',
    'Utilisation :',
    '1. Indiquez le chemin du dossier contenant les fichiers ?? renommer :',
    '>>> Utilisez l\'explorateur de fichiers en cliquant sur le logo \"Dossier + Loupe\"',
    '\n',
    '2. Indiquez le degr?? d\'extraction' ,
    '>>> C\'est lui qui indique combien de fois le programme s\'??xecute',
    '>>> Degr?? 1 : Le programme va extraire les fichiers de tout les dossiers visible',
    '>>> Degr?? 2 : Extraction des premiers dossiers puis des sous dossiers si ils existent',
    '>>> Degr?? 3 : Extraction des premiers dossiers puis des sous-dossiers si ils existent' ,
                  'puis des sous-sous-dossiers si ils existent',
    '\n',
    'Il n\'y ?? pas de limite de degr??',
    'exemple : "3500" est accept??',
    '\n',
    '>>> Renseigner "ALL" pour extraire l\'integralit?? des dossiers / sous-dossiers',
    '\n',
    '3. Cliquez sur la fl??che en bas ?? droite pour lancer l\'op??ration']



    # Tri fichiers
    text_subtitle_tri_info = "Guide Tri"
    text_corps_tri_info = [
    '\n',
    'Ce programme permet de trier les fichiers d\'un r??pertoire',
    '\n',
    '_______________________________________________',
    'Fonctionnement du programme :',
    '1. Il s??lectionne les fichiers selon les param??tres choisit par l\'utilisateur',
    '>>> Param??tre : Extension, Nom, Date',
    '>>> Les param??tres sont cumulable',
    '2. Il cr??e des sous-dossiers avec un nom personnalisable ainsi que les param??tres indiqu??s',
    '3. Il d??place les fichiers dans les sous-dossiers correspondant',
    '\n',
    '_______________________________________________',
    'Utilisation :',
    '1. Indiquez le chemin du dossier contenant les fichiers ?? renommer :',
    '>>> Utilisez l\'explorateur de fichiers en cliquant sur le logo \"Dossier + Loupe\"',
    '\n',
    '_______________________________________________',
    'D??tails des param??tres :',
    '\n',
    '1. Extension :', #_______________________________ EXT
    'Regroupe les fichiers par extension', 
    'Exemple :', 
    '>>> 1 sous-dossier pour les .jpg', 
    '>>> 1 autre sous-dossier pour les .avi',
    '\n',
    '2. Nom :', #_______________________________ NOM
    'Range les fichiers portant le nom recherch?? dans un sous-dossier',
    '\n',
    '3. Date :', #_______________________________ DATE
    'R??cup??re la date de cr??ation dans les m??ta-donn??es du fichier',
    'Regroupe les fichiers par date de cr??ation ou ?? d??faut par date de modification',
    'La sensibilit??e du tri est param??trable :',
    '>>> Par ann??e',
    '>>> Par mois',
    '>>> Par jour',
    '\n',
    '4. Extension + Nom :', #_______________________________ EXT + NOM
    'Regroupe uniquement les fichiers portant le nom recherch?? par extension',
    '\n',
    '5. Extension + Date :', #_______________________________ EXT + DATE
    'Regroupe les fichiers par date en cr??ant un sous-dossier pour chaque extension',
    'Exemple :', 
    '>>> 1 sous-dossier pour les .mp4 de 2016', 
    '>>> 1 autre sous-dossier pour les .jpg de 2016',
    '\n',
    '6. Nom + Date :',
    'Regroupe uniquement les fichiers portant le nom recherch?? par date',
    '\n',
    '7. Extension + Nom + Date :', #_______________________________ EXT + NOM + DATE
    'Regroupe uniquement les fichiers portant le nom recherch?? par date en cr??ant', 
    'un sous-dossier pour chaque extension',
    ]

    # _____________________________________________ MENU_CONFIRMATION _____________________________________________ #
    
    def text_label_elements(Op):
        if Op == 1:
            txt = "Fichiers vont ??tre renomm??s"
        if Op == 2:
            txt=""
        if Op == 3:
            txt = "Fichiers vont ??tre tri??s"
        if Op == 4:
            txt = "Fichiers vont ??tre tri??s"
        if Op == 5:
            txt = "Fichiers vont ??tre tri??s"
        if Op == 6:
            txt = "Fichiers vont ??tre tri??s"
        if Op == 7:
            txt = "Fichiers vont ??tre tri??s"
        if Op == 8:
            txt = "Fichiers vont ??tre tri??s"
        if Op == 9:
            txt = "Fichiers vont ??tre tri??s"

        return txt   

    def text_go(Op):
        if Op == 1:
            txt = "Rename >>>"
        if Op == 2:
            txt=""
        if Op == 3:
            txt = "Tier >>>"
        if Op == 4:
            txt = "Tier >>>"
        if Op == 5:
            txt = "Tier >>>"
        if Op == 6:
            txt = "Tier >>>"
        if Op == 7:
            txt = "Tier >>>"
        if Op == 8:
            txt = "Tier >>>"
        if Op == 9:
            txt = "Tier >>>"

        return txt  

    # _____________________________________________ RAPPORT ERREUR TRAITEMENT _____________________________________________ #
    
    def text_label_error(Op):
        if Op == 1:
            txt = "Fichiers impossible ?? renommer"
        if Op == 2:
            txt="Elements impossible ?? d??placer"
        if Op == 3:
            txt = "Fichiers impossible ?? d??placer"
        if Op == 4:
            txt = "Fichiers impossible ?? d??placer"
        if Op == 5:
            txt = "Fichiers impossible ?? d??placer"
        if Op == 6:
            txt = "Fichiers impossible ?? d??placer"
        if Op == 7:
            txt = "Fichiers impossible ?? d??placer"
        if Op == 8:
            txt = "Fichiers impossible ?? d??placer"
        if Op == 9:
            txt = "Fichiers impossible ?? d??placer"

        return txt   


    def text_msg_error(Op):
        if Op == 1:
            txt = "Un probl??me est survenu lors du traitement des fichiers"
        if Op == 2:
            txt="Un probl??me est survenu lors de l'extraction"
        if Op == 3:
            txt = "Un probl??me est survenu lors du tri"
        if Op == 4:
            txt = "Un probl??me est survenu lors du tri"
        if Op == 5:
            txt = "Un probl??me est survenu lors du tri"
        if Op == 6:
            txt = "Un probl??me est survenu lors du tri"
        if Op == 7:
            txt = "Un probl??me est survenu lors du tri"
        if Op == 8:
            txt = "Un probl??me est survenu lors du tri"
        if Op == 9:
            txt = "Un probl??me est survenu lors du tri"

        return txt   


# _____________________________________________ MESSAGE SUCCES _____________________________________________ #
    
    def text_msg_succes(Op):
        if Op == 1:
            txt = "Fichiers rennom??s avec succ??s"
        if Op == 2:
            txt = "Elements extrait avec succ??s"
        if Op == 3:
            txt = "Fichiers tri??s avec succ??s"
        if Op == 4:
            txt = "Fichiers tri??s avec succ??s"
        if Op == 5:
            txt = "Fichiers tri??s avec succ??s"
        if Op == 6:
            txt = "Fichiers tri??s avec succ??s"
        if Op == 7:
            txt = "Fichiers tri??s avec succ??s"
        if Op == 8:
            txt = "Fichiers tri??s avec succ??s"
        if Op == 9:
            txt = "Fichiers tri??s avec succ??s"

        return txt   
