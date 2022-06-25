from generator import obfuscate
import zlib, base64

def test_obfuscator():
    line = obfuscate('Hello World!').split("\n")[1]
    #instead of decompiling and executing, we just want the decompiled content, no execution
    line = line.replace("exec(", "")
    line = line[:-1]
    #check the decompiled output
    output = eval(f"{line}")
    assert output == "Hello World!"

def test_app():
    from pid import PidFile

test_app()