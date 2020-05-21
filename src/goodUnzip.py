from subprocess import call
from time import sleep
from pathlib import Path
import os
import zipfile
import json

formats = [".zip", ".rar"]
cwd = os.getcwd()
new_wd = None

try:
    with open() as json_file:
        data = json.load(json_file)
        for i in data:
            print(i)
except Exception as e:
    print(e)

# todo
def add_del_folders_stat(amount):
    pass


# todo
def add_unzipped_stat(amount):
    pass


def createBackup(c):
    global new_wd
    try:
        os.mkdir(cwd + r"\{0}_{1}".format(file_name, c))
        new_wd = cwd + r"\{0}_{1}".format(file_name, c)
        print("> created backup folder: {0}".format(new_wd))
    except:
        createBackup(c + 1)


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
                createBackup(1)

            try:
                with zipfile.ZipFile(whole_path, 'r') as zip_ref:
                    zip_ref.extractall(new_wd)
                print("> transfer completed")
                add_unzipped_stat(1)

                try:
                    checker = input(r"> Delete Zip? Insert 'n' for no: ")
                    if checker != "n":
                        os.remove(whole_path)
                        print("> removed zip folder: {0}".format(file_path))
                        add_del_folders_stat()

                except Exception as e:
                    print(e)
                    # error handling
                print("\n")
            except Exception as e:
                print(e)
                # error handling

print("> done!")
sleep(1000)
