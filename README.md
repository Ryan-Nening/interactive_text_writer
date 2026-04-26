# Interactive Text Writer

## Description
This program is an Object-Oriented Graphical User Interface (GUI) tool built with Python and `tkinter`. It functions as a digital diary or line-by-line text logger. The user types sentences into a graphical text field, and the program safely appends each entry to a running text file (`mylife.txt`) without overwriting previous lines, while simultaneously displaying a live history of the session on the screen.

## Features
* **Dark Mode Aesthetics:** Features a sleek, modern interface with a dark gray background and cyan accents.
* **Live Visual History:** Utilizes a `tkinter.Listbox` to create a real-time canvas that displays recent entries as they are typed and saved.
* **Dynamic Status Indicators:** Includes a status label that changes color (green for success, red for errors) to provide immediate visual feedback to the user.
* **Continuous File Appending:** Uses Python's `"a"` (append) mode to safely add new lines to the end of the text file, preserving all previous entries.


## How to Use
1. **Run the Program:** Open your terminal or IDE and execute the main driver file:

   ``python main_program_for_interactive_text_writer.py``
2. **Type an Entry:** When the "Life Writer Pro" window opens, click inside the text entry box and type a sentence about your life.
3. **Save the Line:** Click the "Save Entry" button. The status label will turn green to confirm success, and your sentence will instantly appear in the "Recent Entries" listbox below.
4. **View Your File:** Go to your project folder and open the newly generated mylife.txt file to see your saved entries perfectly logged line by line.
