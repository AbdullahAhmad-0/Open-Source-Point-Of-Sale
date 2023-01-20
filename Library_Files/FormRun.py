import os

try:
    from CallSetting import CallSetting
    from ColorScheme import ColorScheme
except:
    from Library_Files.CallSetting import CallSetting
    from Library_Files.ColorScheme import ColorScheme


class BeforeInIt:
    current_folder = os.getcwd()
    if os.path.basename(current_folder) == 'Library_Files':
        main_folder = os.path.dirname(current_folder)
    else:
        main_folder = current_folder
    setting_folder = f'{main_folder}\\Setting'
    database_folder = f'{main_folder}\\Database'
    temp_folder = f'{main_folder}\\Temp'
    images_folder = f'{main_folder}\\Images'
    library_folder = f'{main_folder}\\Library_Files'
    iconPath = f"{images_folder}\\ico.ico"
    default_db = f'{database_folder}\\Ahmad Soft Main DB.asdb'

    colorList = ColorScheme().getColor()
    advanceSetting = CallSetting().getAdvanceSetting()
    commonSetting = CallSetting().getCommonSetting()
    databaseSetting = CallSetting().getDatabaseSetting()
    formSetting = CallSetting().getFormSetting()
    if advanceSetting[4] == 'Default':
        database = default_db
    else:
        database = advanceSetting[4]

    old_mainW = 0
    old_mainH = 0


def __getFromList__(setting):
    setting = setting.replace('[', '')
    setting = setting.replace(']', '')
    setting = setting.split(',')
    return setting


class AllSettings:
    # Advance Setting
    advset_rtf = CallSetting().getAdvanceSetting()[1]
    advset_dbb = CallSetting().getAdvanceSetting()[2]
    advset_dbe = CallSetting().getAdvanceSetting()[3]
    advset_dbl = CallSetting().getAdvanceSetting()[4]

    # Common Setting
    cmnset_msgboxAadd = CallSetting().getCommonSetting()[1]
    cmnset_Afteradd = CallSetting().getCommonSetting()[2]
    cmnset_msgboxAupd = CallSetting().getCommonSetting()[3]
    cmnset_Afterupd = CallSetting().getCommonSetting()[4]
    cmnset_msgboxAdel = CallSetting().getCommonSetting()[5]
    cmnset_Afterdel = CallSetting().getCommonSetting()[6]
    cmnset_msgboxAimp = CallSetting().getCommonSetting()[7]
    cmnset_msgboxAexp = CallSetting().getCommonSetting()[8]
    cmnset_refA = CallSetting().getCommonSetting()[9]
    cmnset_refT = CallSetting().getCommonSetting()[10]
    cmnset_fullscreen = CallSetting().getCommonSetting()[11]

    # Database Configuration
    dbconfig_db = CallSetting().getDatabaseSetting()[1]
    dbconfig_host = CallSetting().getDatabaseSetting()[2]
    dbconfig_user = CallSetting().getDatabaseSetting()[3]
    dbconfig_pass = CallSetting().getDatabaseSetting()[4]

    # Form Setting
    formset_searchFH = CallSetting().getFormSetting()[1]
    formset_statusFH = CallSetting().getFormSetting()[2]
    formset_btn_detFW = CallSetting().getFormSetting()[3]
    formset_btnFH = CallSetting().getFormSetting()[4]
    formset_mainFBFW = CallSetting().getFormSetting()[5]
    formset_mainFSFH = CallSetting().getFormSetting()[6]
    formset_yInF = CallSetting().getFormSetting()[7]
    formset_wOfF = CallSetting().getFormSetting()[8]
    formset_xOfF = CallSetting().getFormSetting()[9]
    formset_idStart = CallSetting().getFormSetting()[10]
    formset_mainFHB = CallSetting().getFormSetting()[11]
    formset_mainHF = CallSetting().getFormSetting()[12]
    formset_mainF = CallSetting().getFormSetting()[13]

    # Report Setting
    repset_Sauto = CallSetting().getReportSetting()[1]
    repset_Sloc = CallSetting().getReportSetting()[2]
    repset_Lrep = __getFromList__(CallSetting().getReportSetting()[3])
    repset_Prep = __getFromList__(CallSetting().getReportSetting()[4])
    repset_Size = CallSetting().getReportSetting()[5]
    repset_tm = CallSetting().getReportSetting()[6]
    repset_bm = CallSetting().getReportSetting()[7]
    repset_lm = CallSetting().getReportSetting()[8]
    repset_rm = CallSetting().getReportSetting()[9]
    repset_oras = CallSetting().getReportSetting()[10]

    def CallCommonVar(self, height_):
        # common variables
        self.sF_h = int(self.formset_searchFH)  # Search Frame Height
        self.dFsF_y = 20  # Detail Frame And Search Frame Y
        self.dFbFstF_x = 0  # Detail Frame And Button Frame And Status Frame X
        self.stF_h = int(self.formset_statusFH)  # Status Frame Height

        self.dFbF_w = int(self.formset_btn_detFW)  # Detail Frame and Button Frame Width
        self.rF_y = self.dFsF_y + self.sF_h + 1  # Record Frame Y
        self.stF_w = self.mainW  # Status Frame Width
        self.rF_w = self.mainW - self.dFbF_w  # Record Frame Width
        self.rF_h = self.mainH - self.rF_y - self.stF_h - height_ - 1  # Detail Frame and Record Frame Height -1 because we add 1 in stF_y
        self.bF_h = int(self.formset_btnFH)  # Button Frame Height

        self.dF_h = self.mainH - self.dFsF_y - self.bF_h - self.stF_h - height_ - 2
        self.bF_y = self.dFsF_y + self.dF_h + 1
        self.sF_w = self.mainW - self.dFbF_w  # Search Frame Width
        self.rF_x = self.dFbF_w + 1
        self.stF_y = self.rF_y + self.rF_h + 1  # Status Frame Y


class BeforeRun:
    def __init__(self):
        pass


class AfterRun:
    def __init__(self):
        pass
