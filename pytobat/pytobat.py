# Copyright 2024 aallon-pituus (Github)

# Permission is hereby granted, free of charge,
# to any person obtaining a copy of this software
# and associated documentation files (the “Software”),
# to deal in the Software without restriction,
# including without limitation the rights to use, copy,
# modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
def legacy_program():
    loopVar = True
    while loopVar:
        os.system("cls")
        print('''                                                                             
88888888ba           888888888888          88888888ba                        
88      "8b               88               88      "8b                ,d     
88      ,8P               88               88      ,8P                88     
88aaaaaa8P'  8b       d8  88   ,adPPYba,   88aaaaaa8P'  ,adPPYYba,  MM88MMM  
88""""""'    `8b     d8'  88  a8"     "8a  88""""""8b,  ""     `Y8    88     
88            `8b   d8'   88  8b       d8  88      `8b  ,adPPPPP88    88     
88             `8b,d8'    88  "8a,   ,a8"  88      a8P  88,    ,88    88,    
88               Y88'     88   `"YbbdP"'   88888888P"   `"8bbdP"Y8    "Y888  
                 d8'                                                         
                d8'                                                          
''')
        print("\n\n\nWelcome to the PyToBat tool! (legacy)")

        text_to_echo = input('View help (h), read license and credits (l), create a batch file (c) or exit (e): ')
        if text_to_echo == "h":
            os.system("cls")
            print("""
88888888ba           888888888888          88888888ba                           88        88              88               
88      "8b               88               88      "8b                ,d        88        88              88               
88      ,8P               88               88      ,8P                88        88        88              88               
88aaaaaa8P'  8b       d8  88   ,adPPYba,   88aaaaaa8P'  ,adPPYYba,  MM88MMM     88aaaaaaaa88   ,adPPYba,  88  8b,dPPYba,   
88""""""'    `8b     d8'  88  a8"     "8a  88""""""8b,  ""     `Y8    88        88""""""""88  a8P_____88  88  88P'    "8a  
88            `8b   d8'   88  8b       d8  88      `8b  ,adPPPPP88    88        88        88  8PP"""""""  88  88       d8  
88             `8b,d8'    88  "8a,   ,a8"  88      a8P  88,    ,88    88,       88        88  "8b,   ,aa  88  88b,   ,a8"  
88               Y88'     88   `"YbbdP"'   88888888P"   `"8bbdP"Y8    "Y888     88        88   `"Ybbd8"'  88  88`YbbdP"'   
                 d8'                                                                                          88           
                d8'                                                                                           88           

 __                                             
|__) _ _ . _  _ . _  _    _ _  _  _  _  _  _| _ 
|__)(-(_)|| )| )|| )(_)  (_(_)||||||(_|| )(_|_) 
      _/            _/                             

Remember to write the commands in lowercase
H (help) - "h" is a command for accessing the help page (the one you are currently at)
L (licenses) - "l" is a command for reading the license of this program            
C (create) - "c" is a command for starting the process of creating a .bat file through this program
E (exit) - "e" is a command for ending the program

These commands can be executed at the "View help (h), read licenses (l) or create (c) a batch file:" prompt at the beginning
              
 __                                          
|_.| _   _ _ _ _ |_. _  _    _  _ _  _ _ _ _ 
| ||(-  (_| (-(_||_|(_)| )  |_)| (_)(_(-_)_) 
                            |                

1. Entering the name of the file you wish to create
Enter the name of the file you wish to create to the "Enter the name of the file you wish to create:" prompt
2. Entering the folder for the file to be created in
Enter the full path (eg. C:\\users\\your_username\\desktop) to the "Enter the full path of the output folder where the batch file should be saved:" prompt
3. Selecting program mode
Enter number 1 or 2 depending on your preferred option (1 for running the file after writing and 2 for not)
4. Writing the code
Write the code (use enter to create a new line)
When ready, write "STOPWRITE" and press enter
5. Finding the file
After "STOPWRITE" the file should be in the folder you specified

 __          
|_  _ . _    
|__| )|(_)\/ 
      /   / 

Thank you for using this progam
-aallon_pituus
(also there's a lot of text in this page so if you don't fully see it, scroll upwards)
""")
            input("Press enter to continue.")
        elif text_to_echo == "l":
            os.system("cls")
            print("""
88888888ba           888888888888          88888888ba                           88           88                                                                         
88      "8b               88               88      "8b                ,d        88           ""                                                                         
88      ,8P               88               88      ,8P                88        88                                                                                      
88aaaaaa8P'  8b       d8  88   ,adPPYba,   88aaaaaa8P'  ,adPPYYba,  MM88MMM     88           88   ,adPPYba,   ,adPPYba,  8b,dPPYba,   ,adPPYba,   ,adPPYba,  ,adPPYba,  
88""""""'    `8b     d8'  88  a8"     "8a  88""""""8b,  ""     `Y8    88        88           88  a8"     ""  a8P_____88  88P'   `"8a  I8[    ""  a8P_____88  I8[    ""  
88            `8b   d8'   88  8b       d8  88      `8b  ,adPPPPP88    88        88           88  8b          8PP"""""""  88       88   `"Y8ba,   8PP"""""""   `"Y8ba,   
88             `8b,d8'    88  "8a,   ,a8"  88      a8P  88,    ,88    88,       88           88  "8a,   ,aa  "8b,   ,aa  88       88  aa    ]8I  "8b,   ,aa  aa    ]8I  
88               Y88'     88   `"YbbdP"'   88888888P"   `"8bbdP"Y8    "Y888     88888888888  88   `"Ybbd8"'   `"Ybbd8"'  88       88  `"YbbdP"'   `"Ybbd8"'  `"YbbdP"'  
                 d8'                                                                                                                                                    
                d8'                                                                                                                                                     

              (MIT LICENSE)

    Copyright 2024 aallon-pituus (Github)

Permission is hereby granted, free of charge,
to any person obtaining a copy of this software
and associated documentation files (the “Software”),
to deal in the Software without restriction,
including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


                                                                                                                                                            
88888888ba           888888888888          88888888ba                             ,ad8888ba,                                    88  88                      
88      "8b               88               88      "8b                ,d         d8"'    `"8b                                   88  ""    ,d                
88      ,8P               88               88      ,8P                88        d8'                                             88        88                
88aaaaaa8P'  8b       d8  88   ,adPPYba,   88aaaaaa8P'  ,adPPYYba,  MM88MMM     88             8b,dPPYba,   ,adPPYba,   ,adPPYb,88  88  MM88MMM  ,adPPYba,  
88""""""'    `8b     d8'  88  a8"     "8a  88""""""8b,  ""     `Y8    88        88             88P'   "Y8  a8P_____88  a8"    `Y88  88    88     I8[    ""  
88            `8b   d8'   88  8b       d8  88      `8b  ,adPPPPP88    88        Y8,            88          8PP"""""""  8b       88  88    88      `"Y8ba,   
88             `8b,d8'    88  "8a,   ,a8"  88      a8P  88,    ,88    88,        Y8a.    .a8P  88          "8b,   ,aa  "8a,   ,d88  88    88,    aa    ]8I  
88               Y88'     88   `"YbbdP"'   88888888P"   `"8bbdP"Y8    "Y888       `"Y8888Y"'   88           `"Ybbd8"'   `"8bbdP"Y8  88    "Y888  `"YbbdP"'  
                 d8'                                                                                                                                        
                d8'                                                                                                                                         


aallon-pituus (Main Programmer & Creator) (Github)

YHGLeader (Programmer) (Github)



(this is a long page, if all content is not visible, scroll upwards)
""")
            input("Press enter to continue.")
        elif text_to_echo == "e":
            loopVar = False
        elif text_to_echo == "c":
            file_name = input("Enter the name of the file you wish to create: ")
            output_folder = input("Enter the full path of the output folder where the batch file should be saved: ")
            choice = input("Enter the number of your choice (1 or 2): ")

            if not choice.isdigit() or int(choice) not in [1, 2]:
                print("Invalid choice. Please select a valid option.")
            else:
                choice = int(choice)
                lines = []
                print("Enter the lines of code (Type 'STOPWRITE' when done):")
                while True:
                    line = input()
                    if line.strip().upper() == 'STOPWRITE':
                        break
                    lines.append(line)

                create_batch_file(output_folder, file_name, lines=lines, open_after_creation=(choice == 1))

