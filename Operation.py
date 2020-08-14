import csv
import os
import shutil

class DirOperation:

    def firstcheck(b):
        fh = open('filepath.baseconfig','r')
        reader = csv.reader(fh)
        FPCheck = []
        for Line in reader:
            FPCheck.append(Line[0])
        FPCheck.pop(0)
        fh.close()
        if len(FPCheck) == 0:
            print("Hey! Is This Your First Time? Welcome!")
            print("Before You Start File Database")
            print("We Need To Know Which File Path You Want To Store Your Data In")
            while True:
                print("Please Enter The Full File Path")
                filepath = input("- ")
                check = input("Is This Your Correct File Path? (Y/N): " + filepath)
                if check == "Y":
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
                    return FPCheck[0]
                    break
                if check == "N":
                    break
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
        flag = True
        newpath = os.path.join(parent_dir,newdir)
        if not os.path.exists(newpath):
            os.makedirs(newpath)
            fh = open('Directories.baseconfig','a')
            fh.write("\n" + str(newdir))
            fh.close()
            print("Database Folder Created!")
            filename = DirOperation.writeDir(newdir)
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
        filename = str(dirName) + "\system.baseconfig"
        fh = open(filename,'w')
        fh.write("Fields")
        fh.close()
        return dirName
    
    
    def createField(dirName,fieldName,a):
            flag = False
            System = DirOperation.systemconfig(dirName)
            if System == "Error":
                return System
            else:
                filename = str(dirName) +"\Field" + str(a) + "_" + str(fieldName) + ".basefield"
                fh = open(filename,'w')
                fh.write(fieldName)
                fh.close()
                filename2 = str(dirName) + "\system.baseconfig"
                fh2 = open(filename2,'a')
                fh2.write("\n"+str(fieldName))
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
                        for i in Fields:
                            filename = dirName + "\Field" + str(c) + "_" + str(i) + ".basefield"
                            fh = open(filename, 'a')
                            fh.write("\n"+inputs[c-1])
                            fh.close()
                            c = c+1
                        break
                    if check == "N":
                        print("Cancelled")
                        break

        def ReadData(dirName):
            my_lists = []
            for i in range(1,6):
                new_list = []
                for j in range(10):
                    new_list.append(j)
                my_lists.append(new_list)