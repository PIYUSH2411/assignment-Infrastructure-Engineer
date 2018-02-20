1. Install python 3 and set path variable.
2. Download and install pywin32 from [ https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/ ]
3. Open command prompt as administrator, point to the directory where the python script is present.
4. Run the script using the command -> python script.py
5. All files (except shortcuts) on desktop will be moved to subfolder named as per the file extension in document folder and it will show 10 largest files for all the drives present in computer.
6. To give the directory manually from which you want to get 10 largest files, follow these steps --
       -> comment out these two lines in the script.
              [#print("Enter the directory : ")]
              [#dir = input()]

       -> comment this line { for dir in win32api.GetLogicalDriveStrings().split('\000')[:-1]: } and indent the script again.
       -> now, when you will run the script it will ask for the directory name, provide any directory of your choice (eg. C:/Python33/)and it will show 10 largest files present in that directory.

