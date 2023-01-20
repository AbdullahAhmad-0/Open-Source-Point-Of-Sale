import os


class CallSetting:
    setting = ['']

    current_folder = os.getcwd()
    if os.path.basename(current_folder) == 'Library_Files':
        main_folder = os.path.dirname(current_folder)
    else:
        main_folder = current_folder
    setting_folder = f'{main_folder}\\Setting'

    def getAdvanceSetting(self):
        return self.__CommonSetting__("Advance Setting")

    def getCommonSetting(self):
        return self.__CommonSetting__("Common Setting")

    def getDatabaseSetting(self):
        return self.__CommonSetting__("Database Configurations")

    def getFormSetting(self):
        return self.__CommonSetting__("Form Setting")

    def getReportSetting(self):
        return self.__CommonSetting__("Report Setting")

    def __checkFL__(self, setting):
        nList = []
        for i in setting:
            if '+' in i:
                a, b = i.split('+')
                f = open(f'{self.setting_folder}\\{a}.fl', 'r')
                files = f.readlines()
                f.close()
                nList.append(files[int(b) - 1].strip('\n'))
            else:
                nList.append(i)

        return nList

    def __CommonSetting__(self, name):
        self.setting = ['']
        colorFile = f'{self.setting_folder}\\{name}'

        f = open(colorFile, 'r')
        color_set = f.readlines()
        f.close()

        cnt = 0
        for _ in color_set:
            _, a = color_set[cnt].strip('\n').split(':')
            a, *_ = a.split('.')
            self.setting.append(a)
            cnt += 1

        self.setting = self.__checkFL__(self.setting)

        return self.setting


def main():
    a = CallSetting().getCommonSetting()
    print(a)


if __name__ == '__main__':
    main()
