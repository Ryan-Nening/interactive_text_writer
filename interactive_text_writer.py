import tkinter

class InteractiveTextWriter:

    def __init__(self, output_file_name):
        self.output_file_name = output_file_name
        self.main_window = tkinter.Tk()
        self.main_window.title("Life Writer Tool")
        self.main_window.geometry("400x200")

    def build_user_interface(self):
        self.instruction_label = tkinter.Label(self.main_window, text="Enter a line for your life story:")
        self.instruction_label.pack()
        self.user_input_field = tkinter.Entry(self.main_window, width=50)
        self.user_input_field.pack()
    