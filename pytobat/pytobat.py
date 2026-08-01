import os
import platform
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# ----------------------------------------------------------------------
# Core Utility Functions
# ----------------------------------------------------------------------

def clear_screen():
    """Cross-platform terminal screen clear."""
    os.system("cls" if platform.system() == "Windows" else "clear")

def create_batch_file(output_folder, file_name, lines=None, open_after_creation=False):
    """Generates the .bat file and handles file system execution."""
    if lines is None:
        lines = []

    if not output_folder:
        messagebox.showerror("Error", "Output folder path cannot be empty.")
        return False

    if not file_name:
        messagebox.showerror("Error", "File name cannot be empty.")
        return False

    if not file_name.lower().endswith(".bat"):
        file_name += ".bat"

    try:
        os.makedirs(output_folder, exist_ok=True)
        batch_file_path = os.path.join(output_folder, file_name)

        with open(batch_file_path, "w", encoding="utf-8") as batch_file:
            for line in lines:
                batch_file.write(f"{line}\n")

        if open_after_creation:
            if platform.system() == "Windows":
                subprocess.Popen(["start", batch_file_path], shell=True)
            else:
                messagebox.showwarning("Platform Warning", "Auto-run is only supported natively on Windows.")

        messagebox.showinfo("Success", f'Batch file "{file_name}" created in:\n"{output_folder}"')
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Failed to write file: {e}")
        return False


# ----------------------------------------------------------------------
# Legacy CLI Application
# ----------------------------------------------------------------------

ASCII_TITLE = r"""
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
"""

def legacy_program():
    loop_var = True
    while loop_var:
        clear_screen()
        print(ASCII_TITLE)
        print("\nWelcome to the PyToBat tool! (legacy mode)\n")

        choice = input("View help (h), read license (l), create batch file (c), or exit (e): ").strip().lower()

        if choice == "h":
            clear_screen()
            print(ASCII_TITLE)
            print("""
--- HELP PAGE ---
Commands:
  h - Access help page
  l - View licenses and credits
  c - Create a batch file
  e - Exit to main menu

How to create a file:
  1. Provide target filename.
  2. Provide absolute folder destination path.
  3. Select execution behavior mode (1 = Run after write, 2 = Write only).
  4. Write lines sequentially. Type 'STOPWRITE' on a new line when finished.
            """)
            input("\nPress ENTER to continue...")

        elif choice == "l":
            clear_screen()
            print(ASCII_TITLE)
            print("""
--- LICENSE & CREDITS ---
MIT LICENSE
Copyright (c) 2026 aallon-pituus

Main Programmer & Creator: aallon-pituus
Programmer: YHGLeader
            """)
            input("\nPress ENTER to continue...")

        elif choice == "c":
            file_name = input("\nEnter output file name: ").strip()
            output_folder = input("Enter full output folder path: ").strip()
            mode = input("Select mode (1 = run after creation, 2 = do not run): ").strip()

            if mode not in ["1", "2"]:
                print("Invalid selection.")
                input("\nPress ENTER to return...")
                continue

            lines = []
            print("\nEnter batch script content (Type 'STOPWRITE' on a new line to save):")
            while True:
                line = input()
                if line.strip().upper() == "STOPWRITE":
                    break
                lines.append(line)

            create_batch_file(output_folder, file_name, lines, open_after_creation=(mode == "1"))
            input("\nPress ENTER to continue...")

        elif choice == "e":
            loop_var = False


# ----------------------------------------------------------------------
# Modernized Tkinter Application Class
# ----------------------------------------------------------------------

