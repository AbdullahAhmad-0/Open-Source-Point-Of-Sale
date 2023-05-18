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


class temp(BeforeInIt, AllSettings, CommonFunction):
    wSize, hSize = 800, 550
    title = "temp - Point Of Sale"
    mainName = "temp"

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

        frm_bar_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=(y_space * 5) + 10)
        frm_bar_.pack(fill=BOTH, expand=True)
        
        self.var_bar__temp = StringVar()
        lbl_bar_ = Label(frm_bar_, text='Barcode', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_bar_.place(x=10, y=1)
        ent_bar_ = Entry(frm_bar_, textvariable=self.var_bar__temp, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_bar_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w - 100, height=self.formset_fieldH)
        
        btn_bar_ = Button(frm_bar_, command=lambda : self.list_nd_Add(lis_bar_, self.var_bar__temp, self.var_bar_), justify=LEFT, text='Add', font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_bar_.place(x=self.dF_ent_x + self.dF_ent_w - 99, y=1, width=50, height=self.formset_fieldH)
        btn_bar_ = Button(frm_bar_, command=lambda : self.list_Del(lis_bar_, self.var_bar_), justify=LEFT, text='Delete', font=(self.formset_mainF, 13), bd=1, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
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

        self.CommonCall2()

        # Record Frame
        self.recordFrame = Frame(self.root, bg=self.colorList[2])
        self.recordFrame.place(x=self.rF_x, y=self.rF_y, width=self.rF_w, height=self.rF_h)

        scroll_y = Scrollbar(self.recordFrame, orient=VERTICAL)
        scroll_x = Scrollbar(self.recordFrame, orient=HORIZONTAL)

        self.Table = ttk.Treeview(self.recordFrame, columns=['id', 'bar_'], yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.config(command=self.Table.yview)
        scroll_x.config(command=self.Table.xview)
        self.Table.heading('id', text='ID')
        self.Table.heading('bar_', text='Barcode')
        self.Table["show"] = "headings"
        self.Table.column('id', width=50)
        self.Table.column('bar_', width=100)
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
        self.var_bar_ = StringVar()  # Barcode

    def Export_def(self):
        gg = self.Table.get_children()
        id = []
        bar_ = []
        count = 0
        for i in gg:
            content = self.Table.item(i)
            pp = content['values']
            count += 1
            id.append(str(count))
            bar_.append(pp[1])

        headings = self.__list__('head')
        expList = list(zip(id, bar_))
        Log_Generator().addLog(f'[Export] {count} Record Found')
        return count, headings, expList

    def Get_Data(self, e):
        try:
            f = self.Table.focus()
            content = (self.Table.item(f))
            row = content['values']
            self.var_id.set(row[0])
            self.var_bar_.set(row[1])

            self.status(f'[{self.mainName}] [Get Data] Record {self.var_id.get()} Selected Successfully')
        except Exception as ex:
            self.status(f'[{self.mainName}] [Get Data] Error: {ex}')
            pass

    def StarterDb(self, db='sqlite'):
        if db == 'sqlite':
            self.cur.execute('''CREATE TABLE IF NOT EXISTS "''' + self.mainName.replace(' ', '_') + '''" (
                "id"	INTEGER NOT NULL UNIQUE,
                "bar_"	TEXT,
                PRIMARY KEY("id" AUTOINCREMENT))''')
            self.con.commit()
        else:
            self.cur.execute(
                '''CREATE TABLE IF NOT EXISTS ''' + self.mainName.replace(' ', '_') + ''' (
                id SERIAL NOT NULL AUTO_INCREMENT
                , bar_ TEXT NOT NULL )''')
            self.con.commit()

    def __list__(self, fetch):
        list_var = [self.var_id, self.var_bar_]
        list_shn = ['id', 'bar_']
        list_cvar = [[self.var_id, 'ID'], [self.var_bar_, 'Barcode']]
        list_head = ['ID', 'Barcode']
        list_headA = ['ID', 'Barcode']

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
    obj = temp(root)
    root.mainloop()
    Log_Generator().closeLog()
