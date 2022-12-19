from tkinter import *
import awesometkinter as atk


class mainEditor:
    # Main Variables
    title = "Main Editor"
    iconPath = "Image/ico.ico"
    Geometry = ""
    mainLbg = '#3C3F41'
    mainFg = '#A2A2A2'
    mainDbg = '#2B2B2B'
    mainWbg = '#45494A'
    mainWbd = '#646464'
    mainWhBg = '#3D6185'
    mainWfg = '#BBBBBB'

    def __init__(self, wind) -> None:
        self.root = wind
        self.root.title(self.title)
        self.root.geometry(self.Geometry)
        # self.root.resizable(0, 0)
        self.root.config(bg=self.mainDbg)
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.focus_force()
        self.root.after_idle(self.root.attributes, '-topmost', False)
        self.root.state('zoomed')
        self.root.focus_force()

        rootHeight = self.root.winfo_screenheight()
        rootWidth = self.root.winfo_screenwidth()

        self.root.bind("<F11>", lambda event: self.root.attributes("-fullscreen",
                                                                   not self.root.attributes("-fullscreen")))
        self.root.bind("<Escape>", lambda event: self.root.attributes("-fullscreen", False))

        self.root2 = Frame(root, bg=self.mainDbg)
        self.root2.pack(fill=BOTH, expand=True)

        atf = atk.ScrollableFrame(self.root2, hscroll=False, vbar_width=1, hbar_width=1)
        for i in range(50):
            Button(atf, justify=LEFT, command= lambda i=i: self.openRP('pr', i), text='File Name\nFile Url', cursor='hand2', bg=self.mainDbg, fg=self.mainWfg, bd=0, relief=FLAT, activebackground=self.mainDbg, activeforeground=self.mainWfg).pack()

        atf.pack(fill=BOTH, expand=True)
        # # Top Menu Frame
        # topFrame = Frame(root, bg=self.mainLbg)
        # topFrame

        # left Tool Frame
        # lfHeight = rootHeight - 20 - 50 - 30
        # lfWidth = 100
        #
        # frameRP = Frame(self.root2, bg=self.mainLbg)
        # frameRP.place(x=0, y=0, width=lfWidth, height=lfHeight)
        #
        # canvasRP = Canvas(frameRP, bd=0, highlightthickness=0, bg=self.mainLbg, width=300, height=300, scrollregion=(0, 0, 500, 500))
        # vbar = Scrollbar(frameRP, orient=VERTICAL)
        # vbar.place(x=lfWidth-10, y=-12, width=10, height=lfHeight+24)
        # vbar.config(command=canvasRP.yview)
        # canvasRP.config(width=300, height=300)
        # canvasRP.config(yscrollcommand=vbar.set)
        # canvasRP.pack(side=LEFT, expand=True, fill=BOTH)
        #
        # canvasRP.bind('<Configure>', lambda e: canvasRP.configure(scrollregion=canvasRP.bbox('all')))
        # self.leftFrame = Frame(canvasRP, bg=self.mainLbg)
        # canvasRP.create_window((0, 0), window=self.leftFrame, anchor="nw")
        #
        # rowLF = 0
        # colLF = 0
        # lfBtnW = 3
        # lfBtnH = 3
        # self.btn_arrow = Button(self.leftFrame, justify=LEFT, text='F', font=('wingdings', 10), bd=0, cursor='hand2', bg=self.mainLbg, activebackground=self.mainLbg, fg=self.mainWfg, width=lfBtnW, height=lfBtnH)
        # self.btn_arrow.grid(row=rowLF, column=colLF)
        # colLF = 1
        # self.btn_hand = Button(self.leftFrame, justify=LEFT, text='I', font=('wingdings', 10), bd=0, cursor='hand2', bg=self.mainLbg, activebackground=self.mainLbg, fg=self.mainWfg, width=lfBtnW, height=lfBtnH)
        # self.btn_hand.grid(row=rowLF, column=colLF)
        # rowLF += 1
        # self.btn_pen = Button(self.leftFrame, justify=LEFT, text='x', font=('wingdings', 10), bd=0, cursor='hand2', bg=self.mainLbg, activebackground=self.mainLbg, fg=self.mainWfg, width=lfBtnW, height=lfBtnH)
        # self.btn_pen.grid(row=rowLF, column=colLF)
        # colLF = 0
        # self.btn_del = Button(self.leftFrame, justify=LEFT, text='!', font=('wingdings', 10), bd=0, cursor='hand2', bg=self.mainLbg, activebackground=self.mainLbg, fg=self.mainWfg, width=lfBtnW, height=lfBtnH)
        # self.btn_del.grid(row=rowLF, column=colLF)
        # rowLF += 1
        # colLF = 0
        # self.btn_rec = Button(self.leftFrame, justify=LEFT, text='o', font=('wingdings', 10), bd=0, cursor='hand2', bg=self.mainLbg, activebackground=self.mainLbg, fg=self.mainWfg, width=lfBtnW, height=lfBtnH)
        # self.btn_rec.grid(row=rowLF, column=colLF)
        # colLF = 1
        # self.btn_cir = Button(self.leftFrame, justify=LEFT, text='m', font=('wingdings', 10), bd=0, cursor='hand2', bg=self.mainLbg, activebackground=self.mainLbg, fg=self.mainWfg, width=lfBtnW, height=lfBtnH)
        # self.btn_cir.grid(row=rowLF, column=colLF)
        # rowLF += 1
        # self.btn_pol = Button(self.leftFrame, justify=LEFT, text='/', font=('webdings', 8), bd=0, cursor='hand2', bg=self.mainLbg, activebackground=self.mainLbg, fg=self.mainWfg, width=lfBtnW, height=lfBtnH)
        # self.btn_pol.grid(row=rowLF, column=colLF)
        # colLF = 0
        # btn_8 = Button(self.leftFrame, justify=LEFT, text='\'', font=('webdings', 8), bd=0, cursor='hand2', bg=self.mainLbg, activebackground=self.mainLbg, fg=self.mainWfg, width=lfBtnW, height=lfBtnH)
        # btn_8.grid(row=rowLF, column=colLF)
        # rowLF += 1
        # colLF = 0
        # btn_9 = Button(self.leftFrame, justify=LEFT, text='$', font=('wingdings 2', 10), bd=0, cursor='hand2', bg=self.mainLbg, activebackground=self.mainLbg, fg=self.mainWfg, width=lfBtnW, height=lfBtnH)
        # btn_9.grid(row=rowLF, column=colLF)
        # colLF = 1
        # btn_10 = Button(self.leftFrame, justify=LEFT, text='#', font=('wingdings 2', 10), bd=0, cursor='hand2', bg=self.mainLbg, activebackground=self.mainLbg, fg=self.mainWfg, width=lfBtnW, height=lfBtnH)
        # btn_10.grid(row=rowLF, column=colLF)
        # rowLF += 1
        # btn_11 = Button(self.leftFrame, justify=LEFT, text='@', font=('wingdings 2', 10), bd=0, cursor='hand2', bg=self.mainLbg, activebackground=self.mainLbg, fg=self.mainWfg, width=lfBtnW, height=lfBtnH)
        # btn_11.grid(row=rowLF, column=colLF)
        # colLF = 0
        # btn_12 = Button(self.leftFrame, justify=LEFT, text='', font=('wingdings 2', 10), bd=0, cursor='hand2', bg=self.mainLbg, activebackground=self.mainLbg, fg=self.mainWfg, width=lfBtnW, height=lfBtnH)
        # btn_12.grid(row=rowLF, column=colLF)
        # rowLF += 1


if __name__ == '__main__':
    root = Tk()
    obj = mainEditor(root)
    root.mainloop()
