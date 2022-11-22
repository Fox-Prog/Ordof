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

    # _____________________________________________ INFO _____________________________________________ #

    # Auto_rename
    text_subtitle_rename_info = "Guide Auto-Rename"
    text_corps_rename_info = '''
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
        
    '''