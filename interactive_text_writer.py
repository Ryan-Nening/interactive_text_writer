import tkinter
from tkinter import font

class InteractiveTextWriter:

    def __init__(self, output_file_name):
        self.output_file_name = output_file_name
        self.main_window = tkinter.Tk()
        self.main_window.title("Life Writer Pro")
        self.main_window.geometry("500x450")
        self.main_window.configure(bg="#1e1e1e")

   def build_user_interface(self):
        title_font = font.Font(family="Helvetica", size=14, weight="bold")
        normal_font = font.Font(family="Helvetica", size=11)
        
        self.title_label = tkinter.Label(self.main_window, text="📖 Digital Life Journal", font=title_font, bg="#1e1e1e", fg="#ffffff")
        self.title_label.pack(pady=(20, 5))
        
        self.user_input_field = tkinter.Entry(self.main_window, width=45, font=normal_font, bg="#2d2d2d", fg="#ffffff", insertbackground="white", relief="flat")
        self.user_input_field.pack(pady=10, ipady=6) 
        
        self.save_button = tkinter.Button(self.main_window, text="📝 Save Entry", font=normal_font, bg="#00adb5", fg="#ffffff", activebackground="#007a80", activeforeground="#ffffff", relief="flat", cursor="hand2", command=self.save_current_line)
        self.save_button.pack(pady=10, ipadx=10)
        
        self.status_message = tkinter.Label(self.main_window, text="Status: Ready to write...", font=normal_font, bg="#1e1e1e", fg="#aaaaaa")
        self.status_message.pack(pady=5)

        self.history_label = tkinter.Label(self.main_window, text="Recent Entries:", font=normal_font, bg="#1e1e1e", fg="#00adb5")
        self.history_label.pack(pady=(20, 0))
        
        self.entry_history_box = tkinter.Listbox(self.main_window, width=50, height=8, bg="#2d2d2d", fg="#ffffff", relief="flat", highlightthickness=0, font=("Helvetica", 10))
        self.entry_history_box.pack(pady=5)

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

    def run_application(self):
        self.build_user_interface()
        self.main_window.mainloop()
    