class PyToBatGUI:
    def __init__(self, root_window):
        self.root = root_window
        self.root.title("PyToBat Studio")
        self.root.geometry("640x750")
        self.root.minsize(500, 600)

        self._init_styles()
        self._build_ui()

    def _init_styles(self):
        self.root.option_add("*Font", "TkDefaultFont 9")

    def _build_ui(self):
        # Main Container
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Config Section
        config_group = tk.LabelFrame(main_frame, text=" File Configuration ", padx=10, pady=10)
        config_group.pack(fill=tk.X, pady=(0, 10))

        tk.Label(config_group, text="File Name:").grid(row=0, column=0, sticky="w", pady=2)
        self.file_name_entry = tk.Entry(config_group)
        self.file_name_entry.insert(0, "script.bat")
        self.file_name_entry.grid(row=0, column=1, sticky="ew", padx=(10, 0), pady=2)

        tk.Label(config_group, text="Output Directory:").grid(row=1, column=0, sticky="w", pady=2)
        self.output_folder_entry = tk.Entry(config_group)
        self.output_folder_entry.insert(0, os.path.expanduser("~"))
        self.output_folder_entry.grid(row=1, column=1, sticky="ew", padx=(10, 5), pady=2)

        browse_btn = tk.Button(config_group, text="Browse...", command=self.browse_folder)
        browse_btn.grid(row=1, column=2, pady=2)

        config_group.columnconfigure(1, weight=1)

        # Execution Behavior Options (Radio buttons)
        options_group = tk.LabelFrame(main_frame, text=" Post-Creation Action ", padx=10, pady=10)
        options_group.pack(fill=tk.X, pady=(0, 10))

        self.mode_var = tk.IntVar(value=1)
        tk.Radiobutton(options_group, text="Open file after creation", variable=self.mode_var, value=1).pack(anchor="w")
        tk.Radiobutton(options_group, text="Do not open file after creation", variable=self.mode_var, value=2).pack(anchor="w")

        # Independent Template Section (Checkbox + Dynamic Input)
        template_group = tk.LabelFrame(main_frame, text=" Script Prefixes & Templates ", padx=10, pady=10)
        template_group.pack(fill=tk.X, pady=(0, 10))

        self.use_template_var = tk.BooleanVar(value=False)
        self.template_checkbox = tk.Checkbutton(
            template_group,
            text="Add template 'start cmd.exe /k'",
            variable=self.use_template_var,
            command=self._toggle_cmd_field
        )
        self.template_checkbox.pack(anchor="w")

        cmd_frame = tk.Frame(template_group)
        cmd_frame.pack(fill=tk.X, pady=(5, 0))
        tk.Label(cmd_frame, text="Command prefix:").pack(side=tk.LEFT)
        self.cmd_command_entry = tk.Entry(cmd_frame, state=tk.DISABLED)
        self.cmd_command_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))

        # Editor Section
        editor_group = tk.LabelFrame(main_frame, text=" Batch Script Editor ", padx=10, pady=10)
        editor_group.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        self.editor_text = scrolledtext.ScrolledText(editor_group, wrap=tk.NONE, font=("Consolas", 10))
        self.editor_text.pack(fill=tk.BOTH, expand=True)

        # Action Buttons Section
        btn_frame = tk.Frame(main_frame)
        btn_frame.pack(fill=tk.X)

        create_btn = tk.Button(btn_frame, text="Generate Batch File", bg="#2b8a3e", fg="white", font=("TkDefaultFont", 10, "bold"), command=self.on_create)
        create_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        legacy_btn = tk.Button(btn_frame, text="Run Legacy CLI Mode", command=self.run_legacy)
        legacy_btn.pack(side=tk.LEFT, padx=(0, 5))

        help_btn = tk.Button(btn_frame, text="Help & About", command=self.show_help)
        help_btn.pack(side=tk.RIGHT)

    def _toggle_cmd_field(self):
        if self.use_template_var.get():
            self.cmd_command_entry.config(state=tk.NORMAL)
        else:
            self.cmd_command_entry.config(state=tk.DISABLED)

    def browse_folder(self):
        selected = filedialog.askdirectory()
        if selected:
            self.output_folder_entry.delete(0, tk.END)
            self.output_folder_entry.insert(0, selected)

    def on_create(self):
        file_name = self.file_name_entry.get().strip()
        output_folder = self.output_folder_entry.get().strip()
        lines = self.editor_text.get("1.0", tk.END).rstrip().split("\n")

        # Independent Checkbox Logic: Add prefix if enabled
        if self.use_template_var.get():
            additional_cmd = self.cmd_command_entry.get().strip()
            lines.insert(0, f"start cmd.exe /k {additional_cmd}".strip())

        # Independent Radio Logic: Run post-creation action
        open_after = (self.mode_var.get() == 1)

        create_batch_file(output_folder, file_name, lines=lines, open_after_creation=open_after)

    def run_legacy(self):
        self.root.destroy()
        legacy_program()

    def show_help(self):
        help_dialog = tk.Toplevel(self.root)
        help_dialog.title("About PyToBat Studio")
        help_dialog.geometry("520x400")

        text_area = scrolledtext.ScrolledText(help_dialog, wrap=tk.WORD, font=("TkDefaultFont", 9))
        text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        help_text = """PyToBat Studio Documentation

1. Setup Parameters:
   - Provide your .bat target file name.
   - Choose the destination folder path using the browser.

2. Post-Creation Action:
   - Choose whether the script auto-launches upon build independently of content templates.

3. Script Prefixes:
   - Check "Add template 'start cmd.exe /k'" to force the batch file to execute inside a persistent CMD window with optional arguments.

4. Script Syntax:
   - Enter standard Batch / CMD commands line-by-line into the workspace editor.

--------------------------------------------------
Credits:
- aallon-pituus (Main Programmer & Owner)
- YHGLeader (Programmer)

License: MIT
"""
        text_area.insert(tk.END, help_text)
        text_area.config(state=tk.DISABLED)


# ----------------------------------------------------------------------
# Application Entry Point
# ----------------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = PyToBatGUI(root)
    root.mainloop()
