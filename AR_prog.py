import os
import fnmatch
import time
import glob
import sys
from tkinter import messagebox

# _____________________________________________ Contrôle répértoire valide _____________________________________________ #

def ctrl_rep(rep):
    ver = glob.glob(rep)
    if ver == []:                          
        messagebox.showwarning("Erreur", "Répertoire introuvable")
