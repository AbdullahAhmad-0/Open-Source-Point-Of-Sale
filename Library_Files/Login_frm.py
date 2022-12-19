from tkinter import *
from pathlib import Path
try:
    from FormRun import *
    from Log_Generator import Log_Generator
except:
    from Library_Files.FormRun import *
    from Library_Files.Log_Generator import Log_Generator

# OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH = OUTPUT_PATH / \
#     Path(r"D:\Python Projects\Ahmad Soft\Point Of Sale\NOT NEED\Login figma\build\assets\frame0")
# def relative_to_assets(path: str) -> Path:
#     return ASSETS_PATH / Path(path)

class Login(BeforeInIt):
    wSize, hSize = 660, 420
    title = "Pointing Of Sale"
    mainName = title

    def __init__(self, wind) -> None:
        if Log_Generator().findLog():
            Log_Generator().startLog()
        else:
            Log_Generator().createLog()

        self.root = wind
        self.root.title(self.title)
        self.root.iconbitmap(self.iconPath)
        self.root.config(bg="#FFFFFF")
        self.root.minsize(self.wSize, self.hSize)
        self.root.resizable(False, False)

        # Variables
        self.var_user = StringVar()
        self.var_pass = StringVar()

        canvas = Canvas(self.root, bg="#FFFFFF", height=420, width=660, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        canvas.create_rectangle(0.0, 0.0, 330.0, 420.0, fill="#1F86E5", outline="")
        canvas.create_rectangle(0.0, 0.0, 330.0, 420.0, fill="#1F86E5", outline="")

        self.root.entry_image_1 = entry_image_1 = PhotoImage(file=f"{self.images_folder}\\Login\\entry_1.png")
        entry_bg_1 = canvas.create_image(505.00000000000006, 155.5, image=entry_image_1)
        entry_1 = Entry(self.root, textvariable=self.var_user, bd=0, bg="#fafafa", fg="#000716", highlightthickness=0)
        entry_1.place(x=400, y=152, width=217.0, height=20)

        self.root.entry_image_2 = entry_image_2 = PhotoImage(file=f"{self.images_folder}\\Login\\entry_2.png")
        entry_bg_2 = canvas.create_image(505.00000000000006, 229.5, image=entry_image_2)
        entry_2 = Entry(self.root, textvariable=self.var_pass, bd=0, bg="#fafafa", fg="#000716", highlightthickness=0)
        entry_2.place(x=400, y=226, width=217.0, height=20)

        canvas.create_text(390.00000000000006, 136.0, anchor="nw", text="Username", fill="#1F7AD0", font=("Inter", 15 * -1))
        canvas.create_text(390.00000000000006, 210.0, anchor="nw", text="Password", fill="#1F7AD0", font=("Inter", 15 * -1))

        self.root.button_image_1 = button_image_1 = PhotoImage(file=f"{self.images_folder}\\Login\\button_1.png")
        button_1 = Button(self.root, image=button_image_1, borderwidth=0, highlightthickness=0, cursor='hand2', command=self.openForgot, relief="flat")
        button_1.place(x=423.00000000000006, y=326.0, width=155.0, height=34.0)

        self.root.button_image_2 = button_image_2 = PhotoImage(file=f"{self.images_folder}\\Login\\button_2.png")
        button_2 = Button(self.root, image=button_image_2, borderwidth=0, highlightthickness=0, cursor='hand2', command=self.openHelp, relief="flat")
        button_2.place(x=62, y=326, width=200, height=34)

        self.root.button_image_3 = button_image_3 = PhotoImage(file=f"{self.images_folder}\\Login\\button_3.png")
        button_3 = Button(self.root, image=button_image_3, borderwidth=0, highlightthickness=0, cursor='hand2', command=self.loginFunction, relief="flat")
        button_3.place(x=377.00000000000006, y=282.0, width=120.0, height=45)

        self.root.button_image_4 = button_image_4 = PhotoImage(file=f"{self.images_folder}\\Login\\button_4.png")
        button_4 = Button(self.root, image=button_image_4, borderwidth=0, highlightthickness=0, cursor='hand2', command=self.openSignup, relief="flat")
        button_4.place(x=513.0, y=282.0, width=120.0, height=45)

        canvas.create_text(54.00000000000006, 65.0, anchor="nw", text="Welcome To POS", fill="#FFFFFF", font=("Inter", 24 * -1))
        canvas.create_text(54.00000000000006, 94.0, anchor="nw", text="Software", fill="#FFFFFF", font=("Inter", 24 * -1))

        canvas.create_text(54.00000000000006, 140.0, anchor="nw", text="This Software Will Help You To", fill="#FFFFFF", font=("Inter", 15 * -1))
        canvas.create_text(54.00000000000006, 158.0, anchor="nw", text="Take Your Business At Higher Level", fill="#FFFFFF", font=("Inter", 15 * -1))

        canvas.create_text(49.00000000000006, 213.0, anchor="nw", text="Easy To Use GUI", fill="#FFFFFF", font=("Inter", 15 * -1))
        canvas.create_text(49.00000000000006, 231.0, anchor="nw", text="Report Features", fill="#FFFFFF", font=("Inter", 15 * -1))
        canvas.create_text(49.00000000000006, 249.0, anchor="nw", text="Analytics Function", fill="#FFFFFF", font=("Inter", 15 * -1))
        canvas.create_text(49.00000000000006, 267.0, anchor="nw", text="and", fill="#FFFFFF", font=("Inter", 15 * -1))
        canvas.create_text(49.00000000000006, 285.0, anchor="nw", text="Many More", fill="#FFFFFF", font=("Inter", 15 * -1))

    def loginFunction(self):
        print('Login')

    def openSignup(self):
        print('Signup Form')

    def openForgot(self):
        print('Forgot Password')

    def openHelp(self):
        print('Help')


if __name__ == '__main__':
    root = Tk()
    obj = Login(root)
    root.mainloop()
    Log_Generator().closeLog()
