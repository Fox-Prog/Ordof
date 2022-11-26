import os
import fnmatch
import time
import glob
import sys
from tkinter import messagebox
import shutil
import exifread

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
        files_list = []
        all_list = glob.glob(R_ext)
        for el in all_list:
            nfc = os.path.join(rep, el)
            if os.path.isfile(nfc):
                files_list.append(el)

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


def ctrl_deg(deg):             # ___________________________________________________________________________ CTRL deg
    if deg == 'ALL' or deg == 'all':
        return True
    
    try:
        int(deg)
        return True
    except:
        messagebox.showerror("Erreur", "Degré = nombre ou ALL")


    



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                              RENAME

rep = ""
ext = ""
Nname = ""
sep = ""

rename_list = []

def Init_Op():
    os.chdir(rep)
    global tps
    tps = time.time()
    global err_list
    err_list = []



def Rename_ext():          # ___________________________________________________________________________ Rename ext
    Init_Op()
    nbr = 1

    for el in rename_list:
        try:
            nfc = os.path.join(rep, el)
            os.rename(nfc, os.path.join(rep, Nname+sep+str(nbr)+' '+ext))
            nbr = nbr+1
        except:
            err_list.append(el)
    


def Rename_name():      # ___________________________________________________________________________ Rename name
    Init_Op()
    nbr = 1

    for el in rename_list:
        try:
            txt = str(el)
            nfc = os.path.join(rep, el)
            split_ext = txt.split(".")
            os.rename(nfc, os.path.join(rep, Nname+sep+str(nbr)+'.'+str(split_ext[1])))
            nbr = nbr+1
        except:
            err_list.append(el)



def Rename_all():       # ___________________________________________________________________________ Rename all
    Init_Op()
    nbr = 1

    for el in rename_list:
        try :
            txt = str(el)
            nfc = os.path.join(rep, el)
            split_ext = txt.split(".")
            os.rename(nfc, os.path.join(rep, Nname+sep+str(nbr)+'.'+str(split_ext[1])))
            # nbr = nbr+1
        except:
            err_list.append(el)



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                              DEPACK

def Depack(deg):
    Init_Op()
    for i in range(deg):
        all_rep = os.listdir()
        for doss in all_rep:
            if os.path.isdir(doss):
                os.chdir(doss)
                files_SD = os.listdir()
                for el in files_SD:
                    try:
                        shutil.move(rep+'/'+doss+'/'+el, rep)
                    except:
                        if el not in err_list:
                            err_list.append(el)
                        pass
                
                os.chdir(rep)
                try:
                    os.rmdir(rep+'/'+doss)
                except:
                    pass




# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                              TRI

class Mode_Tri:
    T_ext_mode = ['0', '3']
    T_name_mode = ['0', '5']
    T_date_mode = ['0', '7']

    tri_ext = 0
    tri_name = 0
    tri_date = 0

    def Tri_ext():
        Mode_Tri.T_ext_mode = (list(reversed(Mode_Tri.T_ext_mode)))
        Mode_Tri.tri_ext = Mode_Tri.T_ext_mode[0]

    def Tri_name():
        Mode_Tri.T_name_mode = (list(reversed(Mode_Tri.T_name_mode)))
        Mode_Tri.tri_name = Mode_Tri.T_name_mode[0]


    def Tri_date():
        Mode_Tri.T_date_mode = (list(reversed(Mode_Tri.T_date_mode)))
        Mode_Tri.tri_date = Mode_Tri.T_date_mode[0]

    def Reset():
        if Mode_Tri.tri_ext == '3':
            Mode_Tri.T_ext_mode = (list(reversed(Mode_Tri.T_ext_mode)))
            Mode_Tri.tri_ext = 0
        if Mode_Tri.tri_name == '5':
            Mode_Tri.T_name_mode = (list(reversed(Mode_Tri.T_name_mode)))
            Mode_Tri.tri_name = 0
        if Mode_Tri.tri_date == '7':
            Mode_Tri.T_date_mode = (list(reversed(Mode_Tri.T_date_mode)))
            Mode_Tri.tri_date = 0



def Tri_ext():        # ___________________________________________________________________________ Tri ext
    Init_Op()
    


def Tri_name():        # ___________________________________________________________________________ Tri name
    print("tri name")


def Tri_date():        # ___________________________________________________________________________ Tri date
    print("tri date")


def Tri_ext_name():        # ___________________________________________________________________________ Tri ext + name
    print("tri ext name")


def Tri_ext_date():        # ___________________________________________________________________________ Tri ext + date
    print("tri ext date")


def Tri_name_date():        # ___________________________________________________________________________ Tri name + date
    print("tri name date")

def Tri_ext_name_date():        # ___________________________________________________________________________ Tri ext + name + date
    print("tri ext name date")