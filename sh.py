import os 
import subprocess
os.system("git clone https://github.com/Igcifiifigci/mainrepo")
os.chdir("mainrepo")
os.system("python -m pip install --upgrade pip")
process = subprocess.Popen(
        ["python3", "-m", "SuperBot"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,)
out, er = process.communicate()
if er:
    print(er.decode())
print("::::::::::::::")
if out:
    print(out.decode())
