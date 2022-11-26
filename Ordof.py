# v1.0 >>> Start interface graphique
# A faire : Renommage par date

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog
from tkinter import messagebox
import glob
import fnmatch
import time
import os

import Info
import Prog_process



# Fenêtre __________________________________________________________________________________________________________________________
wd=Tk()
from Config import CDT
from Config import ICON
wd.title('Ordof')

lrg = 720
htr = 480

wd.geometry('{}x{}'.format(lrg, htr))
wd.resizable(False, False)


wd.config(background=CDT.bg_color)


wd.iconbitmap(ICON.Logo)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                                           CLASS
class Menu:
    def Title(txtT, txtST):
        frame_title = Frame(wd, bg=CDT.bg_color)
        Title = Label(frame_title, text=txtT, font=(CDT.title_caly, CDT.title_size), bg=CDT.bg_color, fg=CDT.fg_color).pack()
        Subtitle = Label(frame_title, text=txtST, font=(CDT.sub_title_caly, CDT.sub_title_size), bg=CDT.bg_color, fg=CDT.fg_color).pack()
        frame_title.pack(side='top', pady=CDT.title_marge)

    


class Anim:
    def BP(can, icon, max, min, text):
        def enter(event):
            can.itemconfig(icon, image=max)
            try:
                text.config(fg=CDT.fg_color)
            except:
                pass

        def leave(event):
            can.itemconfig(icon, image=min)
            try:
                text.config(fg=CDT.bg_color)
            except:
                pass
                
        can.tag_bind(icon, "<Enter>",enter)
        can.tag_bind(icon, "<Leave>",leave)

        


    def Rename_Mode(event, can_p, can_s1, can_s2):
        can_s1.config(highlightthickness=0)
        can_s2.config(highlightthickness=0)
        can_p.config(highlightthickness=1)




    cadre_ext = ['0', '1']
    cadre_name = ['0', '1']
    cadre_date = ['0', '1']

    def Tri_ext(event, can):
        Anim.cadre_ext = (list(reversed(Anim.cadre_ext)))
        cadre = Anim.cadre_ext[0]
        can.config(highlightthickness=cadre)
    
    def Tri_name(event, can):
        Anim.cadre_name = (list(reversed(Anim.cadre_name)))
        cadre = Anim.cadre_name[0]
        can.config(highlightthickness=cadre)

    def Tri_date(event, can):
        Anim.cadre_date = (list(reversed(Anim.cadre_date)))
        cadre = Anim.cadre_date[0]
        can.config(highlightthickness=cadre)

    def Reset_Tri():
        if Anim.cadre_ext == ['1', '0']:
            Anim.cadre_ext = (list(reversed(Anim.cadre_ext)))
        if Anim.cadre_name == ['1', '0']:
            Anim.cadre_name = (list(reversed(Anim.cadre_name)))
        if Anim.cadre_date == ['1', '0']:
            Anim.cadre_date = (list(reversed(Anim.cadre_date)))


class BP_Strd:
    def BP_back(path):
        can_back = Canvas(wd, bg=CDT.bg_color, width=CDT.can_nav_icon, height=CDT.can_nav_icon, highlightthickness=0)
        can_back.pack()
        can_back.place(x=CDT.bp_bk_mrg_x, y=CDT.bp_bk_mrg_y, anchor='nw')
        icon_back = can_back.create_image(CDT.xy_icon_nav, CDT.xy_icon_nav, image=ICON.back_img)
        Anim.BP(can_back, icon_back, ICON.back_img_max, ICON.back_img, 0)
        can_back.tag_bind(icon_back, "<Button-1>", lambda event,arg1 = True: Naviguation.nav_menu(path, event))



    def BP_info(txtST, txtC):
        can_info = Canvas(wd, bg=CDT.bg_color, width=50, height=50, highlightthickness=0)
        can_info.pack()
        can_info.place(x=CDT.bp_info_mrg_x,y=CDT.bp_info_mrg_y, anchor='ne')

        icon_info = can_info.create_image(CDT.xy_icon_nav, CDT.xy_icon_nav, image=ICON.info_img)
        Anim.BP(can_info, icon_info, ICON.info_img_max, ICON.info_img, 0)
        can_info.tag_bind(icon_info, "<Button-1>", lambda event,arg1 = True: Info.WD_info(txtST, txtC))





class Naviguation:
    def nav_menu(path, event):
        for widget in wd.winfo_children():
            widget.destroy()
        wd.resizable(False, False)
        wd.geometry('{}x{}'.format(lrg, htr))
        Prog_process.Mode_Tri.Reset()
        Anim.Reset_Tri()
        try:
            path(event)
        except:
            path()

      
    


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                              Fenêtre 1 >>> Acceuil

def WD_acceuil():
    # Titre __________________________________________________________________________________________________________________________
    Menu.Title("Ordof", "Mettez de l'ordre dans vos fichiers")

    # Canvas __________________________________________________________________________________________________________________________
    lrg = 160
    htr = 160
    can_rename = Canvas(wd, bg=CDT.bg_color, width=lrg, height=htr, highlightthickness=0)
    can_rename.pack()
    can_rename.place(x=100, y=200)

    can_pack = Canvas(wd, bg=CDT.bg_color, width=lrg, height=htr, highlightthickness=0)
    can_pack.pack()
    can_pack.place(x=460, y=200)

    # Texte mode __________________________________________________________________________________________________________________________
    frame_text = Frame(wd, bg=CDT.bg_color)

    text_rename = Label(frame_text, text="Renommer les fichiers", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.bg_color)
    text_rename.grid(row=0, column=0, sticky=W, padx=80)

    text_pack = Label(frame_text, text="Ranger les fichiers", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.bg_color)
    text_pack.grid(row=0, column=1, sticky=W, padx=100)

    frame_text.pack(side='bottom', ipady=20)

    # Selecteur mode __________________________________________________________________________________________________________________________
    def clic_rename(event):
        for widget in wd.winfo_children():
            widget.destroy()
        WD_rename(event)

    icon_rename = can_rename.create_image(lrg/2, htr/2, image=ICON.rename_img)
    Anim.BP(can_rename, icon_rename, ICON.rename_img_max, ICON.rename_img, text_rename)
    can_rename.tag_bind(icon_rename, "<Button-1>", clic_rename)
    

    def clic_pack(event):
        for widget in wd.winfo_children():
            widget.destroy()
        WD_pack(event)

    icon_pack = can_pack.create_image(80, 80, image=ICON.pack_img)
    Anim.BP(can_pack, icon_pack, ICON.pack_img_max, ICON.pack_img, text_pack)
    can_pack.tag_bind(icon_rename, "<Button-1>", clic_pack)



    # Séparateur vertical __________________________________________________________________________________________________________________________
    styl = ttk.Style()
    styl.configure('TSeparator', background=CDT.fg_color)

    ttk.Separator(master=wd,orient=VERTICAL,style='TSeparator').pack(fill=Y, pady=50, expand=True)



    









# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                              Fenêtre 2 >>> Rename

def WD_rename(event):
    
    # Titre __________________________________________________________________________________________________________________________
    Menu.Title("Auto-Rename", "Renomme les fichiers")

    # BP_back __________________________________________________________________________________________________________________________
    BP_Strd.BP_back(WD_acceuil)

    # BP_info __________________________________________________________________________________________________________________________
    BP_Strd.BP_info(CDT.text_subtitle_rename_info, CDT.text_corps_rename_info)

    # PATH_ENTRY __________________________________________________________________________________________________________________________    
    frame_entry = Frame(wd, bg=CDT.bg_color)
     
    text_path = Label(frame_entry, text="Chemin : ", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)
    entry_path = Entry(frame_entry, width=60, bg=CDT.bg_entry)
    
    text_path.grid(row=0, column=0,padx=20, sticky=W)
    entry_path.grid(row=0, column=1,padx=50, sticky=W)
    
    can_browser = Canvas(wd, bg=CDT.bg_color, width=CDT.can_litle_bp_size, height=CDT.can_litle_bp_size, highlightthickness=0)
    can_browser.pack()
    can_browser.place(x= CDT.bp_browser_mrg_x, y=CDT.bp_browser_mrg_y)

    def REP():
        rep_find = filedialog.askdirectory(title="Choisir le répertoire contenant les fichiers")
        entry_path.delete(0, END)
        entry_path.insert(END, rep_find)

    def clic_browser(event):
        REP()

    icon_browser = can_browser.create_image(37.5,37.5, image=ICON.browser_img)
    Anim.BP(can_browser, icon_browser, ICON.browser_img_max, ICON.browser_img, 0)
    can_browser.tag_bind(icon_browser, "<Button-1>",clic_browser)
   
    frame_entry.place(x=CDT.entry_rep_mrg_x, y=CDT.entry_rep_mrg_y)  
    

    # TYPE __________________________________________________________________________________________________________________________    

    frame_type = Frame(wd, bg=CDT.bg_color)

    text_type = Label(frame_type, text="Sélection : ", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)
    text_ext = Label(frame_type, text="Extension", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.bg_color)
    text_name = Label(frame_type, text="Nom", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.bg_color)
    text_all = Label(frame_type, text="Tous", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.bg_color)
    
    can_ext = Canvas(frame_type, bg=CDT.bg_color, width=CDT.can_litle_bp_size, height=CDT.can_litle_bp_size, highlightthickness=0)
    can_name = Canvas(frame_type, bg=CDT.bg_color, width=CDT.can_litle_bp_size, height=CDT.can_litle_bp_size, highlightthickness=0)
    can_all = Canvas(frame_type, bg=CDT.bg_color, width=CDT.can_litle_bp_size, height=CDT.can_litle_bp_size, highlightthickness=0)      

    def EXT(event):
        Anim.Rename_Mode(event, can_ext, can_name, can_all)
        try:
            frame_menu_name.pack_forget()
            frame_menu_ext.pack()
        except: pass

        global rm_mode
        rm_mode = 1
        
        

    def NAME(event):
        Anim.Rename_Mode(event, can_name, can_ext, can_all)
        try:
            frame_menu_ext.pack_forget()
            frame_menu_name.pack()
        except: pass

        global rm_mode
        rm_mode = 2
        

    def ALL(event):
        Anim.Rename_Mode(event, can_all, can_name, can_ext)
        try:
            frame_menu_name.pack_forget()
            frame_menu_ext.pack_forget()
        except: pass

        global rm_mode
        rm_mode = 3

        

    icon_ext = can_ext.create_image(37.5,37.5, image=ICON.ext_img)
    Anim.BP(can_ext, icon_ext, ICON.ext_img_max, ICON.ext_img, text_ext)
    can_ext.tag_bind(icon_ext, "<Button-1>",EXT)

    icon_name = can_name.create_image(37.5,37.5, image=ICON.name_img)
    Anim.BP(can_name, icon_name, ICON.name_img_max, ICON.name_img, text_name)
    can_name.tag_bind(icon_name, "<Button-1>",NAME)

    icon_all = can_all.create_image(37.5,37.5, image=ICON.all_img)
    Anim.BP(can_all, icon_all, ICON.all_img_max, ICON.all_img, text_all)
    can_all.tag_bind(icon_all, "<Button-1>", ALL)

    text_type.grid(row=0, column=0, padx=22, sticky=W)
    text_ext.grid(row=1, column=1, padx=30, sticky=W)
    text_name.grid(row=1, column=2, padx=50, sticky=W)
    text_all.grid(row=1, column=3, padx=53, sticky=W)

    can_ext.grid(row=0, column=1, padx=35, sticky=W)
    can_name.grid(row=0, column=2, padx=35, sticky=W)
    can_all.grid(row=0, column=3, padx=35, sticky=W)

    frame_type.place(x=0, y=200) 


    # SOUS_MENU __________________________________________________________________________________________________________________________    
    frame_sm = Frame(wd, bg=CDT.bg_color)

    frame_menu_ext = Frame(frame_sm, bg=CDT.bg_color)

    text_menu_ext = Label(frame_menu_ext, text="Extension : ", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)
    entry_extension = Entry(frame_menu_ext, width=6, bg=CDT.bg_entry, font=(CDT.text_entry_caly, CDT.text_entry_size))
    text_ext_ex = Label(frame_menu_ext, text='"Exemple : .avi / .jpg"', font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)

    text_menu_ext.grid(row=0, column=0,padx=20, sticky=W)
    entry_extension.grid(row=0, column=1,padx=35, sticky=W)
    text_ext_ex.grid(row=0, column=2,padx=0, sticky=W)

 
    frame_menu_name = Frame(frame_sm, bg=CDT.bg_color)

    text_menu_name = Label(frame_menu_name, text="Nom : ", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)
    entry_name = Entry(frame_menu_name, width=20, bg=CDT.bg_entry, font=(CDT.text_entry_caly, CDT.text_entry_size))
    text_name_ex = Label(frame_menu_name, text='"Nom complet ou incomplet"', font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)

    text_menu_name.grid(row=0, column=0,padx=20, sticky=W)
    entry_name.grid(row=0, column=1,padx=80, sticky=W)
    text_name_ex.grid(row=0, column=2,padx=0, sticky=W)

    frame_sm.place(x=0, y=310)
            


    # NOUVEAU_NOM + SEPARATEUR __________________________________________________________________________________________________________________________    
    frame_new_name = Frame(wd, bg=CDT.bg_color)

    text_new_name = Label(frame_new_name, text="Nouveau nom : ", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)
    entry_new_name = Entry(frame_new_name, width=24, bg=CDT.bg_entry, font=(CDT.text_entry_caly, CDT.text_entry_size))
    text_sep = Label(frame_new_name, text="Séparateur : ", font=(CDT.text_entry_caly, CDT.text_entry_size), bg=CDT.bg_color, fg=CDT.fg_color)
    entry_sep = Entry(frame_new_name, width=3, bg=CDT.bg_entry, font=(CDT.text_caly, CDT.text_size))

    text_new_name.grid(row=0, column=0,padx=20, sticky=W)
    entry_new_name.grid(row=0, column=1,padx=0, sticky=W)
    text_sep.grid(row=0, column=2,padx=10, sticky=W)
    entry_sep.grid(row=0, column=3,padx=0, sticky=W)

    frame_new_name.place(x=0, y=360)

    # BP_GO __________________________________________________________________________________________________________________________
    frame_go = Frame(wd, bg=CDT.bg_color)
    
    text_go = Label(frame_go, text="Rename >>> ", font=(CDT.title_caly, CDT.title_size), bg=CDT.bg_color, fg=CDT.bg_color)
    can_go = Canvas(frame_go, bg=CDT.bg_color, width=CDT.can_litle_bp_size, height=CDT.can_litle_bp_size, highlightthickness=0)


    def clic_go(event):                 # CTRL entry rep __________________________________________________________________
        rep = entry_path.get()  
        if rep == "":
            messagebox.showerror("Information manquante", "Veuillez renseigner le chemin du répertoire")
        else:
            f1 = Prog_process.ctrl_rep(rep)
            if f1 == True :  
                Prog_process.rep = rep                        
                ctrl_mode(rep)
            else:
                pass


    def ctrl_mode(rep):                   # CTRL entry ext __________________________________________________________________
        try:                    
            R_mode = rm_mode
        except:
            pass
        
        if R_mode == 1:
                ext = entry_extension.get()
                if ext == "":
                    messagebox.showerror("Information manquante", "Veuillez renseigner le nom de l'extension à rechercher")
                elif fnmatch.fnmatch(ext, '*.*'):
                    f2 = Prog_process.ctrl_ext(rep, ext)
                    if f2 == True:
                        Prog_process.ext = ext
                        ctrl_Nname()
                else:
                    messagebox.showwarning("Erreur syntaxe", "Veuillez inscrire l'extension avec un point")

        elif R_mode == 2:
            name = entry_name.get()
            if name == "":
                messagebox.showerror("Information manquante", "Veuillez renseigner le nom à rechercher")
            else:
                f3 = Prog_process.ctrl_name(rep, name)
                if f3 == True:
                    ctrl_Nname()
            
        elif R_mode == 3:
            f4 = Prog_process.ctrl_all_files(rep)
            if f4 == True:
                ctrl_Nname()
        
        else:
            messagebox.showerror("Information manquante", "Veuillez choisir un  mode de sélection")

    def ctrl_Nname():                   # CTRL new name __________________________________________________________________
        Nname = entry_new_name.get()    
        if Nname == "":
            messagebox.showerror("Information manquante", "Veuillez renseigner le nouveau nom")
        else:
            f5 = Prog_process.ctrl_Nname(Nname)
            if f5 == True:
                Prog_process.Nname = Nname
                ctrl_sep()
    

    def ctrl_sep():                     # CTRL sep __________________________________________________________________
        sep = entry_sep.get()
        if sep == "":
            sep = " "
       
        f6 = Prog_process.ctrl_sep(sep)
        if f6 == True:
            Prog_process.sep = sep
            Confirm()
                
                


    icon_go = can_go.create_image(37.5,37.5, image=ICON.go_img)
    Anim.BP(can_go, icon_go, ICON.go_img_max, ICON.go_img, text_go)
    can_go.tag_bind(icon_go, "<Button-1>", lambda event,arg1 = True: clic_go(event))

    text_go.grid(row=0, column=0, padx=40, sticky=W)
    can_go.grid(row=0, column=1, padx=20, sticky=W)

    frame_go.place(x=155, y=390)




    def Confirm():
        R_mode = rm_mode
        F_list = (Prog_process.files_list)
        nbrE = str(len(F_list))
        Op = 1

        Prog_process.rename_list = F_list

        for widget in wd.winfo_children():
            widget.destroy()

        WD_confirm(Op, nbrE, F_list, R_mode, WD_rename)

    
    















# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                              Fenêtre 3 >>> Marshal_files

def WD_pack(event):
    # Titre __________________________________________________________________________________________________________________________
    Menu.Title("Mashal-files", "Tri ou extrait les fichiers")
   
    # BP_back __________________________________________________________________________________________________________________________
    BP_Strd.BP_back(WD_acceuil)

    # Canvas __________________________________________________________________________________________________________________________
    lrg = 160
    htr = 160
    can_tri = Canvas(wd, bg=CDT.bg_color, width=lrg, height=htr, highlightthickness=0)
    can_tri.pack()
    can_tri.place(x=100, y=200)

    can_extract = Canvas(wd, bg=CDT.bg_color, width=lrg, height=htr, highlightthickness=0)
    can_extract.pack()
    can_extract.place(x=460, y=200)

    # Texte mode __________________________________________________________________________________________________________________________
    frame_text = Frame(wd, bg=CDT.bg_color)

    text_tri = Label(frame_text, text="Trier les fichiers", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.bg_color)
    text_tri.grid(row=0, column=0, sticky=W, padx=100)

    text_extract = Label(frame_text, text="Extraire les fichiers", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.bg_color)
    text_extract.grid(row=0, column=1, sticky=W, padx=120)

    frame_text.pack(side='bottom', ipady=20)

    # Selecteur mode __________________________________________________________________________________________________________________________

    def clic_tri(event):
        for widget in wd.winfo_children():
            widget.destroy()
        WD_tri(event)


    icon_tri = can_tri.create_image(lrg/2, htr/2, image=ICON.tri_img)
    Anim.BP(can_tri, icon_tri, ICON.tri_img_max, ICON.tri_img, text_tri)
    can_tri.tag_bind(icon_tri, "<Button-1>", clic_tri)
    

    def clic_extract(event):
        for widget in wd.winfo_children():
            widget.destroy()
        WD_extract(event)

    icon_extract = can_extract.create_image(80, 80, image=ICON.extract_img)
    Anim.BP(can_extract, icon_extract, ICON.extract_img_max, ICON.extract_img, text_extract)
    can_extract.tag_bind(icon_extract, "<Button-1>", clic_extract)


    # Séparateur vertical __________________________________________________________________________________________________________________________
    styl = ttk.Style()
    styl.configure('TSeparator', background=CDT.fg_color)

    ttk.Separator(master=wd,orient=VERTICAL,style='TSeparator').pack(fill=Y, pady=50, expand=True)



















# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                              Fenêtre 4 >>> Tri fichiers
def WD_tri(event):
    wd.geometry('720x720')

    # Titre __________________________________________________________________________________________________________________________
    Menu.Title("Mode tri", "Tri et range les fichiers dans des sous-dossiers")

    # BP_back __________________________________________________________________________________________________________________________
    BP_Strd.BP_back(WD_pack)    
    
    # BP_info __________________________________________________________________________________________________________________________

    # PATH_ENTRY __________________________________________________________________________________________________________________________    
    frame_entry = Frame(wd, bg=CDT.bg_color)
     
    text_path = Label(frame_entry, text="Chemin : ", bg=CDT.bg_color, fg=CDT.fg_color, font=(CDT.text_caly, CDT.text_size))
    entry_path = Entry(frame_entry, width=60, bg=CDT.bg_entry)
    
    text_path.grid(row=0, column=0,padx=20, sticky=W)
    entry_path.grid(row=0, column=1,padx=50, sticky=W)
    
    can_browser = Canvas(wd, bg=CDT.bg_color, width=CDT.can_litle_bp_size, height=CDT.can_litle_bp_size, highlightthickness=0)
    can_browser.pack()
    can_browser.place(x= CDT.bp_browser_mrg_x, y=CDT.bp_browser_mrg_y)

    def REP():
        rep_find = filedialog.askdirectory(title="Choisir le répertoire contenant les fichiers")
        entry_path.delete(0, END)
        entry_path.insert(END, rep_find)

    def clic_browser(event):
        REP()

    icon_browser = can_browser.create_image(37.5,37.5, image=ICON.browser_img)
    Anim.BP(can_browser, icon_browser, ICON.browser_img_max, ICON.browser_img, 0)
    can_browser.tag_bind(icon_browser, "<Button-1>",clic_browser)
   
    frame_entry.place(x=CDT.entry_rep_mrg_x, y=CDT.entry_rep_mrg_y) 


    # TYPE __________________________________________________________________________________________________________________________    

    frame_type = Frame(wd, bg=CDT.bg_color)

    text_type = Label(frame_type, text="Tri : ", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)
    text_ext = Label(frame_type, text="Extension", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.bg_color)
    text_name = Label(frame_type, text="Nom", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.bg_color)
    text_all = Label(frame_type, text="Date", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.bg_color)
    
    can_ext = Canvas(frame_type, bg=CDT.bg_color, width=CDT.can_litle_bp_size, height=CDT.can_litle_bp_size, highlightthickness=0)
    can_name = Canvas(frame_type, bg=CDT.bg_color, width=CDT.can_litle_bp_size, height=CDT.can_litle_bp_size, highlightthickness=0)
    can_date = Canvas(frame_type, bg=CDT.bg_color, width=CDT.can_litle_bp_size, height=CDT.can_litle_bp_size, highlightthickness=0)   

    def Num_tri(mode, rep):
        number_tri = (int(Prog_process.Mode_Tri.tri_ext)+int(Prog_process.Mode_Tri.tri_name)+int(Prog_process.Mode_Tri.tri_date))
        Get_final_num(number_tri, mode, rep)




    def Get_final_num(number_tri, mode, rep):
        if number_tri == 3:                         # ___ Ext uniquement
            if mode == 1:
                try:
                    frame_sm_date.pack_forget()
                except: pass
            elif mode == 2:
                cd = ctrl_isFiles(rep)
                if cd == True:
                    Confirm(3)
                

        if number_tri == 5:                         # ___ Nom uniquement
            if mode == 1:
                try:
                    frame_sm_date.pack_forget()
                except: pass
            elif mode == 2:
                cd = ctrl_isFiles(rep)
                if cd == True:
                    Confirm(4)

        if number_tri == 7:                         # ___ Date uniquement
            if mode == 1:
                try:
                    frame_sm_date.pack(anchor='nw',pady=CDT.sous_menu_mrg_y)
                except: pass
            elif mode == 2:
                cd = ctrl_isFiles(rep)
                if cd == True:
                    Confirm(5)

        if number_tri == 8:                         # ___ Ext + Nom
            if mode == 1:
                try:
                    frame_sm_date.pack_forget()
                except: pass
            elif mode == 2:
                cd = ctrl_isFiles(rep)
                if cd == True:
                    Confirm(6)

        if number_tri == 10:                         # ___ Ext + Date
            if mode == 1:
                try:
                    frame_sm_date.pack(anchor='nw',pady=CDT.sous_menu_mrg_y)
                except: pass
            elif mode == 2:
                cd = ctrl_isFiles(rep)
                if cd == True:
                    Confirm(7)

        if number_tri == 12:                         # ___ Nom + Date
            if mode == 1:
                try:
                    frame_sm_date.pack(anchor='nw',pady=CDT.sous_menu_mrg_y)
                except: pass
            elif mode == 2:
                cd = ctrl_isFiles(rep)
                if cd == True:
                    Confirm(8)

        if number_tri == 15:                         # ___ Ext + Nom + Date
            if mode == 1:
                try:
                    frame_sm_date.pack(anchor='nw',pady=CDT.sous_menu_mrg_y)
                except: pass
            elif mode == 2:
                cd = ctrl_isFiles(rep)
                if cd == True:
                    Confirm(9)

        if number_tri == 0:
            if mode == 1:
                try:
                    frame_sm_date.pack_forget()
                except: pass
            elif mode == 2:
                messagebox.showerror("Information manquante", "Veuillez choisir un  mode de tri")


    def EXT(event):
        Anim.Tri_ext(event, can_ext)
        Prog_process.Mode_Tri.Tri_ext()
        Num_tri(1, 0)
       
    def NAME(event):
        Anim.Tri_name(event, can_name)
        Prog_process.Mode_Tri.Tri_name()
        Num_tri(1, 0)

    def DATE(event):
        Anim.Tri_date(event, can_date)
        Prog_process.Mode_Tri.Tri_date()
        Num_tri(1, 0)
        
        
    icon_ext = can_ext.create_image(37.5,37.5, image=ICON.ext_img)
    Anim.BP(can_ext, icon_ext, ICON.ext_img_max, ICON.ext_img, text_ext)
    can_ext.tag_bind(icon_ext, "<Button-1>",EXT)

    icon_name = can_name.create_image(37.5,37.5, image=ICON.name_img)
    Anim.BP(can_name, icon_name, ICON.name_img_max, ICON.name_img, text_name)
    can_name.tag_bind(icon_name, "<Button-1>",NAME)

    icon_all = can_date.create_image(37.5,37.5, image=ICON.all_img)
    Anim.BP(can_date, icon_all, ICON.all_img_max, ICON.all_img, text_all)
    can_date.tag_bind(icon_all, "<Button-1>", DATE)

    text_type.grid(row=0, column=0, padx=49, sticky=W)
    text_ext.grid(row=1, column=1, padx=30, sticky=W)
    text_name.grid(row=1, column=2, padx=50, sticky=W)
    text_all.grid(row=1, column=3, padx=53, sticky=W)

    can_ext.grid(row=0, column=1, padx=35, sticky=W)
    can_name.grid(row=0, column=2, padx=35, sticky=W)
    can_date.grid(row=0, column=3, padx=35, sticky=W)

    frame_type.place(x=0, y=200) 