# The legacy program function (as modified above)
def run_legacy_program():
    root.destroy()  # Close the GUI
    legacy_program()  # Run the legacy program

def create_batch_file(output_folder, file_name, lines=None, open_after_creation=False):
    os.makedirs(output_folder, exist_ok=True)
    batch_file_path = os.path.join(output_folder, file_name)
    with open(batch_file_path, 'w') as batch_file:
        for line in lines:
            batch_file.write(f'{line}\n')
    if open_after_creation:
        subprocess.Popen(['start', batch_file_path], shell=True)
    messagebox.showinfo("Success", f'Batch file "{file_name}" has been created in "{output_folder}".')

def on_create():
    file_name = file_name_entry.get()
    if not file_name.endswith(".bat"):
        file_name += ".bat"
    output_folder = output_folder_entry.get()
    choice = var.get()
    lines = batch_file_text.get("1.0", tk.END).strip().split('\n')
    if choice == 3:
        additional_command = cmd_command_entry.get().strip()
        cmd_command = f"start cmd.exe /k {additional_command}"
        lines.insert(0, cmd_command)
    create_batch_file(output_folder, file_name, lines=lines, open_after_creation=(choice == 1))

def browse_folder():
    folder_selected = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, folder_selected)

def show_help():
    help_window = tk.Toplevel(root)
    help_window.title("Help, contributors and license")
    help_text = """Instructions for Using PyToBat GUI:
    
1. Enter the File Name: 
   - Type the desired name of your batch file in the "Enter the name of the file you wish to create" field.
   - If you don't include ".bat" at the end, it will be added automatically.

2. Select the Output Folder:
   - Enter the path to the folder where you want to save your batch file.
   - You can also click "Browse" to select the folder.

3. Options:
   - Choose whether to open the file after creation, not open it, or create a file with the template `start cmd.exe /k`.
   - If you select the template option, you can also enter a command to run.

4. Enter Batch File Code:
   - In the text area, enter the lines of code that you want in the batch file.
   - Each line will be added in the order you write them.

5. Create the File:
   - Click "Create Batch File" to generate the batch file with the provided details.

Contributors:

aallon_pituus (Main Programmer & Owner) (Github)
YHGLeader (Programmer) (Github)

License:

Copyright 2024 aallon-pituus (on Github)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”),
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
    help_label = tk.Label(help_window, text=help_text, justify="left", padx=10, pady=10)
    help_label.pack()

root = tk.Tk()
root.title("PyToBat")

# GUI Elements...
tk.Label(root, text="Enter the name of the file you wish to create:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
file_name_entry = tk.Entry(root, width=50)
file_name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter the full path of the output folder:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.grid(row=1, column=1, padx=10, pady=10)
browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.grid(row=1, column=2, padx=10, pady=10)

tk.Label(root, text="Select an option for the batch file:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
var = tk.IntVar(value=1)
tk.Radiobutton(root, text="Open the file after done", variable=var, value=1).grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="Do not open the file after done", variable=var, value=2).grid(row=2, column=2, sticky="w")
tk.Radiobutton(root, text="Create with template 'start cmd.exe /k'", variable=var, value=3).grid(row=3, column=1, sticky="w")

tk.Label(root, text="Command to run with 'start cmd.exe /k':").grid(row=4, column=0, padx=10, pady=10, sticky="w")
cmd_command_entry = tk.Entry(root, width=50)
cmd_command_entry.grid(row=4, column=1, padx=10, pady=10)

tk.Label(root, text="Enter the lines of code for the batch file:").grid(row=5, column=0, padx=10, pady=10, sticky="w")
batch_file_text = scrolledtext.ScrolledText(root, width=60, height=10)
batch_file_text.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

create_button = tk.Button(root, text="Create Batch File", command=on_create)
create_button.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

help_button = tk.Button(root, text="Help, Contributors and License", command=show_help)
help_button.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

# Button to close the GUI and run the legacy program
run_legacy_button = tk.Button(root, text="Run Legacy Program", command=run_legacy_program)
run_legacy_button.grid(row=9, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
