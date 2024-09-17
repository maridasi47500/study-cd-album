from subprocess import check_output as runmyscript
from threading import Thread
from fichier import Fichier
import os
from subprocess import Popen, PIPE, STDOUT
try:
    from subprocess import DEVNULL # py3k
except ImportError:
    import os
    DEVNULL = open(os.devnull, 'wb')
import subprocess
FNULL = open(os.devnull, 'w')
from subprocess import call
class Speak:
  def __init__(self,hey=""):
    self.hey=hey
    self.runprogram=runmyscript
  def talk(self,hey=""):
    Fichier("./","hello.txt").ecrire(self.hey)
    self.someargs=["espeak-ng","-v","fr+f2","-f","hello.txt"]
    runmyscript(["sh","speak.sh"],stderr=subprocess.STDOUT)
    runmyscript(self.someargs,stderr=subprocess.STDOUT)
    #call(self.someargs,stdout=FNULL,stderr=subprocess.STDOUT)
  def myargs(self,a):
    #print(a)
    for x in a:
        print("arg len",len(x))
    self.someargs=a
  def run(self):
    return runmyscript(self.someargs).decode()
    