# SOUS_MENU __________________________________________________________________________________________________________________________    
    frame_sm = Frame(wd, bg=CDT.bg_color)
    
    # MENU DATE___________________________________________
    frame_sm_date = Frame(frame_sm, bg=CDT.bg_color)
    text_menu_date = Label(frame_sm_date, text="Tri part : ", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)
    
    text_annee = Label(frame_sm_date, text="Année", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.bg_color)
    text_mois = Label(frame_sm_date, text="Mois", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.bg_color)
    text_jour = Label(frame_sm_date, text="Jour", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.bg_color)
    
    can_annee = Canvas(frame_sm_date, bg=CDT.bg_color, width=CDT.can_litle_bp_size, height=CDT.can_litle_bp_size, highlightthickness=1)
    can_mois = Canvas(frame_sm_date, bg=CDT.bg_color, width=CDT.can_litle_bp_size, height=CDT.can_litle_bp_size, highlightthickness=1)
    can_jour = Canvas(frame_sm_date, bg=CDT.bg_color, width=CDT.can_litle_bp_size, height=CDT.can_litle_bp_size, highlightthickness=1)      

    icon_ext = can_annee.create_image(37.5,37.5, image=ICON.info_img)
    Anim.BP(can_annee, icon_ext, ICON.info_img_max, ICON.info_img, text_annee)
    # can_ext.tag_bind(icon_ext, "<Button-1>",EXT)

    icon_name = can_mois.create_image(37.5,37.5, image=ICON.info_img)
    Anim.BP(can_mois, icon_name, ICON.info_img_max, ICON.info_img, text_mois)
    # can_name.tag_bind(icon_name, "<Button-1>",NAME)

    icon_all = can_jour.create_image(37.5,37.5, image=ICON.info_img)
    Anim.BP(can_jour, icon_all, ICON.info_img_max, ICON.info_img, text_jour)
    # can_all.tag_bind(icon_all, "<Button-1>", ALL)


    text_menu_date.grid(row=0, column=0, padx=20, sticky=W)
    text_annee.grid(row=1, column=1, padx=60, sticky=W)
    text_mois.grid(row=1, column=2, padx=30, sticky=W)
    text_jour.grid(row=1, column=3, padx=65, sticky=W)

    can_annee.grid(row=0, column=1, padx=53, sticky=W)
    can_mois.grid(row=0, column=2, padx=18, sticky=W)
    can_jour.grid(row=0, column=3, padx=50, sticky=W)


    frame_sm.place(x=0, y=310)


    # NOM SOUS-DOSSIER __________________________________________________________________________________________________________________________    
    frame_new_name = Frame(wd, bg=CDT.bg_color)

    text_new_name = Label(frame_new_name, text="Nom sous-dossiers : ", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)
    entry_new_name = Entry(frame_new_name, width=24, bg=CDT.bg_entry, font=(CDT.text_entry_caly, CDT.text_entry_size))
    text_new_name_ex = Label(frame_new_name, text="(Facultatif)", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)
    
    text_new_name.grid(row=0, column=0,padx=20, sticky=W)
    entry_new_name.grid(row=0, column=1,padx=0, sticky=W)
    text_new_name_ex.grid(row=0, column=2,padx=10, sticky=W)
    
    frame_new_name.place(x=0, y=550)


    # BP_GO __________________________________________________________________________________________________________________________
    frame_go = Frame(wd, bg=CDT.bg_color)
    
    text_go = Label(frame_go, text="Trier >>> ", font=(CDT.title_caly, CDT.title_size), bg=CDT.bg_color, fg=CDT.bg_color)
    can_go = Canvas(frame_go, bg=CDT.bg_color, width=CDT.can_litle_bp_size, height=CDT.can_litle_bp_size, highlightthickness=0)

    def clic_go(event):
        rep = entry_path.get()  
        if rep == "":
            messagebox.showerror("Information manquante", "Veuillez renseigner le chemin du répertoire")
        else:
            f1 = Prog_process.ctrl_rep(rep)
            if f1 == True :  
                Prog_process.rep = rep   
                Num_tri(2, rep)                     
            else:
                pass              

    
    def ctrl_isFiles(rep):
        f4 = Prog_process.ctrl_all_files(rep)
        if f4 == True:
            return True



    def Confirm(Op):
        F_list = (Prog_process.files_list)
        nbrE = str(len(F_list))

        Prog_process.rename_list = F_list

        for widget in wd.winfo_children():
            widget.destroy()

        WD_confirm(Op, nbrE, F_list, 0, WD_tri)




    icon_go = can_go.create_image(37.5,37.5, image=ICON.go_img)
    Anim.BP(can_go, icon_go, ICON.go_img_max, ICON.go_img, text_go)
    can_go.tag_bind(icon_go, "<Button-1>", lambda event,arg1 = True: clic_go(event))

    text_go.grid(row=0, column=0, padx=40, sticky=W)
    can_go.grid(row=0, column=1, padx=20, sticky=W)

    frame_go.pack(side='bottom', pady=20)




















# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                              Fenêtre 5 >>> Extract fichiers
def WD_extract(event):

    # Titre __________________________________________________________________________________________________________________________
    Menu.Title("Mode extraction", "Extrait les fichiers des sous-dossiers")
    
    # BP_back __________________________________________________________________________________________________________________________
    BP_Strd.BP_back(WD_pack)
    
    # BP_info __________________________________________________________________________________________________________________________
    BP_Strd.BP_info(CDT.text_subtitle_depack_info, CDT.text_corps_depack_info)

    # PATH_ENTRY __________________________________________________________________________________________________________________________    
    frame_entry = Frame(wd, bg=CDT.bg_color)
     
    text_path = Label(frame_entry, text="Chemin : ", bg=CDT.bg_color, fg=CDT.fg_color, font=(CDT.text_caly, CDT.text_size))
    entry_path = Entry(frame_entry, width=60, bg=CDT.bg_entry)
    
    text_path.grid(row=0, column=0,padx=20, sticky=W)
    entry_path.grid(row=0, column=1,padx=50, sticky=W)
    
    can_browser = Canvas(wd, bg=CDT.bg_color, width=CDT.can_litle_bp_size, height=CDT.can_litle_bp_size, highlightthickness=0)
    can_browser.pack()
    can_browser.place(x= CDT.bp_browser_mrg_x, y=CDT.bp_browser_mrg_y)

    def REP():
        rep_find = filedialog.askdirectory(title="Choisir le répertoire contenant les fichiers")
        entry_path.delete(0, END)
        entry_path.insert(END, rep_find)

    def clic_browser(event):
        REP()

    icon_browser = can_browser.create_image(37.5,37.5, image=ICON.browser_img)
    Anim.BP(can_browser, icon_browser, ICON.browser_img_max, ICON.browser_img, 0)
    can_browser.tag_bind(icon_browser, "<Button-1>",clic_browser)
   
    frame_entry.place(x=CDT.entry_rep_mrg_x, y=CDT.entry_rep_mrg_y) 


    # DEGRE __________________________________________________________________________________________________________________________
    frame_degre = Frame(wd, bg=CDT.bg_color)

    text_degre = Label(frame_degre, text="Degré : ", bg=CDT.bg_color, fg=CDT.fg_color, font=(CDT.text_caly, CDT.text_size))
    entry_degre = Entry(frame_degre, width=4, bg=CDT.bg_entry, font=(CDT.text_caly, CDT.text_size))
    text_ex_degre = Label(frame_degre, text="1,2,3... ALL pour tous", bg=CDT.bg_color, fg=CDT.fg_color, font=(CDT.text_caly, CDT.text_size))

    text_degre.grid(row=0,column=0,padx=20, sticky=W)
    entry_degre.grid(row=0,column=1,padx=65, sticky=W)
    text_ex_degre.grid(row=0,column=2,padx=10, sticky=W)

    frame_degre.place(x=0, y=220)
    
    # BP_GO __________________________________________________________________________________________________________________________
    frame_go = Frame(wd, bg=CDT.bg_color)
    
    text_go = Label(frame_go, text="Extract >>> ", font=(CDT.title_caly, CDT.title_size), bg=CDT.bg_color, fg=CDT.bg_color)
    can_go = Canvas(frame_go, bg=CDT.bg_color, width=CDT.can_litle_bp_size, height=CDT.can_litle_bp_size, highlightthickness=0)

    def clic_go(event):
        rep = entry_path.get()  
        if rep == "":
            messagebox.showerror("Information manquante", "Veuillez renseigner le chemin du répertoire")
        else:
            f1 = Prog_process.ctrl_rep(rep)
            if f1 == True :  
                deg = entry_degre.get()
                ctrl_deg(rep, deg)
            else:
                pass

    def ctrl_deg(rep, deg):
        f1 = Prog_process.ctrl_deg(deg)
        if f1 == True:
            if deg == 'ALL' or deg == 'all':
                deg = 100
                Prog_process.rep = rep
                Depack(deg, rep)

            else:
                deg = int(deg)
                Prog_process.rep = rep
                Depack(deg, rep)
            

        
        
    def Depack(deg, rep):
        def check_err(rep):
            Op = 2
            err_list = Prog_process.err_list
            if (err_list) != []:
                nbrErr = str(len(err_list))
                for widget in wd.winfo_children():
                    widget.destroy()
                wd.resizable(False, False)
                wd.geometry('{}x{}'.format(lrg, htr))
                err_list.append('\n')
                err_list.append("Erreur   >>>   Plusieurs fichiers ou dossiers ont le même nom...")
                err_report(err_list, nbrErr, Op, WD_extract)
            else:
                files_extract_list = os.listdir(rep)
                nbrE = str(len(files_extract_list))
                Depack_ok(nbrE)


        def Depack_ok(nbrE):
            tpsOp = round(((time.time())-Prog_process.tps), 4)
            ms = round((tpsOp*1000), 3)
            if tpsOp >= 1:
                Ntime = "secondes"
            if tpsOp < 1:
                tpsOp = ms
                Ntime = "millisecondes"
            
            messagebox.showinfo("Succès", '''{}   Elements extrait avec succès
            Temps de l'opération : {} {}'''.format(nbrE, tpsOp, Ntime))

            Naviguation.nav_menu(WD_extract, 0)

        Prog_process.Depack(deg)
        check_err(rep)



    icon_go = can_go.create_image(37.5,37.5, image=ICON.go_img)
    Anim.BP(can_go, icon_go, ICON.go_img_max, ICON.go_img, text_go)
    can_go.tag_bind(icon_go, "<Button-1>", lambda event,arg1 = True: clic_go(event))

    text_go.grid(row=0, column=0, padx=40, sticky=W)
    can_go.grid(row=0, column=1, padx=20, sticky=W)

    frame_go.place(x=155, y=390)















# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                                  Fenêtre confirmation

def WD_confirm(Op, nbrE, F_list, R_mode, back):
        
    # Titre __________________________________________________________________________________________________________________________
    frame_title_confirm_R = Frame(wd, bg=CDT.bg_color)
    Title = Label(frame_title_confirm_R, text="Confirmation", font=(CDT.title_caly, CDT.title_size), bg=CDT.bg_color, fg=CDT.fg_color).pack()
    frame_title_confirm_R.pack(side='top', pady=CDT.title_marge)

    # BP_back __________________________________________________________________________________________________________________________
    BP_Strd.BP_back(back)

    # Indication elements __________________________________________________________________________________________________________________________
    frame_elements = Frame(wd, bg=CDT.bg_color)
    nbr_elements = Label(frame_elements, text=nbrE, font=(CDT.text_big_caly, CDT.text_big_size), bg=CDT.bg_color, fg=CDT.fg_color)
    label_elements = Label(frame_elements, text=CDT.text_label_elements(Op), font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)
    nbr_elements.grid(row=0,column=0,padx=20,sticky=W)
    label_elements.grid(row=0,column=1,padx=20,sticky=W)
    frame_elements.pack(pady=5)

    # Files_list __________________________________________________________________________________________________________________________
    frame_files_list = Frame(wd, bg=CDT.bg_color)
    can_files_list = Canvas(frame_files_list, bg=CDT.bg_color, highlightthickness=0,width=(lrg-250), height=(htr-250))

    hbar = Scrollbar(frame_files_list, orient=VERTICAL, repeatinterval=100)
    hbar.pack(side='right', fill='y')
    
    text_F_list = Text(can_files_list, wrap=WORD, bg=CDT.bg_color, fg=CDT.fg_color, font=(CDT.text_list_caly, CDT.text_list_size), highlightthickness=0, yscrollcommand=hbar.set)
    for el in F_list:
        text_F_list.insert(INSERT,' '+ el + '\n')
    text_F_list.pack()
    text_F_list.config(yscrollcommand=hbar.set)
    
    hbar.config(command=text_F_list.yview)

    can_files_list.pack(side='left')
    frame_files_list.pack()

    text_F_list.update()
    htr_txt = round(text_F_list.winfo_height())
    htr_wd = htr_txt + 350
    if htr_wd > 1920:
        htr_wd = 1920

    wd.geometry('620x{}+5+5'.format(htr_wd))
    can_files_list.config(height=htr_txt)
    
    

    # BP Confirm __________________________________________________________________________________________________________________________
    frame_go = Frame(wd, bg=CDT.bg_color)
    
    text_go = Label(frame_go, text=CDT.text_go(Op), font=(CDT.title_caly, CDT.title_size), bg=CDT.bg_color, fg=CDT.bg_color)
    can_go = Canvas(frame_go, bg=CDT.bg_color, width=CDT.can_litle_bp_size, height=CDT.can_litle_bp_size, highlightthickness=0)

    def clic_go(event):
        def check_err():
            err_list = Prog_process.err_list
            if (err_list) != []:
                nbrErr = str(len(err_list))
                for widget in wd.winfo_children():
                    widget.destroy()
                wd.resizable(False, False)
                wd.geometry('{}x{}'.format(lrg, htr))
                err_report(err_list, nbrErr, Op, WD_rename)
            else:
                rename_ok()

        def rename_ok():
            tpsOp = round(((time.time())-Prog_process.tps), 4)
            ms = round((tpsOp*1000), 3)
            if tpsOp >= 1:
                Ntime = "secondes"
            if tpsOp < 1:
                tpsOP = ms
                Ntime = "millisecondes"
            
            messagebox.showinfo("Succès", '''{}   Fichiers rennomés avec succès
            Temps de l'opération : {} {}'''.format(nbrE, tpsOp, Ntime))

            Naviguation.nav_menu(WD_acceuil, 0)


        if R_mode == 1:
            Prog_process.Rename_ext()
            check_err()
            

        if R_mode == 2:
            Prog_process.Rename_name()
            check_err()
           

        if R_mode == 3:
            Prog_process.Rename_all()
            check_err()
            



        if Op == 3:
            Prog_process.Tri_ext()
            # check_err()
        if Op == 4:
            Prog_process.Tri_name()
            # check_err()
        if Op == 5:
            Prog_process.Tri_date()
            # check_err()
        if Op == 6:
            Prog_process.Tri_ext_name()
            # check_err()
        if Op == 7:
            Prog_process.Tri_ext_date()
            # check_err()
        if Op == 8:
            Prog_process.Tri_name_date()
            # check_err()
        if Op == 9:
            Prog_process.Tri_ext_name_date()
            # check_err()

    icon_go = can_go.create_image(37.5,37.5, image=ICON.go_img)
    Anim.BP(can_go, icon_go, ICON.go_img_max, ICON.go_img, text_go)
    can_go.tag_bind(icon_go, "<Button-1>", lambda event,arg1 = True: clic_go(event))

    text_go.grid(row=0, column=0, padx=40, sticky=W)
    can_go.grid(row=0, column=1, padx=20, sticky=W)

    frame_go.pack(side='bottom', pady=20)



















# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                                  Rapport erreur rename

def err_report(err_list, nbrErr, Op, back):

    # Titre __________________________________________________________________________________________________________________________
    frame_title_confirm_R = Frame(wd, bg=CDT.bg_color)
    Title = Label(frame_title_confirm_R, text="Erreur", font=(CDT.title_caly, CDT.title_size), bg=CDT.bg_color, fg=CDT.fg_color).pack()
    frame_title_confirm_R.pack(side='top', pady=CDT.title_marge)

    # Indication elements __________________________________________________________________________________________________________________________
    frame_elements = Frame(wd, bg=CDT.bg_color)
    nbr_elements = Label(frame_elements, text=nbrErr, font=(CDT.text_big_caly, CDT.text_big_size), bg=CDT.bg_color, fg=CDT.fg_color)
    label_elements = Label(frame_elements, text=CDT.text_label_error(Op), font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)
    nbr_elements.grid(row=0,column=0,padx=20,sticky=W)
    label_elements.grid(row=0,column=1,padx=20,sticky=W)
    frame_elements.pack(pady=5)

    # Liste erreur __________________________________________________________________________________________________________________________
    frame_err = Frame(wd, bg=CDT.bg_color)
    can_err = Canvas(frame_err, bg=CDT.bg_color, highlightthickness=0,width=(lrg-250), height=(htr-250))

    hbar = Scrollbar(frame_err, orient=VERTICAL, repeatinterval=100)
    hbar.pack(side='right', fill='y')
    
    text_err_list = Text(can_err, wrap=WORD, bg=CDT.bg_color, fg=CDT.fg_color, font=(CDT.text_list_caly, CDT.text_list_size), highlightthickness=0, yscrollcommand=hbar.set)
    for el in err_list:
        text_err_list.insert(INSERT,' '+ el + '\n')
    text_err_list.pack()
    text_err_list.config(yscrollcommand=hbar.set)
    
    hbar.config(command=text_err_list.yview)

    can_err.pack(side='left')
    frame_err.pack()

    text_err_list.update()
    htr_txt = round(text_err_list.winfo_height())
    htr_wd = htr_txt + 350
    if htr_wd > 1920:
        htr_wd = 1920

    wd.geometry('620x{}+5+5'.format(htr_wd))
    can_err.config(height=htr_txt)


    # BP Goback __________________________________________________________________________________________________________________________
    frame_goback = Frame(wd, bg=CDT.bg_color)
    
    text_goback = Label(frame_goback, text="Retour", font=(CDT.title_caly, CDT.title_size), bg=CDT.bg_color, fg=CDT.bg_color)
    can_goback = Canvas(frame_goback, bg=CDT.bg_color, width=CDT.can_litle_bp_size, height=CDT.can_litle_bp_size, highlightthickness=0)

    icon_go = can_goback.create_image(37.5,37.5, image=ICON.goback_img)
    Anim.BP(can_goback, icon_go, ICON.goback_img_max, ICON.goback_img, text_goback)
    can_goback.tag_bind(icon_go, "<Button-1>", lambda event,arg1 = True: Naviguation.nav_menu(back, event))

    can_goback.grid(row=0, column=0, padx=20, sticky=W)
    text_goback.grid(row=0, column=1, padx=40, sticky=W)
    
    frame_goback.pack(side='bottom', pady=20)

    messagebox.showwarning("Erreur", CDT.text_msg_error(Op))


WD_acceuil()
# Affichage __________________________________________________________________________________________________________________________
wd.mainloop()










