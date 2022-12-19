import os

data = '''cx_Freeze.Executable(shortcutDir="Library_Files", shortcutName="{EXENAME}_frm", script="Library_Files\\\\{EXENAME}_frm.py", icon='Images\\\\ico.ico', base=base, copyright='Abdullah Ahmad IC Developer,inc Copyright@2021-25'),'''

main_folder = os.getcwd()
main_folder = os.path.dirname(main_folder)
main_folder = os.path.dirname(main_folder)
library_folder = f'{main_folder}\\Library_Files'
list_ = os.listdir(library_folder)
list_ = [x.rstrip('\n') for x in list_]
list_ = [x.replace('_frm.py', '') for x in list_ if x.endswith('_frm.py')]
print(list_)

newData = ''
for i in list_:
    newData += data.replace('{EXENAME}', i) + '\n'

print(newData)
