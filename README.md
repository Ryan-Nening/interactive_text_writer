# Interactive Text Writer

## Description
This program is an Object-Oriented Graphical User Interface (GUI) tool built with Python and `tkinter`. It functions as a digital diary or line-by-line text logger. Instead of using a traditional terminal prompt, the user types sentences into a graphical text field, and the program safely appends each entry to a running text file (`mylife.txt`) without overwriting previous lines.

## Features
* **Interactive GUI:** Provides a clean text entry box, a clickable save button, and a dynamic status message that updates when a line is successfully saved.
* **Two-File OOP Architecture:** Strictly adheres to Object-Oriented Programming best practices by separating the class blueprint from the main execution driver.
* **Continuous File Appending:** Uses Python's `"a"` (append) mode to safely add new lines to the end of the text file, preserving all previous entries.
