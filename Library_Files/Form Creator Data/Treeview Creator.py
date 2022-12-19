import os

print('Started')
f = open('Treeview Creator', 'r')
main = f.readlines()
f.close()

f = open('Treeview Creator Data', 'r')
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

for i in main:
    a = i.strip('\n')
    name, shn, no, width, r = a.split(',')

    data_new = []
    for i in d:
        i = i.replace('{Name}', name)
        i = i.replace('{shn}', shn)
        i = i.replace('{NO Count}', no)
        i = i.replace('{width}', width)
        data_new.append(i)

    # line 1 table {DATA 1}
    det1 = data_new[1 - 1].replace('\n', '').replace('\\n', '\n')

    # line 2 table {DATA 2}
    det2 = data_new[2 - 1].replace('\n', '').replace('\\n', '\n')

    # line 3 table {DATA 3}
    det3 = data_new[3 - 1].replace('\n', '').replace('\\n', '\n')

    # line 4 show {DATA 4}
    det4 = data_new[4 - 1].replace('\n', '').replace('\\n', '\n')

    # line 5 show {DATA 5}
    det5 = data_new[5 - 1].replace('\n', '').replace('\\n', '\n')

    # line 6 get data {DATA 6}
    if r == '1':
        det6 = data_new[6 - 1].replace('\n', '').replace('\\n', '\n')
    else:
        det6 = ''

    # line 7 search {DATA 7}
    det7 = data_new[7 - 1].replace('\n', '').replace('\\n', '\n')

    # line 8 search {DATA 8}
    det8 = data_new[8 - 1].replace('\n', '').replace('\\n', '\n')

    mainData01 += str(det1)
    mainData02 += str(det2)
    mainData03 += str(det3)
    mainData04 += str(det4)
    mainData05 += str(det5)
    mainData06 += str(det6)
    mainData07 += str(det7)
    mainData08 += str(det8)

f = open('Treeview data', 'r')
main = f.read()
f.close()

# main = main.replace('\n', '').replace('\\n', '\n')
main = main.replace('{DATA 1}', mainData01)
main = main.replace('{DATA 2}', mainData02)
main = main.replace('{DATA 3}', mainData03)
main = main.replace('{DATA 4}', mainData04)
main = main.replace('{DATA 5}', mainData05)
main = main.replace('{DATA 6}', mainData06)
main = main.replace('{DATA 7}', mainData07)
main = main.replace('{DATA 8}', mainData08)

tname = input('Enter Name Of Your Table: ')
ord = input('Enter Order: ')
fName = input('Enter Name Of Your Form: ')
ttitle = f'{tname} Record'
main = main.replace('{tTitle}', ttitle)
main = main.replace('{tName}', tname.replace(' ', '_'))
main = main.replace('{ord}', ord)
print(main)

current_folder = os.getcwd()
main_folder = os.path.dirname(current_folder)
main_folder = os.path.dirname(main_folder)
library_folder = f'{main_folder}\\Library_Files'
f = open('Treeview Creator', 'r')
main = f.read()
f.close()
f = open(f"{library_folder}\\Temp\\{fName.replace(' ', '')}_{tname.replace(' ', '')}_treeview_data", 'w')
f.write(main)
f.close()
