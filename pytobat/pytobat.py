import os
import subprocess

#        Copyright 2024 aallon-pituus (Github)
#
# Permission is hereby granted, free of charge,
# to any person obtaining a copy of this software
# and associated documentation files (the “Software”),
# to deal in the Software without restriction,
# including without limitation the rights to use, copy,
# modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


def create_batch_file(output_folder, option, lines=None, open_after_creation=False) :
     # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Define the batch file path
    batch_file_name = file_name_choice
    batch_file_path = os.path.join(output_folder, batch_file_name)

    # Create the batch file with the selected option
    with open(batch_file_path, 'w') as batch_file:
        if option == 1:
            for line in lines:
                batch_file.write(f'{line}\n')
                if open_after_creation:
                    subprocess.Popen(['start', batch_file_path], shell=True)
        elif option == 2:
            for line in lines:
                batch_file.write(f'{line}\n')

    print(f'Batch file "{batch_file_name}" has been created in "{output_folder}".')


while True:
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
    print("\n\n\nWelcome to the PyToBat tool!")

    text_to_echo = input('View help (h), read license and credits (l) or create a batch file (c): ')
    if text_to_echo == "h":
        os.system("cls")
        print('''                                                                                                                         
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
              
H (help) - H is a command for accessing the help page (the one you are currently at)
L (licenses) - L is a command for reading the license of this program            
C (create) - C is a command for starting the process of creating a .bat file through this program

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
''')
        ready_to_move_on = input("Press enter to continue. ")
    elif text_to_echo == "l":
        os.system("cls")
        print('''
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
''')
        ready_to_move_on = input("Press enter to continue. ")
    elif text_to_echo == "c":
        file_name_choice = input("Enter the name of the file you wish to create: ")
        output_folder = input("Enter the full path of the output folder where the batch file should be saved: ")
        print("\nSelect an option for the batch file:")
        print("1. Open the file after done")
        print("2. Do not open file after done")
        choice = input("Enter the number of your choice (1 or 2): ")

        if not choice.isdigit() or int(choice) not in [1, 2, 3]:
            print("\nInvalid choice. Please select a valid option.\n\nPress enter to continue")
            input()
        else:
            choice = int(choice)
            
        if choice == 1:
            print("\nEnter the lines of code you want to include in the batch file. (press enter for a new line)")
            print("Type 'STOPWRITE' on a new line when you are finished.")
            lines = []
            while True:
                line = input()
                if line.strip().upper() == 'STOPWRITE':
                    break
                lines.append(line)
            create_batch_file(output_folder, choice, lines=lines, open_after_creation=True)
        if choice == 2:
            print("Enter the lines of code you want to include in the batch file. (press enter for a new line)")
            print("Type 'STOPWRITE' on a new line when you are finished.")
            lines = []
            while True:
                line = input()
                if line.strip().upper() == 'STOPWRITE':
                    break
                lines.append(line)
            create_batch_file(output_folder, choice, lines=lines)
