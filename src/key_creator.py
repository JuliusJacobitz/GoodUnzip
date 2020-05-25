import os
import sys
import winreg as reg

cwd = os.getcwd()

python_exe = sys.executable

key_path = r"Directory\\Background\\shell\\GoodUnzipKey"

key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)

reg.SetValue(key, '', reg.REG_SZ, '&Good Unzip!')

key1 = reg.CreateKey(key, r"command")
reg.SetValue(key1, '', reg.REG_SZ, python_exe + ' "' + cwd + r"\goodUnzip_02.py" + '"')     # important str has to look like: ...python.exe "..src/test.py"


#print(python_exe + ' "'+cwd+r"\testKey.py"+'"')