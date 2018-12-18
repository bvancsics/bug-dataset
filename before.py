import os
import subprocess as sp

def settings():
    os.chdir("/work/")
    sp.call("npm i --save glob", shell=True)
    sp.call("export PATH=/data/Chain/node/out/Release:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", shell=True)