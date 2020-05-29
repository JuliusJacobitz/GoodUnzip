from subprocess import call
from time import sleep
from pathlib import Path
import os
import zipfile
import json

formats = [".zip"]  #maybe rar ? not tested
Currentwd = os.getcwd()
new_wd = None


def openStatJsonR():
    try:
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"\statistics.txt") as json_file:
            statisticData = json.load(json_file)
            return statisticData
    except Exception as e:
        print(e)


def add_del_folders_stat(amount):
    try:
        statData = openStatJsonR()
        statData["folders_deleted"] += amount
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"\statistics.txt", 'w') as outfile:
            json.dump(statData, outfile)

    except Exception as e:
        print(e)


def add_unzipped_stat(amount):
    try:
        statData = openStatJsonR()
        statData["data_unzipped"] += amount
        with open(str(os.path.dirname(os.path.abspath(__file__))) + r"\statistics.txt", 'w') as outfile:
            json.dump(statData, outfile)

    except Exception as e:
        print(e)


def createBackup(c, file_n, cwd):
    global new_wd
    try:
        os.mkdir(cwd + r"\{0}_{1}".format(file_n, c))
        new_wd = cwd + r"\{0}_{1}".format(file_n, c)
        print("> created backup folder: {0}".format(new_wd))
    except:
        createBackup(c + 1, file_n, cwd)

def searchZip(entry):
    path = Path(entry)
    for i in os.scandir(path):
        if i.is_dir():
            searchZip(i)
        else:
            filepath = Path(i)
            wholefilename = Path(i.name)
            file_name,file_format = os.path.splitext(str(wholefilename))
            if file_format in formats:
                #unzip2(i)
                print("found zip would unzip it !!")
                pass

def unzip2(entry,delcheck=False):   #filepath muss vom typen Path sein, dir auch
    try:
        filepath = Path(entry)
        filedir = os.path.abspath(filepath)
        whole_file_name = Path(entry.name)
        file_name, file_format = os.path.splitext(str(whole_file_name))


    except Exception as e:
        print(e)



def unzip(scandir, cwd, delcheck=False):
    global new_wd
    if type(scandir) == str:
        scandirstr = scandir
        scandir = os.scandir(scandir)
    else:
        scandirstr = cwd

    for entry in scandir:
        if entry.is_dir():
            #todo
            #make it possible to get into this folder and do unzip with auto del for every zip folder
            #print("this is a folder entry: ",entry)
            pass
        if not entry.is_dir():
            file_path = Path(entry.name)
            file_name, file_format = os.path.splitext(str(file_path))
            whole_path = cwd + r"\{0}".format(file_path)

            if file_format in formats:
                try:
                    os.mkdir(cwd + r"\{0}".format(file_name))
                    new_wd = cwd + r"\{0}".format(file_name)
                    print("> created folder: {0}".format(new_wd))
                except Exception as e:
                    createBackup(1, file_name, cwd=scandirstr)

                try:
                    with zipfile.ZipFile(whole_path, 'r') as zip_ref:
                        zip_ref.extractall(new_wd)
                    print("> transfer completed")
                    add_unzipped_stat(1)

                    if delcheck == True:
                        try:
                            checker = input(r"> Delete Zip? Insert 'n' for no: ")
                            if checker != "n":
                                os.remove(whole_path)
                                print("> removed zip folder: {0}".format(file_path))
                                add_del_folders_stat(1)

                        except Exception as e:
                            print(e)
                            # error handling
                        print("\n")

                    elif delcheck == False:
                        try:
                            os.remove(whole_path)
                            print("> removed zip folder: {0}".format(file_path))
                            add_del_folders_stat(1)
                        except Exception as e:
                            print(e)
                            # error handling
                    else:
                        print("sth went wrong with zip file removal")

                except Exception as e:
                    print(e)

                """Before moving on getting into the created directory and searching for zip files"""
                try:
                    unzip(new_wd, new_wd)
                    new_wd = None
                except Exception as e:
                    print(e)
                    sleep(10)

try:
    unzip(os.scandir(), cwd=Currentwd, delcheck=True)
except Exception as e:
    print(e)
    sleep(100)
print("> done!")


"""
#new structure: 

execute script in a folder 

search through folder if folder is found get into it search for folder in it 
if zip is found: unzip it 

problem, what if unzipped data contains zip


"""