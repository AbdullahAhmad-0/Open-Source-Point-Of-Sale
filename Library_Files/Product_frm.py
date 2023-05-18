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


class Product(BeforeInIt, AllSettings, CommonFunction):
    wSize, hSize = 800, 550
    title = "Product - Point Of Sale"
    mainName = "Product"

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

        frm_prn_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_prn_.pack(fill=BOTH, expand=True)
        lbl_prn_ = Label(frm_prn_, text='Product Name', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_prn_.place(x=10, y=1)
        ent_prn_ = Entry(frm_prn_, textvariable=self.var_prn_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_prn_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_prc_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_prc_.pack(fill=BOTH, expand=True)
        lbl_prc_ = Label(frm_prc_, text='Product Code', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_prc_.place(x=10, y=1)
        ent_prc_ = Entry(frm_prc_, textvariable=self.var_prc_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_prc_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_des_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_des_.pack(fill=BOTH, expand=True)
        lbl_des_ = Label(frm_des_, text='Description', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_des_.place(x=10, y=1)
        ent_des_ = Entry(frm_des_, textvariable=self.var_des_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_des_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_bar_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=(y_space * 5) + 10)
        frm_bar_.pack(fill=BOTH, expand=True)

        self.var_bar__temp = StringVar()
        lbl_bar_ = Label(frm_bar_, text='Barcode', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_bar_.place(x=10, y=1)
        ent_bar_ = Entry(frm_bar_, textvariable=self.var_bar__temp, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_bar_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w - 100, height=self.formset_fieldH)

        btn_bar_ = Button(frm_bar_, command=lambda: self.list_nd_Add(lis_bar_, self.var_bar__temp, self.var_bar_), justify=LEFT, text='Add', font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_bar_.place(x=self.dF_ent_x + self.dF_ent_w - 99, y=1, width=50, height=self.formset_fieldH)
        btn_bar_ = Button(frm_bar_, command=lambda: self.list_Del(lis_bar_, self.var_bar_), justify=LEFT, text='Delete', font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_bar_.place(x=self.dF_ent_x + self.dF_ent_w - 49, y=1, width=50, height=self.formset_fieldH)

        lis_bar_ = Listbox(frm_bar_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lis_bar_.place(x=self.dF_ent_x, y=1 + y_space, width=self.dF_ent_w - 10, height=55 + (y_space * 2))
        scl_bar_ = Scrollbar(frm_bar_)
        scl_bar_.place(x=self.dF_ent_x + self.dF_ent_w - 10, y=1 + y_space, width=10, height=55 + (y_space * 2))
        lis_bar_.config(yscrollcommand=scl_bar_.set)
        scl_bar_.config(command=lis_bar_.yview)
        sclx_bar_ = Scrollbar(frm_bar_, orient=HORIZONTAL)
        sclx_bar_.place(x=self.dF_ent_x, y=1 + y_space + 55 + (y_space * 2), width=self.dF_ent_w, height=10)
        lis_bar_.config(xscrollcommand=sclx_bar_.set)
        sclx_bar_.config(command=lis_bar_.xview)

        # Bind the function to the StringVar object
        self.var_bar_.trace("w", lambda name, index, mode: self.bindList(lis_bar_, self.var_bar__temp, self.var_bar_))

        frm_cat_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_cat_.pack(fill=BOTH, expand=True)
        lbl_cat_ = Label(frm_cat_, text='Category', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_cat_.place(x=10, y=1)
        cmb_cat__list = ['']
        cmb_cat_ = AutocompleteCombobox(frm_cat_, values=cmb_cat__list, textvariable=self.var_cat_, font=self.formset_mainF, background=self.colorList[9], foreground=self.colorList[10])
        cmb_cat_.set_completion_list(cmb_cat__list)
        cmb_cat_.tk.eval(f'[ttk::combobox::PopdownWindow %s].f.l configure -background {self.colorList[13]}' % cmb_cat_)
        cmb_cat_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w - 21, height=self.formset_fieldH)
        btn_cat_ = Button(frm_cat_, command=lambda: self.get_combo_list("select cat_ from Product_Category", cmb_cat_, self.var_cat_), justify=LEFT, text='🔃', font=(self.formset_mainF, 13), bd=0, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_cat_.place(x=self.dF_ent_x + self.dF_ent_w - 21, y=1, width=10, height=self.formset_fieldH)
        btn_cat_ = Button(frm_cat_, command=lambda: self.open_libForm('Product Category'), justify=LEFT, text='+', font=(self.formset_mainF, 13), bd=0, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_cat_.place(x=self.dF_ent_x + self.dF_ent_w - 10, y=1, width=10, height=self.formset_fieldH)
        self.get_combo_list("select cat_ from Product_Category", cmb_cat_, self.var_cat_)
        cmb_cat_.current(0)

        def _cat_(e):
            cat_()

        def cat_():
            try:
                self.cur.execute(f"select sct_ from Product_Category where cat_='" + self.var_cat_.get() + "'")
                cmb_sct_.set("")
                self.var_sct_.set("")
                cmb_sct_.delete(cmb_sct_.get())
                fetch = self.cur.fetchall()
                without_bracket = []
                for i in fetch:
                    without_bracket.append(str(i[0]))
                    without_bracket = list(dict.fromkeys(without_bracket))
                    without_bracket.sort()
                    cmb_sct_.config(values=without_bracket)
                    cmb_sct__list = without_bracket
                    cmb_sct_.set_completion_list(cmb_sct__list)
                self.con.commit()
            except Exception as e:
                Log_Generator().addLog(f'[Combobox Error] {e}')
                self.lbl_status.config(text=f'[Combobox Error] {e}')

        cmb_cat_.bind('<<ComboboxSelected>>', _cat_)

        frm_sct_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_sct_.pack(fill=BOTH, expand=True)
        lbl_sct_ = Label(frm_sct_, text='Sub Category', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_sct_.place(x=10, y=1)
        cmb_sct__list = ['']
        cmb_sct_ = AutocompleteCombobox(frm_sct_, values=cmb_sct__list, textvariable=self.var_sct_, font=self.formset_mainF, background=self.colorList[9], foreground=self.colorList[10])
        cmb_sct_.set_completion_list(cmb_sct__list)
        cmb_sct_.tk.eval(f'[ttk::combobox::PopdownWindow %s].f.l configure -background {self.colorList[13]}' % cmb_sct_)
        cmb_sct_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)
        cmb_sct_.current(0)

        frm_snw_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_snw_.pack(fill=BOTH, expand=True)
        lbl_snw_ = Label(frm_snw_, text='Size n Weight', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_snw_.place(x=10, y=1)
        ent_snw_ = Entry(frm_snw_, textvariable=self.var_snw_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_snw_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_sta_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_sta_.pack(fill=BOTH, expand=True)
        lbl_sta_ = Label(frm_sta_, text='Status', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_sta_.place(x=10, y=1)
        cmb_sta__list = ['Available', 'Not Available']
        cmb_sta_ = AutocompleteCombobox(frm_sta_, values=cmb_sta__list, textvariable=self.var_sta_, font=self.formset_mainF, background=self.colorList[9], foreground=self.colorList[10])
        cmb_sta_.set_completion_list(cmb_sta__list)
        cmb_sta_.tk.eval(f'[ttk::combobox::PopdownWindow %s].f.l configure -background {self.colorList[13]}' % cmb_sta_)
        cmb_sta_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)
        cmb_sta_.current(0)

        frm_res_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_res_.pack(fill=BOTH, expand=True)
        lbl_res_ = Label(frm_res_, text='Reserved Product Qty', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_res_.place(x=10, y=1)
        ent_res_ = Entry(frm_res_, textvariable=self.var_res_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_res_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)
        ent_res_.bind("<KeyRelease>", lambda e, x=self.var_res_: self.convertToNo(e, x))

        self.CommonCall2()

        # Record Frame
        self.recordFrame = Frame(self.root, bg=self.colorList[2])
        self.recordFrame.place(x=self.rF_x, y=self.rF_y, width=self.rF_w, height=self.rF_h)

        scroll_y = Scrollbar(self.recordFrame, orient=VERTICAL)
        scroll_x = Scrollbar(self.recordFrame, orient=HORIZONTAL)

        self.Table = ttk.Treeview(self.recordFrame, columns=['id', 'prn_', 'prc_', 'des_', 'bar_', 'cat_', 'sct_', 'snw_', 'sta_', 'res_'], yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.config(command=self.Table.yview)
        scroll_x.config(command=self.Table.xview)
        self.Table.heading('id', text='ID')
        self.Table.heading('prn_', text='Product Name')
        self.Table.heading('prc_', text='Product Code')
        self.Table.heading('des_', text='Description')
        self.Table.heading('bar_', text='Barcode')
        self.Table.heading('cat_', text='Category')
        self.Table.heading('sct_', text='Sub Category')
        self.Table.heading('snw_', text='Size n Weight')
        self.Table.heading('sta_', text='Status')
        self.Table.heading('res_', text='Reserved Product Qty')
        self.Table["show"] = "headings"
        self.Table.column('id', width=50)
        self.Table.column('prn_', width=100)
        self.Table.column('prc_', width=100)
        self.Table.column('des_', width=100)
        self.Table.column('bar_', width=100)
        self.Table.column('cat_', width=100)
        self.Table.column('sct_', width=100)
        self.Table.column('snw_', width=100)
        self.Table.column('sta_', width=100)
        self.Table.column('res_', width=100)
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
        self.var_prn_ = StringVar()  # Product Name
        self.var_prc_ = StringVar()  # Product Code
        self.var_des_ = StringVar()  # Description
        self.var_bar_ = StringVar()  # Barcode
        self.var_cat_ = StringVar()  # Category
        self.var_sct_ = StringVar()  # Sub Category
        self.var_snw_ = StringVar()  # Size n Weight
        self.var_sta_ = StringVar()  # Status
        self.var_res_ = StringVar()  # Reserved Product Qty

    def Export_def(self):
        gg = self.Table.get_children()
        id = []
        prn_ = []
        prc_ = []
        des_ = []
        bar_ = []
        cat_ = []
        sct_ = []
        snw_ = []
        sta_ = []
        res_ = []
        count = 0
        for i in gg:
            content = self.Table.item(i)
            pp = content['values']
            count += 1
            id.append(str(count))
            prn_.append(pp[1])
            prc_.append(pp[2])
            des_.append(pp[3])
            bar_.append(pp[4])
            cat_.append(pp[5])
            sct_.append(pp[6])
            snw_.append(pp[7])
            sta_.append(pp[8])
            res_.append(pp[9])

        headings = self.__list__('head')
        expList = list(zip(id, prn_, prc_, des_, bar_, cat_, sct_, snw_, sta_, res_))
        Log_Generator().addLog(f'[Export] {count} Record Found')
        return count, headings, expList

    def Get_Data(self, e):
        try:
            f = self.Table.focus()
            content = (self.Table.item(f))
            row = content['values']
            self.var_id.set(row[0])
            self.var_prn_.set(row[1])
            self.var_prc_.set(row[2])
            self.var_des_.set(row[3])
            self.var_bar_.set(row[4])
            self.var_cat_.set(row[5])
            self.var_sct_.set(row[6])
            self.var_snw_.set(row[7])
            self.var_sta_.set(row[8])
            self.var_res_.set(row[9])

            self.status(f'[{self.mainName}] [Get Data] Record {self.var_id.get()} Selected Successfully')
        except Exception as ex:
            self.status(f'[{self.mainName}] [Get Data] Error: {ex}')
            pass

    def StarterDb(self, db='sqlite'):
        if db == 'sqlite':
            self.cur.execute('''CREATE TABLE IF NOT EXISTS "''' + self.mainName.replace(' ', '_') + '''" (
                "id"	INTEGER NOT NULL UNIQUE,
                "prn_"	TEXT,
                "prc_"	TEXT,
                "des_"	TEXT,
                "bar_"	TEXT,
                "cat_"	TEXT,
                "sct_"	TEXT,
                "snw_"	TEXT,
                "sta_"	TEXT,
                "res_"	TEXT,
                PRIMARY KEY("id" AUTOINCREMENT))''')
            self.con.commit()
        else:
            self.cur.execute(
                '''CREATE TABLE IF NOT EXISTS ''' + self.mainName.replace(' ', '_') + ''' (
                id SERIAL NOT NULL AUTO_INCREMENT
                , prn_ TEXT NOT NULL
                , prc_ TEXT NOT NULL
                , des_ TEXT NOT NULL
                , bar_ TEXT NOT NULL
                , cat_ TEXT NOT NULL
                , sct_ TEXT NOT NULL
                , snw_ TEXT NOT NULL
                , sta_ TEXT NOT NULL
                , res_ TEXT NOT NULL )''')
            self.con.commit()

    def __list__(self, fetch):
        list_var = [self.var_id, self.var_prn_, self.var_prc_, self.var_des_, self.var_bar_, self.var_cat_, self.var_sct_, self.var_snw_, self.var_sta_, self.var_res_]
        list_shn = ['id', 'prn_', 'prc_', 'des_', 'bar_', 'cat_', 'sct_', 'snw_', 'sta_', 'res_']
        list_cvar = [[self.var_id, 'ID'], [self.var_prn_, 'Product Name'], [self.var_prc_, 'Product Code'], [self.var_cat_, 'Category'], [self.var_sct_, 'Sub Category'], [self.var_sta_, 'Status']]
        list_head = ['ID', 'Product Name', 'Product Code', 'Description', 'Barcode', 'Category', 'Sub Category', 'Size n Weight', 'Status', 'Reserved Product Qty']
        list_headA = ['ID', 'Product Name', 'Product Code', 'Description', 'Barcode', 'Category', 'Sub Category', 'Size n Weight', 'Status', 'Reserved Product Qty']

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
    obj = Product(root)
    root.mainloop()
    Log_Generator().closeLog()
