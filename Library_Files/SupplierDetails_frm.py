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


class SupplierDetails(BeforeInIt, AllSettings, CommonFunction):
    wSize, hSize = 800, 550
    title = "Supplier Details - Point Of Sale"
    mainName = "Supplier Details"

    def __init__(self, wind, libFormList=[]) -> None:
        BeforeInIt.__init__(self)
        AllSettings.__init__(self)
        super().__init__()
        self.root = wind
        self.sortKey = 'x[0]'
        self.split_pdf_rep = {}
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

        frm_sup_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_sup_.pack(fill=BOTH, expand=True)
        lbl_sup_ = Label(frm_sup_, text='Supplier Name', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_sup_.place(x=10, y=1)
        cmb_sup__list = ['']
        cmb_sup_ = AutocompleteCombobox(frm_sup_, values=cmb_sup__list, textvariable=self.var_sup_, font=self.formset_mainF, background=self.colorList[9], foreground=self.colorList[10])
        cmb_sup_.set_completion_list(cmb_sup__list)
        cmb_sup_.tk.eval(f'[ttk::combobox::PopdownWindow %s].f.l configure -background {self.colorList[13]}' % cmb_sup_)
        cmb_sup_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w - 21, height=self.formset_fieldH)
        btn_sup_ = Button(frm_sup_, command=lambda: self.get_combo_list("select sup_ from Supplier", cmb_sup_, self.var_sup_), justify=LEFT, text='🔃', font=(self.formset_mainF, 13), bd=0, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_sup_.place(x=self.dF_ent_x + self.dF_ent_w - 21, y=1, width=10, height=self.formset_fieldH)
        btn_sup_ = Button(frm_sup_, command=lambda: self.open_libForm('Supplier'), justify=LEFT, text='+', font=(self.formset_mainF, 13), bd=0, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_sup_.place(x=self.dF_ent_x + self.dF_ent_w - 10, y=1, width=10, height=self.formset_fieldH)
        self.get_combo_list("select sup_ from Supplier", cmb_sup_, self.var_sup_)
        cmb_sup_.current(0)

        frm_sti_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_sti_.pack(fill=BOTH, expand=True)
        lbl_sti_ = Label(frm_sti_, text='Stock ID', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_sti_.place(x=10, y=1)
        cmb_sti__list = ['']
        cmb_sti_ = AutocompleteCombobox(frm_sti_, values=cmb_sti__list, textvariable=self.var_sti_, font=self.formset_mainF, background=self.colorList[9], foreground=self.colorList[10])
        cmb_sti_.set_completion_list(cmb_sti__list)
        cmb_sti_.tk.eval(f'[ttk::combobox::PopdownWindow %s].f.l configure -background {self.colorList[13]}' % cmb_sti_)
        cmb_sti_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)
        cmb_sti_.current(0)

        frm_pay_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_pay_.pack(fill=BOTH, expand=True)
        lbl_pay_ = Label(frm_pay_, text='Payment', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_pay_.place(x=10, y=1)
        ent_pay_ = Entry(frm_pay_, textvariable=self.var_pay_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_pay_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_ppy_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_ppy_.pack(fill=BOTH, expand=True)
        lbl_ppy_ = Label(frm_ppy_, text='Pending Payment', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_ppy_.place(x=10, y=1)
        ent_ppy_ = Entry(frm_ppy_, textvariable=self.var_ppy_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_ppy_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        def add_pay_ppy(e):
            try:
                pay = int(self.var_pay_.get())
            except:
                pay = 0
            try:
                ppy = int(self.var_ppy_.get())
            except:
                ppy = 0
            self.var_tpy_.set(pay + ppy)

        ent_pay_.bind("<KeyRelease>", lambda e, x=self.var_pay_: (self.convertToNo(e, x), add_pay_ppy(e)))
        ent_ppy_.bind("<KeyRelease>", lambda e, x=self.var_ppy_: (self.convertToNo(e, x), add_pay_ppy(e)))

        frm_tpy_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_tpy_.pack(fill=BOTH, expand=True)
        lbl_tpy_ = Label(frm_tpy_, text='Total', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_tpy_.place(x=10, y=1)
        ent_tpy_ = Entry(frm_tpy_, textvariable=self.var_tpy_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_tpy_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)
        ent_tpy_.bind("<KeyRelease>", lambda e, x=self.var_tpy_: self.convertToNo(e, x))

        frm_det_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_det_.pack(fill=BOTH, expand=True)
        lbl_det_ = Label(frm_det_, text='Details', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_det_.place(x=10, y=1)
        ent_det_ = Entry(frm_det_, textvariable=self.var_det_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_det_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_pyr_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_pyr_.pack(fill=BOTH, expand=True)
        lbl_pyr_ = Label(frm_pyr_, text='Payment Receipt', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_pyr_.place(x=10, y=1)
        ent_att = Entry(frm_pyr_, textvariable=self.var_pyr_3, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_att.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w - 120, height=self.formset_fieldH)
        self.var_pyr_3.set('Not Attached')

        def attach():
            try:
                ff = filedialog.askopenfilename(parent=self.root, title='Select Document')
                if ff != '':
                    self.var_pyr_1.set(ff)
                    abcd = self.convertToBinaryData(ff)
                    self.var_pyr_2.set(abcd.decode('cp437'))
                    self.var_pyr_3.set('Attached')
            except Exception as e:
                messagebox.showerror('Error', e, parent=self.root)

        btn_att = Button(frm_pyr_, text='Attach', command=attach, justify=LEFT, font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_att.place(x=self.dF_ent_x + self.dF_ent_w - 120, y=1, width=60, height=self.formset_fieldH)

        def open_doc():
            try:
                x = random.randint(1, 500000)
                x = str(x)
                z = self.var_pyr_1.get()
                z = os.path.basename(z)
                loc = 'Temp\\Temp' + x + z
                a = self.var_pyr_2.get()
                a = a.encode('cp437')
                if self.var_pyr_2.get() != '':
                    with open(loc, 'wb') as file:
                        file.write(a)
                    os.startfile(loc)
            except Exception as e:
                messagebox.showerror('Error', e, parent=self.root)

        btn_open = Button(frm_pyr_, text='Open', command=open_doc, justify=LEFT, font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_open.place(x=self.dF_ent_x + self.dF_ent_w - 60, y=1, width=59, height=self.formset_fieldH)

        self.CommonCall2()

        # Record Frame
        self.recordFrame = Frame(self.root, bg=self.colorList[2])
        self.recordFrame.place(x=self.rF_x, y=self.rF_y, width=self.rF_w, height=self.rF_h)

        scroll_y = Scrollbar(self.recordFrame, orient=VERTICAL)
        scroll_x = Scrollbar(self.recordFrame, orient=HORIZONTAL)

        self.Table = ttk.Treeview(self.recordFrame, columns=['id', 'sup_', 'sti_', 'pay_', 'ppy_', 'tpy_', 'det_', 'pyr__1', 'pyr_2'], yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.config(command=self.Table.yview)
        scroll_x.config(command=self.Table.xview)
        self.Table.heading('id', text='ID')
        self.Table.heading('sup_', text='Supplier Name')
        self.Table.heading('sti_', text='Stock ID')
        self.Table.heading('pay_', text='Payment')
        self.Table.heading('ppy_', text='Pending Payment')
        self.Table.heading('tpy_', text='Total')
        self.Table.heading('det_', text='Details')
        self.Table.heading('pyr__1', text='Payment Receipt')
        self.Table.heading('pyr_2', text='Payment Receipt')
        self.Table["show"] = "headings"
        self.Table.column('id', width=50)
        self.Table.column('sup_', width=100)
        self.Table.column('sti_', width=150)
        self.Table.column('pay_', width=150)
        self.Table.column('ppy_', width=150)
        self.Table.column('tpy_', width=100)
        self.Table.column('det_', width=150)
        self.Table.column('pyr__1', width=150)
        self.Table.column('pyr_2', width=0, stretch='no')
        self.Table.pack(fill=BOTH, expand=True)

        self.CommonCall3()

    def _Add(self, e):
        self.Add()

    def _Update(self, e):
        self.Update()

    def _Delete(self, e):
        self.Delete()

    def _Clear(self, e):
        self.Clear()

    def _Import(self, e):
        self.Import()

    def _Export(self, e):
        self.Export()

    def Variables(self):
        # Variables
        self.var_id = StringVar()  # id serial Number
        self.var_sup_ = StringVar()  # Supplier Name
        self.var_sti_ = StringVar()  # Stock ID
        self.var_pay_ = StringVar()  # Payment
        self.var_ppy_ = StringVar()  # Pending Payment
        self.var_tpy_ = StringVar()  # Total
        self.var_det_ = StringVar()  # Details
        self.var_pyr_1 = StringVar()  # Payment Receipt
        self.var_pyr_2 = StringVar()  # Payment Receipt
        self.var_pyr_3 = StringVar()  # Payment Receipt

    def Export_def(self):
        gg = self.Table.get_children()
        id = []
        sup_ = []
        sti_ = []
        pay_ = []
        ppy_ = []
        tpy_ = []
        det_ = []
        count = 0
        for i in gg:
            content = self.Table.item(i)
            pp = content['values']
            count += 1
            id.append(str(count))
            sup_.append(pp[1])
            sti_.append(pp[2])
            pay_.append(pp[3])
            ppy_.append(pp[4])
            tpy_.append(pp[5])
            det_.append(pp[6])

        headings = self.__list__('head')[:-1]
        expList = list(zip(id, sup_, sti_, pay_, ppy_, tpy_, det_))
        Log_Generator().addLog(f'[Export] {count} Record Found')
        return count, headings, expList

    def Get_Data(self, e):
        try:
            f = self.Table.focus()
            content = (self.Table.item(f))
            row = content['values']
            self.var_id.set(row[0])
            self.var_sup_.set(row[1])
            self.var_sti_.set(row[2])
            self.var_pay_.set(row[3])
            self.var_ppy_.set(row[4])
            self.var_tpy_.set(row[5])
            self.var_det_.set(row[6])
            self.var_pyr_1.set(row[7])
            self.var_pyr_2.set(row[7 + 1])
            if self.var_pyr_1.get() == '':
                self.var_pyr_3.set('Not Attached')
            elif self.var_pyr_1.get() != '':
                self.var_pyr_3.set('Attached')

            self.status(f'[{self.mainName}] [Get Data] Record {self.var_id.get()} Selected Successfully')
        except Exception as ex:
            self.status(f'[{self.mainName}] [Get Data] Error: {ex}')
            pass

    def StarterDb(self, db='sqlite'):
        if db == 'sqlite':
            self.cur.execute('''CREATE TABLE IF NOT EXISTS "''' + self.mainName.replace(' ', '_') + '''" (
                "id"	INTEGER NOT NULL UNIQUE,
                "sup_"	TEXT,
                "sti_"	TEXT,
                "pay_"	TEXT,
                "ppy_"	TEXT,
                "tpy_"	TEXT,
                "det_"	TEXT,
                "pyr_1"  TEXT,
                "pyr_2"	BLOB,
                PRIMARY KEY("id" AUTOINCREMENT))''')
            self.con.commit()
        else:
            self.cur.execute(
                '''CREATE TABLE IF NOT EXISTS ''' + self.mainName.replace(' ', '_') + ''' (
                id SERIAL NOT NULL AUTO_INCREMENT
                , sup_ TEXT NOT NULL
                , sti_ TEXT NOT NULL
                , pay_ TEXT NOT NULL
                , ppy_ TEXT NOT NULL
                , tpy_ TEXT NOT NULL
                , det_ TEXT NOT NULL
                , pyr_1 TEXT NOT NULL , pyr_2 LONGBLOB NOT NULL )''')
            self.con.commit()

    def __list__(self, fetch):
        list_var = [self.var_id, self.var_sup_, self.var_sti_, self.var_pay_, self.var_ppy_, self.var_tpy_, self.var_det_, self.var_pyr_1, self.var_pyr_2]
        list_shn = ['id', 'sup_', 'sti_', 'pay_', 'ppy_', 'tpy_', 'det_', 'pyr_1', 'pyr_2']
        list_cvar = [[self.var_id, 'ID'], [self.var_sup_, 'Supplier Name'], [self.var_sti_, 'Stock ID'], [self.var_pay_, 'Payment'], [self.var_tpy_, 'Total']]
        list_head = ['ID', 'Supplier Name', 'Stock ID', 'Payment', 'Pending Payment', 'Total', 'Details', 'Payment Receipt']
        list_headA = ['ID', 'Supplier Name', 'Stock ID', 'Payment', 'Pending Payment', 'Total', 'Details', 'Payment Receipt', 'SKIP IT']

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
    obj = SupplierDetails(root)
    root.mainloop()
    Log_Generator().closeLog()
