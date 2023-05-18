try:
    from Autocomplete_Combo import AutocompleteCombobox
    from Log_Generator import Log_Generator
    from Top_Func import Func
    from ColorScheme import ColorScheme
    from FormRun import *
    from FormCommon import *
except:
    from Library_Files.Autocomplete_Combo import AutocompleteCombobox
    from Library_Files.Log_Generator import Log_Generator
    from Library_Files.Top_Func import Func
    from Library_Files.ColorScheme import ColorScheme
    from Library_Files.FormRun import *
    from Library_Files.FormCommon import *


class a(BeforeInIt, AllSettings, CommonFunction):
    wSize, hSize = 800, 550
    title = "a - Point Of Sale"
    mainName = "a"

    def __init__(self, wind) -> None:
        BeforeInIt.__init__(self)
        AllSettings.__init__(self)
        super().__init__()
        self.root = wind
        self.sortKey = 'x[0]'
        self.CommonCall()

        y_space = int(self.formset_yInF)  # 30 for 20 fields limit 40 for 15 fields limit
        self.dF_ent_w = int(self.formset_wOfF)
        self.dF_ent_x = int(self.formset_xOfF)

        frm_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=20)
        frm_.pack(fill=BOTH, expand=True)

        frm_id = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_id.pack(fill=BOTH, expand=True)
        lbl_id = Label(frm_id, text='ID', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_id.place(x=10, y=1)
        ent_id = Entry(frm_id, textvariable=self.var_id, disabledbackground=self.colorList[14], disabledforeground=self.colorList[15], state=DISABLED, border=0, font=self.formset_mainF)
        ent_id.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_dat_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_dat_.pack(fill=BOTH, expand=True)
        lbl_dat_ = Label(frm_dat_, text='Date', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_dat_.place(x=10, y=1)
        ent_dat_ = DateEntry(frm_dat_, textvariable=self.var_dat_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12], justify=CENTER, date_pattern='dd-mm-y')
        ent_dat_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w - 10, height=self.formset_fieldH)
        def cls_dat_():
            self.var_dat_.set("")
            ent_dat_.update()
        btn_dat_ = Button(frm_dat_, command=cls_dat_, justify=LEFT, text='-', font=(self.formset_mainF, 13), bd=0, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_dat_.place(x=self.dF_ent_x + self.dF_ent_w - 10, y=1, width=10, height=self.formset_fieldH)

        frm_r0_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_r0_.pack(fill=BOTH, expand=True)
        lbl_r0_ = Label(frm_r0_, text='text', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_r0_.place(x=10, y=1)
        ent_r0_ = Entry(frm_r0_, textvariable=self.var_r0_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_r0_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_r1_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_r1_.pack(fill=BOTH, expand=True)
        lbl_r1_ = Label(frm_r1_, text='date', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_r1_.place(x=10, y=1)
        ent_r1_ = DateEntry(frm_r1_, textvariable=self.var_r1_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12], justify=CENTER, date_pattern='dd-mm-y')
        ent_r1_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w - 10, height=self.formset_fieldH)
        def cls_r1_():
            self.var_r1_.set("")
            ent_r1_.update()
        btn_r1_ = Button(frm_r1_, command=cls_r1_, justify=LEFT, text='-', font=(self.formset_mainF, 13), bd=0, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_r1_.place(x=self.dF_ent_x + self.dF_ent_w - 10, y=1, width=10, height=self.formset_fieldH)

        frm_r2_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_r2_.pack(fill=BOTH, expand=True)
        lbl_r2_ = Label(frm_r2_, text='combo', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_r2_.place(x=10, y=1)
        cmb_r2__list = ['']
        cmb_r2_ = AutocompleteCombobox(frm_r2_, values=cmb_r2__list, textvariable=self.var_r2_, font=self.formset_mainF, background=self.colorList[9], foreground=self.colorList[10])
        cmb_r2_.set_completion_list(cmb_r2__list)
        cmb_r2_.tk.eval(f'[ttk::combobox::PopdownWindow %s].f.l configure -background {self.colorList[13]}' % cmb_r2_)
        cmb_r2_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)
        cmb_r2_.current(0)

        frm_r3_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_r3_.pack(fill=BOTH, expand=True)
        lbl_r3_ = Label(frm_r3_, text='no', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_r3_.place(x=10, y=1)
        ent_r3_ = Entry(frm_r3_, textvariable=self.var_r3_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_r3_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)
        ent_r3_.bind("<KeyRelease>", lambda e, x=self.var_r3_: self.convertToNo(e, x))

        frm_r4_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_r4_.pack(fill=BOTH, expand=True)
        lbl_r4_ = Label(frm_r4_, text='attach', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_r4_.place(x=10, y=1)
        ent_att = Entry(frm_r4_, textvariable=self.var_r4_3, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_att.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w - 120, height=self.formset_fieldH)
        self.var_r4_3.set('Not Attached')
        def attach():
            try:
                ff = filedialog.askopenfilename(parent=self.root, title='Select Document')
                if ff != '':
                    self.var_r4_1.set(ff)
                    abcd = self.convertToBinaryData(ff)
                    self.var_r4_2.set(abcd.decode('cp437'))
                    self.var_r4_3.set('Attached')
            except Exception as e: messagebox.showerror('Error', e, parent=self.root)
        btn_att = Button(frm_r4_, text='Attach', command=attach, justify=LEFT, font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_att.place(x=self.dF_ent_x+self.dF_ent_w-120, y=1, width=60, height=self.formset_fieldH)
        def open_doc():
            try:
                x = random.randint(1, 500000)
                x = str(x)
                z = self.var_r4_1.get()
                z = os.path.basename(z)
                loc = 'Temp\\Temp' + x + z
                a = self.var_r4_2.get()
                a = a.encode('cp437')
                if self.var_r4_2.get() != '':
                    with open(loc, 'wb') as file:
                        file.write(a)
                    os.startfile(loc)
            except Exception as e: messagebox.showerror('Error', e, parent=self.root)
        btn_open = Button(frm_r4_, text='Open', command=open_doc, justify=LEFT, font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_open.place(x=self.dF_ent_x+self.dF_ent_w-60, y=1, width=59, height=self.formset_fieldH)

        frm_r5_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_r5_.pack(fill=BOTH, expand=True)
        lbl_r5_ = Label(frm_r5_, text='dText', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_r5_.place(x=10, y=1)
        ent_r5_ = Entry(frm_r5_, textvariable=self.var_r5_, border=0, font=self.formset_mainF, disabledbackground=self.colorList[14], disabledforeground=self.colorList[15], state=DISABLED, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_r5_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_r6_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=(y_space * 5) + 10)
        frm_r6_.pack(fill=BOTH, expand=True)
        
        self.var_r6__temp = StringVar()
        lbl_r6_ = Label(frm_r6_, text='listT', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_r6_.place(x=10, y=1)
        ent_r6_ = Entry(frm_r6_, textvariable=self.var_r6__temp, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_r6_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w - 100, height=self.formset_fieldH)
        
        btn_r6_ = Button(frm_r6_, command=lambda : self.list_Add(lis_r6_, self.var_r6__temp, self.var_r6_), justify=LEFT, text='Add', font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_r6_.place(x=self.dF_ent_x + self.dF_ent_w - 99, y=1, width=50, height=self.formset_fieldH)
        btn_r6_ = Button(frm_r6_, command=lambda : self.list_Del(lis_r6_, self.var_r6_), justify=LEFT, text='Delete', font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_r6_.place(x=self.dF_ent_x + self.dF_ent_w - 49, y=1, width=50, height=self.formset_fieldH)
        
        lis_r6_ = Listbox(frm_r6_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lis_r6_.place(x=self.dF_ent_x, y=1 + y_space, width=self.dF_ent_w - 10, height=55 + (y_space * 2))
        scl_r6_ = Scrollbar(frm_r6_)
        scl_r6_.place(x=self.dF_ent_x + self.dF_ent_w - 10, y=1 + y_space, width=10, height=55 + (y_space * 2))
        lis_r6_.config(yscrollcommand=scl_r6_.set)
        scl_r6_.config(command=lis_r6_.yview)
        sclx_r6_ = Scrollbar(frm_r6_, orient=HORIZONTAL)
        sclx_r6_.place(x=self.dF_ent_x, y=1 + y_space + 55 + (y_space * 2), width=self.dF_ent_w, height=10)
        lis_r6_.config(xscrollcommand=sclx_r6_.set)
        sclx_r6_.config(command=lis_r6_.xview)
        
        # Bind the function to the StringVar object
        self.var_r6_.trace("w", lambda name, index, mode: self.bindList(lis_r6_, self.var_r6__temp, self.var_r6_))

        frm_r7_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=(y_space * 5) + 10)
        frm_r7_.pack(fill=BOTH, expand=True)
        
        self.var_r7__temp = StringVar()
        lbl_r7_ = Label(frm_r7_, text='listC', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_r7_.place(x=10, y=1)
        cmb_r7__list = ['Yes', 'No']
        lbl_r7_ = Label(frm_r7_, text='listC', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_r7_.place(x=10, y=1)
        cmb_r7__list = cmb_r7__list
        cmb_r7_ = AutocompleteCombobox(frm_r7_, values=cmb_r7__list, textvariable=self.var_r7__temp, font=self.formset_mainF, background=self.colorList[9], foreground=self.colorList[10])
        cmb_r7_.set_completion_list(cmb_r7__list)
        cmb_r7_.tk.eval(f'[ttk::combobox::PopdownWindow %s].f.l configure -background {self.colorList[13]}' % cmb_r7_)
        cmb_r7_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w - 100, height=self.formset_fieldH)
        cmb_r7_.current(0)
        
        btn_r7_ = Button(frm_r7_, command=lambda : self.list_Add(lis_r7_, self.var_r7__temp, self.var_r7_), justify=LEFT, text='Add', font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_r7_.place(x=self.dF_ent_x + self.dF_ent_w - 99, y=1, width=50, height=self.formset_fieldH)
        btn_r7_ = Button(frm_r7_, command=lambda : self.list_Del(lis_r7_, self.var_r7_), justify=LEFT, text='Delete', font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_r7_.place(x=self.dF_ent_x + self.dF_ent_w - 49, y=1, width=50, height=self.formset_fieldH)
        
        lis_r7_ = Listbox(frm_r7_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lis_r7_.place(x=self.dF_ent_x, y=1 + y_space, width=self.dF_ent_w - 10, height=55 + (y_space * 2))
        scl_r7_ = Scrollbar(frm_r7_)
        scl_r7_.place(x=self.dF_ent_x + self.dF_ent_w - 10, y=1 + y_space, width=10, height=55 + (y_space * 2))
        lis_r7_.config(yscrollcommand=scl_r7_.set)
        scl_r7_.config(command=lis_r7_.yview)
        sclx_r7_ = Scrollbar(frm_r7_, orient=HORIZONTAL)
        sclx_r7_.place(x=self.dF_ent_x, y=1 + y_space + 55 + (y_space * 2), width=self.dF_ent_w, height=10)
        lis_r7_.config(xscrollcommand=sclx_r7_.set)
        sclx_r7_.config(command=lis_r7_.xview)
        
        # Bind the function to the StringVar object
        self.var_r7_.trace("w", lambda name, index, mode: self.bindList(lis_r7_, self.var_r7__temp, self.var_r7_))

        frm_r8_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=(y_space * 5) + 10)
        frm_r8_.pack(fill=BOTH, expand=True)
        
        self.var_r8__temp = StringVar()
        lbl_r8_ = Label(frm_r8_, text='listTD', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_r8_.place(x=10, y=1)
        ent_r8_ = Entry(frm_r8_, textvariable=self.var_r8__temp, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_r8_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w - 100, height=self.formset_fieldH)
        
        btn_r8_ = Button(frm_r8_, command=lambda : self.list_nd_Add(lis_r8_, self.var_r8__temp, self.var_r8_), justify=LEFT, text='Add', font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_r8_.place(x=self.dF_ent_x + self.dF_ent_w - 99, y=1, width=50, height=self.formset_fieldH)
        btn_r8_ = Button(frm_r8_, command=lambda : self.list_Del(lis_r8_, self.var_r8_), justify=LEFT, text='Delete', font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_r8_.place(x=self.dF_ent_x + self.dF_ent_w - 49, y=1, width=50, height=self.formset_fieldH)
        
        lis_r8_ = Listbox(frm_r8_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lis_r8_.place(x=self.dF_ent_x, y=1 + y_space, width=self.dF_ent_w - 10, height=55 + (y_space * 2))
        scl_r8_ = Scrollbar(frm_r8_)
        scl_r8_.place(x=self.dF_ent_x + self.dF_ent_w - 10, y=1 + y_space, width=10, height=55 + (y_space * 2))
        lis_r8_.config(yscrollcommand=scl_r8_.set)
        scl_r8_.config(command=lis_r8_.yview)
        sclx_r8_ = Scrollbar(frm_r8_, orient=HORIZONTAL)
        sclx_r8_.place(x=self.dF_ent_x, y=1 + y_space + 55 + (y_space * 2), width=self.dF_ent_w, height=10)
        lis_r8_.config(xscrollcommand=sclx_r8_.set)
        sclx_r8_.config(command=lis_r8_.xview)
        
        # Bind the function to the StringVar object
        self.var_r8_.trace("w", lambda name, index, mode: self.bindList(lis_r8_, self.var_r8__temp, self.var_r8_))

        frm_r9_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=(y_space * 5) + 10)
        frm_r9_.pack(fill=BOTH, expand=True)
        
        self.var_r9__temp = StringVar()
        lbl_r9_ = Label(frm_r9_, text='listCD', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_r9_.place(x=10, y=1)
        cmb_r9__list = ['Yes', 'No']
        lbl_r9_ = Label(frm_r9_, text='listCD', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_r9_.place(x=10, y=1)
        cmb_r9__list = cmb_r9__list
        cmb_r9_ = AutocompleteCombobox(frm_r9_, values=cmb_r9__list, textvariable=self.var_r9__temp, font=self.formset_mainF, background=self.colorList[9], foreground=self.colorList[10])
        cmb_r9_.set_completion_list(cmb_r9__list)
        cmb_r9_.tk.eval(f'[ttk::combobox::PopdownWindow %s].f.l configure -background {self.colorList[13]}' % cmb_r9_)
        cmb_r9_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w - 100, height=self.formset_fieldH)
        cmb_r9_.current(0)
        
        btn_r9_ = Button(frm_r9_, command=lambda : self.list_ndc_Add(lis_r9_, self.var_r9__temp, self.var_r9_, cmb_r9__list, cmb_r9_), justify=LEFT, text='Add', font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_r9_.place(x=self.dF_ent_x + self.dF_ent_w - 99, y=1, width=50, height=self.formset_fieldH)
        btn_r9_ = Button(frm_r9_, command=lambda : self.list_ndc_Del(lis_r9_, self.var_r9_, self.var_r9__temp, cmb_r9__list, cmb_r9_), justify=LEFT, text='Delete', font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_r9_.place(x=self.dF_ent_x + self.dF_ent_w - 49, y=1, width=50, height=self.formset_fieldH)
        
        lis_r9_ = Listbox(frm_r9_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lis_r9_.place(x=self.dF_ent_x, y=1 + y_space, width=self.dF_ent_w - 10, height=55 + (y_space * 2))
        scl_r9_ = Scrollbar(frm_r9_)
        scl_r9_.place(x=self.dF_ent_x + self.dF_ent_w - 10, y=1 + y_space, width=10, height=55 + (y_space * 2))
        lis_r9_.config(yscrollcommand=scl_r9_.set)
        scl_r9_.config(command=lis_r9_.yview)
        sclx_r9_ = Scrollbar(frm_r9_, orient=HORIZONTAL)
        sclx_r9_.place(x=self.dF_ent_x, y=1 + y_space + 55 + (y_space * 2), width=self.dF_ent_w, height=10)
        lis_r9_.config(xscrollcommand=sclx_r9_.set)
        sclx_r9_.config(command=lis_r9_.xview)
        
        # Bind the function to the StringVar object
        self.var_r9_.trace("w", lambda name, index, mode: self.bindList_ndc(lis_r9_, self.var_r9__temp, self.var_r9_, cmb_r9__list, cmb_r9_))

        self.CommonCall2()

        # Record Frame
        self.recordFrame = Frame(self.root, bg=self.colorList[2])
        self.recordFrame.place(x=self.rF_x, y=self.rF_y, width=self.rF_w, height=self.rF_h)

        scroll_y = Scrollbar(self.recordFrame, orient=VERTICAL)
        scroll_x = Scrollbar(self.recordFrame, orient=HORIZONTAL)

        self.Table = ttk.Treeview(self.recordFrame, columns=['id', 'dat_', 'r0_', 'r1_', 'r2_', 'r3_', 'r4__1', 'r4_2', 'r5_', 'r6_', 'r7_', 'r8_', 'r9_'], yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.config(command=self.Table.yview)
        scroll_x.config(command=self.Table.xview)
        self.Table.heading('id', text='ID')
        self.Table.heading('dat_', text='Date')
        self.Table.heading('r0_', text='text')
        self.Table.heading('r1_', text='date')
        self.Table.heading('r2_', text='combo')
        self.Table.heading('r3_', text='no')
        self.Table.heading('r4__1', text='attach')
        self.Table.heading('r4_2', text='attach')
        self.Table.heading('r5_', text='dText')
        self.Table.heading('r6_', text='listT')
        self.Table.heading('r7_', text='listC')
        self.Table.heading('r8_', text='listTD')
        self.Table.heading('r9_', text='listCD')
        self.Table["show"] = "headings"
        self.Table.column('id', width=50)
        self.Table.column('dat_', width=100)
        self.Table.column('r0_', width=150)
        self.Table.column('r1_', width=150)
        self.Table.column('r2_', width=150)
        self.Table.column('r3_', width=150)
        self.Table.column('r4__1', width=150)
        self.Table.column('r4_2', width=0, stretch='no')
        self.Table.column('r5_', width=150)
        self.Table.column('r6_', width=150)
        self.Table.column('r7_', width=150)
        self.Table.column('r8_', width=150)
        self.Table.column('r9_', width=150)
        self.Table.pack(fill=BOTH, expand=True)

        self.CommonCall3()

    def _Add(self, e): self.Add()
    def _Update(self, e): self.Update()
    def _Delete(self, e): self.Delete()
    def _Clear(self, e): self.Clear()
    def _Import(self, e): self.Import()
    def _Export(self, e): self.Export()

    def Variables(self):
        # Variables
        self.var_id = StringVar()  # id serial Number
        self.var_dat_ = StringVar()  # Date
        self.var_r0_ = StringVar()  # text
        self.var_r1_ = StringVar()  # date
        self.var_r2_ = StringVar()  # combo
        self.var_r3_ = StringVar()  # no
        self.var_r4_1 = StringVar()  # attach
        self.var_r4_2 = StringVar()  # attach
        self.var_r4_3 = StringVar()  # attach
        self.var_r5_ = StringVar()  # dText
        self.var_r6_ = StringVar()  # listT
        self.var_r7_ = StringVar()  # listC
        self.var_r8_ = StringVar()  # listTD
        self.var_r9_ = StringVar()  # listCD

    def Export_def(self):
        gg = self.Table.get_children()
        id = []
        dat_ = []
        r0_ = []
        r1_ = []
        r2_ = []
        r3_ = []
        r4_ = []
        r5_ = []
        r6_ = []
        r7_ = []
        r8_ = []
        r9_ = []
        count = 0
        for i in gg:
            content = self.Table.item(i)
            pp = content['values']
            count += 1
            id.append(str(count))
            dat_.append(pp[1])
            r0_.append(pp[2])
            r1_.append(pp[3])
            r2_.append(pp[4])
            r3_.append(pp[5])
            r4_.append(pp[6])
            r5_.append(pp[8])
            r6_.append(pp[9])
            r7_.append(pp[10])
            r8_.append(pp[11])
            r9_.append(pp[12])

        headings = self.__list__('head')
        expList = list(zip(id, dat_, r0_, r1_, r2_, r3_, r4_, r5_, r6_, r7_, r8_, r9_))
        Log_Generator().addLog(f'[Export] {count} Record Found')
        return count, headings, expList

    def Get_Data(self, e):
        try:
            f = self.Table.focus()
            content = (self.Table.item(f))
            row = content['values']
            self.var_id.set(row[0])
            self.var_dat_.set(row[1])
            self.var_r0_.set(row[2])
            self.var_r1_.set(row[3])
            self.var_r2_.set(row[4])
            self.var_r3_.set(row[5])
            self.var_r4_1.set(row[6])
            self.var_r4_2.set(row[6+1])
            if self.var_r4_1.get() == '':
                self.var_r4_3.set('Not Attached')
            elif self.var_r4_1.get() != '':
                self.var_r4_3.set('Attached')
            self.var_r5_.set(row[8])
            self.var_r6_.set(row[9])
            self.var_r7_.set(row[10])
            self.var_r8_.set(row[11])
            self.var_r9_.set(row[12])

            self.status(f'[{self.mainName}] [Get Data] Record {self.var_id.get()} Selected Successfully')
        except Exception as ex:
            self.status(f'[{self.mainName}] [Get Data] Error: {ex}')
            pass

    def StarterDb(self, db='sqlite'):
        if db == 'sqlite':
            self.cur.execute('''CREATE TABLE IF NOT EXISTS "''' + self.mainName.replace(' ', '_') + '''" (
                "id"	INTEGER NOT NULL UNIQUE,
                "dat_"	TEXT,
                "r0_"	TEXT,
                "r1_"	TEXT,
                "r2_"	TEXT,
                "r3_"	TEXT,
                "r4_1"  TEXT,
                "r4_2"	BLOB,
                "r5_"	TEXT,
                "r6_"	TEXT,
                "r7_"	TEXT,
                "r8_"	TEXT,
                "r9_"	TEXT,
                PRIMARY KEY("id" AUTOINCREMENT))''')
            self.con.commit()
        else:
            self.cur.execute(
                '''CREATE TABLE IF NOT EXISTS ''' + self.mainName.replace(' ', '_') + ''' (
                id SERIAL NOT NULL AUTO_INCREMENT
                , dat_ TEXT NOT NULL
                , r0_ TEXT NOT NULL
                , r1_ TEXT NOT NULL
                , r2_ TEXT NOT NULL
                , r3_ TEXT NOT NULL
                , r4_1 TEXT NOT NULL , r4_2 LONGBLOB NOT NULL
                , r5_ TEXT NOT NULL
                , r6_ TEXT NOT NULL
                , r7_ TEXT NOT NULL
                , r8_ TEXT NOT NULL
                , r9_ TEXT NOT NULL )''')
            self.con.commit()

    def __list__(self, fetch):
        list_var = [self.var_id, self.var_dat_, self.var_r0_, self.var_r1_, self.var_r2_, self.var_r3_, self.var_r4_1, self.var_r4_2, self.var_r5_, self.var_r6_, self.var_r7_, self.var_r8_, self.var_r9_]
        list_shn = ['id', 'dat_', 'r0_', 'r1_', 'r2_', 'r3_', 'r4_1', 'r4_2', 'r5_', 'r6_', 'r7_', 'r8_', 'r9_']
        list_cvar = [[self.var_id, 'ID'], [self.var_r0_, 'text']]
        list_head = ['ID', 'Date', 'text', 'date', 'combo', 'no', 'attach', 'dText', 'listT', 'listC', 'listTD', 'listCD']
        list_headA = ['ID', 'Date', 'text', 'date', 'combo', 'no', 'attach', 'SKIP IT', 'dText', 'listT', 'listC', 'listTD', 'listCD']

        if fetch == 'var':
            return list_var
        elif fetch == 'cvar':
            return list_cvar
        elif fetch == 'shn':
            return list_shn
        elif fetch == 'head':
            return list_head
        elif fetch == 'headA':
            return list_headA

    def __bq__(self, q):
        if q == 'add':
            query = None
            return query
        elif q == 'update':
            query = None
            return query
        elif q == 'delete':
            query = None
            return query

    def __aq__(self, q):
        if q == 'add':
            query = None
            return query
        elif q == 'update':
            query = None
            return query
        elif q == 'delete':
            query = None
            return query


if __name__ == '__main__':
    root = Tk()
    obj = a(root)
    root.mainloop()
    Log_Generator().closeLog()
