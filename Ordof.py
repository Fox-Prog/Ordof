# v1.0 >>> Start interface graphique

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog
import time
import Config


# Ressources __________________________________________________________________________________________________________________________

Logo = 'C:\\Users\\Utilisateur\\Documents\\Programmation\\PYTHON\\Gestion_de_fichiers\\Ordof\\Ressources\\Logo.ico'

# Fenêtre __________________________________________________________________________________________________________________________
wd=Tk()
wd.title('Ordof')
wd.geometry('720x480')
wd.resizable(False, False)
wd.config(background=Config.bg_color)
wd.iconbitmap(Logo)

# Ressources __________________________________________________________________________________________________________________________
rename_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Rename_logo.png")
rename_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Rename_logo_max.png")
pack_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Pack_logo.png")
pack_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Pack_logo_max.png")

back_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Back_logo.png")
back_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Back_logo_max.png")

browser_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Browser_logo.png")
browser_img_max = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/Browser_logo_max.png")

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








# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                              Fenêtre 1 >>> Acceuil

def WD_acceuil():
    # Titre __________________________________________________________________________________________________________________________
    frame_title = Frame(wd, bg=Config.bg_color)
    Title = Label(frame_title, text="Bienvenue dans Ordof", font=(Config.title_caly, Config.title_size), bg=Config.bg_color, fg=Config.fg_color).pack()
    Subtitle = Label(frame_title, text="Mettez de l'ordre dans vos fichiers", font=(Config.sub_title_caly, Config.sub_title_size), bg=Config.bg_color, fg=Config.fg_color).pack()
    frame_title.pack(side=TOP, pady=Config.title_marge)
    # Canvas __________________________________________________________________________________________________________________________
    lrg = 160
    htr = 160
    can_rename = Canvas(wd, bg=Config.bg_color, width=lrg, height=htr, highlightthickness=0)
    can_rename.pack()
    can_rename.place(x=100, y=200)

    can_pack = Canvas(wd, bg=Config.bg_color, width=lrg, height=htr, highlightthickness=0)
    can_pack.pack()
    can_pack.place(x=460, y=200)

    # Selecteur mode __________________________________________________________________________________________________________________________
    def enter_rename(event):
        can_rename.itemconfig(icon_rename, image=rename_img_max)
        text_rename.config(fg=Config.fg_color)
    def leave_rename(event):
        can_rename.itemconfig(icon_rename, image=rename_img)
        text_rename.config(fg=Config.bg_color)
    def clic_rename(event):
        for widget in wd.winfo_children():
            widget.destroy()
        WD_rename(event)


    icon_rename = can_rename.create_image(lrg/2, htr/2, image=rename_img)
    can_rename.tag_bind(icon_rename, "<Enter>", enter_rename)
    can_rename.tag_bind(icon_rename, "<Leave>", leave_rename)
    can_rename.tag_bind(icon_rename, "<Button-1>", clic_rename)
    

    def enter_pack(event):
        can_pack.itemconfig(icon_pack, image=pack_img_max)
        text_pack.config(fg=Config.fg_color)    
    def leave_pack(event):
        can_pack.itemconfig(icon_pack, image=pack_img)
        text_pack.config(fg=Config.bg_color)
    def clic_pack(event):
        for widget in wd.winfo_children():
            widget.destroy()
        WD_pack(event)

    icon_pack = can_pack.create_image(80, 80, image=pack_img)
    can_pack.tag_bind(icon_pack, "<Enter>", enter_pack)
    can_pack.tag_bind(icon_pack, "<Leave>", leave_pack)
    can_pack.tag_bind(icon_rename, "<Button-1>", clic_pack)



    # Séparateur vertical __________________________________________________________________________________________________________________________
    styl = ttk.Style()
    styl.configure('TSeparator', background=Config.fg_color)

    ttk.Separator(master=wd,orient=VERTICAL,style='TSeparator').pack(fill=Y, pady=50, expand=True)



    # Texte mode __________________________________________________________________________________________________________________________
    frame_text = Frame(wd, bg=Config.bg_color)

    text_rename = Label(frame_text, text="Renommer les fichiers", font=(Config.text_caly, Config.text_size), bg=Config.bg_color, fg=Config.bg_color)
    text_rename.grid(row=0, column=0, sticky=W, padx=80)

    text_pack = Label(frame_text, text="Ranger les fichiers", font=(Config.text_caly, Config.text_size), bg=Config.bg_color, fg=Config.bg_color)
    text_pack.grid(row=0, column=1, sticky=W, padx=100)

    frame_text.pack(side=BOTTOM, ipady=20)










# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                              Fenêtre 2 >>> Rename

