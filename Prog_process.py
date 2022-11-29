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
        all_list = []
        all_list = glob.glob(R_ext)
        for el in all_list:
            nfc = os.path.join(rep, el)
            if os.path.isfile(nfc):
                files_list.append(el)

        if files_list == []:
            messagebox.showwarning("Erreur", "Aucun fichiers trouvés avec cette extension")            
        else:
            return True


def ctrl_ext_flag(ext_flag): # ___________________________________________________________________________ CTRL EXT FLAG --> _flag+date
    R_ext = ("*"+ext_flag)

    global files_list
    files_list = []
    all_list = []
    all_list = glob.glob(R_ext)
    for el in all_list:
        files_list.append(el)


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
#                                                              TOOLS


rep = ""
ext = ""
Nname = ""
SDname = ""
sep = ""
name = ""
M_date = ""

rename_list = []

global target_list

def Init_Op():
    os.chdir(rep)

    global date_list
    date_list = []

    global ext_flag_list
    ext_flag_list = []

    global tps
    tps = time.time()

    global err_list
    err_list = []


def Init_inter_flag():
    global date_list
    date_list = []


def Mode_date(JJ,MM,AA, M_date):
    list_mois=['0', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',]

    if MM in list_mois:
        MM = str(list_mois.index(MM)).zfill(2)

    if M_date == 1:
        OD=(AA)
        return OD
    
    if M_date == 2:
        OD=(MM+'-'+AA)
        return OD
    
    if M_date == 3:
        OD=(JJ+'-'+MM+'-'+AA)
        return OD






# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                              RENAME

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
            nbr = nbr+1
        except:
            err_list.append(el)



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                              DEPACK

supp_SD = ""

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
                if supp_SD == '1':
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
        if Mode_Tri.T_ext_mode == ['3', '0']:
            Mode_Tri.T_ext_mode = (list(reversed(Mode_Tri.T_ext_mode)))
            Mode_Tri.tri_ext = 0
        if Mode_Tri.T_name_mode == ['5', '0']:
            Mode_Tri.T_name_mode = (list(reversed(Mode_Tri.T_name_mode)))
            Mode_Tri.tri_name = 0
        if Mode_Tri.T_date_mode == ['7', '0']:
            Mode_Tri.T_date_mode = (list(reversed(Mode_Tri.T_date_mode)))
            Mode_Tri.tri_date = 0







def Find_date(el, M_date):
    im = open(el, 'rb')
    try:                        # >>> Tentative d'extraction date de prise de vue dans la méta-donnée
        dateNF=str((exifread.process_file(im)['EXIF DateTimeOriginal']))
        JJ=(dateNF[8:-9])
        MM=(dateNF[5:-12])
        AA=(dateNF[:-15])
        OD = Mode_date(JJ, MM, AA, M_date)
        date_list.append(OD)
    except:                     # >>> Si méta-donnée inexistante, extraction de la date de modification du fichier
        dateNF=str((time.ctime(os.path.getmtime(el))))
        JJ=(dateNF[8:-14])
        MM=(dateNF[4:-17])
        AA=(dateNF[20:])
        OD = Mode_date(JJ, MM, AA, M_date)
        date_list.append(OD)
    im.close()



def Copy_date_element(el, M_date):
    im = open(el, 'rb')
    try:                        # >>> Tentative d'extraction date de prise de vue dans la méta-donnée
        dateNF=str((exifread.process_file(im)['EXIF DateTimeOriginal']))
        JJ=(dateNF[8:-9])
        MM=(dateNF[5:-12])
        AA=(dateNF[:-15])
        OD = Mode_date(JJ, MM, AA, M_date)
        date_copy = str(OD)
    except:                     # >>> Si méta-donnée inexistante, extraction de la date de modification du fichier
        dateNF=str((time.ctime(os.path.getmtime(el))))
        JJ=(dateNF[8:-14])
        MM=(dateNF[4:-17])
        AA=(dateNF[20:])
        OD = Mode_date(JJ, MM, AA, M_date)
        date_copy = str(OD)
    im.close()

    return date_copy






def Tri_ext():        # ___________________________________________________________________________ Tri ext
    Init_Op()
    for el in files_list:   # ___ Create SD
        txt = str(el)
        split_ext = txt.split(".")
        try:
            os.mkdir(SDname+str(split_ext[1]))
        except: pass

    for el in files_list:   # ___ Copy
        txt = str(el)
        split_ext = txt.split(".")
        try:
            target = (rep+'/'+SDname+str(split_ext[1]))
            shutil.move(rep+'/'+el, target)
        except:
            err_list.append(el)




def Tri_name():        # ___________________________________________________________________________ Tri name
    Init_Op() 
    try:    # ___ Create SD
        os.mkdir(SDname+name)
    except: pass
    
    for el in files_list:   # ___ Copy
        try:
            target = (rep+'/'+SDname+name)
            shutil.move(rep+'/'+el, target)
        except:
            err_list.append(el)



def Tri_date():        # ___________________________________________________________________________ Tri date
    Init_Op()

    for el in files_list:
        Find_date(el, M_date)

    for date in date_list:        # ___ Create SD
        try:
            os.mkdir(SDname+date) 
        except:
            pass


    for el in files_list:       # ___ Copy
        date_copy = Copy_date_element(el, M_date)
        try:
            target=(rep+'/'+SDname+date_copy)
            shutil.move(rep+'/'+el, target)
        except:
            err_list.append(el)
    

    




def Tri_ext_name():        # ___________________________________________________________________________ Tri ext + nom
    Init_Op()
    for el in files_list:   # ___ Create SD
        txt = str(el)
        split_ext = txt.split(".")
        try:
            os.mkdir(SDname+name+' - '+str(split_ext[1]))
        except: pass

    for el in files_list:   # ___ Copy
        txt = str(el)
        split_ext = txt.split(".")
        try:
            target = (rep+'/'+SDname+name+' - '+str(split_ext[1]))
            shutil.move(rep+'/'+el, target)
        except:
            err_list.append(el)





def Tri_ext_date():        # ___________________________________________________________________________ Tri ext + date
    Init_Op()

    for el in files_list:               # ___ Recup des flag (type d'extension presente dans le dossier)
        txt = str(el)
        split_ext = txt.split(".")
        ext_flag = ("."+split_ext[1])

        if ext_flag not in ext_flag_list:
            ext_flag_list.append(ext_flag)


    for els in ext_flag_list:              
        Init_inter_flag()

        ctrl_ext_flag(els)

        for el in files_list:               # ___ ID Date
            Find_date(el, M_date)

        for date in date_list:              # ___ Create SD
            try:
                os.mkdir(SDname+ date+' - '+els[1:])
            except: pass

        for el in files_list:               # ___ Copy
            date_copy = Copy_date_element(el, M_date)
            try:
                target=(rep+'/'+SDname+ date_copy+' - '+els[1:])
                shutil.move(rep+'/'+el, target)
            except:
                err_list.append(el)


        




def Tri_name_date():        # ___________________________________________________________________________ Tri name + date
    Init_Op()

    for el in files_list:
        Find_date(el, M_date)

    for date in date_list:        # ___ Create SD
        try:
            os.mkdir(SDname+name+' - '+date) 
        except: pass

    
    for el in files_list:       # ___ Copy
        date_copy = Copy_date_element(el, M_date)
        try:
            target=(rep+'/'+SDname+name+' - '+date_copy)
            shutil.move(rep+'/'+el, target)
        except:
            err_list.append(el)





def Tri_ext_name_date():        # ___________________________________________________________________________ Tri ext + name + date
    print("tri ext name date")

