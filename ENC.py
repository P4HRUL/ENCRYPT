import os, requests, marshal, zlib, base64

logo = ('''
    ______                            __ 
   / ____/___  ____________  ______  / /_
  / __/ / __ \/ ___/ ___/ / / / __ \/ __/
 / /___/ / / / /__/ /  / /_/ / /_/ / /_  
/_____/_/ /_/\___/_/   \__, / .___/\__/  
                      /____/_/           

[1] Encrypt base16
[2] Encrypt base32
[3] Encrypt base64
[4] Encrypt Marshal
[5] Encrypt Marshal-zlib-base16
[6] Encrypt Marshal-zlib-base32
[7] Encrypt Marshal-zlib-base64
''')

def masuk():
	os.system('clear')
	print(logo)
	pilih()
	
def pilih():
	pahrul = input ("[+] choice : ")
	if pahrul =="":
		print ("\n[+] ngetik apaan lu bangsad !!!")
		exit()
	elif pahrul =="1":
		x()
	elif pahrul =="2":
		xx()
	elif pahrul =="3":
		xxx()
	elif pahrul =="4":
		xxxx()
	elif pahrul =="5":
		xxxxx()
	elif pahrul =="6":
		xxxxxx()
	elif pahrul =="7":
		xxxxxxx()
	else:
		print("\n[+] ngetik apaan lu bangsad !!!")
		exit()
		


def x():
    kun = input('\n[+] file name : ')
    ups = open(kun, 'rb').read()
    ui = base64.b16encode(ups)
    output = kun.replace('.py', '') + '_enc.py'
    cok = open(output, 'w').write('# Coding By : Pahrul Aguspriana XD.\n# Github : https://github.com/P4HRUL\n\nimport base64\nexec(base64.b16decode(' + str(ui) + '))')
    print("[+] successfully encrypted %s" % kun)
    print("[+] saved as %s" % output)

def xx():
	kun = input('\n[+] file name : ')
	ups = open(kun, 'rb').read()
	ui = base64.b32encode(ups)
	output = kun.replace('.py', '') + '_enc.py'
	cok = open(output, 'w').write('# Coding By : Pahrul Aguspriana XD.\n# Github : https://github.com/P4HRUL\n\nimport base64\nexec(base64.b32decode(' + str(ui) + '))')
	print("[+] successfully encrypted %s" % kun)
	print("[+] saved as %s" % output)
	
def xxx():
	kun = input('\n[+] file name : ')
	ups = open(kun, 'rb').read()
	ui = base64.b64encode(ups)
	output = kun.replace('.py', '') + '_enc.py'
	cok = open(output, 'w').write('# Coding By : Pahrul Aguspriana XD.\n# Github : https://github.com/P4HRUL\n\nimport base64\nexec(base64.b64decode(' + str(ui) + '))')
	print("[+] successfully encrypted %s" % kun)
	print("[+] saved as %s" % output)
	
def xxxx():
	kun = input('\n[+] file name : ')
	fileopen = open(kun, 'rb').read()
	a = compile(fileopen, 'dg', 'exec')
	m = marshal.dumps(a)
	s = repr(m)
	output = kun.replace('.py', '') + '_enc.py'
	d = open(output, 'w').write('# Coding By : Pahrul Aguspriana XD.\n# Github : https://github.com/P4HRUL\n\nimport marshal\nexec(marshal.loads(' + s + '))')
	print("[+] successfully encrypted %s" % kun)
	print("[+] saved as %s" % output)

def xxxxx():
	kun = input('\n[+] file name : ')
	fileopen = open(kun, 'rb').read()
	a = compile(fileopen, 'dg', 'exec')
	m = marshal.dumps(a)
	z = zlib.compress(m)
	b = base64.b16encode(z)
	output = kun.replace('.py', '') + '_enc.py'
	d = open(output, 'w').write('# Coding By : Pahrul Aguspriana XD.\n# Github : https://github.com/P4HRUL\n\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b16decode(' + str(b) + '))))')
	print("[+] successfully encrypted %s" % kun)
	print("[+] saved as %s" % output)
	
def xxxxxx():
	kun = input('\n[+] file name : ')
	fileopen = open(kun, 'rb').read()
	a = compile(fileopen, 'dg', 'exec')
	m = marshal.dumps(a)
	z = zlib.compress(m)
	b = base64.b32encode(z)
	output = kun.replace('.py', '') + '_enc.py'
	d = open(output, 'w').write('# Coding By : Pahrul Aguspriana XD.\n# Github : https://github.com/P4HRUL\n\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b32decode(' + str(b) + '))))') 
	print("[+] successfully encrypted %s" % kun)
	print("[+] saved as %s" % output)
	
def xxxxxxx():
	kun = input('\n[+] file name : ')
	fileopen = open(kun, 'rb').read()
	a = compile(fileopen, 'dg', 'exec')
	m = marshal.dumps(a)
	z = zlib.compress(m)
	b = base64.b64encode(z)
	output = kun.replace('.py', '') + '_enc.py'
	d = open(output, 'w').write('# Coding By : Pahrul Aguspriana XD.\n# Github : https://github.com/P4HRUL\n\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode(' + str(b) + '))))')
	print("[+] successfully encrypted %s" % kun)
	print("[+] saved as %s" % output)
	
	
masuk()