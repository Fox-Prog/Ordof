from tkinter import *

# _____________________________________________ INFO _____________________________________________ #


def WD_info(txtST, txtC):
        wd_info=Tk()
        from Config import CDT
        from Config import ICON
        wd_info.title('Info')
        lrg = 900
        htr = 480
        wd_info.geometry('{}x{}'.format(lrg, htr))
        wd_info.resizable(False, False)
        wd_info.config(background=CDT.bg_color)
        wd_info.iconbitmap(ICON.Logo)

        # Titre __________________________________________________________________________________________________________________________
        frame_title_info = Frame(wd_info, bg=CDT.bg_color)
        Title = Label(frame_title_info, text="Info", font=(CDT.title_caly, CDT.title_size), bg=CDT.bg_color, fg=CDT.fg_color).pack()
        Subtitle = Label(frame_title_info, text=txtST, font=(CDT.sub_title_caly, CDT.sub_title_size), bg=CDT.bg_color, fg=CDT.fg_color).pack()
        frame_title_info.pack(side=TOP, pady=CDT.title_marge)

        frame_text = Frame(wd_info, bg=CDT.bg_color)
        can_text = Canvas(frame_text,width=(lrg-50), height=(htr-50), bg=CDT.bg_color, highlightthickness=0)

        hbar = Scrollbar(frame_text, orient=VERTICAL)
        hbar.pack(side="right", fill="y")

        textC = Text(can_text, wrap=WORD, bg=CDT.bg_color, fg=CDT.fg_color, font=(CDT.text_caly, CDT.text_size), highlightthickness=0, yscrollcommand=hbar.set)
        for el in txtC:
                textC.insert(INSERT,'  '+ el + '\n')
        textC.pack(side='top')#, fill="both")
        textC.config(yscrollcommand=hbar.set)

        hbar.config(command=textC.yview)
        
        can_text.pack(side='left')
        frame_text.pack()

        textC.update()
        htr_txt = round(textC.winfo_height())
        htr_wd = htr_txt + 400
        if htr_wd > 1920:
                htr_wd = 1920

        wd_info.geometry('{}x{}+5+5'.format((lrg-50), htr_wd))
        can_text.config(height=htr_txt)

        wd_info.mainloop()
