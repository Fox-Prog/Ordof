from tkinter import *

# _____________________________________________ INFO _____________________________________________ #


def WD_info(txtST, txtC):
        wd_info=Tk()
        from Config import CDT
        from Config import ICON
        wd_info.title('Info')
        wd_info.resizable(False, False)
        wd_info.config(background=CDT.bg_color)
        wd_info.iconbitmap(ICON.Logo)

        # Titre __________________________________________________________________________________________________________________________
        frame_title_info = Frame(wd_info, bg=CDT.bg_color)
        Title = Label(frame_title_info, text="Info", font=(CDT.title_caly, CDT.title_size), bg=CDT.bg_color, fg=CDT.fg_color).pack()
        Subtitle = Label(frame_title_info, text=txtST, font=(CDT.sub_title_caly, CDT.sub_title_size), bg=CDT.bg_color, fg=CDT.fg_color).pack()
        frame_title_info.pack(side=TOP, pady=CDT.title_marge)

        can_text = Canvas(wd_info, width=790, height=550, bg=CDT.bg_color, highlightthickness=0)
        can_text.create_text(5, 0, anchor='nw',justify='left', text=txtC, font=(CDT.text_caly, CDT.text_size), fill=CDT.fg_color)
        can_text.pack(side=BOTTOM, pady=10)
        


        wd_info.mainloop()




# nbrF, files_list
def WD_confirm_R(nbrF, F_list):
    wd_confirm_R = Tk()
    from Config import CDT
    from Config import ICON

    htr = int(nbrF)
    if htr > 750:
        htr = 750
    if htr < 510:
        htr = 510
        
    lrg = round(htr/2)
    if lrg > 1900:
        lrg = 1900
    if lrg < 480:
        lrg = 480
 
    wd_confirm_R.title('Auto_rename')
    wd_confirm_R.geometry('{}x{}'.format(lrg, htr))
    wd_confirm_R.maxsize(height=1080)
    wd_confirm_R.resizable(False, False)
    wd_confirm_R.config(background=CDT.bg_color)
    wd_confirm_R.iconbitmap(ICON.Logo)

    # Titre __________________________________________________________________________________________________________________________
    frame_title_confirm_R = Frame(wd_confirm_R, bg=CDT.bg_color)
    Title = Label(frame_title_confirm_R, text="Confirmation", font=(CDT.title_caly, CDT.title_size), bg=CDT.bg_color, fg=CDT.fg_color).pack()
    frame_title_confirm_R.pack(side=TOP, pady=CDT.title_marge)


    # Indication elements __________________________________________________________________________________________________________________________
    frame_elements = Frame(wd_confirm_R, bg=CDT.bg_color)
    nbr_elements = Label(frame_elements, text=nbrF, font=(CDT.text_big_caly, CDT.text_big_size), bg=CDT.bg_color, fg=CDT.fg_color)
    label_elements = Label(frame_elements, text="Elements vont être renommés", font=(CDT.text_caly, CDT.text_size), bg=CDT.bg_color, fg=CDT.fg_color)
    nbr_elements.grid(row=0,column=0,padx=20,sticky=W)
    label_elements.grid(row=0,column=1,padx=20,sticky=W)
    frame_elements.pack(pady=5)

    # Files_list __________________________________________________________________________________________________________________________
    frame_files_list = Frame(wd_confirm_R, bg=CDT.bg_color)
    can_files_list = Canvas(frame_files_list, bg=CDT.bg_color, highlightthickness=0,width=(lrg-80), height=(htr-250))

    hbar = Scrollbar(frame_files_list, orient=VERTICAL, repeatinterval=100)
    hbar.pack(side=RIGHT, fill=Y)
    

    text_F_list = Text(can_files_list, wrap=WORD, bg=CDT.bg_color, fg=CDT.fg_color, font=(CDT.text_list_caly, CDT.text_list_size), highlightthickness=0, yscrollcommand=hbar.set)
    for el in F_list:
        text_F_list.insert(INSERT, el + '\n')
    text_F_list.place(x=0, y=0, anchor='nw')
    text_F_list.config(yscrollcommand=hbar.set)

    hbar.config(command=text_F_list.yview)

    can_files_list.pack(side=LEFT)
    frame_files_list.pack()
    


    # Confirm rename __________________________________________________________________________________________________________________________
    frame_confirm_R = Frame(wd_confirm_R, bg=CDT.bg_color)
    text_confirm_R = Label(frame_confirm_R, text="Rename >>> ", font=(CDT.title_caly, CDT.title_size), bg=CDT.bg_color, fg=CDT.fg_color)
    can_confirm_R = Canvas(frame_confirm_R, bg=CDT.bg_color, width=CDT.can_litle_bp_size, height=CDT.can_litle_bp_size, highlightthickness=1)

    test_img = PhotoImage(file="C:/Users/Utilisateur/Documents/Programmation/PYTHON/Gestion_de_fichiers/Ordof/Ressources/TEST.png")

    def enter_confirm_R(event):                 
        can_confirm_R.itemconfig(icon_confirm_R, image=ICON.go_img_max)
        text_confirm_R.config(fg=CDT.fg_color)

    def leave_confirm_R(event):                 
        can_confirm_R.itemconfig(icon_confirm_R, image=ICON.go_img)
        text_confirm_R.config(fg=CDT.bg_color)

    def clic_confirm_R(event):                 
        print("GO")

    icon_confirm_R = can_confirm_R.create_image(37.5,37.5, image=test_img)

    can_confirm_R.tag_bind(icon_confirm_R, "<Enter>",enter_confirm_R)
    can_confirm_R.tag_bind(icon_confirm_R, "<Leave>",leave_confirm_R)
    can_confirm_R.tag_bind(icon_confirm_R, "<Button-1>",clic_confirm_R)

    text_confirm_R.grid(row=0, column=0, padx=0, sticky=W)
    can_confirm_R.grid(row=0, column=1, padx=0, sticky=W)

    frame_confirm_R.pack(side=BOTTOM, pady=10)

    wd_confirm_R.mainloop()

