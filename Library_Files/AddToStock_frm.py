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


class AddToStock(BeforeInIt, AllSettings, CommonFunction):
    wSize, hSize = 800, 550
    title = "Add To Stock - Point Of Sale"
    mainName = "Add To Stock"

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

        frm_prc_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_prc_.pack(fill=BOTH, expand=True)
        lbl_prc_ = Label(frm_prc_, text='Product Code', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_prc_.place(x=10, y=1)
        cmb_prc__list = ['']
        cmb_prc_ = AutocompleteCombobox(frm_prc_, values=cmb_prc__list, textvariable=self.var_prc_, font=self.formset_mainF, background=self.colorList[9], foreground=self.colorList[10])
        cmb_prc_.set_completion_list(cmb_prc__list)
        cmb_prc_.tk.eval(f'[ttk::combobox::PopdownWindow %s].f.l configure -background {self.colorList[13]}' % cmb_prc_)
        cmb_prc_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w - 21, height=self.formset_fieldH)
        btn_prc_ = Button(frm_prc_, command=lambda: self.get_combo_list("select Product from Product", cmb_prc_, self.var_prc_), justify=LEFT, text='🔃', font=(self.formset_mainF, 13), bd=0, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_prc_.place(x=self.dF_ent_x + self.dF_ent_w - 21, y=1, width=10, height=self.formset_fieldH)
        btn_prc_ = Button(frm_prc_, command=lambda: self.open_libForm('Product'), justify=LEFT, text='+', font=(self.formset_mainF, 13), bd=0, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_prc_.place(x=self.dF_ent_x + self.dF_ent_w - 10, y=1, width=10, height=self.formset_fieldH)
        self.get_combo_list("select prc_ from Product", cmb_prc_, self.var_prc_)
        self.set_combo_text("select prn_, cat_, sct_ from Product where prc_='{var}'", self.var_prc_, cmb_prc_, [self.var_prn_, self.var_cat_, self.var_sct_])
        cmb_prc_.current(0)

        frm_prn_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_prn_.pack(fill=BOTH, expand=True)
        lbl_prn_ = Label(frm_prn_, text='Product Name', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_prn_.place(x=10, y=1)
        ent_prn_ = Entry(frm_prn_, textvariable=self.var_prn_, border=0, font=self.formset_mainF, disabledbackground=self.colorList[14], disabledforeground=self.colorList[15], state=DISABLED, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_prn_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_cat_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_cat_.pack(fill=BOTH, expand=True)
        lbl_cat_ = Label(frm_cat_, text='Category', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_cat_.place(x=10, y=1)
        ent_cat_ = Entry(frm_cat_, textvariable=self.var_cat_, border=0, font=self.formset_mainF, disabledbackground=self.colorList[14], disabledforeground=self.colorList[15], state=DISABLED, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_cat_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_sct_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_sct_.pack(fill=BOTH, expand=True)
        lbl_sct_ = Label(frm_sct_, text='Sub Category', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_sct_.place(x=10, y=1)
        ent_sct_ = Entry(frm_sct_, textvariable=self.var_sct_, border=0, font=self.formset_mainF, disabledbackground=self.colorList[14], disabledforeground=self.colorList[15], state=DISABLED, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_sct_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_des_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_des_.pack(fill=BOTH, expand=True)
        lbl_des_ = Label(frm_des_, text='Description', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_des_.place(x=10, y=1)
        ent_des_ = Entry(frm_des_, textvariable=self.var_des_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_des_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_bar_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_bar_.pack(fill=BOTH, expand=True)
        lbl_bar_ = Label(frm_bar_, text='Barcode', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_bar_.place(x=10, y=1)
        ent_bar_ = Entry(frm_bar_, textvariable=self.var_bar_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_bar_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_snw_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_snw_.pack(fill=BOTH, expand=True)
        lbl_snw_ = Label(frm_snw_, text='Size n Weight', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_snw_.place(x=10, y=1)
        ent_snw_ = Entry(frm_snw_, textvariable=self.var_snw_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_snw_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_sup_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_sup_.pack(fill=BOTH, expand=True)
        lbl_sup_ = Label(frm_sup_, text='Supplier', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_sup_.place(x=10, y=1)
        cmb_sup__list = ['']
        cmb_sup_ = AutocompleteCombobox(frm_sup_, values=cmb_sup__list, textvariable=self.var_sup_, font=self.formset_mainF, background=self.colorList[9], foreground=self.colorList[10])
        cmb_sup_.set_completion_list(cmb_sup__list)
        cmb_sup_.tk.eval(f'[ttk::combobox::PopdownWindow %s].f.l configure -background {self.colorList[13]}' % cmb_sup_)
        cmb_sup_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w - 21, height=self.formset_fieldH)
        btn_sup_ = Button(frm_sup_, command=lambda: self.get_combo_list("select Supploer from Supplier", cmb_sup_, self.var_sup_), justify=LEFT, text='🔃', font=(self.formset_mainF, 13), bd=0, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_sup_.place(x=self.dF_ent_x + self.dF_ent_w - 21, y=1, width=10, height=self.formset_fieldH)
        btn_sup_ = Button(frm_sup_, command=lambda: self.open_libForm('Supplier'), justify=LEFT, text='+', font=(self.formset_mainF, 13), bd=0, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_sup_.place(x=self.dF_ent_x + self.dF_ent_w - 10, y=1, width=10, height=self.formset_fieldH)
        self.get_combo_list("select sup_ from Supplier", cmb_sup_, self.var_sup_)
        cmb_sup_.current(0)

        def mrk_():
            slp_ = self.GetNumber(self.var_slp_)
            self.var_slp_.set(slp_)
            unp_ = self.GetNumber(self.var_unp_)
            self.var_unp_.set(unp_)
            self.var_mrk_.set(str(slp_ - unp_))
        frm_unp_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_unp_.pack(fill=BOTH, expand=True)
        lbl_unp_ = Label(frm_unp_, text='Unit Price', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_unp_.place(x=10, y=1)
        ent_unp_ = Entry(frm_unp_, textvariable=self.var_unp_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_unp_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)
        ent_unp_.bind("<KeyRelease>", lambda e, x=self.var_unp_: (self.convertToNo(e, x), mrk_()))

        frm_slp_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_slp_.pack(fill=BOTH, expand=True)
        lbl_slp_ = Label(frm_slp_, text='Sale Price', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_slp_.place(x=10, y=1)
        ent_slp_ = Entry(frm_slp_, textvariable=self.var_slp_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_slp_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)
        ent_slp_.bind("<KeyRelease>", lambda e, x=self.var_slp_: (self.convertToNo(e, x), mrk_()))

        frm_mrk_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_mrk_.pack(fill=BOTH, expand=True)
        lbl_mrk_ = Label(frm_mrk_, text='Markup', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_mrk_.place(x=10, y=1)
        ent_mrk_ = Entry(frm_mrk_, textvariable=self.var_mrk_, border=0, font=self.formset_mainF, disabledbackground=self.colorList[14], disabledforeground=self.colorList[15], state=DISABLED, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_mrk_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_tax_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_tax_.pack(fill=BOTH, expand=True)
        lbl_tax_ = Label(frm_tax_, text='Tax', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_tax_.place(x=10, y=1)
        ent_tax_ = Entry(frm_tax_, textvariable=self.var_tax_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_tax_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)
        ent_tax_.bind("<KeyRelease>", lambda e, x=self.var_tax_: self.convertToNo(e, x))

        frm_dis_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_dis_.pack(fill=BOTH, expand=True)
        lbl_dis_ = Label(frm_dis_, text='Discount', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_dis_.place(x=10, y=1)
        ent_dis_ = Entry(frm_dis_, textvariable=self.var_dis_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_dis_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)
        ent_dis_.bind("<KeyRelease>", lambda e, x=self.var_dis_: self.convertToNo(e, x))

        frm_prp_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_prp_.pack(fill=BOTH, expand=True)
        lbl_prp_ = Label(frm_prp_, text='Product Price', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_prp_.place(x=10, y=1)
        ent_prp_ = Entry(frm_prp_, textvariable=self.var_prp_, border=0, font=self.formset_mainF, disabledbackground=self.colorList[14], disabledforeground=self.colorList[15], state=DISABLED, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_prp_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_qty_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_qty_.pack(fill=BOTH, expand=True)
        lbl_qty_ = Label(frm_qty_, text='Total Qty', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_qty_.place(x=10, y=1)
        ent_qty_ = Entry(frm_qty_, textvariable=self.var_qty_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_qty_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)
        ent_qty_.bind("<KeyRelease>", lambda e, x=self.var_qty_: self.convertToNo(e, x))

        frm_sld_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_sld_.pack(fill=BOTH, expand=True)
        lbl_sld_ = Label(frm_sld_, text='Sold', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_sld_.place(x=10, y=1)
        ent_sld_ = Entry(frm_sld_, textvariable=self.var_sld_, border=0, font=self.formset_mainF, disabledbackground=self.colorList[14], disabledforeground=self.colorList[15], state=DISABLED, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_sld_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_exd_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_exd_.pack(fill=BOTH, expand=True)
        lbl_exd_ = Label(frm_exd_, text='Expire Date', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_exd_.place(x=10, y=1)
        ent_exd_ = DateEntry(frm_exd_, textvariable=self.var_exd_, border=0, font=self.formset_mainF, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12], justify=CENTER, date_pattern='dd-mm-y')
        ent_exd_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w - 10, height=self.formset_fieldH)
        def cls_exd_():
            self.var_exd_.set("")
            ent_exd_.update()
        btn_exd_ = Button(frm_exd_, command=cls_exd_, justify=LEFT, text='-', font=(self.formset_mainF, 13), bd=0, cursor='hand2', bg=self.colorList[5], activeforeground=self.colorList[22], activebackground=self.colorList[21], fg=self.colorList[6])
        btn_exd_.place(x=self.dF_ent_x + self.dF_ent_w - 10, y=1, width=10, height=self.formset_fieldH)

        frm_exp_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_exp_.pack(fill=BOTH, expand=True)
        lbl_exp_ = Label(frm_exp_, text='Expired Products', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_exp_.place(x=10, y=1)
        ent_exp_ = Entry(frm_exp_, textvariable=self.var_exp_, border=0, font=self.formset_mainF, disabledbackground=self.colorList[14], disabledforeground=self.colorList[15], state=DISABLED, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_exp_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_inv_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_inv_.pack(fill=BOTH, expand=True)
        lbl_inv_ = Label(frm_inv_, text='Inventory Value', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_inv_.place(x=10, y=1)
        ent_inv_ = Entry(frm_inv_, textvariable=self.var_inv_, border=0, font=self.formset_mainF, disabledbackground=self.colorList[14], disabledforeground=self.colorList[15], state=DISABLED, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_inv_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_rem_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_rem_.pack(fill=BOTH, expand=True)
        lbl_rem_ = Label(frm_rem_, text='Remaining Stock Value', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_rem_.place(x=10, y=1)
        ent_rem_ = Entry(frm_rem_, textvariable=self.var_rem_, border=0, font=self.formset_mainF, disabledbackground=self.colorList[14], disabledforeground=self.colorList[15], state=DISABLED, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_rem_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        frm_ssv_ = Frame(self.detailFrame, bg=self.colorList[2], width=self.dFbF_w - 10, height=y_space)
        frm_ssv_.pack(fill=BOTH, expand=True)
        lbl_ssv_ = Label(frm_ssv_, text='Sold Stock Value', font=self.formset_mainF, bg=self.colorList[7], fg=self.colorList[8], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        lbl_ssv_.place(x=10, y=1)
        ent_ssv_ = Entry(frm_ssv_, textvariable=self.var_ssv_, border=0, font=self.formset_mainF, disabledbackground=self.colorList[14], disabledforeground=self.colorList[15], state=DISABLED, bg=self.colorList[9], fg=self.colorList[10], highlightbackground=self.colorList[11], highlightthickness=2, highlightcolor=self.colorList[12])
        ent_ssv_.place(x=self.dF_ent_x, y=1, width=self.dF_ent_w, height=self.formset_fieldH)

        self.CommonCall2()

        # Record Frame
        self.recordFrame = Frame(self.root, bg=self.colorList[2])
        self.recordFrame.place(x=self.rF_x, y=self.rF_y, width=self.rF_w, height=self.rF_h)

        scroll_y = Scrollbar(self.recordFrame, orient=VERTICAL)
        scroll_x = Scrollbar(self.recordFrame, orient=HORIZONTAL)

        self.Table = ttk.Treeview(self.recordFrame, columns=['id', 'dat_', 'prc_', 'prn_', 'cat_', 'sct_', 'des_', 'bar_', 'snw_', 'sup_', 'unp_', 'slp_', 'mrk_', 'tax_', 'dis_', 'prp_', 'qty_', 'sld_', 'exd_', 'exp_', 'inv_', 'rem_', 'ssv_'], yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.config(command=self.Table.yview)
        scroll_x.config(command=self.Table.xview)
        self.Table.heading('id', text='ID')
        self.Table.heading('dat_', text='Date')
        self.Table.heading('prc_', text='Product Code')
        self.Table.heading('prn_', text='Product Name')
        self.Table.heading('cat_', text='Category')
        self.Table.heading('sct_', text='Sub Category')
        self.Table.heading('des_', text='Description')
        self.Table.heading('bar_', text='Barcode')
        self.Table.heading('snw_', text='Size n Weight')
        self.Table.heading('sup_', text='Supplier')
        self.Table.heading('unp_', text='Unit Price')
        self.Table.heading('slp_', text='Sale Price')
        self.Table.heading('mrk_', text='Markup')
        self.Table.heading('tax_', text='Tax')
        self.Table.heading('dis_', text='Discount')
        self.Table.heading('prp_', text='Product Price')
        self.Table.heading('qty_', text='Total Qty')
        self.Table.heading('sld_', text='Sold')
        self.Table.heading('exd_', text='Expire Date')
        self.Table.heading('exp_', text='Expired Products')
        self.Table.heading('inv_', text='Inventory Value')
        self.Table.heading('rem_', text='Remaining Stock Value')
        self.Table.heading('ssv_', text='Sold Stock Value')
        self.Table["show"] = "headings"
        self.Table.column('id', width=50)
        self.Table.column('dat_', width=100)
        self.Table.column('prc_', width=100)
        self.Table.column('prn_', width=100)
        self.Table.column('cat_', width=100)
        self.Table.column('sct_', width=100)
        self.Table.column('des_', width=100)
        self.Table.column('bar_', width=100)
        self.Table.column('snw_', width=100)
        self.Table.column('sup_', width=100)
        self.Table.column('unp_', width=100)
        self.Table.column('slp_', width=100)
        self.Table.column('mrk_', width=100)
        self.Table.column('tax_', width=100)
        self.Table.column('dis_', width=100)
        self.Table.column('prp_', width=100)
        self.Table.column('qty_', width=100)
        self.Table.column('sld_', width=100)
        self.Table.column('exd_', width=100)
        self.Table.column('exp_', width=100)
        self.Table.column('inv_', width=100)
        self.Table.column('rem_', width=100)
        self.Table.column('ssv_', width=100)
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
        self.var_prc_ = StringVar()  # Product Code
        self.var_prn_ = StringVar()  # Product Name
        self.var_cat_ = StringVar()  # Category
        self.var_sct_ = StringVar()  # Sub Category
        self.var_des_ = StringVar()  # Description
        self.var_bar_ = StringVar()  # Barcode
        self.var_snw_ = StringVar()  # Size n Weight
        self.var_sup_ = StringVar()  # Supplier
        self.var_unp_ = StringVar()  # Unit Price
        self.var_slp_ = StringVar()  # Sale Price
        self.var_mrk_ = StringVar()  # Markup
        self.var_tax_ = StringVar()  # Tax
        self.var_dis_ = StringVar()  # Discount
        self.var_prp_ = StringVar()  # Product Price
        self.var_qty_ = StringVar()  # Total Qty
        self.var_sld_ = StringVar()  # Sold
        self.var_exd_ = StringVar()  # Expire Date
        self.var_exp_ = StringVar()  # Expired Products
        self.var_inv_ = StringVar()  # Inventory Value
        self.var_rem_ = StringVar()  # Remaining Stock Value
        self.var_ssv_ = StringVar()  # Sold Stock Value

    def Export_def(self):
        gg = self.Table.get_children()
        id = []
        dat_ = []
        prc_ = []
        prn_ = []
        cat_ = []
        sct_ = []
        des_ = []
        bar_ = []
        snw_ = []
        sup_ = []
        unp_ = []
        slp_ = []
        mrk_ = []
        tax_ = []
        dis_ = []
        prp_ = []
        qty_ = []
        sld_ = []
        exd_ = []
        exp_ = []
        inv_ = []
        rem_ = []
        ssv_ = []
        count = 0
        for i in gg:
            content = self.Table.item(i)
            pp = content['values']
            count += 1
            id.append(str(count))
            dat_.append(pp[1])
            prc_.append(pp[2])
            prn_.append(pp[3])
            cat_.append(pp[4])
            sct_.append(pp[5])
            des_.append(pp[6])
            bar_.append(pp[7])
            snw_.append(pp[8])
            sup_.append(pp[9])
            unp_.append(pp[10])
            slp_.append(pp[11])
            mrk_.append(pp[12])
            tax_.append(pp[13])
            dis_.append(pp[14])
            prp_.append(pp[15])
            qty_.append(pp[16])
            sld_.append(pp[17])
            exd_.append(pp[18])
            exp_.append(pp[19])
            inv_.append(pp[20])
            rem_.append(pp[21])
            ssv_.append(pp[22])

        headings = self.__list__('head')
        expList = list(zip(id, dat_, prc_, prn_, cat_, sct_, des_, bar_, snw_, sup_, unp_, slp_, mrk_, tax_, dis_, prp_, qty_, sld_, exd_, exp_, inv_, rem_, ssv_))
        Log_Generator().addLog(f'[Export] {count} Record Found')
        return count, headings, expList

    def Get_Data(self, e):
        try:
            f = self.Table.focus()
            content = (self.Table.item(f))
            row = content['values']
            self.var_id.set(row[0])
            self.var_dat_.set(row[1])
            self.var_prc_.set(row[2])
            self.var_prn_.set(row[3])
            self.var_cat_.set(row[4])
            self.var_sct_.set(row[5])
            self.var_des_.set(row[6])
            self.var_bar_.set(row[7])
            self.var_snw_.set(row[8])
            self.var_sup_.set(row[9])
            self.var_unp_.set(row[10])
            self.var_slp_.set(row[11])
            self.var_mrk_.set(row[12])
            self.var_tax_.set(row[13])
            self.var_dis_.set(row[14])
            self.var_prp_.set(row[15])
            self.var_qty_.set(row[16])
            self.var_sld_.set(row[17])
            self.var_exd_.set(row[18])
            self.var_exp_.set(row[19])
            self.var_inv_.set(row[20])
            self.var_rem_.set(row[21])
            self.var_ssv_.set(row[22])

            self.status(f'[{self.mainName}] [Get Data] Record {self.var_id.get()} Selected Successfully')
        except Exception as ex:
            self.status(f'[{self.mainName}] [Get Data] Error: {ex}')
            pass

    def StarterDb(self, db='sqlite'):
        if db == 'sqlite':
            self.cur.execute('''CREATE TABLE IF NOT EXISTS "''' + self.mainName.replace(' ', '_') + '''" (
                "id"	INTEGER NOT NULL UNIQUE,
                "dat_"	TEXT,
                "prc_"	TEXT,
                "prn_"	TEXT,
                "cat_"	TEXT,
                "sct_"	TEXT,
                "des_"	TEXT,
                "bar_"	TEXT,
                "snw_"	TEXT,
                "sup_"	TEXT,
                "unp_"	TEXT,
                "slp_"	TEXT,
                "mrk_"	TEXT,
                "tax_"	TEXT,
                "dis_"	TEXT,
                "prp_"	TEXT,
                "qty_"	TEXT,
                "sld_"	TEXT,
                "exd_"	TEXT,
                "exp_"	TEXT,
                "inv_"	TEXT,
                "rem_"	TEXT,
                "ssv_"	TEXT,
                PRIMARY KEY("id" AUTOINCREMENT))''')
            self.con.commit()
        else:
            self.cur.execute(
                '''CREATE TABLE IF NOT EXISTS ''' + self.mainName.replace(' ', '_') + ''' (
                id SERIAL NOT NULL AUTO_INCREMENT
                , dat_ TEXT NOT NULL
                , prc_ TEXT NOT NULL
                , prn_ TEXT NOT NULL
                , cat_ TEXT NOT NULL
                , sct_ TEXT NOT NULL
                , des_ TEXT NOT NULL
                , bar_ TEXT NOT NULL
                , snw_ TEXT NOT NULL
                , sup_ TEXT NOT NULL
                , unp_ TEXT NOT NULL
                , slp_ TEXT NOT NULL
                , mrk_ TEXT NOT NULL
                , tax_ TEXT NOT NULL
                , dis_ TEXT NOT NULL
                , prp_ TEXT NOT NULL
                , qty_ TEXT NOT NULL
                , sld_ TEXT NOT NULL
                , exd_ TEXT NOT NULL
                , exp_ TEXT NOT NULL
                , inv_ TEXT NOT NULL
                , rem_ TEXT NOT NULL
                , ssv_ TEXT NOT NULL )''')
            self.con.commit()

    def __list__(self, fetch):
        list_var = [self.var_id, self.var_dat_, self.var_prc_, self.var_prn_, self.var_cat_, self.var_sct_, self.var_des_, self.var_bar_, self.var_snw_, self.var_sup_, self.var_unp_, self.var_slp_, self.var_mrk_, self.var_tax_, self.var_dis_, self.var_prp_, self.var_qty_, self.var_sld_, self.var_exd_, self.var_exp_, self.var_inv_, self.var_rem_, self.var_ssv_]
        list_shn = ['id', 'dat_', 'prc_', 'prn_', 'cat_', 'sct_', 'des_', 'bar_', 'snw_', 'sup_', 'unp_', 'slp_', 'mrk_', 'tax_', 'dis_', 'prp_', 'qty_', 'sld_', 'exd_', 'exp_', 'inv_', 'rem_', 'ssv_']
        list_cvar = [[self.var_id, 'ID'], [self.var_dat_, 'Date'], [self.var_prc_, 'Product Code'], [self.var_bar_, 'Barcode'], [self.var_sup_, 'Supplier'], [self.var_unp_, 'Unit Price'], [self.var_slp_, 'Sale Price'], [self.var_qty_, 'Total Qty'], [self.var_exd_, 'Expire Date']]
        list_head = ['ID', 'Date', 'Product Code', 'Product Name', 'Category', 'Sub Category', 'Description', 'Barcode', 'Size n Weight', 'Supplier', 'Unit Price', 'Sale Price', 'Markup', 'Tax', 'Discount', 'Product Price', 'Total Qty', 'Sold', 'Expire Date', 'Expired Products', 'Inventory Value', 'Remaining Stock Value', 'Sold Stock Value']
        list_headA = ['ID', 'Date', 'Product Code', 'Product Name', 'Category', 'Sub Category', 'Description', 'Barcode', 'Size n Weight', 'Supplier', 'Unit Price', 'Sale Price', 'Markup', 'Tax', 'Discount', 'Product Price', 'Total Qty', 'Sold', 'Expire Date', 'Expired Products', 'Inventory Value', 'Remaining Stock Value', 'Sold Stock Value']

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
    obj = AddToStock(root)
    root.mainloop()
    Log_Generator().closeLog()
