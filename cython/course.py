import os, requests
from setuptools import setup
from Cython.Build import cythonize

logo = ('''
   ______   _______ _   _  ___  _   _ 
  / ___\ \ / /_   _| | | |/ _ \| \ | |
 | |    \ V /  | | | |_| | | | |  \| |
 | |___  | |   | | |  _  | |_| | |\  |
  \____| |_|   |_| |_| |_|\___/|_| \_|
''')

def masuk():
	os.system("clear")
	print (logo)
	try:
		file = input ("[+] file name : ")
		data = open(file).read()
	except IOError:
		print ("[+] file not found !!!");exit()
	setup(ext_modules = cythonize(""+file+"",compiler_directives={'language_level' : "3"}))
	output = file.replace('.py', '') + '.c'
	print("\n[+] successfully encrypted %s" % file);print("[+] saved as %s" % output)

masuk()