import importlib.util

from tkinter import *
from tkinter import ttk, messagebox, filedialog
from tkcalendar import Calendar, DateEntry
import re, os, random, time, pandas, csv, threading
import pymysql, sqlite3
from reportlab.lib import colors as abcdef
from reportlab.lib import pagesizes  # For creating reports
from reportlab.lib.units import mm, inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle  # For creating reports
from reportlab.lib.styles import getSampleStyleSheet  # For creating reports
from datetime import datetime, timedelta
import textwrap
import webbrowser  # For Opening Links
# import openpyxl # for creating the excel report xlsx format

class importFile:
    current_folder = os.getcwd()
    if os.path.basename(current_folder) == 'Library_Files':
        main_folder = os.path.dirname(current_folder)
    else:
        main_folder = current_folder
    def __init__(self):
        pass

    # def Import(self, ):

    def importFRM(self, skip=[], others={}):
        list_of_libFiles = os.listdir(self.main_folder)
        list_of_libFiles = [x for x in list_of_libFiles if x.endswith('_frm.py')]
        list_of_libFiles.sort(reverse=True)
        try: list_of_libFiles = [x for x in list_of_libFiles if x not in skip]
        except: pass
        for i in list_of_libFiles:
            module_name = f"Library_Files.{i.replace('.py', '')}"
            class_name = i.replace('_frm.py', '')
            module = importlib.import_module(module_name)
            globals()[class_name] = getattr(module, class_name)
        try:
            for fn, fp in others.items():
                module_name = f"{fp}.{fn.replace('.py', '')}"
                class_name = fn.replace('_frm.py', '')
                module = importlib.import_module(module_name)
                globals()[class_name] = getattr(module, class_name)
        except: pass

    # def DynamicImport(self, fn, fp):
    #     # Use the importlib module to import the module dynamically
    #     spec = importlib.util.spec_from_file_location(fn, fp + "/" + fn)
    #     module = importlib.util.module_from_spec(spec)
    #     spec.loader.exec_module(module)
    #
    #     return module
