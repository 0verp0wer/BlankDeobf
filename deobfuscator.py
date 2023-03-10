import os

from pystyle import Center, Anime, Colors, Colorate, System, Write


banner = '''
$$$$$$$\  $$\                     $$\       $$$$$$$\  $$$$$$$$\  $$$$$$\  $$$$$$$\  $$$$$$$$\ 
$$  __$$\ $$ |                    $$ |      $$  __$$\ $$  _____|$$  __$$\ $$  __$$\ $$  _____|
$$ |  $$ |$$ | $$$$$$\  $$$$$$$\  $$ |  $$\ $$ |  $$ |$$ |      $$ /  $$ |$$ |  $$ |$$ |      
$$$$$$$\ |$$ | \____$$\ $$  __$$\ $$ | $$  |$$ |  $$ |$$$$$\    $$ |  $$ |$$$$$$$\ |$$$$$\    
$$  __$$\ $$ | $$$$$$$ |$$ |  $$ |$$$$$$  / $$ |  $$ |$$  __|   $$ |  $$ |$$  __$$\ $$  __|   
$$ |  $$ |$$ |$$  __$$ |$$ |  $$ |$$  _$$<  $$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |      
$$$$$$$  |$$ |\$$$$$$$ |$$ |  $$ |$$ | \$$\ $$$$$$$  |$$$$$$$$\  $$$$$$  |$$$$$$$  |$$ |      
\_______/ \__| \_______|\__|  \__|\__|  \__|\_______/ \________| \______/ \_______/ \__|         
'''[1:]

text = '''                                                                                                 
             ,,                                                                                         
`7MM"""Yp, `7MM                       `7MM      `7MM"""Yb. `7MM"""YMM    .g8""8q. `7MM"""Yp, `7MM"""YMM 
  MM    Yb   MM                         MM        MM    `Yb. MM    `7  .dP'    `YM. MM    Yb   MM    `7 
  MM    dP   MM   ,6"Yb.  `7MMpMMMb.    MM  ,MP'  MM     `Mb MM   d    dM'      `MM MM    dP   MM   d   
  MM"""bg.   MM  8)   MM    MM    MM    MM ;Y     MM      MM MMmmMM    MM        MM MM"""bg.   MM""MM   
  MM    `Y   MM   ,pm9MM    MM    MM    MM;Mm     MM     ,MP MM   Y  , MM.      ,MP MM    `Y   MM   Y   
  MM    ,9   MM  8M   MM    MM    MM    MM `Mb.   MM    ,dP' MM     ,M `Mb.    ,dP' MM    ,9   MM       
.JMMmmmd9  .JMML.`Moo9^Yo..JMML  JMML..JMML. YA..JMMmmmdP' .JMMmmmmMMM   `"bmmd"' .JMMmmmd9  .JMML.  

                                        a BlankOBF deobfuscator
'''[1:]

System.Clear()
System.Title("BlankDEOBF by ꧁𝕆𝕧𝕖𝕣𝕡𝕠𝕨𝕖𝕣༄꧂#2524")
System.Size(140, 45)
Anime.Fade(Center.Center(banner), Colors.red_to_yellow, Colorate.Vertical, enter=True)
System.Size(130, 30)
print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(text)))

file_path = Write.Input("insert the name of your file:", Colors.red_to_yellow, interval=0.005)

with open(file_path, "r") as file:
    content = file.read()
    content = content.replace("import base64, lzma; exec(", "import base64, lzma, marshal, sys, struct; a = (")

with open("temp.py", 'w') as f:
    f.write(content + '''
def code_to_bytecode(code):
    def uint32(val):
        return struct.pack("<I", val)
    
    if sys.version_info >= (3,4):
        from importlib.util import MAGIC_NUMBER

    data = bytearray(MAGIC_NUMBER)
    if sys.version_info >= (3,7):
        data.extend(uint32(0))

    data.extend(uint32(int(0)))

    if sys.version_info >= (3,2):
        data.extend(uint32(0))

    data.extend(marshal.dumps(code))
    return data
    
with open("temp.pyc", 'wb') as f:
    f.write((code_to_bytecode(a)))''')


os.system("python temp.py")
os.system("pycdas.exe temp.pyc > dis.txt")
os.remove("temp.py")
os.remove("temp.pyc")

with open("dis.txt", "r") as file:
    for line in file:
        if "b'" in line:
            lzma_string = line.lstrip()
            break

os.remove("dis.txt")

with open("temp2.py", "w") as file:
    file.write(f'''
import lzma
a = lzma.decompress({lzma_string})
with open("temp3.py", 'wb') as f:
    f.write(a)
    ''')

os.system("python temp2.py")
os.remove("temp2.py")

with open("temp3.py", "r") as file:
    content = file.read()
    content = content.replace(".exec", "\na = ")

with open("temp3.py", "w") as file:
    file.write(content + '''
import marshal, sys, struct
def code_to_bytecode(code):
    def uint32(val):
        return struct.pack("<I", val)
    
    if sys.version_info >= (3,4):
        from importlib.util import MAGIC_NUMBER

    data = bytearray(MAGIC_NUMBER)
    if sys.version_info >= (3,7):
        data.extend(uint32(0))

    data.extend(uint32(int(0)))

    if sys.version_info >= (3,2):
        data.extend(uint32(0))

    data.extend(marshal.dumps(code))
    return data
    
with open("out.pyc", 'wb') as f:
    f.write((code_to_bytecode(a)))''')

os.system("python temp3.py")
os.remove("temp3.py")
Write.Print("Done...", Colors.red_to_yellow, interval=0.005)
