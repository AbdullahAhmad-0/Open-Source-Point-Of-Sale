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


class UserRole(BeforeInIt, AllSettings, CommonFunction):
    wSize, hSize = 800, 550
    title = "User Role - Point Of Sale"
    mainName = "User Role"

    def __init__(self, wind, libFormList=[]) -> None:
        BeforeInIt.__init__(self)
        AllSettings.__init__(self)
        super().__init__()
        self.root = wind
        self.sortKey = 'x[0]'
        self.split_pdf_rep = {3:', '}
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
        lbl_fln_ = Label(frm_fln_, text='Role Name', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_fln_.place(x=10, y=1)
        ent_fln_ = Entry(frm_fln_, textvariable=self.var_fln_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_fln_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_adr_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_adr_.pack(fill=BOTH, expand=True)
        lbl_adr_ = Label(frm_adr_, text='Description', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_adr_.place(x=10, y=1)
        ent_adr_ = Entry(frm_adr_, textvariable=self.var_adr_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_adr_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_frl__temp = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_frl__temp.pack(fill=BOTH, expand=True)
        lbl_frl__temp = Label(frm_frl__temp, text='Forms List', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_frl__temp.place(x=10, y=1)
        cmb_frl__temp_list = self.getFormsName()
        cmb_frl__temp = AutocompleteCombobox(frm_frl__temp, values=cmb_frl__temp_list, textvariable=self.var_frl__temp, font=self.formset_mainF, background=self.colorList[9], foreground=self.colorList[10])
        cmb_frl__temp.set_completion_list(cmb_frl__temp_list)
        cmb_frl__temp.tk.eval(f'[ttk::combobox::PopdownWindow %s].f.l configure -background {self.colorList[13]}' % cmb_frl__temp)
        cmb_frl__temp.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)
        cmb_frl__temp.current(0)

        frm_fnl__temp = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space * 5)
        frm_fnl__temp.pack(fill=BOTH, expand=True)

        self.var_fnl__temp_temp = StringVar()
        lbl_fnl__temp = Label(frm_fnl__temp, text='Function List', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_fnl__temp.place(x=10, y=1)
        cmb_fnl__temp_list = self.getFuncList()
        lbl_fnl__temp = Label(frm_fnl__temp, text='Function List', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_fnl__temp.place(x=10, y=1)
        cmb_fnl__temp_list = cmb_fnl__temp_list
        cmb_fnl__temp = AutocompleteCombobox(frm_fnl__temp, values=cmb_fnl__temp_list, textvariable=self.var_fnl__temp_temp, font=self.formset_mainF, background=self.colorList[9], foreground=self.colorList[10])
        cmb_fnl__temp.set_completion_list(cmb_fnl__temp_list)
        cmb_fnl__temp.tk.eval(f'[ttk::combobox::PopdownWindow %s].f.l configure -background {self.colorList[13]}' % cmb_fnl__temp)
        cmb_fnl__temp.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w - 100, height=self.formset_fieldH)
        cmb_fnl__temp.current(0)

        btn_fnl__temp = Button(frm_fnl__temp, command=lambda: self.list_ndc_Add(lis_fnl__temp, self.var_fnl__temp_temp, self.var_fnl__temp, cmb_fnl__temp_list, cmb_fnl__temp), justify=LEFT, text='Add', font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_fnl__temp.place(x=self.dF_ent_x + self.dF_ent_w - 99, y=1, width=50, height=self.formset_fieldH)
        btn_fnl__temp = Button(frm_fnl__temp, command=lambda: self.list_ndc_Del(lis_fnl__temp, self.var_fnl__temp, self.var_fnl__temp_temp, cmb_fnl__temp_list, cmb_fnl__temp), justify=LEFT, text='Delete', font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_fnl__temp.place(x=self.dF_ent_x + self.dF_ent_w - 49, y=1, width=50, height=self.formset_fieldH)
        lis_fnl__temp = Listbox(frm_fnl__temp, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lis_fnl__temp.place(x=self.dF_ent_x, y=1 + y_space, width=self.dF_ent_w - 10, height=55 + (y_space * 2))
        scl_fnl__temp = Scrollbar(frm_fnl__temp)
        scl_fnl__temp.place(x=self.dF_ent_x + self.dF_ent_w - 10, y=1 + y_space, width=10, height=55 + (y_space * 2))
        lis_fnl__temp.config(yscrollcommand=scl_fnl__temp.set)
        scl_fnl__temp.config(command=lis_fnl__temp.yview)
        # Bind the function to the StringVar object
        self.var_fnl__temp.trace("w", lambda name, index, mode: self.bindList_ndc(lis_fnl__temp, self.var_fnl__temp_temp, self.var_fnl__temp, cmb_fnl__temp_list, cmb_fnl__temp))

        frm_acf_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=(y_space * 11) + 10)
        frm_acf_.pack(fill=BOTH, expand=True)
        self.var_acf__temp = StringVar()
        lbl_acf_ = Label(frm_acf_, text='Accessible Forms', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_acf_.place(x=10, y=1)

        btn_acf_ = Button(frm_acf_, command=lambda: self.add_accessableForms(lis_acf_, self.var_acf_), justify=LEFT, text='Add', font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_acf_.place(x=self.dF_ent_x + self.dF_ent_w - 99, y=1, width=50, height=self.formset_fieldH)
        btn_acf_ = Button(frm_acf_, command=lambda: self.list_Del(lis_acf_, self.var_acf_), justify=LEFT, text='Delete', font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_acf_.place(x=self.dF_ent_x + self.dF_ent_w - 49, y=1, width=50, height=self.formset_fieldH)

        lis_acf_ = Listbox(frm_acf_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lis_acf_.place(x=self.dF_ent_x, y=1 + y_space, width=self.dF_ent_w - 10, height=55 + (y_space * 8))
        scl_acf_ = Scrollbar(frm_acf_)
        scl_acf_.place(x=self.dF_ent_x + self.dF_ent_w - 10, y=1 + y_space, width=10, height=55 + (y_space * 8))
        lis_acf_.config(yscrollcommand=scl_acf_.set)
        scl_acf_.config(command=lis_acf_.yview)
        sclx_acf_ = Scrollbar(frm_acf_, orient=HORIZONTAL)
        sclx_acf_.place(x=self.dF_ent_x, y=1 + y_space + 55 + (y_space * 8), width=self.dF_ent_w, height=10)
        lis_acf_.config(xscrollcommand=sclx_acf_.set)
        sclx_acf_.config(command=lis_acf_.xview)

        # Bind the function to the StringVar object
        self.var_acf_.trace("w", lambda name, index, mode: self.bindList_ndc(lis_acf_, self.var_acf__temp, self.var_acf_, cmb_frl__temp_list, cmb_frl__temp, ':'))
        lis_acf_.bind("<<ListboxSelect>>", self.on_select)

        self.CommonCall2()

        # Record Frame
        self.recordFrame = Frame(self.root, bg=self.colorList[2])
        self.recordFrame.place(x=self.rF_x, y=self.rF_y, width=self.rF_w, height=self.rF_h)

        scroll_y = Scrollbar(self.recordFrame, orient=VERTICAL)
        scroll_x = Scrollbar(self.recordFrame, orient=HORIZONTAL)

        self.Table = ttk.Treeview(self.recordFrame, columns=['id', 'fln_', 'adr_', 'acf_'], yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.config(command=self.Table.yview)
        scroll_x.config(command=self.Table.xview)
        self.Table.heading('id', text='ID')
        self.Table.heading('fln_', text='Role Name')
        self.Table.heading('adr_', text='Description')
        self.Table.heading('acf_', text='Accessible Forms')
        self.Table["show"] = "headings"
        self.Table.column('id', width=50)
        self.Table.column('fln_', width=150)
        self.Table.column('adr_', width=250)
        self.Table.column('acf_', width=150)
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
        self.var_fln_ = StringVar()  # Role Name
        self.var_adr_ = StringVar()  # Description
        self.var_acf_ = StringVar()  # Accessible Forms
        self.var_frl__temp = StringVar()  # Forms List
        self.var_fnl__temp = StringVar()  # Function List

    def Export_def(self):
        gg = self.Table.get_children()
        id = []
        fln_ = []
        adr_ = []
        acf_ = []
        count = 0
        for i in gg:
            content = self.Table.item(i)
            pp = content['values']
            count += 1
            id.append(str(count))
            fln_.append(pp[1])
            adr_.append(pp[2])
            acf_.append(pp[3])

        headings = self.__list__('head')
        expList = list(zip(id, fln_, adr_, acf_))
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
            self.var_acf_.set(row[3])

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
                "acf_"	TEXT,
                PRIMARY KEY("id" AUTOINCREMENT))''')
            self.con.commit()
        else:
            self.cur.execute(
                '''CREATE TABLE IF NOT EXISTS ''' + self.mainName.replace(' ', '_') + ''' (
                id SERIAL NOT NULL AUTO_INCREMENT
                , fln_ TEXT NOT NULL
                , adr_ TEXT NOT NULL
                , acf_ TEXT NOT NULL )''')
            self.con.commit()

    def __list__(self, fetch):
        list_var = [self.var_id, self.var_fln_, self.var_adr_, self.var_acf_]
        list_shn = ['id', 'fln_', 'adr_', 'acf_']
        list_cvar = [[self.var_id, 'ID'], [self.var_fln_, 'Role Name'], [self.var_acf_, 'Accessible Forms']]
        list_head = ['ID', 'Role Name', 'Description', 'Accessible Forms']
        list_headA = ['ID', 'Role Name', 'Description', 'Accessible Forms']
        list_extra_clear = [self.var_frl__temp, self.var_fnl__temp, self.var_fnl__temp_temp]
        list_colWidth = [50, 150, 250, 150]

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
        elif fetch == 'extra_clear':
            return list_extra_clear
        elif fetch == 'colWidth':
            return list_colWidth

    def add_accessableForms(self, lis, outVar):
        def _fnl(frl):
            ls = self.getFuncList()
            items = ''
            for i in ls:
                items += str(i) + ','
            ls = f'{frl}:{items.strip(",")}'

            for i, item in enumerate(lis.get(0, END)):
                try:
                    name, value = item.split(':')
                    if name == ls.split(':')[0]:
                        lis.delete(i)
                        break
                except:
                    pass
            lis.insert(END, ls)

        ls = f'{self.var_frl__temp.get()}:{self.var_fnl__temp.get().replace(", ", ",")}'
        if self.var_frl__temp.get() == '':
            fnl = self.getFormsName()
            for i in fnl:
                _fnl(i)
        elif self.var_fnl__temp.get() == '':
            _fnl(self.var_frl__temp.get())
        elif ls != "" and ls.strip('\t') != '':
            for i, item in enumerate(lis.get(0, END)):
                try:
                    name, value = item.split(':')
                    if name == ls.split(':')[0]:
                        lis.delete(i)
                        break
                except:
                    pass
            lis.insert(END, ls)

        self.var_frl__temp.set('')
        self.var_fnl__temp.set('')

        items = ''
        for i in range(lis.size()):
            items += lis.get(i) + ', '
        items = items.strip(', ')

        outVar.set(items)

    def on_select(self, event):
        try:
            index = event.widget.curselection()[0]
            value = event.widget.get(index)
            frl, fnl = value.split(':')
            self.var_frl__temp.set(frl)
            self.var_fnl__temp.set(fnl.replace(",", ", "))
        except:
            pass

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
    obj = UserRole(root)
    root.mainloop()
    Log_Generator().closeLog()
