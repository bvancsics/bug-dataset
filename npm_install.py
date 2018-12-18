import subprocess as sp
import os

for x in range(3,8):
    #sp.call("python3 main_sanity_check.py -p Express -b "+str(x)+" -o ./Ex-b_"+str(x)+"_o1 -O ./Ex-b_"+str(x)+"_o2 > ./results_"+str(x)+".txt", shell=True)
    os.chdir("./Karma-b_"+str(x)+"_test/karma")
    sp.call("npm install", shell=True)
    os.chdir("../..")