from tkinter import *
from tkinter import ttk, messagebox, filedialog
from tkcalendar import Calendar, DateEntry
import os, random, time, pandas, csv, threading
import pymysql, sqlite3
from reportlab.lib import colors as abcdef
from reportlab.lib import pagesizes  # For creating reports
from reportlab.lib.units import mm, inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle  # For creating reports
from reportlab.lib.styles import getSampleStyleSheet  # For creating reports
from datetime import datetime, timedelta
# import openpyxl # for creating the excel report xlsx format

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


class Demo(BeforeInIt, AllSettings, CommonFunction):
    wSize, hSize = 800, 550
    title = "Demo - Company Management System"
    mainName = "Demo"

    def __init__(self, wind) -> None:
        self.root = wind
        self.sortKey = 'x[2]'
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
        ent_id.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w)

        frm_dat_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_dat_.pack(fill=BOTH, expand=True)
        lbl_dat_ = Label(frm_dat_, text='Date', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_dat_.place(x=10, y=1)
        ent_dat_ = DateEntry(frm_dat_, textvariable=self.var_dat_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12], justify=CENTER, date_pattern='dd-mm-y')
        ent_dat_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w - 10)
        def cls_dat_():
            self.var_dat_.set("")
            ent_dat_.update()
        btn_dat_ = Button(frm_dat_, command=cls_dat_, justify=LEFT, text='-', font=(self.formset_mainF, 13), bd=0, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_dat_.place(x=self.dF_ent_x + self.dF_ent_w - 10, y=1, width=10, height=25)

        frm_reg_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_reg_.pack(fill=BOTH, expand=True)
        lbl_reg_ = Label(frm_reg_, text='Region', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_reg_.place(x=10, y=1)
        cmb_reg__list = ['Lahore', 'Karachi', 'Peshawar', 'quetta']
        cmb_reg_ = AutocompleteCombobox(frm_reg_, values=cmb_reg__list, textvariable=self.var_reg_, font=self.formset_mainF, background=self.colorList[9], foreground=self.colorList[10])
        cmb_reg_.set_completion_list(cmb_reg__list)
        cmb_reg_.tk.eval(f'[ttk::combobox::PopdownWindow %s].f.l configure -background {self.colorList[13]}' % cmb_reg_)
        cmb_reg_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w)
        cmb_reg_.current(0)

        self.CommonCall2()

        # Record Frame
        self.recordFrame = Frame(self.root, bg=self.colorList[2])
        self.recordFrame.place(x=self.rF_x, y=self.rF_y, width=self.rF_w, height=self.rF_h)

        scroll_y = Scrollbar(self.recordFrame, orient=VERTICAL)
        scroll_x = Scrollbar(self.recordFrame, orient=HORIZONTAL)

        self.Table = ttk.Treeview(self.recordFrame, columns=['id','dat_','reg_'], yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.config(command=self.Table.yview)
        scroll_x.config(command=self.Table.xview)
        self.Table.heading('id', text='ID')
        self.Table.heading('dat_', text='Date')
        self.Table.heading('reg_', text='Region')
        self.Table["show"] = "headings"
        self.Table.column('id')
        self.Table.column('dat_')
        self.Table.column('reg_')
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
        self.var_reg_ = StringVar()  # Region

    def Export_def(self):
        gg = self.Table.get_children()
        id = []
        dat_ = []
        reg_ = []
        count = 0
        for i in gg:
            content = self.Table.item(i)
            pp = content['values']
            count += 1
            id.append(str(count))
            dat_.append(pp[1])
            reg_.append(pp[2])

        headings = self.__list__('head')
        expList = list(zip(id,dat_,reg_))
        Log_Generator().addLog(f'[Export] {count} Record Found')
        return count, headings, expList

    def Get_Data(self, e):
        try:
            f = self.Table.focus()
            content = (self.Table.item(f))
            row = content['values']
            self.var_id.set(row[0])
            self.var_dat_.set(row[1])
            self.var_reg_.set(row[2])

            self.status(f'[{self.mainName}] [Get Data] Record {self.var_id.get()} Selected Successfully')
        except Exception as ex:
            self.status(f'[{self.mainName}] [Get Data] Error: {ex}')
            pass

    def EnableDb(self):
        try:
            open_db_set = open(self.setting_folder + '\\Database Configurations', 'r')
            txt_db_set = open_db_set.readlines()
            open_db_set.close()
            _, db_type = txt_db_set[0].strip('\n').split(':')
            db_type, *_ = db_type.split('.')
            Log_Generator().addLog(f'[Database] {db_type}', )

            if db_type == 'sqlite':
                try:
                    self.con = sqlite3.connect(database=self.database)
                    self.cur = self.con.cursor()
                    Log_Generator().addLog('[Database] Connected with sqlite')

                    try:
                        self.cur.execute('''CREATE TABLE IF NOT EXISTS "''' + self.mainName.replace(' ', '_') + '''" (
                            "id"	INTEGER NOT NULL UNIQUE,
                            "dat_"	TEXT,
                            "reg_"	TEXT,
                            PRIMARY KEY("id" AUTOINCREMENT)
                        )
                        ''')
                        self.con.commit()
                        self.lbl_status.config(text='Database: Enabled')
                        Log_Generator().addLog('[Database] Enabled')
                    except Exception as e:
                        Log_Generator().addLog(f'[DB Error] {e}')

                except Exception as e:
                    Log_Generator().addLog(f'[DB Error] {e}')
                    messagebox.showerror('Error', str(e) + '\n\nContact With Creator +923150490481', parent=self.root)

            elif db_type == 'mysql':
                _, host_ = txt_db_set[1].strip('\n').split(':')
                host_, *_ = db_type.split('.')
                _, user_ = txt_db_set[2].strip('\n').split(':')
                user_, *_ = db_type.split('.')
                _, password_ = txt_db_set[3].strip('\n').split(':')
                password_, *_ = db_type.split('.')

                try:
                    self.con = pymysql.connect(host=host_, user=user_, passwd=password_)
                    self.cur = self.con.cursor()
                    Log_Generator().addLog('[Database] Login successfully')
                    db_login = True
                except Exception as e:
                    db_login = False
                    Log_Generator().addLog(f'[DB Error] {e}')
                    messagebox.showerror('Error', str(e) + '\n\nContact With Creator +923150490481', parent=self.root)

                if db_login:
                    try:
                        self.cur.execute('use AS_DB')
                        Log_Generator().addLog(f'[Database] Connected with mysql')
                    except Exception as e:
                        self.cur.execute('create database AS_DB')
                        self.cur.execute('use AS_DB')
                        Log_Generator().addLog(f'[Database] Created and Connected with mysql')

                    try:
                        self.cur.execute(
                            '''CREATE TABLE IF NOT EXISTS ''' + self.mainName.replace(' ', '_') + ''' ( id SERIAL NOT NULL AUTO_INCREMENT 
                              , dat_ TEXT NOT NULL
                              , reg_ TEXT NOT NULL )''')
                        self.con.commit()
                        self.lbl_status.config(text='Database: Enabled')
                        Log_Generator().addLog('[Database] Enabled')
                    except Exception as e:
                        Log_Generator().addLog(f'[DB Error] {e}')
                else:
                    messagebox.showerror('Error',
                                         'Enter Correct Database Credentials We are not able to Login Database\n\nContact With Creator +923150490481',
                                         parent=self.root)
                    Log_Generator().addLog(f'[DB Error] Wrong Credentials You Enter')
                    # Call DB Settings
            else:
                messagebox.showerror('Error',
                                     'Select Database We Cannot Find Any Database\n\nContact With Creator +923150490481',
                                     parent=self.root)
                Log_Generator().addLog(f'[DB Error] Cannot Find Database Setting')
                # Call DB Settings
        except Exception as e:
            Log_Generator().addLog(f'[DB Error] {e}')
            messagebox.showerror('Error', str(e) + '\n\nContact With Creator +923150490481', parent=self.root)

    def __list__(self, fetch):
        list_var = [
            self.var_id,
            self.var_dat_,
            self.var_reg_
        ]
        list_shn = [
            'id',
            'dat_',
            'reg_'
        ]
        list_cvar = [
            [self.var_id, 'ID'],
            [self.var_dat_, 'Date'],
            [self.var_reg_, 'Region']
        ]
        list_head = ['ID','Date','Region']

        if fetch == 'var':
            return list_var
        elif fetch == 'cvar':
            return list_cvar
        elif fetch == 'shn':
            return list_shn
        elif fetch == 'head':
            return list_head

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
    obj = Demo(root)
    root.mainloop()
    Log_Generator().closeLog()
