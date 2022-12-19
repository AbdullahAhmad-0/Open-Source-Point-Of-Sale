try:
    from LogViewer_frm import LogViewer
except:
    from Library_Files.LogViewer_frm import LogViewer
from tkinter import *

class Func:
    def __init__(self) -> None:
        pass

    def LogViewer_frm(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = LogViewer(self.new_win)
