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


class Supplier(BeforeInIt, AllSettings, CommonFunction):
    wSize, hSize = 800, 550
    title = "Supplier - Point Of Sale"
    mainName = "Supplier"

    def __init__(self, wind, libFormList=[]) -> None:
        BeforeInIt.__init__(self)
        AllSettings.__init__(self)
        super().__init__()
        self.root = wind
        self.sortKey = 'x[0]'
        self.split_pdf_rep = {8:25}
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
        ent_sup_ = Entry(frm_sup_, textvariable=self.var_sup_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_sup_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_add_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_add_.pack(fill=BOTH, expand=True)
        lbl_add_ = Label(frm_add_, text='Address', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_add_.place(x=10, y=1)
        ent_add_ = Entry(frm_add_, textvariable=self.var_add_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_add_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

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

        frm_cmp_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_cmp_.pack(fill=BOTH, expand=True)
        lbl_cmp_ = Label(frm_cmp_, text='Company Name', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_cmp_.place(x=10, y=1)
        ent_cmp_ = Entry(frm_cmp_, textvariable=self.var_cmp_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_cmp_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_cmc_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_cmc_.pack(fill=BOTH, expand=True)
        lbl_cmc_ = Label(frm_cmc_, text='Company Contact', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_cmc_.place(x=10, y=1)
        ent_cmc_ = Entry(frm_cmc_, textvariable=self.var_cmc_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_cmc_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_cme_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_cme_.pack(fill=BOTH, expand=True)
        lbl_cme_ = Label(frm_cme_, text='Company Email', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_cme_.place(x=10, y=1)
        ent_cme_ = Entry(frm_cme_, textvariable=self.var_cme_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_cme_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_des_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_des_.pack(fill=BOTH, expand=True)
        lbl_des_ = Label(frm_des_, text='Description', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_des_.place(x=10, y=1)
        ent_des_ = Entry(frm_des_, textvariable=self.var_des_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_des_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_note_1 = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=20)
        frm_note_1.pack(fill=BOTH, expand=True)
        lbl_note_1 = Label(frm_note_1, text='Purchase History Available In Supplier Detail Form Open It', font=(self.formset_mainF, 10), bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_note_1.place(x=10, y=1)
        btn_note_1 = Button(frm_note_1, command=lambda: self.open_libForm('Supplier Details'), justify=LEFT, text='+', font=(self.formset_mainF, 13), bd=0, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_note_1.place(x=self.dF_ent_x + self.dF_ent_w - 20, y=1, width=20, height=self.formset_fieldH)

        self.CommonCall2()

        # Record Frame
        self.recordFrame = Frame(self.root, bg=self.colorList[2])
        self.recordFrame.place(x=self.rF_x, y=self.rF_y, width=self.rF_w, height=self.rF_h)

        scroll_y = Scrollbar(self.recordFrame, orient=VERTICAL)
        scroll_x = Scrollbar(self.recordFrame, orient=HORIZONTAL)

        self.Table = ttk.Treeview(self.recordFrame, columns=['id', 'sup_', 'add_', 'phn_', 'eml_', 'cmp_', 'cmc_', 'cme_', 'des_'], yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.config(command=self.Table.yview)
        scroll_x.config(command=self.Table.xview)
        self.Table.heading('id', text='ID')
        self.Table.heading('sup_', text='Supplier Name')
        self.Table.heading('add_', text='Address')
        self.Table.heading('phn_', text='Phone')
        self.Table.heading('eml_', text='Email')
        self.Table.heading('cmp_', text='Company Name')
        self.Table.heading('cmc_', text='Company Contact')
        self.Table.heading('cme_', text='Company Email')
        self.Table.heading('des_', text='Description')
        self.Table["show"] = "headings"
        self.Table.column('id', width=50)
        self.Table.column('sup_', width=100)
        self.Table.column('add_', width=150)
        self.Table.column('phn_', width=150)
        self.Table.column('eml_', width=150)
        self.Table.column('cmp_', width=100)
        self.Table.column('cmc_', width=150)
        self.Table.column('cme_', width=150)
        self.Table.column('des_', width=150)
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
        self.var_sup_ = StringVar()  # Supplier Name
        self.var_add_ = StringVar()  # Address
        self.var_phn_ = StringVar()  # Phone
        self.var_eml_ = StringVar()  # Email
        self.var_cmp_ = StringVar()  # Company Name
        self.var_cmc_ = StringVar()  # Company Contact
        self.var_cme_ = StringVar()  # Company Email
        self.var_des_ = StringVar()  # Description

    def Export_def(self):
        gg = self.Table.get_children()
        id = []
        sup_ = []
        add_ = []
        phn_ = []
        eml_ = []
        cmp_ = []
        cmc_ = []
        cme_ = []
        des_ = []
        count = 0
        for i in gg:
            content = self.Table.item(i)
            pp = content['values']
            count += 1
            id.append(str(count))
            sup_.append(pp[1])
            add_.append(pp[2])
            phn_.append(pp[3])
            eml_.append(pp[4])
            cmp_.append(pp[5])
            cmc_.append(pp[6])
            cme_.append(pp[7])
            des_.append(pp[8])

        headings = self.__list__('head')
        expList = list(zip(id, sup_, add_, phn_, eml_, cmp_, cmc_, cme_, des_))
        Log_Generator().addLog(f'[Export] {count} Record Found')
        return count, headings, expList

    def Get_Data(self, e):
        try:
            f = self.Table.focus()
            content = (self.Table.item(f))
            row = content['values']
            self.var_id.set(row[0])
            self.var_sup_.set(row[1])
            self.var_add_.set(row[2])
            self.var_phn_.set(row[3])
            self.var_eml_.set(row[4])
            self.var_cmp_.set(row[5])
            self.var_cmc_.set(row[6])
            self.var_cme_.set(row[7])
            self.var_des_.set(row[8])

            self.status(f'[{self.mainName}] [Get Data] Record {self.var_id.get()} Selected Successfully')
        except Exception as ex:
            self.status(f'[{self.mainName}] [Get Data] Error: {ex}')
            pass

    def StarterDb(self, db='sqlite'):
        if db == 'sqlite':
            self.cur.execute('''CREATE TABLE IF NOT EXISTS "''' + self.mainName.replace(' ', '_') + '''" (
                "id"	INTEGER NOT NULL UNIQUE,
                "sup_"	TEXT,
                "add_"	TEXT,
                "phn_"	TEXT,
                "eml_"	TEXT,
                "cmp_"	TEXT,
                "cmc_"	TEXT,
                "cme_"	TEXT,
                "des_"	TEXT,
                PRIMARY KEY("id" AUTOINCREMENT))''')
            self.con.commit()
        else:
            self.cur.execute(
                '''CREATE TABLE IF NOT EXISTS ''' + self.mainName.replace(' ', '_') + ''' (
                id SERIAL NOT NULL AUTO_INCREMENT
                , sup_ TEXT NOT NULL
                , add_ TEXT NOT NULL
                , phn_ TEXT NOT NULL
                , eml_ TEXT NOT NULL
                , cmp_ TEXT NOT NULL
                , cmc_ TEXT NOT NULL
                , cme_ TEXT NOT NULL
                , des_ TEXT NOT NULL )''')
            self.con.commit()

    def __list__(self, fetch):
        list_var = [self.var_id, self.var_sup_, self.var_add_, self.var_phn_, self.var_eml_, self.var_cmp_, self.var_cmc_, self.var_cme_, self.var_des_]
        list_shn = ['id', 'sup_', 'add_', 'phn_', 'eml_', 'cmp_', 'cmc_', 'cme_', 'des_']
        list_cvar = [[self.var_id, 'ID'], [self.var_sup_, 'Supplier Name'], [self.var_add_, 'Address'], [self.var_phn_, 'Phone']]
        list_head = ['ID', 'Supplier Name', 'Address', 'Phone', 'Email', 'Company Name', 'Company Contact', 'Company Email', 'Description']
        list_headA = ['ID', 'Supplier Name', 'Address', 'Phone', 'Email', 'Company Name', 'Company Contact', 'Company Email', 'Description']

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
    obj = Supplier(root)
    root.mainloop()
    Log_Generator().closeLog()
