f = open('Combo Data', 'r')
main = f.readlines()
f.close()

d = ['''\n        {lbl2}_{Name}.set("")\\n        self.var_{Name}.set("")''']
d2 = ['''and {Name}='" + self.var_{old}.get() + "\'''']

mainData01 = str()

for i in main:
    name, lbl2 = i.split(',')
    data_new = []
    for i in d:
        i = i.replace('{Name}', name)
        i = i.replace('{lbl2}', lbl2)
        data_new.append(i)

    det1 = data_new[0].replace('\n', '').replace('\\n', '\n')
    mainData01 += str(det1)

f = open('Combo Data Creator', 'r')
main = f.read()
f.close()
main = main.replace('{DATA 1}', mainData01)

old_shn = input('Enter Old Name: ')
main = main.replace('{old}', old_shn)
new_shn = input('Enter New Name: ')
main = main.replace('{new}', new_shn)
new_lbl = input('Enter New Label: ')
main = main.replace('{lbl}', new_lbl)
new_tbl = input('Enter Table Name: ')
main = main.replace('{tName}', new_tbl)

print(main)
