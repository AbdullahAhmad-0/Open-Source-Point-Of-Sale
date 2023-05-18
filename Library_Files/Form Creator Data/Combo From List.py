f = open('Combo From List Data', 'r')
main = f.readlines()
f.close()

d = ['''\\n    cmb_{Name}.set("")\\n    self.var_{Name}.set("")\\n    cmb_{Name}.delete(cmb_{Name}.get())''']
d2 = ['''\\n        cmb_{Name}.config(values=without_bracket)\\n        cmb_{Name}_list = without_bracket\\n        cmb_{Name}.set_completion_list(cmb_{Name}_list)''']

mainData01 = str()
mainData02 = str()

for i in main:
    name = i
    data_new = []
    data_new2 = []
    for i in d:
        i = i.replace('{Name}', name)
        data_new.append(i)
    for i in d2:
        i = i.replace('{Name}', name)
        data_new2.append(i)

    det1 = data_new[0].replace('\n', '').replace('\\n', '\n')
    det2 = data_new2[0].replace('\n', '').replace('\\n', '\n')
    mainData01 += str(det1)
    mainData02 += str(det2)

f = open('Combo From List', 'r')
main = f.read()
f.close()
main = main.replace('{DATA 1}', mainData01)
main = main.replace('{DATA 2}', mainData02)

new_shn = input('Enter New Name: ')
main = main.replace('{new}', new_shn)
new_shn = input('Enter Fetch Form: ')
main = main.replace('{fetch_from}', new_shn)
new_tbl = input('Enter Table Name: ')
main = main.replace('{tName_}', new_tbl.replace(' ', '_'))
main = main.replace('{tName}', new_tbl.replace('_', ' '))
main = main.replace('{btn_ref}', '🔃')

print(main)
