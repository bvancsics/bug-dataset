import subprocess as sp
import os

def create_data_folders(dir_name):
    cmd = "mkdir -p "+str(dir_name)
    sp.call(cmd, shell=True)

    cmd = "mkdir -p "+str(dir_name)+"/pertest_coverage/0"
    sp.call(cmd, shell=True)

    cmd = "mkdir -p "+str(dir_name)+"/perchain_coverage/0"
    sp.call(cmd, shell=True)

    cmd = "mkdir -p "+str(dir_name)+"/result/0"
    sp.call(cmd, shell=True)


def test_coverage_copy(source_dir_name, target_dir_name):
    cmd = "cp "+os.path.abspath(source_dir_name)+"/coverage/test_* "+os.path.abspath(target_dir_name)+"/pertest_coverage/0"
    sp.call(cmd, shell=True)

def chain_coverage_copy(source_dir_name, target_dir_name):
    cmd = "cp "+os.path.abspath(source_dir_name)+"/test_* "+os.path.abspath(target_dir_name)+"/perchain_coverage/0"
    sp.call(cmd, shell=True)

def result_copy(source_dir_name, target_dir_name):
    cmd = "cp "+os.path.abspath(source_dir_name)+"/perTest_results.txt "+os.path.abspath(target_dir_name)+"/result/0"
    sp.call(cmd, shell=True)
    cmd = "cp "+os.path.abspath(source_dir_name)+"/perTest_results.txt_skipped.txt "+os.path.abspath(target_dir_name)
    sp.call(cmd, shell=True)

def dummy_copy(cwd, target_dir_name):
    cmd = "cp "+os.path.abspath(cwd+"/dummy.chg.SoDA")+" "+os.path.abspath(target_dir_name)
    sp.call(cmd, shell=True)
