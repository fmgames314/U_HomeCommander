import urllib
import subprocess  
import os
version = "";
if(os.path.isfile("version.txt")):
	version = open("version.txt").read()
link = "https://github.com/fmgames314/U_HomeCommander/raw/master/README.md"
f = urllib.urlopen(link)
myfile = f.read()
if(os.path.isfile("version.txt")):
	os.remove("version.txt")
file = open('version.txt', 'w')
file.write(myfile)
file.close()
print (version)
print (myfile)
print (version != myfile)
if(version != myfile):
	if(os.path.isfile("U_Home_Commander.exe")):
		os.remove("U_Home_Commander.exe")
	urllib.urlretrieve ("https://github.com/fmgames314/U_HomeCommander/raw/master/U_HomeCommander.exe", "U_Home_Commander.exe")
subprocess.Popen([r"U_Home_Commander.exe"])  