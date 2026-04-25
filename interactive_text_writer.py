import tkinter

class InteractiveTextWriter:

    def __init__(self, output_file_name):
        self.output_file_name = output_file_name
        self.main_window = tkinter.Tk()
        self.main_window.title("Life Writer Tool")
        self.main_window.geometry("400x200")
    