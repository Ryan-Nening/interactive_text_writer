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

    def build_user_interface(self):
        self.instruction_label = tkinter.Label(self.main_window, text="Enter a line for your life story:")
        self.instruction_label.pack()
        self.user_input_field = tkinter.Entry(self.main_window, width=50)
        self.user_input_field.pack()
        self.save_button = tkinter.Button(self.main_window, text="Save Line", command=self.save_current_line)
        self.save_button.pack()
        self.status_message = tkinter.Label(self.main_window, text="Status: Waiting for input...")
        self.status_message.pack()

    def save_current_line(self):
        current_text = self.user_input_field.get()
        if current_text != "":
            output_file = open(self.output_file_name, "a")
            output_file.write(current_text + "\n")
            output_file.close()
            self.status_message.config(text="Status: Line saved successfully!")
            self.user_input_field.delete(0, tkinter.END)
        else:
            self.status_message.config(text="Status: Please enter text first.")
    