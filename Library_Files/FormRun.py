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

    if advanceSetting == 'Default':
        database = default_db
    else:
        database = advanceSetting[4]

    old_mainW = 0
    old_mainH = 0


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


class BeforeRun:
    def __init__(self):
        pass


class AfterRun:
    def __init__(self):
        pass
