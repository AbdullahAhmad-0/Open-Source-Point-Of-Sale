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


class Users(BeforeInIt, AllSettings, CommonFunction):
    wSize, hSize = 800, 550
    title = "Users - Point Of Sale"
    mainName = "Users"

    def __init__(self, wind, libFormList=[]) -> None:
        BeforeInIt.__init__(self)
        AllSettings.__init__(self)
        super().__init__()
        self.root = wind
        self.sortKey = 'x[0]'
        self.split_pdf_rep = {2:20,5:10, 8:12,9:12}
        self.split_pdf_rep_auto = True
        self.split_pdf_rep_auto_len = 15
        self.CommonCall()
        self.libFormList = libFormList

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

        frm_fln_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_fln_.pack(fill=BOTH, expand=True)
        lbl_fln_ = Label(frm_fln_, text='Full Name', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_fln_.place(x=10, y=1)
        ent_fln_ = Entry(frm_fln_, textvariable=self.var_fln_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_fln_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_adr_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_adr_.pack(fill=BOTH, expand=True)
        lbl_adr_ = Label(frm_adr_, text='Address', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_adr_.place(x=10, y=1)
        ent_adr_ = Entry(frm_adr_, textvariable=self.var_adr_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_adr_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_phn_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_phn_.pack(fill=BOTH, expand=True)
        lbl_phn_ = Label(frm_phn_, text='Phone', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_phn_.place(x=10, y=1)
        ent_phn_ = Entry(frm_phn_, textvariable=self.var_phn_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_phn_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_eml_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_eml_.pack(fill=BOTH, expand=True)
        lbl_eml_ = Label(frm_eml_, text='Email', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_eml_.place(x=10, y=1)
        ent_eml_ = Entry(frm_eml_, textvariable=self.var_eml_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_eml_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_rle_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_rle_.pack(fill=BOTH, expand=True)
        lbl_rle_ = Label(frm_rle_, text='Role', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_rle_.place(x=10, y=1)
        cmb_rle__list = ['']
        cmb_rle_ = AutocompleteCombobox(frm_rle_, values=cmb_rle__list, textvariable=self.var_rle_, font=self.formset_mainF, background=self.colorList[9], foreground=self.colorList[10])
        cmb_rle_.set_completion_list(cmb_rle__list)
        cmb_rle_.tk.eval(f'[ttk::combobox::PopdownWindow %s].f.l configure -background {self.colorList[13]}' % cmb_rle_)
        cmb_rle_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w - 21, height=self.formset_fieldH)
        btn_rle_ = Button(frm_rle_, command=lambda: self.get_combo_list("select fln_ from User_Role", cmb_rle_, self.var_rle_), justify=LEFT, text='🔃', font=(self.formset_mainF, 13), bd=0, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_rle_.place(x=self.dF_ent_x + self.dF_ent_w - 21, y=1, width=10, height=self.formset_fieldH)
        btn_rle_ = Button(frm_rle_, command=lambda: self.open_libForm('User Role'), justify=LEFT, text='+', font=(self.formset_mainF, 13), bd=0, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_rle_.place(x=self.dF_ent_x + self.dF_ent_w - 10, y=1, width=10, height=self.formset_fieldH)
        self.get_combo_list("select fln_ from User_Role", cmb_rle_, self.var_rle_)
        cmb_rle_.current(0)

        frm_sal_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_sal_.pack(fill=BOTH, expand=True)
        lbl_sal_ = Label(frm_sal_, text='Salary', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_sal_.place(x=10, y=1)
        ent_sal_ = Entry(frm_sal_, textvariable=self.var_sal_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_sal_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_doj_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_doj_.pack(fill=BOTH, expand=True)
        lbl_doj_ = Label(frm_doj_, text='Date Of Join', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_doj_.place(x=10, y=1)
        ent_doj_ = DateEntry(frm_doj_, textvariable=self.var_doj_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12], justify=CENTER, date_pattern='dd-mm-y')
        ent_doj_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w - 10, height=self.formset_fieldH)
        def cls_doj_():
            self.var_doj_.set("")
            ent_doj_.update()
        btn_doj_ = Button(frm_doj_, command=cls_doj_, justify=LEFT, text='-', font=(self.formset_mainF, 13), bd=0, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_doj_.place(x=self.dF_ent_x + self.dF_ent_w - 10, y=1, width=10, height=self.formset_fieldH)

        frm_usn_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_usn_.pack(fill=BOTH, expand=True)
        lbl_usn_ = Label(frm_usn_, text='User Name', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_usn_.place(x=10, y=1)
        ent_usn_ = Entry(frm_usn_, textvariable=self.var_usn_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_usn_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_pas_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_pas_.pack(fill=BOTH, expand=True)
        lbl_pas_ = Label(frm_pas_, text='Password', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_pas_.place(x=10, y=1)
        ent_pas_ = Entry(frm_pas_, textvariable=self.var_pas_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_pas_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        self.CommonCall2()

        # Record Frame
        self.recordFrame = Frame(self.root, bg=self.colorList[2])
        self.recordFrame.place(x=self.rF_x, y=self.rF_y, width=self.rF_w, height=self.rF_h)

        scroll_y = Scrollbar(self.recordFrame, orient=VERTICAL)
        scroll_x = Scrollbar(self.recordFrame, orient=HORIZONTAL)

        self.Table = ttk.Treeview(self.recordFrame, columns=['id', 'fln_', 'adr_', 'phn_', 'eml_', 'rle_', 'sal_', 'doj_', 'usn_', 'pas_'], yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.config(command=self.Table.yview)
        scroll_x.config(command=self.Table.xview)
        self.Table.heading('id', text='ID')
        self.Table.heading('fln_', text='Full Name')
        self.Table.heading('adr_', text='Address')
        self.Table.heading('phn_', text='Phone')
        self.Table.heading('eml_', text='Email')
        self.Table.heading('rle_', text='Role')
        self.Table.heading('sal_', text='Salary')
        self.Table.heading('doj_', text='Date Of Join')
        self.Table.heading('usn_', text='User Name')
        self.Table.heading('pas_', text='Password')
        self.Table["show"] = "headings"
        self.Table.column('id', width=50)
        self.Table.column('fln_', width=150)
        self.Table.column('adr_', width=250)
        self.Table.column('phn_', width=150)
        self.Table.column('eml_', width=150)
        self.Table.column('rle_', width=150)
        self.Table.column('sal_', width=150)
        self.Table.column('doj_', width=150)
        self.Table.column('usn_', width=150)
        self.Table.column('pas_', width=150)
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
        self.var_fln_ = StringVar()  # Full Name
        self.var_adr_ = StringVar()  # Address
        self.var_phn_ = StringVar()  # Phone
        self.var_eml_ = StringVar()  # Email
        self.var_rle_ = StringVar()  # Role
        self.var_sal_ = StringVar()  # Salary
        self.var_doj_ = StringVar()  # Date Of Join
        self.var_usn_ = StringVar()  # User Name
        self.var_pas_ = StringVar()  # Password

    def Export_def(self):
        gg = self.Table.get_children()
        id = []
        fln_ = []
        adr_ = []
        phn_ = []
        eml_ = []
        rle_ = []
        sal_ = []
        doj_ = []
        usn_ = []
        pas_ = []
        count = 0
        for i in gg:
            content = self.Table.item(i)
            pp = content['values']
            count += 1
            id.append(str(count))
            fln_.append(pp[1])
            adr_.append(pp[2])
            phn_.append(pp[3])
            eml_.append(pp[4])
            rle_.append(pp[5])
            sal_.append(pp[6])
            doj_.append(pp[7])
            usn_.append(pp[8])
            pas_.append(pp[9])

        headings = self.__list__('head')
        expList = list(zip(id, fln_, adr_, phn_, eml_, rle_, sal_, doj_, usn_, pas_))
        Log_Generator().addLog(f'[Export] {count} Record Found')
        return count, headings, expList

    def Get_Data(self, e):
        try:
            f = self.Table.focus()
            content = (self.Table.item(f))
            row = content['values']
            self.var_id.set(row[0])
            self.var_fln_.set(row[1])
            self.var_adr_.set(row[2])
            self.var_phn_.set(row[3])
            self.var_eml_.set(row[4])
            self.var_rle_.set(row[5])
            self.var_sal_.set(row[6])
            self.var_doj_.set(row[7])
            self.var_usn_.set(row[8])
            self.var_pas_.set(row[9])

            self.status(f'[{self.mainName}] [Get Data] Record {self.var_id.get()} Selected Successfully')
        except Exception as ex:
            self.status(f'[{self.mainName}] [Get Data] Error: {ex}')
            pass

    def StarterDb(self, db='sqlite'):
        if db == 'sqlite':
            self.cur.execute('''CREATE TABLE IF NOT EXISTS "''' + self.mainName.replace(' ', '_') + '''" (
                "id"	INTEGER NOT NULL UNIQUE,
                "fln_"	TEXT,
                "adr_"	TEXT,
                "phn_"	TEXT,
                "eml_"	TEXT,
                "rle_"	TEXT,
                "sal_"	TEXT,
                "doj_"	TEXT,
                "usn_"	TEXT,
                "pas_"	TEXT,
                PRIMARY KEY("id" AUTOINCREMENT))''')
            self.con.commit()
        else:
            self.cur.execute(
                '''CREATE TABLE IF NOT EXISTS ''' + self.mainName.replace(' ', '_') + ''' (
                id SERIAL NOT NULL AUTO_INCREMENT
                , fln_ TEXT NOT NULL
                , adr_ TEXT NOT NULL
                , phn_ TEXT NOT NULL
                , eml_ TEXT NOT NULL
                , rle_ TEXT NOT NULL
                , sal_ TEXT NOT NULL
                , doj_ TEXT NOT NULL
                , usn_ TEXT NOT NULL
                , pas_ TEXT NOT NULL )''')
            self.con.commit()

    def __list__(self, fetch):
        list_var = [self.var_id, self.var_fln_, self.var_adr_, self.var_phn_, self.var_eml_, self.var_rle_, self.var_sal_, self.var_doj_, self.var_usn_, self.var_pas_]
        list_shn = ['id', 'fln_', 'adr_', 'phn_', 'eml_', 'rle_', 'sal_', 'doj_', 'usn_', 'pas_']
        list_cvar = [[self.var_id, 'ID'], [self.var_fln_, 'Full Name'], [self.var_rle_, 'Role'], [self.var_usn_, 'User Name'], [self.var_pas_, 'Password']]
        list_head = ['ID', 'Full Name', 'Address', 'Phone', 'Email', 'Role', 'Salary', 'Date Of Join', 'User Name', 'Password']
        list_headA = ['ID', 'Full Name', 'Address', 'Phone', 'Email', 'Role', 'Salary', 'Date Of Join', 'User Name', 'Password']

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
    obj = Users(root)
    root.mainloop()
    Log_Generator().closeLog()
