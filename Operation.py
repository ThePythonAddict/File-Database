import csv
import os
import shutil
import pathlib
import git
import datetime

class DirOperation:

    def firstcheck(b):
        try:
            fh = open('GitBackup.baseconfig','r')
        except:
            fh = open("Directories.baseconfig",'w')
            fh.write("Directories")
            fh.close()
            fh = open("filepath.baseconfig",'w')
            fh.write("Filepath")
            fh.close()
            fh = open("GitBackup.baseconfig",'w')
            fh.close()
        fh = open('filepath.baseconfig','r')
        reader = csv.reader(fh)
        FPCheck = []
        for Line in reader:
            FPCheck.append(Line[0])
        FPCheck.pop(0)
        fh.close()
        if len(FPCheck) == 0:
            print("Enter GitHub Repository Name (With Hyphens) (SSS = Skip)")
            name = input("- ")
            if name == "SSS":
                print("Skipping")
                filepath = str(pathlib.Path(__file__).parent.absolute())
                fh = open('filepath.baseconfig','a')
                fh.write("\n"+filepath)
                fh.write("\n"+filepath + "\\")
                fh.close()
                fh = open('filepath.baseconfig','r')
                reader = csv.reader(fh)
                FPCheck = []
                for Line in reader:
                    FPCheck.append(Line[0])
                FPCheck.pop(0)
                fh.close()
            else:
                print("Are You Sure This Is Correct?")
                check = input("Y/N")
                if check == "Y":
                    fh = open("GitBackup.baseconfig", 'w')
                    fh.write(name + "\n")
                    fh.close()
                    print("Enter GitHub Repository Link")
                    repo = input("- ")
                    print("Are You Sure This Is Correct?")
                    check = input("Y/N")
                    if check == "Y":
                        fh = open("GitBackup.baseconfig", 'a')
                        fh.write(repo)
                        fh.close()
                        print("Cloning Repository. Please Wait")
                        try:
                            git.Git().clone(repo)
                        except:
                            print("There Was An Error Downloading The Repository")
                        filepath = str(pathlib.Path(__file__).parent.absolute())
                        fh = open('filepath.baseconfig','a')
                        fh.write("\n"+filepath + "\\"+name)
                        fh.write("\n"+filepath + "\\"+name+"\\")
                        fh.close()
                        fh = open('filepath.baseconfig','r')
                        reader = csv.reader(fh)
                        FPCheck = []
                        for Line in reader:
                            FPCheck.append(Line[0])
                        FPCheck.pop(0)
                        fh.close()
                    elif check == "N":
                        pass
                elif check == "N":
                    pass
        else:
            fh = open('filepath.baseconfig','r')
            reader = csv.reader(fh)
            FPCheck = []
            for Line in reader:
                FPCheck.append(Line[0])
            FPCheck.pop(0)
            fh.close()
            return FPCheck[b]

    def config():
        fh = open('Directories.baseconfig','r')
        reader = csv.reader(fh)
        Directories = []
        for Line in reader:
            Directories.append(Line[0])
        Directories.pop(0)
        return Directories

    def makeDir(newdir, parent_dir):
        flag = False
        newpath = os.path.join(parent_dir,newdir)
        if not os.path.exists(newpath):
            os.makedirs(newpath)
            fh = open('Directories.baseconfig','a')
            fh.write("\n"+str(newdir))
            fh.close()
            print("Database Folder Created!")
            filename = DirOperation.writeDir(newpath)
            return newdir, filename


    def openDir(searchdir, Directories):
        flag2 = False
        for i in range(len(Directories)):
            if Directories[i] == searchdir:
                print(i)
                b = i
                flag2 = True
        if flag2 == True:
            print("Directory Found")
            return Directories[b]
        else:
            print("Directory Not Found")
            return "Error"

    def systemconfig(dirName):
        parent_dir = DirOperation.firstcheck(1)
        print(parent_dir)
        fh = open(parent_dir + dirName + "\system.baseconfig", 'r')
        reader = csv.reader(fh)
        Fields = []
        try:
            for Line in reader:
                Fields.append(Line[0])
            fh.close()
            return Fields
        except:
            print("There was an error adding the field. Please make sure this field does not exist. ")
            Flag = "Error"
            return Flag
    
    def writeDir(dirName):
        fh = open(str(dirName)+"/system.baseconfig",'w')
        fh.write("Fields\n")
        fh.close()
        fh = open(str(dirName)+"/filepath.baseconfig",'w')
        fh.write("Filepath\n")
        fh.close()
        fh = open(str(dirName)+"/subfolders.baseconfig",'w')
        fh.write("Subfolders\n")
        fh.close()
        fh = open(str(dirName)+"/FieldCounter.baseconfig",'w')
        fh.close()
        return dirName
    
    
    def createField(dirName,fieldName,a):
            flag = False
            System = DirOperation.systemconfig(dirName)
            repo = DirOperation.firstcheck(1)
            if System == "Error":
                return System
            else:
                filename = str(repo + dirName) +"\Field" + str(a) + "_" + str(fieldName) + ".basefield"
                fh = open(filename,'w')
                fh.write(fieldName)
                fh.close()
                filename2 = str(repo + dirName) + "\system.baseconfig"
                fh2 = open(filename2,'a')
                fh2.write(str(fieldName)+"\n")
                fh2.close()
                return "Success"

    #Delete Dir Operations

    def deleteDir(dirName,Directories):
        path = '/' + str(dirName)
        shutil.rmtree(path)
        print("Database Succesfully Deleted")
        fh = open('Directories.baseconfig', 'w')
        Directories.insert(0,"Directories")
        for i in Directories:
            fh.write(i + "\n")
        fh.close()


    #Open Dir Operations

    class InBF:

        def NewData(dirName):
            Fields = DirOperation.systemconfig(dirName)
            if Fields == "Error":
                print("There was an error")
            else:
                c = 1
                Fields.pop(0)
                inputs = []
                for i in Fields:
                    m = input("Enter information for column, '" + i + "': ")
                    inputs.append(m)
                print("Is this information correct?")
                for i in inputs:
                    print(i)
                while True:
                    check = input("- ")
                    if check == "Y":
                        repo = DirOperation.firstcheck(1)
                        for i in Fields:
                            filename = dirName + "\Field" + str(c) + "_" + str(i) + ".basefield"
                            fh = open(repo+filename, 'a')
                            fh.write("\n"+inputs[c-1])
                            fh.close()
                            c = c+1
                        break
                    if check == "N":
                        print("Cancelled")
                        break

        def ReadData(dirName):
            filename = dirName+"\\system.baseconfig"
            rangecounter = dirName+"\\FieldCounter.baseconfig"
            fh = open(filename, 'r')
            fh2 = open(rangecounter, 'r')
            
            reader = csv.reader(fh)
            fields = []
            for line in reader:
                fields.append(line[0])
            
            reader2 = csv.reader(fh2)
            for line in reader2:
                reader2 = line[0]

            lists = []
            print(reader2)
            for i in range(int(reader2)-1):
                print(i+1)
                fieldname = dirName + "\\Field" + str(i+1) + "_" + fields[i+1] + ".basefield"
                fieldlist = []
                fh3 = open(fieldname, 'r')
                reader3 = csv.reader(fh3)
                for line in reader3:
                    fieldlist.append(line[0])
                lists.append(fieldlist)
                fh3.close()
            compdata = dirName + "\\Compiled_Data.csv"
            fieldnames = []
            for i in range(int(reader2)-1):
                fieldnames.append(lists[i][0])
            print(fieldnames)
            for i in lists:
                 i.pop(0)
            for i in range(len(lists[0])):
                for j in range(len(fieldnames)):
                    print(fieldnames[j] + ": " + lists[j][i])
                print("==========================")
        
        def NewDir(dirMain,dirSub):
            os.makedirs(dirMain+"/"+dirSub)
            fh = open("filepath.baseconfig",'r')
            reader = csv.reader(fh)
            filepath = []
            for line in reader:
                filepath.append(line[0])
            fh.close()
            fh = open(dirMain+"/filepath.baseconfig",'a')
            fh.write(filepath[2]+dirMain+"\\"+dirSub+"\n")
            fh.close()
            fh = open(dirMain+"/subfolders.baseconfig",'a')
            fh.write(dirSub+"\n")
            fh.close()

        def GitBackup():
            # try:
                fh = open("GitBackup.baseconfig",'r')
                reader = csv.reader(fh)
                repo = []
                for line in reader:
                    repo.append(line[0])
                if len(repo) == 0:
                    print("You Need To Add A GitHub Repository Before Using This")
                    print("Would You Like To Add Your GitHub Repository? (Y/N)")
                    check = input("- ")
                    if check == "Y":
                        print("Enter GitHub Repository Name (With Hyphens)")
                        name = input("- ")
                        print("Are You Sure This Is Correct?")
                        check = input("Y/N")
                        if check == "Y":
                            fh = open("GitBackup.baseconfig", 'w')
                            fh.write(name + "\n")
                            fh.close()                        
                        print("Enter GitHub Repository Link")
                        repo = input("- ")
                        print("Are You Sure This Is Correct?")
                        check = input("Y/N")
                        if check == "Y":
                            fh = open("GitBackup.baseconfig", 'a')
                            fh.write(repo)
                            fh.close()
                else:
                    fh = open("GitBackup.baseconfig",'r')
                    gitrepo = []
                    reader = csv.reader(fh)
                    for line in reader:
                        gitrepo.append(line[0])
                    fh.close()
                    repo = git.Repo(gitrepo[0])
                    fh = open("Directories.baseconfig",'r')
                    directories = []
                    reader = csv.reader(fh)
                    for line in reader:
                        directories.append(line[0])
                    fh.close()
                    directories.pop(0)
                    totalfiles = []
                    for i in directories:
                        fields = []
                        fh = open(gitrepo[0]+"/"+ i + "/system.baseconfig",'r')
                        reader = csv.reader(fh)
                        for line in reader:
                            fields.append(line[0])
                        fh.close()
                        fields.pop(0)
                        for j in range(len(fields)):
                            totalfiles.append(i +"/Field"+str(j+1)+"_"+fields[j]+".basefield")
                        totalfiles.append(i + "/system.baseconfig")
                        totalfiles.append(i + "/subfolders.baseconfig")
                        totalfiles.append(i + "/filepath.baseconfig")
                        totalfiles.append(i + "/FieldCounter.baseconfig")
                    print(totalfiles)
                    repo.index.add(totalfiles)
                    repo.index.commit("Database Backed Up By File Database 1.8")
                    origin = repo.remote('origin')
                    origin.push()
                    print("Database Backup Successfull")