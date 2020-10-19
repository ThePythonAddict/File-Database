import os
import csv
from Operation import DirOperation

filepath = DirOperation.firstcheck(0)
fh = open("GitBackup.baseconfig",'r')
gitRepositoryName = []
reader = csv.reader(fh)
for line in reader:
    gitRepositoryName.append(line[0])


while True:
    Directories = DirOperation.config()
    print("What Do You Want To Do?")
    print("i = Insert New Directory | o = Open Existing Directory | Delete Existing Directory")
    a = input("- ")

    if a == "i":
        c = 1
        basename = input("Insert Database Name: ")
        if os.path.exists(gitRepositoryName[0]+"\\"+basename) == True:
            print("Database Already Exists!")
            continue
        else:
            dirname, filename = DirOperation.makeDir(basename, filepath)
            print("You are in the '" + dirname + "' database.")
            while True:
                print("Add a new field (EEE = exit)")
                b = input("- ")
                if b == "EEE":
                    fh = open(filename + "\FieldCounter.baseconfig", 'w')
                    fh.write(str(c))
                    fh.close()
                    break
                else:
                    while True:
                        print("Are you sure you want to create the field: " + b + "? (Y/N)")
                        check = input("- ")
                        if check == "Y":
                            check = DirOperation.createField(dirname, b, c)
                            if check == "Error":
                                pass
                            else:
                                c = c+1
                            break
                        
                        elif check == "N":
                            break

    
    if a == "o":
        if len(Directories) == 0:
            print("Database Is Empty!")
        else: 
            print("What Do You Want To Do?")
            print("i = Insert New Data | r = Read Existing Data | b = Backup Existing Data | s = Database Settings")
            g = input("- ")
            if g == "i":
                query = input("Enter Database Name: ")
                check2 = DirOperation.openDir(query, Directories)
                if check2 == "Error":
                    continue
                else:
                    print("You Are In The '" + query + "' Database")
                    DirOperation.InBF.NewData(query)
                continue

            if g == "r":
                query = input("Enter Database Name: ")
                check2 = DirOperation.openDir(query, Directories)
                if check2 == "Error":
                    continue
                else:
                    print("Compiling Process Will Start When You Press Enter. Restart Program If You Don't Want To Continue: ")
                    input(" ")
                    DirOperation.InBF.ReadData(query)
            
            if g == "s":
                query = input("Enter Database Name: ")
                check2 = DirOperation.openDir(query, Directories)
                if check2 == "Error":
                    continue
                else:
                    print("i = Insert Subdirectory")
                    h = input("- ")
                    if h == "i":
                        subDirName = input("Enter Name Of Subdirecotry: ")
                        print("Are You Sure You Want This Subdirectory?\n(Y/N) " + subDirName)
                        check = input("- ")
                        if check == "Y": 
                            DirOperation.InBF.NewDir(query, subDirName)
                            break
                        if check == "N":
                            print("Cancelled")
                            continue
            if g == "b":
                print("Do You Want To Backup Your Data?")
                check = input("- ")
                if check == "Y": 
                    print("Backing Database Up")
                    DirOperation.InBF.GitBackup()
                    continue
                if check == "N":
                    print("Cancelled")
                    continue




    if a == "d":
        if len(Directories) == 0:
            print("Please Add A Database!")
        else:
            print("Which Directory Do You Want To Delete?")
            Directories = DirOperation.config()
            for i in Directories:
                print(i)
            DName = input("- ")
            for i in Directories:
                if i == DName:
                    print("Are You Sure You Want To Delete '" + DName+ "'?\nTHIS CANNOT BE UNDONE!!\n(Y/N)" )
                    check = input("- ")
                    if check == "Y":
                        Directories.remove(DName)
                        DirOperation.deleteDir(DName,Directories)