import subprocess as sp
import os


cwd = os.getcwd()
for x in range(1,2):
    cmd = "mkdir -p ./Hessian_"+str(x)+"_traces"
    sp.call(cmd, shell=True)

    cmd = "cp ./Hessian_1_uj/hessian.js/test_* ./Hessian_"+str(x)+"_traces"
    sp.call(cmd, shell=True)

    os.chdir(cwd)