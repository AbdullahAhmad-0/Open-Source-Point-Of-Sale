import os

current_folder = os.getcwd()
main_folder = os.path.dirname(current_folder)
main_folder = os.path.dirname(main_folder)
setting_folder = f'{main_folder}\\Setting'

fName = input('Enter Name Of Your File: ')
fshn = input('Enter shn Of Your Field: ')

data = '''f = open(f"{self.setting_folder}\\\\{fName}.ls", 'r')
cmb_{fshn}_list = f.readlines()
cmb_{fshn}_list = [x.rstrip('\\n') for x in cmb_{fshn}_list]
f.close()'''

newData = data.replace('{fName}', fName)
newData = newData.replace('{fshn}', fshn)
try:
    f = open(f'{setting_folder}\\{fName}.ls', 'r')
    f.write('')
    f.close()
except:
    f = open(f'{setting_folder}\\{fName}.ls', 'w')
    f.write('')
    f.close()

print(newData)
