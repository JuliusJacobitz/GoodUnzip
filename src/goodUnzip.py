from subprocess import call
from time import sleep
from pathlib import Path
import os
import zipfile

formats = [".zip", ".rar"]
cwd = os.getcwd()
new_wd = None

def createBackup(c):
    global new_wd
    try:
        os.mkdir(cwd + r"\{0}_{1}".format(file_name, c))
        new_wd = cwd + r"\{0}_{1}".format(file_name, c)
        print("> created backup folder: {0}".format(new_wd))
    except:
        createBackup(c+1)


for entry in os.scandir():
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
                #print(e)
                createBackup(1)

            try:
                with zipfile.ZipFile(whole_path, 'r') as zip_ref:
                    zip_ref.extractall(new_wd)
                print("> transfer completed")

                try:
                    checker = input(r"Delete Zip? Insert 'n' for no: ")
                    if checker != "n":
                        os.remove(whole_path)
                        print("> removed zip folder: {0}".format(file_path))
                except Exception as e:
                    print(e)
                    # error handling 
            except Exception as e:
                    print(e)
                    # error handling

print("> done!")
sleep(0.2)
