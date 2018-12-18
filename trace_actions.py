import subprocess as sp
import os

def trace_copy(in_dir_name, out_dir_name):
    cmd = "mkdir -p "+str(out_dir_name)
    sp.call(cmd, shell=True)
    cmd = "cp "+str(in_dir_name)+"/test_* "+str(out_dir_name)
    sp.call(cmd, shell=True)


def trace_convert_to_soda(trace_folder, pattern, filter_script, out_dir_name):
    cmd =   "python3 main_chain_convert_to_soda.py " \
            "-f "+str(os.path.abspath(trace_folder))+" " \
            "-p "+str(pattern)+" " \
            "-c "+str(os.path.abspath(filter_script))+" " \
            "-o "+str(out_dir_name)
    sp.call(cmd, shell=True)