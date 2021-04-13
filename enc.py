# -*- coding: utf-8
# open source jangan lupa kasih bintang ajg
# angga kurniawan (fb.me/gaaaarzxd)
import os,sys,time
from platform import system

logo = """     \033[0;91m██████  ██    ██ ███████ ███    ██  ██████ 
     \033[0;91m██   ██  ██  ██  ██      ████   ██ ██      
     \033[0;91m██████    ████   █████   ██ ██  ██ ██      
     \033[0;97m██         ██    ██      ██  ██ ██ ██      
     \033[0;97m██         ██    ███████ ██   ████  ██████ 
 ---------------------------------------------------
 ➣ Author    : Angga Kurniawan
 ➣ GitHub    : https://github.com/anggaxd
 ---------------------------------------------------
 ➣ Instagram : @gaaarzxd
 ➣ Facebook  : https://fb.me/gaaaarzxd\n"""

def menu():
	os.system("clear")
	print logo
	print " [!] Masukan Nama File Nya Ajah Tanpa .py" 
	print " [*] Contoh : pyenc.py (masukan filenya : pyenc)" 
	name_files = raw_input(" [+] Masukan File : ")
	sv_file = raw_input(" [+] Simpan File : ")
	py_datt = (str(name_files)+".pyo")
	print " [#] Bentar Lagi Encrypt SC Nya...."
	time.sleep(1)
	os.system('python2 -OO -m py_compile ' + name_files+'.py')
	os.system("mv "+str(py_datt)+" "+str(sv_file)+".py")
	print " [*] Oke Sudah Di Encrypt"
	print " [+] Nama File : "+str(sv_file)+".py"

if __name__ == '__main__':
	menu()
