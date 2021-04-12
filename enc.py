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

def menupy2():
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

def menupy3():
	os.system("clear")
	print logo
	print " [!] Masukan Nama File Nya Ajah Tanpa .py" 
	print " [*] Contoh : pyenc.py (masukan filenya : pyenc)" 
	name_file = raw_input(" [+] Masukan File : ")
	saved_file = raw_input(" [+] Simpan File : ")
	py_dato = ("__pycache__/"+str(name_file)+".cpython-38.opt-2.pyc")
	print " [#] Bentar Lagi Encrypt SC Nya...."
	time.sleep(1)
	os.system('python -OO -m py_compile ' + name_file+'.py')
	os.system("mv "+str(py_dato)+" "+str(saved_file)+".py")
	os.system('rm -rf __pycache__')
	print " [*] Oke Sudah Di Encrypt"
	print " [+] Nama File : "+str(saved_file)+".py"
	
if __name__ == '__main__':
	if len(sys.argv) == 2:
		if sys.argv[1] == 'enc_py2':
			menupy2()
		if sys.argv[1] == 'enc_py3':
			menupy3()
		else:
			print " [!] Cara Menggunakan Nya :"
			print " [+] Encrypt Python2 Ketik : python2 enc.py enc_py2"
			exit (" [+] Encrypt Python3 Ketik : python2 enc.py enc_py3")
	print " [!] Cara Menggunakan Nya :"
	print " [+] Encrypt Python2 Ketik : python2 enc.py enc_py2"
	exit (" [+] Encrypt Python3 Ketik : python2 enc.py enc_py3")
