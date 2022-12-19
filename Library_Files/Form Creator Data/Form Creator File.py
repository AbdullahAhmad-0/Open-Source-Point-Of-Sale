import os

print('Started')
f = open('Form Creator', 'r')
main = f.readlines()
f.close()

f = open('data', 'r')
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
mainData17 = str()
mainData18 = str()
mainData19 = str()
mainData20 = str()
mainData21 = str()
mainData22 = str()
mainData23 = str()

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
    # line 01: 05 fields {DATA 2}
    if field == 'text':
        det2 = data_new[0].replace('\n', '').replace('\\n', '\n')
    elif field == 'date':
        det2 = data_new[1].replace('\n', '').replace('\\n', '\n')
    elif field == 'combo':
        det2 = data_new[2].replace('\n', '').replace('\\n', '\n')
    elif field == 'no':
        det2 = data_new[3].replace('\n', '').replace('\\n', '\n')
    elif field == 'attach':
        det2 = data_new[4].replace('\n', '').replace('\\n', '\n')
    elif field == 'sta':
        det2 = ''
    elif field == 'dText':
        det2 = data_new[5].replace('\n', '').replace('\\n', '\n')

    # line 07, 08 variable {DATA 1}
    if field == 'attach':
        det1 = data_new[7].replace('\n', '').replace('\\n', '\n')
    else:
        det1 = data_new[6].replace('\n', '').replace('\\n', '\n')

    # line 10, 11 add {DATA 7}
    if field == 'attach':
        det7 = data_new[11 - 1].replace('\n', '').replace('\\n', '\n')
    elif field == 'sta':
        det7 = data_new[12 - 1].replace('\n', '').replace('\\n', '\n')
    else:
        det7 = data_new[10 - 1].replace('\n', '').replace('\\n', '\n')

    # line 13, 14 update {DATA 8}
    if field == 'attach':
        det8 = data_new[14 - 1].replace('\n', '').replace('\\n', '\n')
    else:
        det8 = data_new[13 - 1].replace('\n', '').replace('\\n', '\n')

    # line 16, 17 clear {DATA 9}
    if field == 'attach':
        det9 = data_new[17 - 1].replace('\n', '').replace('\\n', '\n')
    else:
        det9 = data_new[16 - 1].replace('\n', '').replace('\\n', '\n')

    # line 19 export {DATA 10}
    det10 = data_new[19 - 1].replace('\n', '').replace('\\n', '\n')

    # line 20 export {DATA 11}
    det11 = data_new[20 - 1].replace('\n', '').replace('\\n', '\n')

    # line 21 export {DATA 12}
    det12 = data_new[21 - 1].replace('\n', '').replace('\\n', '\n')

    # line 22 export {DATA 13}
    det13 = data_new[22 - 1].replace('\n', '').replace('\\n', '\n')

    # line 24, 25 import {DATA 14}
    if field == 'attach':
        det14 = data_new[25 - 1].replace('\n', '').replace('\\n', '\n')
    elif field == 'sta':
        det14 = data_new[27 - 1].replace('\n', '').replace('\\n', '\n')
    else:
        det14 = data_new[24 - 1].replace('\n', '').replace('\\n', '\n')

    # line 26 import {DATA 15}
    det15 = data_new[26 - 1].replace('\n', '').replace('\\n', '\n')

    # line 28 search {DATA 16}
    det16 = data_new[28 - 1].replace('\n', '').replace('\\n', '\n')

    # line 29 search {DATA 3}
    det3 = data_new[29 - 1].replace('\n', '').replace('\\n', '\n')

    # line 31, 32 get data {DATA 17}
    if field == 'attach':
        det17 = data_new[32 - 1].replace('\n', '').replace('\\n', '\n')
    else:
        det17 = data_new[31 - 1].replace('\n', '').replace('\\n', '\n')

    # line 34, 35 db {DATA 18}
    if field == 'attach':
        det18 = data_new[35-1].replace('\n', '').replace('\\n', '\n')
    else:
        det18 = data_new[34-1].replace('\n', '').replace('\\n', '\n')

    # line 36, 37 db {DATA 19}
    if field == 'attach':
        det19 = data_new[37-1].replace('\n', '').replace('\\n', '\n')
    else:
        det19 = data_new[36-1].replace('\n', '').replace('\\n', '\n')

    # line 39 table {DATA 4}
    det4 = data_new[39 - 1].replace('\n', '').replace('\\n', '\n')

    # line 40 table {DATA 5}
    det5 = data_new[40 - 1].replace('\n', '').replace('\\n', '\n')

    # line 41 table {DATA 6}
    det6 = data_new[41 - 1].replace('\n', '').replace('\\n', '\n')

    # line 42 Add {DATA 20}
    if field == 'attach':
        det20 = data_new[42 - 1].replace('\n', '').replace('\\n', '\n')
        det20 = det20 + det20
    else:
        det20 = data_new[42 - 1].replace('\n', '').replace('\\n', '\n')

    # line 43 Add {DATA 21}
    if field == 'attach':
        det21 = data_new[44 - 1].replace('\n', '').replace('\\n', '\n')
    else:
        det21 = data_new[43 - 1].replace('\n', '').replace('\\n', '\n')

    # line 45 Add {DATA 22}
    if r == '1':
        det22 = data_new[45 - 1].replace('\n', '').replace('\\n', '\n')
    else:
        det22 = ''

    # line 45 Update {DATA 23}
    if r == '1':
        det23 = data_new[46 - 1].replace('\n', '').replace('\\n', '\n')
    else:
        det23 = ''

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
    mainData17 += str(det17)
    mainData18 += str(det18)
    mainData19 += str(det19)
    mainData20 += str(det20)
    mainData21 += str(det21)
    mainData22 += str(det22)
    mainData23 += str(det23)

f = open('data main', 'r')
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
main = main.replace('{DATA 9}', mainData09)
main = main.replace('{DATA 10}', mainData10)
main = main.replace('{DATA 11}', mainData11)
main = main.replace('{DATA 12}', mainData12)
main = main.replace('{DATA 13}', mainData13)
main = main.replace('{DATA 14}', mainData14)
main = main.replace('{DATA 15}', mainData15)
main = main.replace('{DATA 16}', mainData16)
main = main.replace('{DATA 17}', mainData17)
main = main.replace('{DATA 18}', mainData18)
main = main.replace('{DATA 19}', mainData19)
main = main.replace('{DATA 20}', mainData20)
main = main.replace('{DATA 21}', mainData21)
main = main.replace('{DATA 22}', mainData22)
main = main.replace('{DATA 23}', mainData23)

mname = input('Enter Name Of Your Form: ')
title = f'{mname} - Company Management System'  # input('Enter Title Of Your Form: ')
cname = mname.replace(' ', '')
fname = f'{cname}_frm'
print("for one element : x[Order]")
print("for more than one element : (x[Order], x[Order])")
oby = input('Enter Order By: ')
main = main.replace('[Title]', title)
main = main.replace('[cName]', cname)
main = main.replace('[mName]', mname)
main = main.replace('{Order By}', oby)

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
