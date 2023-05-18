import os

print('Started')
f = open('Form Creator', 'r')
main = f.readlines()
f.close()

f = open('Widgets', 'r')
Widgets = f.readlines()
f.close()

f = open('Data', 'r')
d = f.readlines()
f.close()

mainData01 = str()
mainData02 = str()
mainData03 = str()
mainData04 = str()
mainData05 = str()
mainData06 = str()
mainData07 = str()
mainData08 = str()
mainData09 = str()
mainData10 = str()
mainData11 = str()
mainData12 = str()
mainData13 = str()
mainData14 = str()
mainData15 = str()
mainData16 = str()

for i in main:
    a = i.strip('\n')
    name, shn, field, no, width, r = a.split(',')

    data_new = []
    for i in d:
        i = i.replace('{Name}', name)
        i = i.replace('{shn}', shn)
        i = i.replace('{NO Count}', no)
        i = i.replace('{width}', width)
        data_new.append(i)

    widgets = []
    for i in Widgets:
        i = i.replace('{Name}', name)
        i = i.replace('{shn}', shn)
        i = i.replace('{NO Count}', no)
        i = i.replace('{width}', width)
        widgets.append(i)

    # {DATA 1}
    for i in widgets:
        if i.startswith(field):
            det1 = i.replace('\n', '').replace('\\n', '\n').replace(f'{field}: ', '')
            break

    if field == 'attach':
        # line 2 table {DATA 2}
        det2 = data_new[35 - 1].replace('\n', '').replace('\\n', '\n')
        # line 3 table {DATA 3}
        det3 = data_new[36 - 1].replace('\n', '').replace('\\n', '\n')
        # line 4 table {DATA 4}
        det4 = data_new[37 - 1].replace('\n', '').replace('\\n', '\n')
    else:
        # line 2 table {DATA 2}
        det2 = data_new[2 - 1].replace('\n', '').replace('\\n', '\n')
        # line 3 table {DATA 3}
        det3 = data_new[3 - 1].replace('\n', '').replace('\\n', '\n')
        # line 4 table {DATA 4}
        det4 = data_new[4 - 1].replace('\n', '').replace('\\n', '\n')

    # line 07, 08 variable {DATA 5}
    if field == 'attach':
        det5 = data_new[8 - 1].replace('\n', '').replace('\\n', '\n')
    else:
        det5 = data_new[7 - 1].replace('\n', '').replace('\\n', '\n')

    # line 11 variable {DATA 6}
    det6 = data_new[11 - 1].replace('\n', '').replace('\\n', '\n')
    # line 12 variable {DATA 7}
    det7 = data_new[12 - 1].replace('\n', '').replace('\\n', '\n')
    # line 13 variable {DATA 8}
    det8 = data_new[13 - 1].replace('\n', '').replace('\\n', '\n')

    # line 16, 17 variable {DATA 9}
    if field == 'attach':
        det9 = data_new[17 - 1].replace('\n', '').replace('\\n', '\n')
    else:
        det9 = data_new[16 - 1].replace('\n', '').replace('\\n', '\n')

    # line 20, 21 db {DATA 10}
    if field == 'attach':
        det10 = data_new[21 - 1].replace('\n', '').replace('\\n', '\n')
    else:
        det10 = data_new[20 - 1].replace('\n', '').replace('\\n', '\n')

    # line 22, 23 db {DATA 11}
    if field == 'attach':
        det11 = data_new[23 - 1].replace('\n', '').replace('\\n', '\n')
    else:
        det11 = data_new[22 - 1].replace('\n', '').replace('\\n', '\n')

    # line 26, 27 variable {DATA 12}
    if field == 'attach':
        det12 = data_new[27 - 1].replace('\n', '').replace('\\n', '\n')
    else:
        det12 = data_new[26 - 1].replace('\n', '').replace('\\n', '\n')

    # line 28, 29 variable {DATA 13}
    if field == 'attach':
        det13 = data_new[29 - 1].replace('\n', '').replace('\\n', '\n')
    else:
        det13 = data_new[28 - 1].replace('\n', '').replace('\\n', '\n')

    # line 30, 31 variable {DATA 14}
    if r == '1':
        if field == 'attach':
            det14 = data_new[31 - 1].replace('\n', '').replace('\\n', '\n')
        else:
            det14 = data_new[30 - 1].replace('\n', '').replace('\\n', '\n')
    else:
        det14 = ''

    # line 32 variable {DATA 15}
    det15 = data_new[32 - 1].replace('\n', '').replace('\\n', '\n')

    # line 32 variable {DATA 16}
    if field == 'attach':
        det16 = data_new[38 - 1].replace('\n', '').replace('\\n', '\n')
    else:
        det16 = data_new[32 - 1].replace('\n', '').replace('\\n', '\n')

    mainData01 += str(det1)
    mainData02 += str(det2)
    mainData03 += str(det3)
    mainData04 += str(det4)
    mainData05 += str(det5)
    mainData06 += str(det6)
    mainData07 += str(det7)
    mainData08 += str(det8)
    mainData09 += str(det9)
    mainData10 += str(det10)
    mainData11 += str(det11)
    mainData12 += str(det12)
    mainData13 += str(det13)
    mainData14 += str(det14)
    mainData15 += str(det15)
    mainData16 += str(det16)

f = open('Template', 'r')
main = f.read()
f.close()

main = main.replace('{DATA 1}', mainData01)
main = main.replace('{DATA 2}', mainData02)
main = main.replace('{DATA 3}', mainData03)
main = main.replace('{DATA 4}', mainData04)
main = main.replace('{DATA 5}', mainData05)
main = main.replace('{DATA 6}', mainData06)
main = main.replace('{DATA 7}', mainData07)
main = main.replace('{DATA 8}', mainData08)
main = main.replace('{DATA 9}', mainData09)
main = main.replace('{DATA 10}', mainData10)
main = main.replace('{DATA 11}', mainData11)
main = main.replace('{DATA 12}', mainData12)
main = main.replace('{DATA 13}', mainData13)
main = main.replace('{DATA 14}', mainData14)
main = main.replace('{DATA 15}', mainData15)
main = main.replace('{DATA 16}', mainData16)

mname = input('Enter Name Of Your Form: ')
title = f'{mname} - Point Of Sale'  # input('Enter Title Of Your Form: ')
cname = mname.replace(' ', '')
fname = f'{cname}_frm'
print("for one element : x[Order]")
print("for more than one element : (x[Order], x[Order])")
oby = input('Enter Order By: ')
main = main.replace('[Title]', title)
main = main.replace('[cName]', cname)
main = main.replace('[mName]', mname)
main = main.replace('[Order By]', oby)

current_folder = os.getcwd()
main_folder = os.path.dirname(current_folder)
main_folder = os.path.dirname(main_folder)
library_folder = f'{main_folder}\\Library_Files'

f = open(f'{library_folder}\\{fname}.py', 'w')
f.write(main)
f.close()
f = open('Form Creator', 'r')
main = f.read()
f.close()
f = open(f'{library_folder}\\Temp\\{fname}_data', 'w')
f.write(main)
f.close()