def WD_rename(event):
    # Titre __________________________________________________________________________________________________________________________
    frame_title = Frame(wd, bg=Config.bg_color)
    Title = Label(frame_title, text="Auto-Rename", font=(Config.title_caly, Config.title_size), bg=Config.bg_color, fg=Config.fg_color).pack()
    Subtitle = Label(frame_title, text="Renomme les fichiers automatiquement", font=(Config.sub_title_caly, Config.sub_title_size), bg=Config.bg_color, fg=Config.fg_color).pack()
    frame_title.pack(side=TOP, pady=Config.title_marge)

    # Canvas_back __________________________________________________________________________________________________________________________
    can_back = Canvas(wd, bg=Config.bg_color, width=50, height=50, highlightthickness=0)
    can_back.pack()
    can_back.place(x=Config.bp_bk_mrg_x, y=Config.bp_bk_mrg_y, anchor='nw')

    # BP_back __________________________________________________________________________________________________________________________
    def enter_back(event):
        can_back.itemconfig(icon_back, image=back_img_max)
    def leave_back(event):
        can_back.itemconfig(icon_back, image=back_img)
    def clic_back(event):
        for widget in wd.winfo_children():
            widget.destroy()
        WD_acceuil()

    icon_back = can_back.create_image(20, 20, image=back_img)
    can_back.tag_bind(icon_back, "<Enter>", enter_back)
    can_back.tag_bind(icon_back, "<Leave>", leave_back)
    can_back.tag_bind(icon_back, "<Button-1>", clic_back)    

    # PATH_ENTRY __________________________________________________________________________________________________________________________    
    frame_entry = Frame(wd, bg=Config.bg_color)

    def REP():
        rep_find = filedialog.askdirectory(title="Choisir le répertoire contenant les fichiers")
        path.delete(0, END)
        path.insert(END, rep_find)
        
    text_path = Label(frame_entry, text="Chemin : ", font=(Config.text_caly, Config.text_size), bg=Config.bg_color, fg=Config.fg_color)
    path = Entry(frame_entry, width=Config.entry_rep_lrg)
    
    text_path.grid(row=0, column=0,padx=20, sticky=W)
    path.grid(row=0, column=1,padx=20, sticky=W)
    
    can_browser = Canvas(wd, bg=Config.bg_color, width=Config.can_litle_bp_size, height=Config.can_litle_bp_size, highlightthickness=0)
    can_browser.pack()
    can_browser.place(x= 580, y=135)

    def enter_browser(event):
        can_browser.itemconfig(icon_browser, image=browser_img_max)
    def leave_browser(event):
        can_browser.itemconfig(icon_browser, image=browser_img)
    def clic_browser(event):
        REP()

    icon_browser = can_browser.create_image(37.5,37.5, image=browser_img)
    can_browser.tag_bind(icon_browser, "<Enter>",enter_browser)    
    can_browser.tag_bind(icon_browser, "<Leave>",leave_browser)
    can_browser.tag_bind(icon_browser, "<Button-1>",clic_browser)
   
    frame_entry.pack(side=TOP)
    frame_entry.place(x=0, y=160) 
    

    # TYPE __________________________________________________________________________________________________________________________    
    frame_type = Frame(wd, bg=Config.bg_color)

    text_type = Label(frame_type, text="Sélection : ", font=(Config.text_caly, Config.text_size), bg=Config.bg_color, fg=Config.fg_color)
    text_ext = Label(frame_type, text="Extension", font=(Config.text_caly, Config.text_size), bg=Config.bg_color, fg=Config.bg_color)
    text_name = Label(frame_type, text="Nom", font=(Config.text_caly, Config.text_size), bg=Config.bg_color, fg=Config.bg_color)
    text_all = Label(frame_type, text="Tous", font=(Config.text_caly, Config.text_size), bg=Config.bg_color, fg=Config.bg_color)
    
    can_ext = Canvas(frame_type, bg=Config.bg_color, width=Config.can_litle_bp_size, height=Config.can_litle_bp_size, highlightthickness=0)
    can_name = Canvas(frame_type, bg=Config.bg_color, width=Config.can_litle_bp_size, height=Config.can_litle_bp_size, highlightthickness=0)
    can_all = Canvas(frame_type, bg=Config.bg_color, width=Config.can_litle_bp_size, height=Config.can_litle_bp_size, highlightthickness=0)
   
    def enter_ext(event):
        can_ext.itemconfig(icon_ext, image=ext_img_max)
        text_ext.config(fg=Config.fg_color)
    def leave_ext(event):
        can_ext.itemconfig(icon_ext, image=ext_img)
        text_ext.config(fg=Config.bg_color)

    def enter_name(event):
        can_name.itemconfig(icon_name, image=name_img_max)
        text_name.config(fg=Config.fg_color)
    def leave_name(event):
        can_name.itemconfig(icon_name, image=name_img)
        text_name.config(fg=Config.bg_color)

    def enter_all(event):
        can_all.itemconfig(icon_all, image=all_img_max)
        text_all.config(fg=Config.fg_color)
    def leave_all(event):
        can_all.itemconfig(icon_all, image=all_img)
        text_all.config(fg=Config.bg_color)

    icon_ext = can_ext.create_image(37.5,37.5, image=ext_img)
    can_ext.tag_bind(icon_ext, "<Enter>", enter_ext)
    can_ext.tag_bind(icon_ext, "<Leave>", leave_ext)
    #can_ext.tag_bind(icon_ext, "<Button-1>", clic_ext)

    icon_name = can_name.create_image(37.5,37.5, image=name_img)
    can_name.tag_bind(icon_name, "<Enter>", enter_name)
    can_name.tag_bind(icon_name, "<Leave>", leave_name)
    #can_name.tag_bind(icon_name, "<Button-1>", clic_name)

    icon_all = can_all.create_image(37.5,37.5, image=all_img)
    can_all.tag_bind(icon_all, "<Enter>", enter_all)
    can_all.tag_bind(icon_all, "<Leave>", leave_all)
    #can_all.tag_bind(icon_all, "<Button-1>", clic_all)

    text_type.grid(row=0, column=0, padx=20, sticky=W)
    text_ext.grid(row=1, column=1, padx=20, sticky=W)
    text_name.grid(row=1, column=2, padx=45, sticky=W)
    text_all.grid(row=1, column=3, padx=45, sticky=W)

    can_ext.grid(row=0, column=1, padx=28, sticky=W)
    can_name.grid(row=0, column=2, padx=28, sticky=W)
    can_all.grid(row=0, column=3, padx=28, sticky=W)

    frame_type.pack(side=TOP)
    frame_type.place(x=0, y=240) 

    # rep = path.get()
    
    






# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                              Fenêtre 3 >>> Marshal_files

def WD_pack(event):
    # Titre __________________________________________________________________________________________________________________________
    frame_title = Frame(wd, bg=Config.bg_color)
    Title = Label(frame_title, text="Mashal-files", font=(Config.title_caly, Config.title_size), bg=Config.bg_color, fg=Config.fg_color).pack()
    Subtitle = Label(frame_title, text="Tri et range les fichiers automatiquement", font=(Config.sub_title_caly, Config.sub_title_size), bg=Config.bg_color, fg=Config.fg_color).pack()
    Subtitle_2 = Label(frame_title, text="Extrait les fichiers des sous-dossiers vers le dossier principal", font=(Config.sub_title_caly, Config.sub_title_size), bg=Config.bg_color, fg=Config.fg_color).pack()
    frame_title.pack(side=TOP, pady=Config.title_marge)

    # Canvas_back __________________________________________________________________________________________________________________________
    can_back = Canvas(wd, bg=Config.bg_color, width=50, height=50, highlightthickness=0)
    can_back.pack()
    can_back.place(x=Config.bp_bk_mrg_x, y=Config.bp_bk_mrg_y, anchor='nw')

    # BP_back __________________________________________________________________________________________________________________________
    def enter_back(event):
        can_back.itemconfig(icon_back, image=back_img_max)
    def leave_back(event):
        can_back.itemconfig(icon_back, image=back_img)
    def clic_back(event):
        for widget in wd.winfo_children():
            widget.destroy()
        WD_acceuil()

    icon_back = can_back.create_image(20, 20, image=back_img)
    can_back.tag_bind(icon_back, "<Enter>", enter_back)
    can_back.tag_bind(icon_back, "<Leave>", leave_back)
    can_back.tag_bind(icon_back, "<Button-1>", clic_back)




    # Canvas __________________________________________________________________________________________________________________________
    lrg = 160
    htr = 160
    can_tri = Canvas(wd, bg=Config.bg_color, width=lrg, height=htr, highlightthickness=0)
    can_tri.pack()
    can_tri.place(x=100, y=200)

    can_extract = Canvas(wd, bg=Config.bg_color, width=lrg, height=htr, highlightthickness=0)
    can_extract.pack()
    can_extract.place(x=460, y=200)

    # Selecteur mode __________________________________________________________________________________________________________________________
    def enter_tri(event):
        can_tri.itemconfig(icon_tri, image=tri_img_max)
        text_tri.config(fg=Config.fg_color)
    def leave_tri(event):
        can_tri.itemconfig(icon_tri, image=tri_img)
        text_tri.config(fg=Config.bg_color)
    def clic_tri(event):
        for widget in wd.winfo_children():
            widget.destroy()
        WD_tri(event)


    icon_tri = can_tri.create_image(lrg/2, htr/2, image=tri_img)
    can_tri.tag_bind(icon_tri, "<Enter>", enter_tri)
    can_tri.tag_bind(icon_tri, "<Leave>", leave_tri)
    can_tri.tag_bind(icon_tri, "<Button-1>", clic_tri)
    

    def enter_extract(event):
        can_extract.itemconfig(icon_extract, image=extract_img_max)
        text_extract.config(fg=Config.fg_color)    
    def leave_extract(event):
        can_extract.itemconfig(icon_extract, image=extract_img)
        text_extract.config(fg=Config.bg_color)
    def clic_extract(event):
        for widget in wd.winfo_children():
            widget.destroy()
        WD_extract(event)

    icon_extract = can_extract.create_image(80, 80, image=extract_img)
    can_extract.tag_bind(icon_extract, "<Enter>", enter_extract)
    can_extract.tag_bind(icon_extract, "<Leave>", leave_extract)
    can_extract.tag_bind(icon_extract, "<Button-1>", clic_extract)



    # Séparateur vertical __________________________________________________________________________________________________________________________
    styl = ttk.Style()
    styl.configure('TSeparator', background=Config.fg_color)

    ttk.Separator(master=wd,orient=VERTICAL,style='TSeparator').pack(fill=Y, pady=50, expand=True)



    # Texte mode __________________________________________________________________________________________________________________________
    frame_text = Frame(wd, bg=Config.bg_color)

    text_tri = Label(frame_text, text="Trier les fichiers", font=(Config.text_caly, Config.text_size), bg=Config.bg_color, fg=Config.bg_color)
    text_tri.grid(row=0, column=0, sticky=W, padx=100)

    text_extract = Label(frame_text, text="Extraire les fichiers", font=(Config.text_caly, Config.text_size), bg=Config.bg_color, fg=Config.bg_color)
    text_extract.grid(row=0, column=1, sticky=W, padx=120)

    frame_text.pack(side=BOTTOM, ipady=20)

















# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                              Fenêtre 4 >>> Tri fichiers
def WD_tri(event):
    # Titre __________________________________________________________________________________________________________________________
    frame_title = Frame(wd, bg=Config.bg_color)
    Title = Label(frame_title, text="Mode tri", font=(Config.title_caly, Config.title_size), bg=Config.bg_color, fg=Config.fg_color).pack()
    frame_title.pack(side=TOP, pady=Config.title_marge)

     # Canvas_back __________________________________________________________________________________________________________________________
    can_back = Canvas(wd, bg=Config.bg_color, width=50, height=50, highlightthickness=0)
    can_back.pack()
    can_back.place(x=Config.bp_bk_mrg_x, y=Config.bp_bk_mrg_y, anchor='nw')

    # BP_back __________________________________________________________________________________________________________________________
    def enter_back(event):
        can_back.itemconfig(icon_back, image=back_img_max)
    def leave_back(event):
        can_back.itemconfig(icon_back, image=back_img)
    def clic_back(event):
        for widget in wd.winfo_children():
            widget.destroy()
        WD_pack(event)

    icon_back = can_back.create_image(20, 20, image=back_img)
    can_back.tag_bind(icon_back, "<Enter>", enter_back)
    can_back.tag_bind(icon_back, "<Leave>", leave_back)
    can_back.tag_bind(icon_back, "<Button-1>", clic_back)   

















# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                              Fenêtre 5 >>> Extract fichiers
def WD_extract(event):
    # Titre __________________________________________________________________________________________________________________________
    frame_title = Frame(wd, bg=Config.bg_color)
    Title = Label(frame_title, text="Mode extraction", font=(Config.title_caly, Config.title_size), bg=Config.bg_color, fg=Config.fg_color).pack()
    frame_title.pack(side=TOP, pady=Config.title_marge)
    
    # Canvas_back __________________________________________________________________________________________________________________________
    can_back = Canvas(wd, bg=Config.bg_color, width=50, height=50, highlightthickness=0)
    can_back.pack()
    can_back.place(x=Config.bp_bk_mrg_x, y=Config.bp_bk_mrg_y, anchor='nw')

    # BP_back __________________________________________________________________________________________________________________________
    def enter_back(event):
        can_back.itemconfig(icon_back, image=back_img_max)
    def leave_back(event):
        can_back.itemconfig(icon_back, image=back_img)
    def clic_back(event):
        for widget in wd.winfo_children():
            widget.destroy()
        WD_pack(event)

    icon_back = can_back.create_image(20, 20, image=back_img)
    can_back.tag_bind(icon_back, "<Enter>", enter_back)
    can_back.tag_bind(icon_back, "<Leave>", leave_back)
    can_back.tag_bind(icon_back, "<Button-1>", clic_back)



WD_acceuil()
# Affichage __________________________________________________________________________________________________________________________
wd.mainloop()










