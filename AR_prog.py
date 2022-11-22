import os
import fnmatch
import time
import glob
import sys
from tkinter import messagebox

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                              Contrôle des entrées


def ctrl_rep(rep):      # ___________________________________________________________________________ CTRL REP
    ver = glob.glob(rep)
    if ver == []:                          
        messagebox.showwarning("Erreur", "Répertoire introuvable")
    else:
        return True


def ctrl_ext(rep, ext):  # ___________________________________________________________________________ CTRL EXT
        R_ext = ("*"+ext)

        os.chdir(rep)
        global files_list
        files_list = glob.glob(R_ext)
        if files_list == []:
            messagebox.showwarning("Erreur", "Aucun fichiers trouvés avec cette extension")            
        else:
            return True


def ctrl_name(rep, name): # ___________________________________________________________________________ CTRL NAME & FILES
    os.chdir(rep)

    global files_list
    files_list=[]

    files = os.listdir()
    found_files=[]

    for nom in files:
        nfc = os.path.join(rep, nom)
        if os.path.isfile(nfc):
            found_files.append(nom)
    
    for el in found_files:
        esc_set=("*"+glob.escape(name)+"*")
        if fnmatch.fnmatch(el, esc_set):
            files_list.append(el)
            
    if files_list == []:
        messagebox.showwarning("Erreur", "Aucun fichiers trouvés avec ce nom")
    else:
        return True

def ctrl_all_files(rep):   # ___________________________________________________________________________ CTRL ALL is FILES
        os.chdir(rep)
        files = os.listdir()

        global files_list
        files_list=[]

        for nom in files:
            nfc = os.path.join(rep, nom)
            if os.path.isfile(nfc):
                files_list.append(nom)
        
        if files_list == []:
            messagebox.showwarning("Erreur", "Aucun fichiers trouvés dans ce répertoire")
        else:
            return True


def ctrl_Nname(Nname):           # ___________________________________________________________________________ CTRL New Name
    syb_list=['*.*', '*\\*', '*/*', '*:*', '*>*', '*<*']
    for el in syb_list:
        if fnmatch.fnmatch(Nname, el):
            messagebox.showerror("Erreur nouveau nom", "Symbole interdit >>> ( . \\  / ? : * > < )")
            return False
        else:
            return True
            

def ctrl_sep(sep):           # ___________________________________________________________________________ CTRL Sep
    syb_list=['*.*', '*\\*', '*/*', '*:*', '*>*', '*<*']
    for el in syb_list:
        if fnmatch.fnmatch(sep, el):
            messagebox.showerror("Erreur séparateur", "Symbole interdit >>> ( . \\  / ? : * > < )")
        else:
            return True