# v1.0 >>> Start interface graphique

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog
from tkinter import messagebox
import glob
import fnmatch
import time


import WD_secondary
import AR_prog



# Fenêtre __________________________________________________________________________________________________________________________
wd=Tk()
from Config import CDT
from Config import ICON
wd.title('Ordof')
wd.geometry('720x480')
wd.resizable(False, False)


wd.config(background=CDT.bg_color)


wd.iconbitmap(ICON.Logo)


# CLASS __________________________________________________________________________________________________________________________

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


    def clic_back(path, event):
        for widget in wd.winfo_children():
            widget.destroy()
        try:
            path(event)
        except:
            path()

        
    def Rename_Mode(event, can_p, can_s1, can_s2):
        can_s1.config(highlightthickness=0)
        can_s2.config(highlightthickness=0)
        can_p.config(highlightthickness=1)



        
    




# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                              Fenêtre 1 >>> Acceuil

def WD_acceuil():
    # Titre __________________________________________________________________________________________________________________________
    frame_title = Frame(wd, bg=CDT.bg_color)
    Title = Label(frame_title, text="Bienvenue dans Ordof", font=(CDT.title_caly, CDT.title_size), bg=CDT.bg_color, fg=CDT.fg_color).pack()
    Subtitle = Label(frame_title, text="Mettez de l'ordre dans vos fichiers", font=(CDT.sub_title_caly, CDT.sub_title_size), bg=CDT.bg_color, fg=CDT.fg_color).pack()
    frame_title.pack(side=TOP, pady=CDT.title_marge)

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

    frame_text.pack(side=BOTTOM, ipady=20)

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
    frame_title = Frame(wd, bg=CDT.bg_color)
    Title = Label(frame_title, text="Auto-Rename", font=(CDT.title_caly, CDT.title_size), bg=CDT.bg_color, fg=CDT.fg_color).pack()
    Subtitle = Label(frame_title, text="Renomme les fichiers automatiquement", font=(CDT.sub_title_caly, CDT.sub_title_size), bg=CDT.bg_color, fg=CDT.fg_color).pack()
    frame_title.pack(side=TOP, pady=CDT.title_marge)

    # BP_back __________________________________________________________________________________________________________________________
    can_back = Canvas(wd, bg=CDT.bg_color, width=CDT.can_nav_icon, height=CDT.can_nav_icon, highlightthickness=0)
    can_back.pack()
    can_back.place(x=CDT.bp_bk_mrg_x, y=CDT.bp_bk_mrg_y, anchor='nw')

    icon_back = can_back.create_image(CDT.xy_icon_nav, CDT.xy_icon_nav, image=ICON.back_img)
    Anim.BP(can_back, icon_back, ICON.back_img_max, ICON.back_img, 0)
    can_back.tag_bind(icon_back, "<Button-1>", lambda event,arg1 = True: Anim.clic_back(WD_acceuil, 0))

    # BP_info __________________________________________________________________________________________________________________________
    can_info = Canvas(wd, bg=CDT.bg_color, width=50, height=50, highlightthickness=0)
    can_info.pack()
    can_info.place(x=CDT.bp_info_mrg_x,y=CDT.bp_info_mrg_y, anchor='ne')

    icon_info = can_info.create_image(CDT.xy_icon_nav, CDT.xy_icon_nav, image=ICON.info_img)
    Anim.BP(can_info, icon_info, ICON.info_img_max, ICON.info_img, 0)
    can_info.tag_bind(icon_info, "<Button-1>", lambda event,arg1 = True: WD_secondary.WD_info(CDT.text_subtitle_rename_info, CDT.text_corps_rename_info))


    # PATH_ENTRY __________________________________________________________________________________________________________________________    
    frame_entry = Frame(wd, bg=CDT.bg_color)
     
    text_path = Label(frame_entry, text="Chemin : ", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)
    entry_path = Entry(frame_entry, width=60, bg=CDT.bg_entry)
    
    text_path.grid(row=0, column=0,padx=20, sticky=W)
    entry_path.grid(row=0, column=1,padx=50, sticky=W)
    
    can_browser = Canvas(wd, bg=CDT.bg_color, width=CDT.can_litle_bp_size, height=CDT.can_litle_bp_size, highlightthickness=0)
    can_browser.pack()
    can_browser.place(x= 610, y=135)

    def REP():
        rep_find = filedialog.askdirectory(title="Choisir le répertoire contenant les fichiers")
        entry_path.delete(0, END)
        entry_path.insert(END, rep_find)

    def clic_browser(event):
        REP()

    icon_browser = can_browser.create_image(37.5,37.5, image=ICON.browser_img)
    Anim.BP(can_browser, icon_browser, ICON.browser_img_max, ICON.browser_img, 0)
    can_browser.tag_bind(icon_browser, "<Button-1>",clic_browser)
   
    frame_entry.place(x=0, y=160) 
    

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
    entry_extension = Entry(frame_menu_ext, width=8, bg=CDT.bg_entry)
    text_ext_ex = Label(frame_menu_ext, text='"Exemple : .avi / .jpg"', font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)

    text_menu_ext.grid(row=0, column=0,padx=20, sticky=W)
    entry_extension.grid(row=0, column=1,padx=35, sticky=W)
    text_ext_ex.grid(row=0, column=2,padx=0, sticky=W)

 
    frame_menu_name = Frame(frame_sm, bg=CDT.bg_color)

    text_menu_name = Label(frame_menu_name, text="Nom : ", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)
    entry_name = Entry(frame_menu_name, width=20, bg=CDT.bg_entry)
    text_name_ex = Label(frame_menu_name, text='"Nom complet ou incomplet"', font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)

    text_menu_name.grid(row=0, column=0,padx=20, sticky=W)
    entry_name.grid(row=0, column=1,padx=78, sticky=W)
    text_name_ex.grid(row=0, column=2,padx=0, sticky=W)

    frame_sm.place(x=0, y=310)
            


    # NOUVEAU_NOM + SEPARATEUR __________________________________________________________________________________________________________________________    
    frame_new_name = Frame(wd, bg=CDT.bg_color)

    text_new_name = Label(frame_new_name, text="Nouveau nom : ", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)
    entry_new_name = Entry(frame_new_name, width=30, bg=CDT.bg_entry)
    text_sep = Label(frame_new_name, text="Séparateur : ", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)
    entry_sep = Entry(frame_new_name, width=6, bg=CDT.bg_entry)

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
            f1 = AR_prog.ctrl_rep(rep)
            if f1 == True :                          
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
                    f2 = AR_prog.ctrl_ext(rep, ext)
                    if f2 == True:
                        print(AR_prog.files_list)
                        ctrl_Nname()
                else:
                    messagebox.showwarning("Erreur syntaxe", "Veuillez inscrire l'extension avec un point")

        elif R_mode == 2:
            name = entry_name.get()
            if name == "":
                messagebox.showerror("Information manquante", "Veuillez renseigner le nom à rechercher")
            else:
                f3 = AR_prog.ctrl_name(rep, name)
                if f3 == True:
                    print(AR_prog.files_list)
                    ctrl_Nname()
            
        elif R_mode == 3:
            f4 = AR_prog.ctrl_all_files(rep)
            if f4 == True:
                print(AR_prog.files_list)
                ctrl_Nname()
        
        else:
            messagebox.showerror("Information manquante", "Veuillez choisir un  mode de sélection")

    def ctrl_Nname():                   # CTRL new name __________________________________________________________________
        Nname = entry_new_name.get()    
        if Nname == "":
            messagebox.showerror("Information manquante", "Veuillez renseigner le nouveau nom")
        else:
            f5 = AR_prog.ctrl_Nname(Nname)
            if f5 == True:
                ctrl_sep()
    

    def ctrl_sep():                     # CTRL sep __________________________________________________________________
        sep = entry_sep.get()
        if sep == "":
            messagebox.showerror("Information manquante", "Veuillez indiquer le séparateur à utiliser")
        else:
            f6 = AR_prog.ctrl_sep(sep)
            if f6 == True:
                Confirm()
                
                
                
    
    # Listes des fichiers à rennomer : AR_prog.files_list


    icon_go = can_go.create_image(37.5,37.5, image=ICON.go_img)
    Anim.BP(can_go, icon_go, ICON.go_img_max, ICON.go_img, text_go)
    can_go.tag_bind(icon_go, "<Button-1>", lambda event,arg1 = True: clic_go(event))

    text_go.grid(row=0, column=0, padx=40, sticky=W)
    can_go.grid(row=0, column=1, padx=20, sticky=W)

    frame_go.place(x=155, y=390)




    def Confirm():
        frame_go.destroy()

        nbrF = str(len(AR_prog.files_list))
        F_list = []
        for el in AR_prog.files_list:
            F_list.append(el)
            
        print(F_list)
        WD_secondary.WD_confirm_R(nbrF, F_list)

    
    






# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                              Fenêtre 3 >>> Marshal_files

def WD_pack(event):
    # Titre __________________________________________________________________________________________________________________________
    frame_title = Frame(wd, bg=CDT.bg_color)
    Title = Label(frame_title, text="Mashal-files", font=(CDT.title_caly, CDT.title_size), bg=CDT.bg_color, fg=CDT.fg_color).pack()
    Subtitle = Label(frame_title, text="Tri et range les fichiers automatiquement", font=(CDT.sub_title_caly, CDT.sub_title_size), bg=CDT.bg_color, fg=CDT.fg_color).pack()
    Subtitle_2 = Label(frame_title, text="Extrait les fichiers des sous-dossiers vers le dossier principal", font=(CDT.sub_title_caly, CDT.sub_title_size), bg=CDT.bg_color, fg=CDT.fg_color).pack()
    frame_title.pack(side=TOP, pady=CDT.title_marge)
   
    # BP_back __________________________________________________________________________________________________________________________
    can_back = Canvas(wd, bg=CDT.bg_color, width=CDT.can_nav_icon, height=CDT.can_nav_icon, highlightthickness=0)
    can_back.pack()
    can_back.place(x=CDT.bp_bk_mrg_x, y=CDT.bp_bk_mrg_y, anchor='nw')

    icon_back = can_back.create_image(CDT.xy_icon_nav, CDT.xy_icon_nav, image=ICON.back_img)
    Anim.BP(can_back, icon_back, ICON.back_img_max, ICON.back_img, 0)
    can_back.tag_bind(icon_back, "<Button-1>", lambda event,arg1 = True: Anim.clic_back(WD_acceuil, 0))    




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

    frame_text.pack(side=BOTTOM, ipady=20)

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
    # Titre __________________________________________________________________________________________________________________________
    frame_title = Frame(wd, bg=CDT.bg_color)
    Title = Label(frame_title, text="Mode tri", font=(CDT.title_caly, CDT.title_size), bg=CDT.bg_color, fg=CDT.fg_color).pack()
    frame_title.pack(side=TOP, pady=CDT.title_marge)

    # BP_back __________________________________________________________________________________________________________________________
    can_back = Canvas(wd, bg=CDT.bg_color, width=CDT.can_nav_icon, height=CDT.can_nav_icon, highlightthickness=0)
    can_back.pack()
    can_back.place(x=CDT.bp_bk_mrg_x, y=CDT.bp_bk_mrg_y, anchor='nw')

    icon_back = can_back.create_image(CDT.xy_icon_nav, CDT.xy_icon_nav, image=ICON.back_img)
    Anim.BP(can_back, icon_back, ICON.back_img_max, ICON.back_img, 0)
    can_back.tag_bind(icon_back, "<Button-1>", lambda event,arg1 = True: Anim.clic_back(WD_pack, event))    
  














# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                              Fenêtre 5 >>> Extract fichiers
def WD_extract(event):
    # Titre __________________________________________________________________________________________________________________________
    frame_title = Frame(wd, bg=CDT.bg_color)
    Title = Label(frame_title, text="Mode extraction", font=(CDT.title_caly, CDT.title_size), bg=CDT.bg_color, fg=CDT.fg_color).pack()
    frame_title.pack(side=TOP, pady=CDT.title_marge)
    
    # BP_back __________________________________________________________________________________________________________________________
    can_back = Canvas(wd, bg=CDT.bg_color, width=CDT.can_nav_icon, height=CDT.can_nav_icon, highlightthickness=0)
    can_back.pack()
    can_back.place(x=CDT.bp_bk_mrg_x, y=CDT.bp_bk_mrg_y, anchor='nw')

    icon_back = can_back.create_image(CDT.xy_icon_nav, CDT.xy_icon_nav, image=ICON.back_img)
    Anim.BP(can_back, icon_back, ICON.back_img_max, ICON.back_img, 0)
    can_back.tag_bind(icon_back, "<Button-1>", lambda event,arg1 = True: Anim.clic_back(WD_pack, event))    
  


WD_acceuil()
# Affichage __________________________________________________________________________________________________________________________
wd.mainloop()










