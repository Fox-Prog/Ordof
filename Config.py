from tkinter import *





# ______________________________________________________________ Ressources ______________________________________________________________ #


class ICON:
    Logo = 'C:\\Users\\Utilisateur\\Documents\\Programmation\\PYTHON\\Gestion_de_fichiers\\Ordof\\Ressources\\Logo.ico'

    rename_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Rename_logo.png")
    rename_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Rename_logo_max.png")

    pack_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Pack_logo.png")
    pack_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Pack_logo_max.png")

    back_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Back_logo.png")
    back_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Back_logo_max.png")

    browser_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Browser_logo.png")
    browser_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Browser_logo_max.png")

    info_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Info_logo.png")
    info_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Info_logo_max.png")
    
    go_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Go_logo.png")
    go_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Go_logo_max.png")

    goback_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Goback_logo.png")
    goback_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Goback_logo_max.png")


    tri_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Tri_logo.png")
    tri_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Tri_logo_max.png")

    extract_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Extract_logo.png")
    extract_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Extract_logo_max.png")

    ext_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Ext_logo.png")
    ext_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Ext_logo_max.png")

    name_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Name_logo.png")
    name_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Name_logo_max.png")

    all_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/All_logo.png")
    all_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/All_logo_max.png")

    vide_75_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Vide_75.png")

    date_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Date_logo.png")
    date_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Date_logo_max.png")

    an_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/An_logo.png")
    an_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/An_logo_max.png")

    mois_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Mois_logo.png")
    mois_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Mois_logo_max.png")

    jour_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Jour_logo.png")
    jour_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Jour_logo_max.png")

    suppSD_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/SuppSD_logo.png")
    keepSD_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/KeepSD_logo.png")
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
    'Ce programme renomme tous les fichiers sélectionnés par un nouveau nom ',
    'définit par l\'utilisateur ainsi qu\'un numéro automatiquement incrémenté',
    '\n',
    'Utilisation:',
    '1. Indiquez le chemin du dossier contenant les fichiers à renommer',
    '>>> Méthode 1 : Localisez ce dossier sur votre machine puis copiez/collez le chemin ici',
    '>>> Méthode 2 : Utilisez l\'explorateur de fichiers en cliquant sur le logo \"Dossier + Loupe\"',
    '\n',
    '2. Sélectionnez le mode de recherche de fichiers',
    '>>> Soit par extension (tous les fichiers avec l\'extension renseigné seront renommés)',
    '>>> Soit par nom (tous les fichiers contenant les caractères renseignés seront renommés)',
    '>>> Soit tous les fichiers sans disctinction',
    '\n',
    '3. Renseignez le nouveau nom à attribuer',
    '>>> Attention >>> Symbole interdit : ( . \\  / ? : * > < )',
    '\n',
    '4. Renseignez le séparateur entre le nom et le numero attribué automatiquement',
    '>>> Exemple : séparateur = " - " >>> Nouveau_nom - 1, Nouveau_nom - 2, Nouveau_nom - 3',
    '>>> Attention >>> Symbole interdit : ( . \\  / ? : * > < )',
    '\n',
    '5. Cliquez sur la flèche en bas à droite pour lancer l\'opération'
    ]

    # Extraction fichiers
    text_subtitle_depack_info = "Guide Extraction"
    text_corps_depack_info = [
    'Fonctionnement du programme :',
    '1. Il identifie les dossiers contenu dans le répertoire renseigné',
    '2. Il déplace les fichiers présent dans ces dossiers pour les placer dans le répertoire',
    '3. Il supprime les dossiers à présent vide',
    '\n',
    'Utilisation :',
    '1. Indiquez le chemin du répertoire contenant les sous-dossiers à extraire',
    '>>> Méthode 1 : Localisez ce dossier sur votre machine puis copiez/collez le chemin ici',
    '>>> Méthode 2 : Utilisez l\'explorateur de fichiers en cliquant sur le logo "Dossier + Loupe"',
    '\n',
    '2. Indiquez le degré d\'extraction' ,
    '>>> C\'est lui qui indique combien de fois le programme s\'éxecute',
    '>>> Degré 1 : Le programme va extraire les fichiers de tout les dossiers visible',
    '>>> Degré 2 : Extraction des premiers dossiers puis des sous dossiers si ils existent',
    '>>> Degré 3 : Extraction des premiers dossiers puis des sous-dossiers si ils existent' ,
                  'puis des sous-sous-dossiers si ils existent',
    '\n',
    'Il n\'y à pas de limite de degré',
    'exemple : "3500" est accepté',
    '\n',
    '>>> Renseigner "ALL" pour extraire l\'integralité des dossiers / sous-dossiers',
    '\n',
    '3. Cliquez sur la flèche en bas à droite pour lancer l\'opération'
]


    # _____________________________________________ MENU_CONFIRMATION _____________________________________________ #
    
    def text_label_elements(Op):
        if Op == 1:
            txt = "Fichiers vont être renommés"
        if Op == 2:
            txt=""
        if Op == 3:
            txt = "Fichiers vont être triés"
        if Op == 4:
            txt = "Fichiers vont être triés"
        if Op == 5:
            txt = "Fichiers vont être triés"
        if Op == 6:
            txt = "Fichiers vont être triés"
        if Op == 7:
            txt = "Fichiers vont être triés"
        if Op == 8:
            txt = "Fichiers vont être triés"
        if Op == 9:
            txt = "Fichiers vont être triés"

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
            txt = "Fichiers impossible à renommer"
        if Op == 2:
            txt="Elements impossible à déplacer"
        if Op == 3:
            txt = "Fichiers impossible à déplacer"
        if Op == 4:
            txt = "Fichiers impossible à déplacer"
        if Op == 5:
            txt = "Fichiers impossible à déplacer"
        if Op == 6:
            txt = "Fichiers impossible à déplacer"
        if Op == 7:
            txt = "Fichiers impossible à déplacer"
        if Op == 8:
            txt = "Fichiers impossible à déplacer"
        if Op == 9:
            txt = "Fichiers impossible à déplacer"

        return txt   


    def text_msg_error(Op):
        if Op == 1:
            txt = "Un problème est survenu lors du traitement des fichiers"
        if Op == 2:
            txt="Un problème est survenu lors de l'extraction"
        if Op == 3:
            txt = "Un problème est survenu lors du tri"
        if Op == 4:
            txt = "Un problème est survenu lors du tri"
        if Op == 5:
            txt = "Un problème est survenu lors du tri"
        if Op == 6:
            txt = "Un problème est survenu lors du tri"
        if Op == 7:
            txt = "Un problème est survenu lors du tri"
        if Op == 8:
            txt = "Un problème est survenu lors du tri"
        if Op == 9:
            txt = "Un problème est survenu lors du tri"

        return txt   


# _____________________________________________ MESSAGE SUCCES _____________________________________________ #
    
    def text_msg_succes(Op):
        if Op == 1:
            txt = "Fichiers rennomés avec succès"
        if Op == 2:
            txt = "Elements extrait avec succès"
        if Op == 3:
            txt = "Fichiers triés avec succès"
        if Op == 4:
            txt = "Fichiers triés avec succès"
        if Op == 5:
            txt = "Fichiers triés avec succès"
        if Op == 6:
            txt = "Fichiers triés avec succès"
        if Op == 7:
            txt = "Fichiers triés avec succès"
        if Op == 8:
            txt = "Fichiers triés avec succès"
        if Op == 9:
            txt = "Fichiers triés avec succès"

        return txt   
