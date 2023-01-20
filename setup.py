import cx_Freeze
import sys
from LibFilesGen import Generate

base = "Win32GUI"
shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "Complaint Management System",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]\CMS.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     "TARGETDIR",  # WkDir
     )
]
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}

executables = [
    cx_Freeze.Executable(script="CMS.py", icon='Images\\ico.ico', base=base, copyright='Abdullah Ahmad Ahmad Soft,inc Copyright@2021-25')
]

cx_Freeze.setup(
    version="2.1.0",
    description="Abdullah Ahmad AS,inc Copyright@2021-25",
    author="ABDULLAH AHMAD",
    name="Complaint Management System",
    options={"build_exe": {"packages": ["tkinter", "tkcalendar", "os", "random", "time", "pandas", "csv", "threading", "shutil", "pymysql", "sqlite3", "re", "reportlab.lib", "reportlab.lib.units", "reportlab.platypus", "reportlab.lib.styles", "datetime", "openpyxl", "webbrowser"],
                           "includes": Generate(),
                           "include_files": ['Database', 'Images', 'Library_Files', 'Setting', 'Temp', 'Forms'],
                           "include_msvcr": True},
             "bdist_msi": bdist_msi_options,
             },
    executables=executables

)
